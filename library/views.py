from django.shortcuts import render
from .models import Authors as a
from .models import Books as b
from .models import AuthorsBooks as ab



# Authors = [
#     {"id": 1, "Name": "Mostafa Ragab"},
#     {"id": 2, "Name": "Ahmed Mostafa"},
#     {"id": 3, "Name": "Ragab Ali"},
#     {"id": 4, "Name": "Mohamed Ragab"},
#     {"id": 5, "Name": "Ahmed Ragab"},
# ]
# Books = [
#     {"id": 1, "name": "Java Book"},
#     {"id": 2, "name": "CPP Book"},
#     {"id": 3, "name": "Python Book"},
#     {"id": 4, "name": "Great Book"},
#     {"id": 5, "name": "Fiction Book"},
# ]

# AuthorsBooks = [
#     {"BookId": 1,  "AuthorID":2 },
#     {"BookId": 1,  "AuthorID":3 },
#     {"BookId": 1,  "AuthorID":4 },
#     {"BookId": 1,  "AuthorID":1 },
#     {"BookId": 2,  "AuthorID":1 },
#     {"BookId": 4,  "AuthorID":5 },
#     {"BookId": 5,  "AuthorID":1 },
#     {"BookId": 3,  "AuthorID":1 },
# ]

DELETED_STUDENTS = [

]

def home(request):
    return render(request, 'home.html')

def book_list(request):
    result = a.objects.values()             
    Authors = [entry for entry in result]  
    result = b.objects.values() 
    Books = [entry for entry in result]
    result = ab.objects.values()     

    AuthorsBooks = [entry for entry in result]        
    return render(request, 'library/book_list.html', {"books": Books , "authors":Authors , "AuthorsBooks" : AuthorsBooks})

def author_detail(request, author_id):
    result = a.objects.values()             
    Authors = [entry for entry in result]  
    result = b.objects.values() 
    Books = [entry for entry in result]
    result = ab.objects.values()     
    AuthorsBooks = [entry for entry in result]



    author = None
    for au in Authors:
        if str(au.get("id")) == str(author_id):
            author = au
            break
    return render(request, 'library/author_detail.html', {"books": Books , "author":author , "AuthorsBooks" : AuthorsBooks})

def author_list(request):
    result = a.objects.values()             
    Authors = [entry for entry in result]  
    result = b.objects.values() 
    Books = [entry for entry in result]
    result = ab.objects.values()     
    AuthorsBooks = [entry for entry in result]    

    return render(request, 'library/author_list.html', {"books": Books , "authors":Authors , "AuthorsBooks" : AuthorsBooks})