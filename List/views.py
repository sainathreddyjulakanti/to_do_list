from django.shortcuts import render, redirect, get_object_or_404
from .models import Lists

def show(request):
    items = Lists.objects.all()
    return render(request, 'List/task_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        s_no = request.POST.get('S_No')
        items = request.POST.get('Items')
        
        if s_no and items:
            Lists.objects.create(S_No=s_no, Items=items)
            return redirect('task_list')
        else:
            return render(request, 'List/add.html', {'error': 'Both fields are required!'})

    return render(request, 'List/add.html')

def delete(request, S_No):
    item = get_object_or_404(Lists, S_No=S_No)
    if request.method == "POST":
        item.delete()
        return redirect('task_list')
    
    return render(request, 'List/delete.html', {'item': item})

def update(request, S_No):
    item = get_object_or_404(Lists, S_No=S_No)
    
    if request.method == "POST":
        updated_item_name = request.POST.get('Items')
        
        if updated_item_name:
            item.Items = updated_item_name
            item.save()

        return redirect('task_list')
    
    return render(request, 'List/update.html', {'item': item})
