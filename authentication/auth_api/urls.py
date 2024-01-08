from django.contrib import admin
from django.urls import path, include
from auth_api.views import HumanRegisterationView, HumanLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', HumanRegisterationView.as_view(), name='signup'),
    path('login/', HumanLoginView.as_view(), name='login'),
    path('all_human/', HumanRegisterationView.as_view(), name='all_human'),
]    