from django.conf.urls import url,include

from .views import *

app_name = "jobs"

urlpatterns = [
    url('^$', HomeView.as_view(), name='home'),
    url(r'^search', SearchView.as_view(), name='searh'),
    url(r'^employer/dashboard/', include([
        url(r'^', DashboardView.as_view(), name='employer-dashboard'),
        url(r'^all-applicants', ApplicantsListView.as_view(), name='employer-all-applicants'),
        url(r'^applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='employer-dashboard-applicants'),
        url(r'^mark-filled/<int:job_id>', filled, name='job-mark-filled'),
    ])),
    url(r'^apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    url(r'^jobs', JobListView.as_view(), name='jobs'),
    url(r'^jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    url(r'^employer/jobs/create', JobCreateView.as_view(), name='employer-jobs-create'),
]
