Book.objects.create(title="Brainstorm",desc="Between the ages of 12 and 24, the brain changes in important, and oftentimes maddening and challenging ways. In this book, the author, a psychiatrist busts a number of commonly held myths about adolescence")
Author.objects.create(first_name="Siegel",last_name="Daniel J.")
this_book = Book.objects.get(id=1)
this_Author = Author.objects.get(id=1)
this_Author.books.add(this_book)

Book.objects.create(title="C Sharp",desc="Between the ages of 12 and 24, the brain changes in important, and oftentimes maddening and challenging ways. In this book, the author, a psychiatrist busts a number of commonly held myths about adolescence")
Author.objects.create(first_name="Jane",last_name="Austen")



Book.objects.create(title="Java",desc="Between the ages of 12 and 24, the brain changes in important, and oftentimes maddening and challenging ways. In this book, the author, a psychiatrist busts a number of commonly held myths about adolescence")
Author.objects.create(first_name="Emily",last_name="Dickinson")



Book.objects.create(title="Python",desc="Between the ages of 12 and 24, the brain changes in important, and oftentimes maddening and challenging ways. In this book, the author, a psychiatrist busts a number of commonly held myths about adolescence")
Author.objects.create(first_name="Fyodor",last_name="Dostoevsky")



Book.objects.create(title="PHP",desc="Between the ages of 12 and 24, the brain changes in important, and oftentimes maddening and challenging ways. In this book, the author, a psychiatrist busts a number of commonly held myths about adolescence")
Author.objects.create(first_name="William",last_name="Shakespeare")


Book.objects.create(title="Ruby",desc="Between the ages of 12 and 24, the brain changes in important, and oftentimes maddening and challenging ways. In this book, the author, a psychiatrist busts a number of commonly held myths about adolescence")
Author.objects.create(first_name="Lao",last_name="Tzu")


update=Book.objects.get(id=2)
update.title="C"
update.save()

update=Author.objects.get(id=2)
update.first_name="Bill"
update.save()

this_book = Book.objects.get(id=2)
this_Author = Author.objects.get(id=2)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=3)
this_Author = Author.objects.get(id=2)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=2)
this_Author = Author.objects.get(id=3)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=3)
this_Author = Author.objects.get(id=3)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=4)
this_Author = Author.objects.get(id=3)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=2)
this_Author = Author.objects.get(id=4)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=3)
this_Author = Author.objects.get(id=4)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=4)
this_Author = Author.objects.get(id=4)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=5)
this_Author = Author.objects.get(id=4)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=2)
this_Author = Author.objects.get(id=5)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=3)
this_Author = Author.objects.get(id=5)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=4)
this_Author = Author.objects.get(id=5)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=5)
this_Author = Author.objects.get(id=5)
this_Author.books.add(this_book)

this_book = Book.objects.get(id=6)
this_Author = Author.objects.get(id=5)
this_Author.books.add(this_book)

query=Author.objects.filter(books=Book.objects.get(id=4))

this_Author = Author.objects.get(id=3)
this_book = Book.objects.get(id=4)
this_Author.books.remove(this_book)

this_book = Book.objects.get(id=3)
this_Author = Author.objects.get(id=6)
this_Author.books.add(this_book)

this_Author=Author.objects.get(id=4)
this_Author.books.all()

this_book=Book.objects.get(id=6)
this_book.Authors.all()

this_author = Author.objects.get(id=1)

