from django.urls import path
from .views import IndexView, MyView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("mine/", MyView.as_view(), name="my-view"),
]