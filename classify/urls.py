from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from classify.views import breedify, index, contact, about, works, fruitsify

urlpatterns = [
    path('',index, name='index' ),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('works/', works, name='works'),
    path('works/breedify', breedify, name='breedify'),
    path('works/fruitsify', fruitsify, name='fruitsify')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)