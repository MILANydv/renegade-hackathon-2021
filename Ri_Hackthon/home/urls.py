
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Homepage, name ="homepage"),
    path('form/', views.form, name="form"),



]
