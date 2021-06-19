from django.urls import path
from zakaznici import views
urlpatterns = [
    path('', views.index, name='index'),
    path('zakaznici/', views.ZakaznikListView.as_view(), name='prehled_zakazniku'),
    path('zakaznici/<int:pk>/', views.ZakaznikDetailView.as_view(), name='podrobnosti_zakaznika'),
    path('zakaznik/create/', views.ZakaznikCreateView.as_view(), name='zakaznik-create'),
    path('zakaznik/<int:pk>/update/', views.ZakaznikUpdateView.as_view(), name='zakaznik-update'),
    path('zakaznik/<int:pk>/delete/', views.ZakaznikDeleteView.as_view(), name='zakaznik-delete'),
]