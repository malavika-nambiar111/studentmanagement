from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name= 'home'),
    path('login', views.signin,name= 'login'),
    path('signup', views.signup,name= 'signup'),
    path('courses', views.courses,name= 'courses'),
    path('gallery', views.gallery,name= 'gallery'),
    path('contact', views.contact,name= 'contact'),
    path('forgot', views.forgot,name= 'forgot'),
]