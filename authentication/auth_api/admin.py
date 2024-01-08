from django.contrib import admin
from auth_api.models import Human
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class HumanModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base HumanModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["id", "email", "name", "tnc", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["tnc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. HumanModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "tnc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []


# Now register the new HumanModelAdmin...
admin.site.register(Human, HumanModelAdmin)