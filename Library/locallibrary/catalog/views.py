from django.shortcuts import render
from .models import Book,BookInstance,Genre,Author,Language
from django.views import generic

# Create your views here.

def index(request):
    """View function for the home page of the site."""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_books_word = Book.objects.filter(title__contains='and').count() 

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
        'num_genres':num_genres,
        'num_books_word':num_books_word,
        'num_visits':num_visits,
    }

    return render(request,'index.html',context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.all()
    template_name = 'books/my_arbitrary_template_name_list.html'
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    queryset = Author.objects.all()
    template_name = 'authors/my_arbitrary_template_name_list.html'
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author