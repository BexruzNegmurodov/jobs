from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from .forms import AccountCreationForm, AccountChangeForm


class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    list_display = (
        'id', 'email', 'first_name', 'last_name', 'role', 'is_superuser', 'is_staff', 'is_active', 'modified_date',
        'created_date')
    list_filter = ('created_date', 'role', 'is_superuser', 'is_staff', 'is_active')
    date_hierarchy = 'created_date'
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('modified_date', 'created_date')
    filter_horizontal = ('groups', 'user_permissions')
    ordering = ()
    fieldsets = (
        (None, {"fields": ('password', 'first_name', 'last_name', 'avatar')}),
        ("Documents", {"fields": ('cv',)}),
        ("Permissions", {"fields": ('groups', 'user_permissions', 'role', 'is_superuser', 'is_staff', 'is_active')}),
        ("important dates", {"fields": ('modified_date', 'created_date')})
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2'), }),
    )


admin.site.register(Account, AccountAdmin)
