from django.shortcuts import redirect, render
from .models import Book,Author

# Create your views here.
def index(request):
    context={'all_books':Book.objects.all()}
    return render(request,'books.html',context)

def authors(request):
    context={'all_authors':Author.objects.all()}
    return render(request,'author.html',context)
    
def create(request):
    if request.method == "POST":
        if 'add_books' in request.POST:
            Book.objects.create(title=request.POST["Title"],desc=request.POST["Description"])
        if 'add_author' in request.POST:
            Author.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],notes=request.POST["notes"])
    return redirect('/')

def view_books(request, id):
    context={'book_data':Book.objects.get(id=id),
    'all_authors':Author.objects.exclude(books__id=id)}
    return render(request,'book_details.html',context)

def view_authors(request, id):
    context={'author_data':Author.objects.get(id=id),
    'all_books':Book.objects.exclude(authors__id=id)}
    return render(request,'Author_details.html',context)

def add(request):
    if request.method == "POST":
        id=0
        url_to=''
        if 'add_Book_auth' in request.POST:
            id=request.POST["book_id"]
            url_to="books"
            this_book = Book.objects.get(id=id)
            this_Author = Author.objects.get(id=request.POST["author_select"])
            this_Author.books.add(this_book)
        if 'add_auth_book' in request.POST:
            id=request.POST["book_id"]
            url_to="authors"
            this_author = Author.objects.get(id=id)
            this_book = Book.objects.get(id=request.POST["book_select"])
            this_book.authors.add(this_author)
    return redirect(f'/{url_to}/{id}')
