from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

# Create your views here.
def FBV_string(request):
    return HttpResponse('this is FBV string')

class CBV_string(View):
    def get(self,request):
        return HttpResponse('this is CBV string')
    
def FBV_html(request):
    return render(request,'FBV_html.html')


class CBV_html(View):
    def get(self,request):
        return render(request,'CBV_html.html')
    
def FBV_forms(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method == 'POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')


    return render(request,'FBV_forms.html',d)
class CBV_forms(View):
    def get(self, request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'CBV_forms.html',d)

    def post(self, request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')

# def FBV_forms(request):
#     WFO=Webpageform()
#     d={'WFO':WFO}

#     if request.method=='POST':
#         WFD=Webpageform(request.POST)
#         if WFD.is_valid():
#             WFD.save()
#             return HttpResponse('data is inserted')
#     return render(request,'CBV_forms.html',d)