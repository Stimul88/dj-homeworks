from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

def all_books(request):
    template = 'books/books.html'
    all_books = Book.objects.all()
    context = {'books': all_books}
    return render(request, template, context)

def date_books(request, pub_date):
    template = 'books/book.html'
    books = Book.objects.filter(pub_date=pub_date)
    paginator = Paginator(books, 10)
    page_date = request.GET.get('date')
    page = paginator.get_page(page_date)
    context = {
            'books': books,
            'page': page,
               }
    return render(request, template, context)
