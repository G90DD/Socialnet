from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  #auto pou kanei to name=index einai na dinei ena onoma sto mapping, prokeimenou na anaferomaste se auto allou ston kodika-reverse url mapping
    path('profile/', views.profile, name='profile'),
    path('front_page/', views.front_page, name='front_page'),
    path('groups/', views.groups, name='groups'),
]
