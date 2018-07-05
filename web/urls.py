from django.urls import path

from . import views
urlpatterns = [
    path(r'submit/expense/', views.submit_expense, name="submit_expense"),
    path(r'beep/', views.beep, name="beep"),
    path(r'', views.index, name="index")
]