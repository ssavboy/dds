from django.urls import path

from . import views

urlpatterns = [
    path("", views.records_list, name="records_list"),
    path("records/create/", views.record_create, name="record_create"),
    path("records/<int:pk>/edit/", views.record_update, name="record_update"),
    path("records/<int:pk>/delete/", views.record_delete, name="record_delete"),
]
