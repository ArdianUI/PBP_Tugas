from django.urls import path
from study_tracker.views import show_tracker, create_assignment, show_xml, show_json, register, login_user, logout_user, modify_assignment, delete_assignment, create_assignment_ajax
app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create', create_assignment, name='create_assignment'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('modify/<int:id>', modify_assignment, name='modify_assignment'),
    path('delete/<int:id>', delete_assignment, name='delete_assignment'),
    path('create-ajax/', create_assignment_ajax, name='create_assignment_ajax')
]
