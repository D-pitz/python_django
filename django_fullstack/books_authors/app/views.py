from django.shortcuts import render, HttpResponse, redirect
from app.models import Book, Author

def index(request):
    context = {
        'books': Book.objects.all()
    }

    return render(request, 'index.html', context)

def create_book(request):#process to add book to index page
    print(request.POST)
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/')

def view_book(request, books_id):
    v_book = Book.objects.get(id=books_id)
    auth = Author.objects.all()
    not_auth = Author.objects.exclude(books__id = books_id).all()
    print(not_auth.all())

    context = {
        'v_book': v_book,
        'auth': auth,
        'not_auth': not_auth
    }
    return render(request, 'view_book.html', context)

def add_auth(request, book_id): # process view to add auth to book
    if request.POST['auth_id'] == '-1':
        return redirect(f'/books/{book_id}')
    book_same = Book.objects.get(id=book_id)
    add_auth = Author.objects.get(id=request.POST['auth_id'])
    # (**COMMON PROBLEM**)if this does not update on server:
    # shut down server --> close browser tab, restart server and browser.
    book_same.authors.add(add_auth)
    return redirect(f'/books/{book_id}')

def delete_auth_from_book(request, book_id, auth_id):
    auth_to_delete = Author.objects.get(id=auth_id)
    from_book = Book.objects.get(id=book_id)
    print(from_book, auth_to_delete)
    from_book.authors.remove(auth_to_delete)
    #.delete does not work with M-M relationship. Must use .remove()
    return redirect(f'/books/{book_id}')

def return_home_book(request):
    return redirect('/')
    
def author_home(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'author_home.html', context)

def create_auth(request):#process to add author to author home page
    # print(request.POST)
    Author.objects.create(
        first_name= request.POST['first_name'],
        last_name= request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/author_home')
        

def view_author(request, auth_id):
    v_auth = Author.objects.get(id=auth_id)
    book = Book.objects.all()
    not_book = Book.objects.exclude(authors__id = auth_id).all()
    # print(not_auth.all())

    context = {
        'v_auth': v_auth,
        'book': book,
        'not_book': not_book
    }
    return render(request, 'view_author.html', context)

def add_book(request, auth_id): # process view to add book to author
    if request.POST['book_id'] == '-1':
        return redirect(f'/author/{auth_id}')
    auth_same = Author.objects.get(id=auth_id)
    add_book = Book.objects.get(id=request.POST['book_id'])
    # (**COMMON PROBLEM**)if this does not update on server:
    # shut down server --> close browser tab, restart server and browser.
    auth_same.books.add(add_book)
    return redirect(f'/author/{auth_id}')

def delete_book_from_auth(request, auth_id, book_id):
    book_to_delete = Book.objects.get(id=book_id)
    from_auth = Author.objects.get(id=auth_id)
    from_auth.books.remove(book_to_delete)
    #.delete does not work with M-M relationship. Must use .remove()
    return redirect(f'/author/{auth_id}')

def delete_author(request, auth_id):
    auth_to_delete = Author.objects.get(id=auth_id)
    auth_to_delete.delete()
    return redirect('/author_home')

def delete_book(request, book_id):
    book_to_delete = Book.objects.get(id=book_id)
    book_to_delete.delete()
    return redirect('/')