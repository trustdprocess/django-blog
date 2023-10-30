from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='loginpage'),
    path('homepage/', views.homepage, name='homepage'),
    path('logout/', views.logout_page, name='logoutpage'),
    path('addpost/', views.addpost, name='addpost'),
    path('addcomment/', views.addcomment, name='addcomment'),
    path('detailpage/<int:id>/', views.detailposts, name='detailpage'),
    
    
    
]
