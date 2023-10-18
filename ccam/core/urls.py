from django.urls import path

from ccam.core import views

app_name = "core"

urlpatterns = [path("modal/", views.ModalView.as_view(), name="modal")]
