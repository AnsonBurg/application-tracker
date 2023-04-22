from django.shortcuts import render
# from .models import Person

# Create your views here.


def home(request):
    return render(request, "base.html")


# def userInput(request):
#     if request.method == 'Person':

#     return render