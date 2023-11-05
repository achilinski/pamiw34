import json
import requests
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from pamiw3.forms import BookForm

urlSetting = json.loads(open("./api/appsetting.json").read())
urlSetting = urlSetting['ApiSettings']

def index(request):
    context = {}
    return render(request,'home.html', context)

def allBooksView(request):
    bookList = requests.get(urlSetting['BaseUrl'] + urlSetting['GetAllUrl'])
    bookList = bookList.json()
    context = {}
    return render(request,"allBooks.html",{"data" : bookList})

def bestBooks(request):
    bookList = requests.get(urlSetting['BaseUrl'] + urlSetting['BestRatingUrl'])
    bookList = bookList.json()
    context = {}
    return render(request,"bestBooks.html",{"data" : bookList})

def newestBooks(request):
    bookList = requests.get(urlSetting['BaseUrl'] + urlSetting['NewestBooksUrl'])
    bookList = bookList.json()
    context = {}
    return render(request,"newestBooks.html",{"data" : bookList})

def bookView(request, id):
    book = requests.get(urlSetting['BaseUrl'] + urlSetting["GetBookByIdUrl"], params= {"id" : id})
    book = book.json()
    print(book)


    return render(request, "bookView.html", {"book" : book[0]})

def deleteBookButton(request,book_id):
    url = urlSetting['BaseUrl'] + "book/" + str(book_id) + "/" + urlSetting['DeleteBookUrl']
    print(url)
    if request.method == 'POST':
        print("chuj")
        response = requests.delete(url)
        if response.status_code == 202:
            return redirect('/')
        else:
            return JsonResponse({'status': 'error'}, status=response.status_code)

    return HttpResponseRedirect('/')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book_data = form.cleaned_data
            book_data['date_of_publishing'] = book_data['date_of_publishing'].isoformat()
            api_url = urlSetting['BaseUrl'] + urlSetting['AddNewBookUrl']
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.post(api_url, data=json.dumps(book_data), headers=headers)
            if response.status_code == 200:
                print("Book successfully created")
            else:
                print("Failed to create book", response.status_code, response.text)
            return redirect('/')
    else:
        form = BookForm()

    return render(request, 'addBook.html', {'form': form})

def edit_book(request, book_id):
    response = requests.get(urlSetting['BaseUrl'] + urlSetting["GetBookByIdUrl"], params= {"id" : book_id})

    if response.status_code == 200:
        book_data = response.json()[0]

        if request.method == 'POST':
            form = BookForm(request.POST)
            print(form)

            if form.is_valid():
                book_data = form.cleaned_data
                book_data['date_of_publishing'] = book_data['date_of_publishing'].isoformat()
                api_url = urlSetting['BaseUrl']+"book/"+ str(book_id) +"/" + urlSetting['UpdateBookUrl']
                headers = {
                    'Content-Type': 'application/json'
                }
                response = requests.post(api_url, data=json.dumps(book_data), headers=headers)
                if response.status_code == 200:
                    print("Book successfully created")
                else:
                    print("Failed to create book", response.status_code, response.text)
                return redirect('/')
        else:
            form = BookForm(initial=book_data)
    else:
        form = BookForm()

    return render(request, 'editbook.html', {'form': form})

