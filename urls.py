from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', auth_views.login, name='login'),  #auto pou kanei to name=index einai na dinei ena onoma sto mapping, prokeimenou na anaferomaste se auto allou ston kodika-reverse url mapping
    path('profile/', views.profile, name='profile'),
    path('front_page/', views.front_page, name='front_page'),
    path('groups/', views.groups, name='groups'),
]
