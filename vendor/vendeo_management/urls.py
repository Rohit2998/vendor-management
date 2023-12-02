from django.urls import path
from . import views

app_name='vendeo_managememnt'
urlpatterns = [
    path('ind/', views.index, name='index'),
    path('ind2/', views.index2, name='index'),
    path('vendor', views.VendorAPIView.as_view(),name='vendor')

]