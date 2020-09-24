from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'overview']
        labels = {'text':'', 'overview': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 40,'rows':2, 'placeholder':'Write your Topic here.'})}
        

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 42,'rows':10, 'placeholder':'Write your Entry here.'})}