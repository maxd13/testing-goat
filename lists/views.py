from django.shortcuts import render, redirect
from .models import Item
# Create your views here.


def home_page(request):
    if request.method == 'POST':
        return home_page_POST(request)
    return render(request, 'lists/home_page.html')


def home_page_POST(request):
    item = Item()
    item.text = request.POST.get('item_text', '')
    if item.text:
        item.save()
    return redirect('/lists/the-only-list-in-the-world/')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})
