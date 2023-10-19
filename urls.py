from django.urls import path
from busapp1 import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    
    path('index.html', views.index, name='index_html'),
    path('registration.html', views.reg, name='reg'),
  
    path('about_website.html', views.about, name='about'),

    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_page, name='logout_page'),
    path('register/', views.register_view, name='register_view'),
    path('login/dashboard.html', views.dashboard_view, name='dashboard'),
    path('timetable/', views.timetable_view, name='timetable'),

  
    
    # Other URL patterns for busapp1
]