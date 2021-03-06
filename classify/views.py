from django.shortcuts import render

from classify.forms import ContactForm
from classify.predict import breed, fruits

def index(request):
    return render(request, 'classify/index.html', context={})
def contact(request):
    if request.method == 'POST':
        form  = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'classify/contact.html', context)

def about(request):
    return render(request, 'classify/about.html')

def works(request):
    return render(request, 'classify/works.html')

def breedify(request):
    if request.method == 'POST':
        pred_breed = breed(request)
        context = {
            'pred_breed': pred_breed,
        }
        return render(request, 'classify/breedify.html', context)
    else:
        return render(request, 'classify/breedify.html')

def fruitsify(request):
    if request.method == 'POST':
        pred_class = fruits(request)
        context = {
            'pred_class':pred_class
        }
        return render(request, 'classify/fruitsify.html', context)
    else:
        return render(request, 'classify/fruitsify.html')