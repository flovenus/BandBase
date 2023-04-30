from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('userlist', views.user_list, name='userlist'),
    path('verify_user/<user_id>', views.verify_user, name='verify_user'),
    path('delete_user/<user_id>', views.delete_user, name='delete_user'),
]
