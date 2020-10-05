from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from django.views.generic import ListView
from django.db.models import Q
from .forms import QuestionCreationForm, AnswerCreationForm


# Views for rendering templates
def index(request):
   """The Home page that shows all Questions asked"""
   questions = Question.objects.order_by('-pub_date')
   context = {'questions': questions}
   return render(request, 'community/index.html', context)

@login_required
def question(request, question_id):
    """Show a single question and all its answers."""
    question = Question.objects.get(id=question_id)
    answers = question.answer_set.order_by('-pub_date')
    context = {'question': question, 'answers': answers}

    return render(request, 'community/question.html', context)

@login_required
def ask_question(request):
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = QuestionCreationForm()
    else:
        # POST data submitted; Process data
        form = QuestionCreationForm(data=request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.owner = request.user
            new_question.save()
            return redirect('community:index')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'community/ask_question.html', context)

@login_required
def new_answer(request, question_id):
    question = Question.objects.get(id=question_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = AnswerCreationForm()
    else:
        # POST data submitted; process data
        form = AnswerCreationForm(data=request.POST)
        if form.is_valid():
            new_anser = form.save(commit=False)
            new_anser.question = question
            new_anser.save()
            return redirect('community:question', question_id=question_id)
    # Display a blank or invalid form
    context = {'question': question, 'form':form}
    return render(request,'community/new_answer.html', context)
 

class SearchResultsListView(ListView):
    model = Question
    context_object_name = 'question_list'
    template_name = 'community/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('search')
        return Question.objects.filter(
            Q(question__icontains =query) | Q(author__icontains = query) | Q(pub_date__icontains=query)
        )