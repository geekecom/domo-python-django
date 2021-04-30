from django.urls import path

from . import views

urlpatterns = [
    path('controls/<int:pk>/', views.ControlDetail.as_view()),
]
