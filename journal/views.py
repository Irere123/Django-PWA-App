from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView 
from django.db.models import Q
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.views.generic import ListView
from analytics.signals import object_veiwed_signal

# Views for rendering templates


def index(request):
    """The Home page for learning log."""
    return render(request, 'journal/index.html')

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context ={'topics': topics}
    return render(request, 'journal/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)
    object_veiwed_signal.send(topic.__class__, instance=topic, request=request)

    # Make sure the topic belongs to the current user
    if topic.owner != request.user:
       raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'journal/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; Process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('journal:topics')
    # Display a blank invalid form
    context = {'form': form}
    return render(request, 'journal/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic=Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; Process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('journal:topic', topic_id = topic_id)
    # Display a blank invalid form
    context = {'topic': topic,'form': form}
    return render(request, 'journal/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Add a new entry for a particular topic."""
    entry =Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Make sure the topic belongs to the current user
    if topic.owner != request.user:
       raise Http404
    

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance= entry)
        
    else:
        # POST data submitted; Process data.
        form = EntryForm(instance= entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal:topic', topic_id = topic.id)
    # Display a blank invalid form
    context = {'entry': entry,'topic': topic,'form': form}
    return render(request, 'journal/edit_entry.html', context)

# The About page or Info Page
def about(request):
    return render(request, 'journal/about.html')

# The About page or Info Page
def contact_us(request):
    return render(request, 'journal/contact_us.html')

#Delete post
def delete(request, pk, template_name='journal/confirm_delete.html'):
    entry= get_object_or_404(Entry, pk=pk)    
    if request.method=='POST':
        entry.delete()
        return redirect('journal:topics')
    return render(request, template_name, {'object':entry})
