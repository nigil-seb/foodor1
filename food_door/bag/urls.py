from django.urls import path
from . import views
app_name='bag'
urlpatterns=[
    path('add/<int:item_id>/',views.add_bag,name='add_bag'),
    path('',views.bag_detail,name='bag_detail'),
    path('remove/<int:item_id>/',views.bag_remove,name='bag_remove'),
    path('full_remove/<int:item_id>/',views.full_remove,name='full_remove'),
]