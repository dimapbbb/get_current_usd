from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('get_currency.urls', namespace="Получить курс вылюты"))
]
