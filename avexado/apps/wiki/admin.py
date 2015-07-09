from django.contrib import admin
from avexado.apps.wiki.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_edited_at', )
    list_filter = ['last_edited_at', ]
    search_fields = ['content',]

admin.site.register(Page, PageAdmin)
