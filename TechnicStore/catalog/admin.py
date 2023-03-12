from django.contrib import admin
from django.utils.safestring import mark_safe

from catalog.models import Products, ProductsBrand, ProductsType, ProductsImg, ProductAttributes, ValueProductAttributes


class ProductsImgAdmin(admin.ModelAdmin):
    list_display = ('get_img', )
    fields = ('img', 'get_img', )
    readonly_fields = ('get_img', )

    def get_img(self, obj):
        return mark_safe(f"<div class='div_img_admin'> <img src='/{obj.img}' class='img_admin'> </div>")

    get_img.short_description = 'Зображення'


class ValueProductAttributesAdmin(admin.ModelAdmin):
    list_display = ('value', )
    list_display_links = ('value', )
    search_fields = ('value', )


class ProductAttributesAdmin(admin.ModelAdmin):
    list_display = ('attribute', 'value')
    list_display_links = ('attribute', )
    search_fields = ('attribute', )


class ProductsTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'get_characteritic')
    list_display_links = ('type', )
    search_fields = ('type', )

    def get_characteritic(self, obj):
        return "\n".join([c.attribute for c in obj.characteristic.all()])

    get_characteritic.short_description = 'Характеристики'


class ProductsBrandAdmin(admin.ModelAdmin):
    list_display = ('brand', )
    list_display_links = ('brand', )
    search_fields = ('brand', )


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'get_img', 'amount')
    list_display_links = ('title', )
    list_editable = ['amount']
    search_fields = ('title', )
    fields = ('title', 'price', 'type', 'brand',
              'amount', 'img', 'get_img')
    readonly_fields = ('get_img', )
    filter_horizontal = ('img',)

    def get_img(self, obj):
        context = ''
        try:
            for p in obj.img.all():
                context += f"<div class='div_img_admin'> <img src='{p.img.url}' class='img_admin'> </div>"
        except TypeError:
            pass
        return mark_safe(context)

    get_img.short_description = 'Зображення'


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductsBrand, ProductsBrandAdmin)
admin.site.register(ProductsType, ProductsTypeAdmin)
admin.site.register(ProductsImg, ProductsImgAdmin)
admin.site.register(ProductAttributes, ProductAttributesAdmin)
admin.site.register(ValueProductAttributes, ValueProductAttributesAdmin)
