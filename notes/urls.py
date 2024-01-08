from django.urls import path
from notes.views import AddNoteView,AllNotesView,EditNoteView,DeleteNoteView

urlpatterns = [
    path('', AllNotesView.as_view(), name='notes'),
    path('add_note', AddNoteView.as_view(), name='add_note'),
    path('note/<int:pk>/edit/', EditNoteView.as_view(), name='edit_note'),
    path('note/<int:pk>/delete/', DeleteNoteView.as_view(), name='delete_note'),
]
