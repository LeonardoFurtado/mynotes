from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('notes/', views.get_notes, name='notes'),
    path('notes/<str:pk>/', views.get_note, name='note'),
    path('notes/<str:pk>/update', views.update_note, name='update-note'),
    path('new_note/', views.post_notes, name='new_note')
]
