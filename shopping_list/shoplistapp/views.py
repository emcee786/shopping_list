from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def item_list(request):
    tasks = Item.objects.all()
    form = ItemForm()
    if request.method=='POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("item-list")
        
    context = {"items":tasks, "form": form}
    return render(request, 'item_list.html', context)

def item_update(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item-list")
    
    context = {"form": form}
    return render(request, 'item_list.html', context)

def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect("item-list")
    context = {"item": item}
    return render(request, 'item_delete.html', context)
