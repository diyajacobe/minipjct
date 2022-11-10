from django.contrib import admin
# import admin_thumbnails


# Register your models here.

from .models import House_Product, Car_Product, Bike_Product, Other_Product,Furn_Product,Category


class CatAdmin(admin.ModelAdmin):
    list_display = (
        'thumbnail_preview5',
        'category_name',
        'description',
    )
    # prepopulated_fields = {'slug': ('ad_title',)}





    def thumbnail_preview5(self, obj):
        return obj.thumbnail_preview5
    thumbnail_preview5.short_description = 'Image Preview'
    thumbnail_preview5.allow_tags = True


admin.site.register(Category,CatAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'thumbnail_preview',

        'ad_title',
        'rent',
        'type',
        'furnish',
        'bedroom',
        'bathroom',
        'user',
        'created_date',
        'is_available',
    )
    # prepopulated_fields = {'slug': ('ad_title',)}

    list_editable = ['is_available']

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

        # This will help you to disable delete functionaliyt

    def has_delete_permission(self, request, obj=None):
        return False


    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview
    thumbnail_preview.short_description = 'Image Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(House_Product,ProductAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = (
        'thumbnail_preview1',

        'ad_title',
        'rent',
        'brand',
        'fuel',
        'own',
        'user',
        'created_date',
        'is_available',
    )
    # prepopulated_fields = {'slug': ('ad_title',)}

    list_editable = ['is_available']

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

        # This will help you to disable delete functionaliyt

    def has_delete_permission(self, request, obj=None):
        return False


    def thumbnail_preview1(self, obj):
        return obj.thumbnail_preview1
    thumbnail_preview1.short_description = 'Image Preview'
    thumbnail_preview1.allow_tags = True

admin.site.register(Car_Product,CarAdmin)

class BikeAdmin(admin.ModelAdmin):
    list_display = (
        'thumbnail_preview2',
        'ad_title',
        'rent',
        'brand',
        'own',
        'user',
        'created_date',
        'is_available',
    )
    # prepopulated_fields = {'slug': ('ad_title',)}

    list_editable = ['is_available']

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

        # This will help you to disable delete functionaliyt

    def has_delete_permission(self, request, obj=None):
        return False


    def thumbnail_preview2(self, obj):
        return obj.thumbnail_preview2
    thumbnail_preview2.short_description = 'Image Preview'
    thumbnail_preview2.allow_tags = True

admin.site.register(Bike_Product,BikeAdmin)

class FurnAdmin(admin.ModelAdmin):
    list_display = (
        'thumbnail_preview3',
        'ad_title',
        'type',
        'rent',
        'user',
        'created_date',
        'is_available',
    )
    # prepopulated_fields = {'slug': ('ad_title',)}

    list_editable = ['is_available']

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

        # This will help you to disable delete functionaliyt

    def has_delete_permission(self, request, obj=None):
        return False


    def thumbnail_preview3(self, obj):
        return obj.thumbnail_preview3
    thumbnail_preview3.short_description = 'Image Preview'
    thumbnail_preview3.allow_tags = True

admin.site.register(Furn_Product,FurnAdmin)

class OtherAdmin(admin.ModelAdmin):
    list_display = (
        'thumbnail_preview4',
        'ad_title',
        'rent',
        'user',
        'created_date',
        'is_available',
    )
    # prepopulated_fields = {'slug': ('ad_title',)}

    list_editable = ['is_available']

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

        # This will help you to disable delete functionaliyt

    def has_delete_permission(self, request, obj=None):
        return False


    def thumbnail_preview4(self, obj):
        return obj.thumbnail_preview4
    thumbnail_preview4.short_description = 'Image Preview'
    thumbnail_preview4.allow_tags = True

admin.site.register(Other_Product,OtherAdmin)
