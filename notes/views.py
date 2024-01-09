from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from notes.forms import NoteForm
from notes.models import Note
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

############## SEND EMAIL TO USER ########
def send_email(user,email_type,mail_subject,template):
    message = render_to_string(template, {
        'user': user,
        'type': email_type,
    })
    from_email = "NOTEBOOK <delwarjnu24@gmail.com>"
    send_email = EmailMultiAlternatives(mail_subject, '', to=[user.email], from_email=from_email, reply_to=[from_email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()

# Create your views here.
############## ADD NOTES VIEW #############
class AddNoteView(LoginRequiredMixin,CreateView):
    template_name = 'notes/add_note.html'
    form_class = NoteForm
    model = Note
    success_url = reverse_lazy('notes')

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
        queryset = Note.objects.filter(user=self.request.user, status = 1)
        return queryset
    
############## COMPLETED NOTES LIST VIEW #############   
class CompletedNotesView(LoginRequiredMixin, ListView):       
    template_name = 'notes/note.html'
    model = Note
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = Note.objects.filter(user=self.request.user, status = 2)
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
    
############## DELETE NOTES VIEW #############   
class DeleteNoteView(DeleteView):
    template_name = 'notes/delete_note.html'
    model = Note
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        messages.success(self.request, 'your note deleted successfully done!!!')
        return super().form_valid(form)
    
from datetime import datetime
def completeNote(request, pk):
    note = get_object_or_404(Note, id = pk)
    note.status = 2
    note.save()
    messages.success(request, 'congrats!!! your note completed')
    # send email feature apply here
    send_email(request.user, 'completed', 'Your note completed success message', 'notes/email.html')
    return redirect('notes')