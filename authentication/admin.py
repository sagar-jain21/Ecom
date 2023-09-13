from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from authentication.models import User
from django.contrib.auth.models import Permission


class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = [
        "email",
        "first_name",
        "last_name",
        "type",
        "is_staff"
    ]
    list_filter = ["is_staff"]
    fieldsets = [
        ("User Credentials", {"fields": [
            "email",
            "password"
            ]}),
        ("Personal info", {"fields":
                           ["first_name",
                            "last_name",
                            "type",
                            "profile_image"]
                           }),
        ("Permissions", {"fields": [
            "is_staff",
            "is_superuser",
            "is_active",
            "groups",
            "user_permissions"
            ]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "type",
                    "profile_image",
                    "password1",
                    "password2",
                ],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
# admin.site.register(User)
admin.site.register(Permission)