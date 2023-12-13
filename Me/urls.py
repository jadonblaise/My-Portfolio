from django.urls import path
from .views import frontpage, contact_view


app_name = "Me"
urlpatterns = [
    path("", frontpage, name='frontpage'),
    path("contact/", contact_view, name='contact_view')
]