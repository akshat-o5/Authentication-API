from django.contrib import admin
from django.urls import path, include
from auth_api.views import HumanRegisterationView, HumanLoginView, HumanProfileView, ChangePasswordView, SendPasswordResetEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', HumanRegisterationView.as_view(), name='signup'),
    path('login/', HumanLoginView.as_view(), name='login'),
    path('all_human/', HumanRegisterationView.as_view(), name='all_human'),
    path('profile/', HumanProfileView.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('send_password_reset_email/', SendPasswordResetEmailView.as_view(), name='send_password_reset_email'),
]    