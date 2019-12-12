from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('jobs', JobViewSet, base_name='jobs')

urlpatterns = [
    url(r'^search/', SearchApiView.as_view()),
    url(r'^apply-job/<int:job_id>', ApplyJobApiView.as_view())
]

urlpatterns += router.urls
