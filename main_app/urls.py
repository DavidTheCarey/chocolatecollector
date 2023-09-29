from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chocolates/', views.chocolates_index, name="index"),
  path('chocolates/<int:chocolate_id>', views.chocolate_detail, name="detail"),
  path('chocolates/create/', views.ChocolateCreate.as_view(), name='chocolates_create'),
  path('chocolates/<int:pk>/update/', views.ChocolateUpdate.as_view(), name='chocolates_update'),
  path('chocolates/<int:pk>/delete/', views.ChocolateDelete.as_view(), name='chocolates_delete'),

]