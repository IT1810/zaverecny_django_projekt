from django.urls import path
from zakaznici import views
urlpatterns = [
    path('', views.index, name='index')
]