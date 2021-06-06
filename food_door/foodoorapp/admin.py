from django.contrib import admin
from .models import Category,Item
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','update','image']
    list_editable = ['price','stock','available','image']

    prepopulated_fields = {'slug':('name',)}
admin.site.register(Item,ItemAdmin)