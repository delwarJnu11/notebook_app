from django import forms 
from notes.models import Note,Tag

class NoteForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Note
        fields = ['title', 'description', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'required', 'placeholder': 'Note title...'}),
            'description': forms.Textarea(attrs={'id': 'required', 'placeholder': 'Note Description...'}),
        }