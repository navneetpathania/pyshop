from django.urls import path
from . import views


urlpatterns = [
    path("",views.index),
    path("add/",views.add),
    path("delete/<id>",views.delete),
    path("edit/<id>",views.edit),
    path("upload/",views.upload)
]

