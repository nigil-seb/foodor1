from django.urls import path
from . import views
app_name ='foodoorapp'
urlpatterns=[
    path('',views.allItmCat,name='allItmCat'),
    path('<slug:c_slug>/',views.allItmCat,name='items_by_category'),
    path('<slug:c_slug>/<slug:item_slug>/',views.ItemCatDetail,name='ItemCatDetail'),
]