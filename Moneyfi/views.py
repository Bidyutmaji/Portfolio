import requests

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from Moneyfi.forms import MoneyfiForm
from Moneyfi.models import MoneyfiModel
from Moneyfi.serilizers import MfSerializer
# Create your views here.


def SchemeCode(mf_name):
  mf_name = mf_name.split()
  rk = requests.get('https://api.mfapi.in/mf').json()
  for mf in rk:
    mf_n = mf['schemeName']
    if mf_name[0][1:].upper() in mf_n \
      and mf_name[1][1:] in mf_n \
        and mf_name[2][1:] in mf_n \
          and mf_name[3][1:] in mf_n:
            return mf['schemeCode']
    elif mf_name[0][1:] in mf_n \
      and mf_name[1][1:] in mf_n \
        and mf_name[2][1:] in mf_n \
          and mf_name[3][1:] in mf_n:
            return mf['schemeCode']


def get_mf(apc,units):
  mf_code = SchemeCode(apc)
  apc = requests.get(f'https://api.mfapi.in/mf/{mf_code}').json()
  if apc['status'] =='SUCCESS':
    today_nav = apc['data'][0]['nav']
    yesterday_nav = apc['data'][1]['nav']

    fund_name = apc['meta']['scheme_name'].split('-')[0]
    if fund_name[0].islower():
      fund_name = fund_name[0].upper()+fund_name[1:]

    diff = float(today_nav)-float(yesterday_nav)
    day_return ='{:0,.2f}({}%)'.format(round(diff*units, 2), 
                                        str(round((diff/float(today_nav))*100, 2)))
    fund_return = '{:0,.2f}'.format(round(float(today_nav)*units, 2))

    data = '''
{}
Today: {}
    '''.format(fund_name.split()[0]+' '+fund_name.split()[1], day_return)
    return fund_name, day_return, fund_return

def get_data(request):
  data = MoneyfiModel.objects.filter(mobile=request.user.username)
  rk_data = [rk for rk in data]
  gn_data = [[rk.mf_name, rk.mf_units] for rk in rk_data]
  for apc_data in gn_data:
    dcj, jps, apc = get_mf(apc_data[0], apc_data[1])
    gn_data[gn_data.index(apc_data)][0] = dcj
    gn_data[gn_data.index(apc_data)].append(jps)
    gn_data[gn_data.index(apc_data)].append(apc)
  return gn_data


@login_required(login_url='users:login')
def moneyfi(request):
  print(type(request.user.username))

  rk_data = get_data(request)
  if request.method=='POST':
      form = MoneyfiForm(request.POST, initial={'mobile':request.user.username})
      if form.is_valid():
        if request.user.username != '9997775555':
          form.save(commit=False)
          rk_data = get_data(request)
          context = {
            'form':form,
            'rk_data': rk_data
            }
        else:
          form.save()
          rk_data = get_data(request)
          context = {
            'form':form,
            'rk_data': rk_data
            }
          return render(request, 'moneyfi/moneyfi.html', context)
  else:
      form = MoneyfiForm(initial={'mobile':request.user.username})
      rk_data = get_data(request)
      context = {
            'form':form,
            'rk_data': rk_data
        }
      return render(request, 'moneyfi/moneyfi.html', context)

def send_otp(mobile):
  pass


def moneyfi_update(request,mfunits):
  gn_form_data = MoneyfiModel.objects.get(mobile=request.user.username, mf_units=mfunits)
  if request.method=='POST':
      form = MoneyfiForm(request.POST, instance=gn_form_data)
      print(type(request.user.username))
      if form.is_valid:
        if request.user.username == '9997775555':
          form.save(commit=False)
          rk_data = get_data(request)
          context = {
            'form':form,
            'rk_data': rk_data
            }
        else:
          form.save()
          rk_data = get_data(request)
          context = {
            'form':form,
            'rk_data': rk_data
            }
        return redirect('moneyfi:moneyfi')
  else:
      form = MoneyfiForm(instance=gn_form_data)
      context = {
            'form':form
        }
      return render(request, 'moneyfi/moneyfi_update.html', context)
def moneyfi_delete(request, mfunits):
  if request.user.username != '9997775555':
    gn_form_data = MoneyfiModel.objects.get(mobile=request.user.username, mf_units=mfunits)
    gn_form_data.delete()
  return redirect('moneyfi:moneyfi')


class MfViewSet(viewsets.ModelViewSet):

  queryset = MoneyfiModel.objects.all()

  serializer_class = MfSerializer


