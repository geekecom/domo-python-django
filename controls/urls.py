from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('redirect-to-login/', views.redirect_to_login, name='redirect_to_login'),
]
