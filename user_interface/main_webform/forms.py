from django.forms import ModelForm, TextInput, Textarea, FileInput
from .models import Document

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ('document', 'text', 'word_to_search')
        widgets = {'text': Textarea(attrs={'rows': 10, 'cols': 200, 'placeholder': 'Введите текст'
                                           }),
                   'document': FileInput(attrs={})}
