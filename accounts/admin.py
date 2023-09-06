from django.contrib import admin
from .models import User , UserProfile

from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    list_display = ("email","username","role","phone_number")
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2'),
        }),
    )



class CustomUserProfile(admin.ModelAdmin):
     list_display = ("user","latitude" ,"longitude"  ,"created_at")



admin.site.register(User,CustomUserAdmin)
admin.site.register(UserProfile,CustomUserProfile)

