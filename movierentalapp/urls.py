"""movierentalapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', views.MovieService.as_view()),
    path('users/', views.UserService.as_view()),
    path('user/<slug:usernameparam>/<slug:passwordparam>', views.UserService.get_one),
    path('rents/', views.RentService.as_view()),
    path('new_rent/', views.RentService.post),
    path('update_rent/', views.RentService.put),
    path('rentmovies/', views.RentMoviesService.as_view()),
    path('rentmoviesuser/<slug:useridparam>', views.RentMoviesService.get_by_userid),
    path('rentmoviesinprocess/', views.RentMoviesService.get_all_inprocess),
    path('rentmoviesprocessed/', views.RentMoviesService.get_all_processed),
]
