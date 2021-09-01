from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm
# Create your views here.
import requests



def main_page(request):
    if request.method == "POST":
        text=request.POST
        url='https://api.github.com/users/'+ text['user_name']
        
        result= requests.get(url, auth=('luzanov99', '1996baba_'))
        info=result.json()
        '''
        for element in info:
            print(element['name'])
        '''
    
        return render(request, 'info.html', {'result':result.text})
    else:
        form=DataForm()
        return render(request, 'main.html', {'form':form})

def info_page(request):
    info_url="https://api.github.com/zen"
    result= requests.get('https://api.github.com/users/luzanov99', auth=('luzanov99', '1996baba_'))
    return render(request, 'info.html', {'result':result.text})
