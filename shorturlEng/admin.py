from django.contrib import admin
from shorturlEng.models import Urls
# Register your models here.
 
class ShorturlAdmin(admin.ModelAdmin):
    list_display = ('id','url','short_date')
    ordering = ('-short_date',)
 
admin.site.register(Urls, ShorturlAdmin)
