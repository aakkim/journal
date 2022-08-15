from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('create', views.create_journal, name='create_journal'),
    path('read_entry/<int:id>', views.read_entry, name='read_entry'),
    path('delete_entry/<int:id>', views.delete_entry, name='delete_entry'),
    path('update/<int:id>', views.update, name='update'),
    path('update_entry/<int:id>', views.update_entry, name='update_entry'),
    path('view_account', views.view_account, name='view_account'),
    path('change_password', views.change_password, name='change_password'),
    path('success', views.success, name='success'),
    
]