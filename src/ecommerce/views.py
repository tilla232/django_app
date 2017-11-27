from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm

def home_page(request):
    context = {
    "title":"Hello World!",
    "content":"Welcome to Hell"
    }
    return render(request,"home_page.html",context)

def about_page(request):
    context = {
    "title":"About",
    "content":"About dis ting"
    }
    return render(request, "home_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
    "title":"Contact",
    "content":"Call me Now",
    "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    return render(request, "contact/view.html",context)
