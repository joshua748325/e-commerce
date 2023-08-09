from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.db.models import Q
from .models import Item, Category
from item.forms import NewItemForm, EditItemForm
from django.contrib.auth.decorators import login_required

def browse(request):
    items = Item.objects.filter(is_sold=False)
    query=request.GET.get('query','')
    category_id=request.GET.get('category_id',0)
    categories=Category.objects.all()

    if category_id:
        items=Item.objects.filter(category_id=category_id)

    if query:
        items=Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category_id and query:
        items=Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query),category_id=category_id)

    return  render(request,'item/browse.html',{'items':items,'query':query,'categories':categories,'category_id':int(category_id)})

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items=Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]
    return render(request,'item/detail.html',{'item':item, 'related_items':related_items})

def category(request, category_id):
    items = Item.objects.filter(category_id=category_id).all()
    category = Category.objects.get(pk=category_id)
    return render(request,'item/category.html',{'items':items,'category':category})

@login_required
def new(request):
    if request.method=='POST':
        form=NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect(reverse('item:detail', kwargs={'pk': item.id}))        
    else:
        form = NewItemForm()
    return render(request, 'item/create_form.html',{'form':form})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect(reverse('dashboard:index'))

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method=="POST":
        form=EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:index'))
    else:
        form=EditItemForm(instance=item)
    return render(request,'item/edit_form.html',{'form':form})
