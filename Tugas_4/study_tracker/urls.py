from django.urls import path
from study_tracker.views import show_tracker
from study_tracker.views import create_assignment
from study_tracker.views import show_xml
from study_tracker.views import show_json
from study_tracker.views import register

app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create', create_assignment, name='create_assignment'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('register/', register, name='register'),
]
