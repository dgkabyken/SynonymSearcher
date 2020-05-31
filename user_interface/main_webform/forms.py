from django.forms import ModelForm, TextInput
from .models import Document

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ('text', 'document', 'word_to_search')
        #widgets = {'text': TextInput(attrs={'placeholder': 'Введите текст'})}
