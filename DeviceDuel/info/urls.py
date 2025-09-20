
from django.urls import path
from . import views


urlpatterns = [
    path('contact/',views.Contact,name="Contact"),
    path('about/',views.About,name="about")
]