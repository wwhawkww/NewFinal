from django.contrib import admin

from Login.models import Entry, Profile


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'level', 'links', 'description',)
    list_display_links = ('title', )
    ordering = ('-pub_date', )
    date_hierarchy = 'pub_date'
    exclude = ('pub_date', )


admin.site.register(Entry, EntryAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('groups', 'location',)
    list_display_links = ('groups', )
    ordering = ('groups', )

admin.site.register(Profile, ProfileAdmin)
