from .import views
from django.urls import path
from .views import menuMore
urlpatterns = [
     # path('create_menu/', views.create_menu, name='create_menu'),
     path('menumore2/',menuMore, name='menumore2'),
]


