from django.urls import path

from . import views

urlpatterns =[
    path('calc/',views.home,name='calc'),
    path('add',views.add,name='add')
    
]