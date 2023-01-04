from django.urls import path
from . import views

urlpatterns = [
    path('newhome', views.Home.as_view(),name= 'newhome'),
    path('showstaffs', views.Staffs.as_view(),name= 'showstaffs'),
    path('showstudents', views.Student.as_view(),name= 'showstudents'),
    path('enquiry', views.Enquiry.as_view(),name= 'enquiry'),
    path('form', views.Form.as_view(),name= 'form'),
    path('student', views.Student.as_view(),name= 'student'),
    path('edit', views.Edit.as_view(),name= 'edit'),
    path('delete', views.Delete.as_view(),name= 'delete'),
    path('profile', views.Profile.as_view(),name= 'profile'),
    path('editprofile', views.Editprofile.as_view(),name= 'editprofile'),
]
