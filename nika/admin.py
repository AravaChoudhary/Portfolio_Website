from django.contrib import admin
from .models import cp,Visitor,Projects

# Register your models here.
admin.site.register(cp)


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address','user_agent','path','timestamp')
    list_filter = ('timestamp','path')
    search_fields = ('ip_address','user_agent')

admin.site.register(Visitor,VisitorAdmin)

admin.site.register(Projects)