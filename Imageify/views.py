from email.mime import image
import re
from urllib.error import HTTPError
from django.shortcuts import render
from Imageify.froms import ImageSearch
import requests as r
import zipfile
import wget
from django.conf import settings
import os 
import shutil

# Create your views here.

# def getImage(request):
    
        
#     print("RK+GN+APC+JPS")
#     print(path)
#     return image_url


def imageify(request):
    if request.method=="POST":
        term = request.POST.get('term')
        key = 'Cx-w98RTghUSdri6MQYkoJ9EHajtcVXgEtFk1iPB45A'
        url = 'https://api.unsplash.com/search/photos/?query='+term+'&per_page=25&client_id='+key
        text = '''
        I'm Bidyut Maji...
        Check out https://bidyutmaji.herokuapp.com/.

        Thanks For Downloading.


        '''
        try:
            url_content = r.get(url).json()
            link = url_content['results']
            image_url = [image['urls']['regular'] for image in link]
            # path = []
            folder_root = os.path.join(settings.MEDIA_ROOT, 'download')

            # os.mkdir(folder_root)
            for file in os.listdir(folder_root):
                os.remove(os.path.join(folder_root, file))
            
            file = term+'.zip'
            zip_file = os.path.join(folder_root, file)
            text_path = os.path.join(folder_root, term+'.txt')
            with open(text_path, 'w') as f:
                f.write(text)
            zf = zipfile.ZipFile(zip_file, 'w')
            zf.write(text_path)
            for i, item in enumerate(image_url, 1):
                f_name = term+'_'+str(i)+'.jpg'

                path = os.path.join(folder_root, f_name.title())
                try:
                    wget.download(item, path, bar=False)
                    zf.write(path, os.path.basename(path))
                except HTTPError:
                    pass
                zf.close()
            context={
                'image':image_url[0],
                'file': file,
                'term':term,
                'image_count': i
                }

            return render(request, 'Imageify/imageify.html', context)
        except ConnectionError:
           return render(request, 'Imageify/imageify.html')
    else:
        return render(request, "Imageify/imageify.html")