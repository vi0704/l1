from django.urls import path, include
from .views import LogView
urlpatterns = [
    path('', view=LogView, name='LogView'),

]