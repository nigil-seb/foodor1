from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
from.models import Category,Item


# def home(request):
#     return HttpResponse('hrllo')
def allItmCat(request,c_slug=None,):
    c_page = None
    items_list = None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug,)
        items_list=Item.objects.filter(category=c_page,available=True)
    else:
        items_list=Item.objects.all().filter(available=True)
    paginator=Paginator(items_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        items=paginator.page(page)
    except(EmptyPage,InvalidPage):
        items=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'category':c_page,'items':items})

def ItemCatDetail(request,c_slug,item_slug):
    try:
        item=Item.objects.get(category__slug=c_slug,slug=item_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'item':item})