from django.urls import path
from . import views
urlpatterns = [

    #path('<programmer_id>/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/', views.about, name='about')
]