from django.contrib import admin
from django.urls import path, include
from auth_api.views import HumanRegisterationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_human/', HumanRegisterationView.as_view(), name='add_human'),
    path('all_human/', HumanRegisterationView.as_view(), name='all_human')
]    