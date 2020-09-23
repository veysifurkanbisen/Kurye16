from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('iletisim', views.contact_form, name='contact_form'),
    path('hakkımızda', views.about, name='about'),
    path('politikalar', views.politics, name='politics')
]