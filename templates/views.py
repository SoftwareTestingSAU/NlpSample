from django.shortcuts import render
from django.http import HttpResponse
from NlpSample.models import Metin

def index(request):
    if request.method == "POST":
        metin = Metin(request.POST)
        if metin.is_valid():    
            if metin.tur_getir() == 'fiiller':
                fiilerstr = ', '.join(metin.fiiller_getir())
                return render(request,'Sonuc.html',{'tur' : 'Fiiller','ifadeler' : fiilerstr})
            else:
                isimlerstr = ', '.join(metin.isimler_getir())
                return render(request,'Sonuc.html',{'tur' : 'isimler','ifadeler' : isimlerstr})
    
    else:
        metin = Metin()
        return render(request,'index.html',{'metin' : metin})
