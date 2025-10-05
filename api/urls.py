from django.urls import path
from userauths import views as userauths_views
from store import views as store_views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns=[
    path('user/register',userauths_views.RegisterView.as_view()),
    path('user/emailverify',userauths_views.VerifyOTPView.as_view(), name="verifyotp"),
    path('user/resendotp',userauths_views.ResendOTPView.as_view(), name="resendotp"),
    path('user/login',userauths_views.LoginView.as_view()),
    path('user/token/refresh',userauths_views.CookieTokenRefreshView.as_view()),
    path('user/logout',userauths_views.LogoutView.as_view()),
    path('user/passwordresetemail',userauths_views.PasswordResetEmail.as_view()),
    path('user/PasswordResetConfirm',userauths_views.PasswordResetConfirm.as_view()),
    path('user/UserProfileView',userauths_views.UserProfileView.as_view()),
    path('user/auth/changepassword', userauths_views.ChangePasswordView.as_view(), name='change-password'),
    path('user/deleteaccount',userauths_views.DeleteAccountView.as_view()),
    path('user/authviewcheck',userauths_views.CheckAuthView().as_view())
]