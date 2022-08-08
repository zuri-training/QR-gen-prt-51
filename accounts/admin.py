from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'full_name', 'is_staff']
    ordering = ('email',)
    search_fields = ('email', 'full_name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)