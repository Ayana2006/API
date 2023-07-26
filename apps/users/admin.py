from django.contrib import admin
from apps.users.models import EmailCheckCode, User
# Register your models here.
admin.site.register(EmailCheckCode)
admin.site.register(User)