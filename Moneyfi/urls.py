from posixpath import basename
from django.urls import path, include
from rest_framework import routers
from Moneyfi.models import MoneyfiModel

from Moneyfi.views import MfViewSet, moneyfi, moneyfi_delete, moneyfi_update

router = routers.DefaultRouter()
router.register(r'api', MfViewSet, basename=MoneyfiModel)


app_name = 'moneyfi'

urlpatterns = [
    path('works/moneyfi/', moneyfi, name='moneyfi'),
    path('works/moneyfi/<mfunits>/update', moneyfi_update, name='update'),
    path('works/moneyfi/<mfunits>/delete', moneyfi_delete, name='delete'),
    path('', include(router.urls)),
]


