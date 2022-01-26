from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from Imageify.views import imageify

urlpatterns = [
    path('works/imageify', imageify, name='imageify')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


