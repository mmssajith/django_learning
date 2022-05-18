from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='notes'),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name='note_detail'),
    path('notes/new', views.NotesCreateView.as_view(), name='notes_create'),
]
