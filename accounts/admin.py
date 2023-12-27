from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm

class UserAdmin (UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["email", "is_staff", "is_active"]
    list_filter = ["is_staff", "is_active"]
    fieldsets=(
        ("User details",{'fields':("email","password")}),
        ("Permissions",{"fields":("is_staff","is_active")}),
    )
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
    }),
    )
    search_fields=["email"]
    ordering = ["email"]
    
# Register your models here.
admin.site.register (User, UserAdmin)