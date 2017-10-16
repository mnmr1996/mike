from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Visitor)
admin.site.register(Client)
admin.site.register(Developer)
admin.site.register(User)
admin.site.register(Bid)#this can be removed, only for test
admin.site.register(SysDemand)#this can be removed, only for test