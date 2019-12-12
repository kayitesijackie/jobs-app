from django.conf.urls import url,include

from django.conf import settings
from django.conf.urls.static import static

from jobsapp.views import EditProfileView
from .views import *

app_name = "accounts"

urlpatterns = [
    url(r'^employee/register', RegisterEmployeeView.as_view(), name='employee-register'),
    url(r'^employer/register', RegisterEmployerView.as_view(), name='employer-register'),
    url(r'^employee/profile/update', EditProfileView.as_view(), name='employer-profile-update'),
    url(r'^logout', LogoutView.as_view(), name='logout'),
    url(r'^login', LoginView.as_view(), name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
