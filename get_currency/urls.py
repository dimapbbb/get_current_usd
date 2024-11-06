from django.urls import path

from get_currency.apps import GetCurrencyConfig
from get_currency.views import GetCurrencyAPIView

app_name = GetCurrencyConfig.name

urlpatterns = [
    path('get_currency/<str:currency>/', GetCurrencyAPIView.as_view(), name='get_currency')
]