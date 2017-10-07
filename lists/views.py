from django.shortcuts import render, redirect
from .models import Item
# Create your views here.


def home_page(request):
    if request.method == 'POST':
        return home_page_POST(request)
    items = Item.objects.all()
    return render(request, 'lists/home_page.html', {'items': items})


def home_page_POST(request):
    item = Item()
    item.text = request.POST.get('item_text', '')
    if item.text:
        item.save()
    return redirect('/') #return render(request, 'lists/home_page.html', {'new_item_text': item.text})

