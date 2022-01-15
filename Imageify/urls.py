import imp
from re import I
from django.urls import path
from Imageify.views import imageify
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('works/imageify', imageify, name='imageify')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


