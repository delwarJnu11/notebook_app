from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView,DeleteView
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

    def get_queryset(self):
        queryset = Note.objects.filter(user=self.request.user)
        print(queryset)
        return queryset

############## EDIT NOTES VIEW ############# 
class EditNoteView(UpdateView):
    template_name = 'notes/add_note.html'
    form_class = NoteForm
    model = Note
    success_url = reverse_lazy('notes')

    def get_queryset(self):
        queryset = Note.objects.filter(user=self.request.user)
        print(queryset)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Note"
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, 'There was an error happened, try again later!')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, 'Note updated successfully.')
        return super().form_valid(form)
    
        
class DeleteNoteView(DeleteView):
    template_name = 'notes/delete_note.html'
    model = Note
    success_url = reverse_lazy('notes')
    