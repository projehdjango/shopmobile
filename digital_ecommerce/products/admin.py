from django.contrib import admin
from .models import product,Catgory,Image,propert,Producta

# Register your models here.
admin.site.register(Catgory)
admin.site.register(Image)
admin.site.register(propert)
#admin.site.register(Producta)
#admin.site.register(ProductFilter)


@admin.register(product)
class productadmin(admin.ModelAdmin):
    raw_id_fields = ('category',)

@admin.register(Producta)
class productadmin1(admin.ModelAdmin):
    raw_id_fields = ('image','propertya',)
