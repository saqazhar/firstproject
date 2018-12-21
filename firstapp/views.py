from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    my_dic = {'insert' : 'This from view file in firstapp'}
    return render(request, 'index.html' , context= my_dic)
