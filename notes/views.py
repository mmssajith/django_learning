from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView


class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    template_name = 'notes/notes_form.html'
    success_url = '/smart/notes'

class NotesListView(ListView):
    model = Notes
    context_object_name = 'all_notes'
    template_name = 'notes/all_notes.html'


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/details.html'

# def all_notes(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/all_notes.html', {'all_notes': all_notes})

# def details(request, note_id):
#     try:
#         note = Notes.objects.get(id=note_id)
#     except Notes.DoesNotExist:
#         raise Http404('Note does not exist')
#     return render(request, 'notes/details.html', {'note': note})