from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

#function based view for returning string
def fbv_string(request):
    return HttpResponse('this is function based view')


#class based view representation
class cbv_string(View):
    def get(self,request):
        return HttpResponse('This is classs based view')

#function based template view
def fbv_html(request):
    return render(request,'fbv_html.html')

#class based template view
class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')

#handling forms by using fbv

def fbv_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method == 'POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()        
            return HttpResponse('Data inserted successfully')
    return render(request,'fbv_form.html',d)

#handling forms by using cbv
class cbv_form(View):
    def get(self,request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'cbv_form.html',d)

    def post(self,request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data inserted successfully')