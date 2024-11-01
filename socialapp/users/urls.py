from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name="users/password_change_form.html"), name="password_change"),
    path('password_change/done', auth_view.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name="password_change_done"),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name="users/password_resete_form.html"), name="password_reset"),
    path('password_reset/done', auth_view.PasswordResetDoneView.as_view(template_name="users/password_resete_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name="users/password_resete_confirm.html"), name="password_reset_confirm"),
    path('password_reset/complete', auth_view.PasswordResetCompleteView.as_view(template_name="users/password_resete_complete.html"), name="password_reset_complete"),

    path('register/', views.register, name="register"),
    path('register/done', views.register_done, name="register_done"),
]