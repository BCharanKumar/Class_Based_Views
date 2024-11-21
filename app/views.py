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


#CBV for rendering HTML Page as Response

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


#Inserting Data into category Model By using CBV

class Inserting_By_Cbv(View):
    def get(self,request):
        ECMFO=CategoryMF()
        d={'ECMFO':ECMFO}
        return render(request,'inserting_By_Cbv.html',d)
    
    def post(self,request):
        CMFDO=CategoryMF(request.POST)
        if CMFDO.is_valid():
            CMFDO.save()
            return HttpResponse('<center><h1>Inserted Successfully</h1></center>')
        else:
            return render('<center><h2>Invalid Data Heere</h2></center>')