from django.contrib import admin

from users_page.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'is_superuser')
    list_display_links = ('id', 'first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_editable = ['is_superuser']
    filter_horizontal = ('like', 'comparison')
    

admin.site.register(User, UserAdmin)
