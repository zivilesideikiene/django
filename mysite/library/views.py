from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book, BookInstance, Author

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact="g").count

    context = {
        'num_books': num_books, #pirmas yra key num_books, antras- skaicius
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)

