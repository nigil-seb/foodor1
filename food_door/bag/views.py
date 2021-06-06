from django.shortcuts import render, redirect, get_object_or_404
from foodoorapp.models import Item
from .models import Bag,BagItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _bag_id(request):
    bag=request.session.session_key
    if not bag:
        bag=request.session.create()
    return  bag
def add_bag(request,item_id):
    item=Item.objects.get(id=item_id)
    try:
        bag=Bag.objects.get(bag_id=_bag_id(request))
    except Bag.DoesNotExist:
        bag=Bag.objects.create(bag_id=_bag_id(request))
        bag.save()
    try:
        bag_item=BagItem.objects.get(item=item,bag=bag)
        if bag_item.quantity < bag_item.item.stock:
            bag_item.quantity +=1
        bag_item.save();
    except BagItem.DoesNotExist:
        bag_item=BagItem.objects.create(
            item=item,
            quantity=1,
            bag=bag
        )
        bag_item.save()
    return redirect('bag:bag_detail')
def bag_detail(request,total=0,counter=0,bag_items=None):
    try:
        bbag=Bag.objects.get(bag_id=_bag_id(request))
        bag_items=BagItem.objects.filter(bag=bag,active=True)
        for bag_item in bag_items:
            total +=(bag_item.item.price * bag_item.quantity)
            counter += bag_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'bag.html',dict(bag_items=bag_items,total=total,counter=counter))

def bag_remove(request,item_id):
    bag = Bag.objects.get(bag_id=_bag_id(request))
    item=get_object_or_404(Item,id=item_id)
    bag_item=BagItem.objects.get(item=item,bag=bag)
    if bag_item.quantity>1:
        bag_item.quantity-=1
        bag_item.save()
    else:
        bag_item.delete()
    return redirect('bag:bag_detail')
def full_remove(request,item_id):
    bag = Bag.objects.get(bag_id=_bag_id(request))
    item = get_object_or_404(Item, id=item_id)
    bag_item = BagItem.objects.get(item=item, bag=bag)
    bag_item.delete()
    return redirect('bag:bag_detail')
