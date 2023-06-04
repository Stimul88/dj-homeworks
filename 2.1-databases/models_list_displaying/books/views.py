from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from books.models import Book

def index(request):
    return redirect('books')


def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    if not pub_date == None:
        all_books = Book.objects.filter(pub_date=pub_date)
        context = {'books': all_books}
        return render(request, template, context)
    else:
        all_books = Book.objects.all()
        paginator = Paginator(all_books, 10)
        page_date = request.GET.get('date')
        page = paginator.get_page(page_date)
        context = {
            'books': all_books,
            'page': page,
                }
        return render(request, template, context)