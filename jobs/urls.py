from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('jobsapp.urls')),
    url(r'^', include('accounts.urls')),
    url(r'^api/', include([
        url(r'^', include('jobsapp.api.urls')),
    ])),
]
