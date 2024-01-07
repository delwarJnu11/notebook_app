from django.urls import path
from notes.views import AddNoteView,AllNotesView

urlpatterns = [
    path('', AllNotesView.as_view(), name='notes'),
    path('add_note', AddNoteView.as_view(), name='add_note'),
]
