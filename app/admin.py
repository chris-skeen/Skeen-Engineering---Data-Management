from django.contrib import admin
from unfold.admin import ModelAdmin

from django.contrib.admin import register
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
# Register your models here.

admin.site.unregister(User)

@register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
  form = UserChangeForm
  add_form = UserCreationForm
  change_password_form = AdminPasswordChangeForm