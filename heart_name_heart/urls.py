from django.urls import path

from heart_name_heart import views

urlpatterns = [
    path("generate", views.generate_api, name="generate"),
]
