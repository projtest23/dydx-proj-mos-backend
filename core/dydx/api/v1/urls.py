from django.urls import path, include
from . import views

app_name = "api-v1"

urlpatterns = [
    path('positions/',views.PositionsView.as_view(),name="post-list"),
]