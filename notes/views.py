from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from notes.forms import NoteForm
from notes.models import Note

# Create your views here.
############## ADD NOTES VIEW #############
class AddNoteView(LoginRequiredMixin,CreateView):
    template_name = 'notes/add_note.html'
    form_class = NoteForm
    model = Note
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error to create new note, try again later.')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'note added successfully done!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Note"
        return context
    
############## NOTES LIST VIEW #############   
class AllNotesView(LoginRequiredMixin, ListView):       
    template_name = 'notes/note.html'
    model = Note
    context_object_name = 'notes'