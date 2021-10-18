from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm
from .config import ADMIN_PASSWORD
# Create your views here.
import requests



def main_page(request):
    if request.method == "POST":
        text=request.POST
        url='https://api.github.com/users/'+ text['user_name']+'/repos'
        result= requests.get(url, auth=('luzanov99', ADMIN_PASSWORD))
        info=result.json()
        projects_list=list()
        for element in info:
            projects_list.append(element['name'])

        data = request.POST.copy()
        form = DataForm(data)
        if form.is_valid():
            return render(request, 'info.html', {'result':result, 'projects_list':projects_list})
        else:
            return render(request, 'main.html', {'form':form})
    else:
        form=DataForm()
        return render(request, 'main.html', {'form':form})

def info_page(request):
    info_url="https://api.github.com/zen"
    result= requests.get('https://api.github.com/users/luzanov99', auth=('luzanov99', ADMIN_PASSWORD))
    return render(request, 'info.html', {'result':result.text})
