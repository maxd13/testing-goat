from django.shortcuts import render, redirect
from .models import Item, List
# Create your views here.


def home_page(request):
    return render(request, 'lists/home_page.html')

def new_list(request):
    if request.method != 'POST':
        return redirect('/')
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list = list_)
    return redirect(f'/lists/{list_.id}/')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', {'list': list_})

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list = list_)
    return redirect(f'/lists/{list_.id}/')
