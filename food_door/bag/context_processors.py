from . models import Bag, BagItem
from .views import _bag_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return  {}
    else:
        try:
            bag=Bag.objects.filter(cart_id=_bag_id(request))
            bag_items=BagItem.objects.all().filter(bag=bag[:1])
            for bag_item in bag_items:
                item_count+=bag_item.quantity
        except Bag.DoesNotEixst:
            item_count=0
        return dict(item_count=item_count)