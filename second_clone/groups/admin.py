from django.contrib import admin
from . import models


# Register your models here.
class GroupMember(admin.TabularInline):
    """docstring for GroupMember"""
    model = models.GroupMember


admin.site.register(models.Group)
