from urllib.error import HTTPError
from django.shortcuts import render
import requests as r
import zipfile
import wget
from django.conf import settings
import os 

def imageify(request):
    api_key = os.getenv('API_KEY')

    if request.method=="POST":
        term = request.POST.get('term')
        img_num = request.POST.get('num')
        img_quality = request.POST.get('quality')
        
        url = 'https://api.unsplash.com/search/photos/?query='+term+'&per_page='+img_num+'&client_id='+api_key
        
        text = '''
        I'm Bidyut Maji...
        Check out https://bidyutmaji.herokuapp.com/.

        Thanks For Downloading.
        '''
        try:
            url_content = r.get(url).json()
            link = url_content['results']
            image_url = [image['urls'][img_quality] for image in link]
            if image_url:
                img_url = [img['urls']['regular'] for img in link]

                folder_root = os.path.join(settings.MEDIA_ROOT, 'download')

                for file in os.listdir(folder_root):
                    os.remove(os.path.join(folder_root, file))
                
                file = term.title()+'.zip'
                zip_file = os.path.join(folder_root, file)
                text_path = os.path.join(folder_root, term+'.txt')
                with open(text_path, 'w') as f:
                    f.write(text)
                zf = zipfile.ZipFile(zip_file, 'w')
                zf.write(text_path, os.path.basename(text_path))
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
                    'image':img_url[0],
                    'file': file,
                    'term':term.title(),
                    'image_count': i
                    }
                return render(request, 'Imageify/imageify.html', context)
            else:
                context={
                    'image_not_found': 'Doesn\'t found any image'
                }
                return render(request, 'Imageify/imageify.html', context)
        except ConnectionError:
           return render(request, 'Imageify/imageify.html')
    else:
        return render(request, "Imageify/imageify.html")