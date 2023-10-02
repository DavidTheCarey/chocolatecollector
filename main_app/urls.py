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
  path('chocolates/<int:chocolate_id>/add_order/', views.add_order, name='add_order'),
  path('chocolates/<int:chocolate_id>/assoc_store/<int:store_id>/', views.assoc_store, name='assoc_store'),
  path('chocolates/<int:chocolate_id>/unassoc_store/<int:store_id>/', views.unassoc_store, name='unassoc_store'),
  path('stores/', views.StoreList.as_view(), name='stores_index'),
  path('stores/<int:pk>/', views.StoreDetail.as_view(), name='stores_detail'),
  path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),
  path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='stores_update'),
  path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='stores_delete'),
]