import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy

from musicmachine.models import Song

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_songs = Song.objects.all().count()
    
    # Songs with tempo 120
    num_songs_tempo120 = Song.objects.filter(tempo__exact=120).count()
    
    # The 'all()' is implied by default.    
    #num_creators = Author.objects.count()
    
    context = {
        'num_songs': num_songs,
        'num_songs_tempo120': num_songs_tempo120,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'musicmachine/index.html', context=context)

class SongListView(generic.ListView):
    model = Song
    paginate_by = 10
    # context_object_name = 'book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/book_list.html'  # Specify your own template name/location

    # We can override methods as so, this way of changing queryset is apparently more flexible
    # def get_queryset(self):
    #    return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war

    # We might also override get_context_data() in order to pass additional context variables to the template 
    # (e.g. the list of books is passed by default). The fragment below shows how to add a variable named 
    # "some_data" to the context (it would then be available as a template variable).

    # def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        # context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        # context['some_data'] = 'This is just some data'
        # return context

    # When doing this it is important to follow the pattern used above:
	# First get the existing context from our superclass.
	# Then add your new context information.
	# Then return the new (updated) context.

class SongDetailView(generic.DetailView):
    model = Song