from django.contrib import admin
from .models import Account



# Register your models here.
class UserAdmin(admin.ModelAdmin):
    exclude =('password','Groups')
    list_display = (
        'email', 'fname', 'lname', 'last_login', 'is_active', 'date_joined'
    )
    list_display_links = (
        'email', 'fname', 'lname',
    )
    readonly_fields = (
        'last_login', 'date_joined',
    )
    ordering = (
        '-date_joined',
    )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

        # This will help you to disable delete functionaliyt

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Account,UserAdmin)
