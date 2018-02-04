from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm
from django.utils.translation import ugettext_lazy as _

from .models import User


class UserChangeForm(AuthUserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)

    class Meta(AuthUserChangeForm.Meta):
        model = User


class UserAdmin(AuthUserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)

    form = UserChangeForm

    fieldsets = AuthUserAdmin.fieldsets + (
        (_('Extra fields'), {'fields': ('birthday', 'number')}),
    )


admin.site.register(User, UserAdmin)
