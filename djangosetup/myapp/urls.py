from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]