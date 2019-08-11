from django.urls import path
from formapp.apiviews import AmarformView, AmarformDetailView

urlpatterns = [
    path("amarformdata/", AmarformView.as_view()),
    path("amarformdata/<int:pk>", AmarformDetailView.as_view())
]

