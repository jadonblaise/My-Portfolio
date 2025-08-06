from django.urls import path
from .views import contact_view, download_cv_unavailable


app_name = "Me"
urlpatterns = [
    path("", contact_view, name='contact_view'),
    path("raise404/", download_cv_unavailable, name='download_cv_unavailable')
]