from django.shortcuts import render
from django.db.models import Avg, Max
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    num_books = books.count()
    Avg_rating = books.aggregate(Avg("rating"), Max("rating"))
    return render(request, "polls/index.html", {
        "books": books,
        "average_rating": Avg_rating,
        "num_books": num_books
    })
def book_detail(request, slug):
    single_book = Book.objects.get(slug=slug)
    return render(request, "polls/book_detail.html", {
        "single_book": single_book
    })