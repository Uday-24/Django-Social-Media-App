from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('pass_change/', auth_view.PasswordChangeView.as_view(template_name = "users/change_pass.html"), name="password_change"),
    path('pass_change/done/', auth_view.PasswordChangeDoneView.as_view(template_name = "users/change_pass_done.html"), name="password_change_done"),
    path('pass_reset/', auth_view.PasswordResetView.as_view(template_name = "users/reset_pass.html"), name="password_change_done"),
    path('pass_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name = "users/reset_pass_done.html"), name="password_reset_done"),
]