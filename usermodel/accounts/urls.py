from django.contrib import admin;
from django.urls import path;
from accounts import views;
from django.contrib.auth.views import(LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView);
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',LoginView.as_view(template_name="registeration/login.html"),name="login"),
    path('logout/',LogoutView.as_view(template_name="registeration/login.html"),name="logout"),
    path('register/',views.UserRegister,name="register"),
    path('password-reset/',PasswordResetView.as_view(template_name="registeration/password-reset.html"),name="password_reset"),
    path('password-reset-done/',PasswordResetDoneView.as_view(template_name="registeration/password-reset-done.html"),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name="registeration/password-reset-confirm.html"),name="password_reset_confirm"),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name="registeration/password-reset-complete.html"),name="password_reset_complete"),
    path('password-change/',PasswordChangeView.as_view(template_name="registeration/password-change.html"),name="password_change"),
    path('password-change-done/',PasswordChangeDoneView.as_view(template_name="registeration/password-change-done.html"),name="password_change_done"),
];
