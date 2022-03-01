from unicodedata import name
from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
from .models import Link
# Create your views here.


def scrape(request):
  if request.method == "POST":
    site = request.POST.get("site",' ')
    print(site)
    page = requests.get(site)
    soup = BeautifulSoup(page.text,'html.parser')

    for link in soup.find_all('a'):
      link_address = link.get('href')
      link_text = link.string
      Link.objects.create(address=link_address,name=link_text)
    return HttpResponseRedirect('/')
  else:
    print("Else..")
    data = Link.objects.all()

  return render(request,'myApp/result.html',{'data':data})


def clear(request):
  Link.objects.all().delete()
  return render(request,'myApp/result.html')