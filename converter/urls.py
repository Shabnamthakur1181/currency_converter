from django.urls import path
from .views import CurrencyConverterView

from . import views  # ✅ this line was missing



urlpatterns = [
    path('', CurrencyConverterView.as_view(), name='home'),
   
]


