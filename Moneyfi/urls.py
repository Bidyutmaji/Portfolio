from django.urls import path
from Moneyfi.views import moneyfi, moneyfi_delete, moneyfi_update

app_name = 'moneyfi'
urlpatterns = [
    path('works/moneyfi/', moneyfi, name='moneyfi'),
    path('works/moneyfi/<mfunits>/update', moneyfi_update, name='update'),
    path('works/moneyfi/<mfunits>/delete', moneyfi_delete, name='delete'),
]


