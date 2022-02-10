import os
import requests
from urllib.error import HTTPError
import zipfile
from concurrent.futures import ThreadPoolExecutor

from django.shortcuts import render
from django.conf import settings
import wget


def imageify(request):
    API_KEY = 'Cx-w98RTghUSdri6MQYkoJ9EHajtcVXgEtFk1iPB45A'#os.getenv('API_KEY')
    
    if request.method=="POST":
        term = request.POST.get('term')
        img_num = request.POST.get('num')
        img_quality = request.POST.get('quality')
        
        url = 'https://api.unsplash.com/search/photos/?query='+term+'&per_page='+img_num+'&client_id='+API_KEY
        
        text = '''
        I'm Bidyut Maji...
        Check out https://bidyutmaji.herokuapp.com/.

        Thanks For Downloading.
        '''
        try:
            url_content = requests.get(url).json()
            link = url_content['results']
            image_url = [image['urls'][img_quality] for image in link]

            if image_url:
                img_url = [img['urls']['regular'] for img in link]
                g_number = [i+1 for i in range(len(img_url)) ]
                folder_root = os.path.join(settings.MEDIA_ROOT, 'download')

                for file in os.listdir(folder_root):
                    os.remove(os.path.join(folder_root, file))
                
                file = term+'.zip'
                zip_file = os.path.join(folder_root, file)
                text_path = os.path.join(folder_root, term+'.txt')
                with open(text_path, 'w') as f:
                    f.write(text)
                zf = zipfile.ZipFile(zip_file, 'w')
                zf.write(text_path, os.path.basename(text_path))

                def a_image_download(ij_url, g_number):
                    f_name = term+'_'+str(g_number)+'.jpg'
                    path = os.path.join(folder_root, f_name)
                    try:
                        wget.download(ij_url, path, bar=False)
                        zf.write(path, os.path.basename(path))
                    except HTTPError:
                        pass
                with ThreadPoolExecutor() as rk_excutor:
                    rk_excutor.map(a_image_download, image_url, g_number)
                # for i, item in enumerate(image_url, 1):
                #     f_name = term+'_'+str(i)+'.jpg'

                #     path = os.path.join(folder_root, f_name)
                #     try:
                #         wget.download(item, path, bar=False)
                #         zf.write(path, os.path.basename(path))
                #     except HTTPError:
                #         pass
                zf.close()

                if open(zip_file, 'r'):
                    print(zip_file)

                context={
                    'image':img_url[0],
                    'file': file,
                    'term':term,
                    'image_count': len(g_number)
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