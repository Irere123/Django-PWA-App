from django import forms
from .models import Question, Answer

class QuestionCreationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']
        labels = {'question': ''}
        widgets = {'question': forms.Textarea(attrs={'cols':44,'rows':10})}
class AnswerCreationForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer','author']
        labels = {'answer': ''}
        widgets = {'answer': forms.Textarea(attrs={'cols': 44, 'rows':10})}

