from django.shortcuts import render

# Create your views here.

# sample function to return a value to a request
def say_hello(request):
    # here, we can pull data from db
    # we can Transform
    # we can send email
    # to call html file.
    # return HttpResponse('Hello World')
    # return render(request, 'hello.html')
    
    return render(request, 'hello.html', { 'name': 'Marvin' })

def paulo(request):
    return render(request, 'paulo.html')

def rocelle(request):
    return render(request, 'rocelle.html')