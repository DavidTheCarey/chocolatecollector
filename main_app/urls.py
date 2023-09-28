from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chocolates/', views.chocolates_index, name="index"),
  path('chocolates/<int:chocolate_id>', views.chocolate_detail, name="detail"),
]