from django.urls import path
from formapp.apiviews import AmarformView

urlpatterns = [
    path("amarformdata/", AmarformView.as_view())
]
