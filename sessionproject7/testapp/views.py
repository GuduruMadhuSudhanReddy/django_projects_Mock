from django.shortcuts import render
from testapp.forms import AddItemForm
# Create your views here.
def add_item_view(request):
    form = AddItemForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name] = quantity
    return render(request,'testapp/additem.html',{'form':form})

def display_items_view(request):
    return render(request,'testapp/display.html')  