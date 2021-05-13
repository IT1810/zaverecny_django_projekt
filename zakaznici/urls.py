from django.urls import path
from zakaznici import views
urlpatterns = [
    path('', views.index, name='index'),
    path('zakaznici/', views.ZakaznikListView.as_view(), name='prehled_zakazniku'),
    path('zakaznici/<int:pk>/', views.ZakaznikDetailView.as_view(), name='podrobnosti_zakaznika')
]