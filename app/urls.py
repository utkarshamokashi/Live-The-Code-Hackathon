from django.urls import path
from app import views

urlpatterns = [
    path("signin", views.signin, name="signin"),
    path("info", views.info, name="info"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("form", views.form, name="form"),
    path("community", views.community, name="community"),
    path("update_id", views.update_id, name="update_id"),
    path("aboutUs", views.aboutUs, name="aboutUs"),
    
]

