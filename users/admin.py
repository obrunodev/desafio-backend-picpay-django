from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Extras', {'fields': ('cpf', 'user_type')}),
    )

admin.site.register(User, CustomUserAdmin)