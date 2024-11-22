from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from app.forms import *
# Create your views here.

#FBV for returning string as response

def fbv_str(request):
    return HttpResponse('<center><h1>FBV_STRING</h1></center>')

#CBV for returning string as response

class Cbv_str(View):
    def get(self,reguest):
        return HttpResponse('<center><h1>CBV_STRING</h1></center>')



#FBV for rendering HTML Page as Response

def fbv_html(request):
    return render(request,'fbv_html.html')


#CBV for rendering HTML Page as Response By inheriting View Class
class Cbv_html(View):
    def get(self,request):
        return render(request,'Cbv_html.html')
    


#Inserting Data into category Model By using FBV

def inserting_By_Fbv(request):
    ECMFO=CategoryMF()
    d={'ECMFO':ECMFO}
    
    if request.method=='POST':
        CMFDO=CategoryMF(request.POST)
        if CMFDO.is_valid():
            CMFDO.save()
            return HttpResponse('<center><h3>Inserted Successfully</h3></center>')
        else:
            return render('<center><h2>Invalid Data Heere</h2></center>')
    return render(request,'inserting_By_Fbv.html',d)


#Inserting Data into category Model By using CBV By inheriting View Class

class Inserting_By_Cbv(View):
    def get(self,request):
        ECMFO=CategoryMF()
        d={'ECMFO':ECMFO}
        return render(request,'Inserting_By_Cbv.html',d)
    def post(self,request):
        CMFDO=CategoryMF(request.POST)
        if CMFDO.is_valid():
            CMFDO.save()
            return HttpResponse('<center><h1>Inserting of the data is successfully done</h1></center>')
        else:
            return HttpResponse('<center><h1>Invalid Data</h1></center>')


#Rendering Of Html Page By using TemplateView Class

class Renderhtml(TemplateView):
    template_name='Renderhtml.html'
    
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='charan Kumar B'
        ECDO['age']=21
        ECDO['ESFO']=SchoolForm()
        return ECDO
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Inserting successfully done')


#Sending data From frond to back end  and saving in database that taken by   Html Page By using Form Class

class SchoolFV(FormView):
    template_name='SchoolFv.html'
    form_class=SchoolForm
    def form_valid(self, form):
        form.save()
        return HttpResponse('this is from form view insertion')


    

