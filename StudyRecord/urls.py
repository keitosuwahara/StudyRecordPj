from django.urls import path
from .views import index

app_name = "StudyRecord"
urlpatterns = [
    path("", index, name="index"),
    
]