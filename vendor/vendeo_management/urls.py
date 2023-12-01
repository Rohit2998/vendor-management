from django.urls import path
from . import views

app_name='vendeo_managememnt'
urlpatterns = [
    path('ind/', views.index, name='index'),
]