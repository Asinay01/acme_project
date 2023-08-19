from django.contrib import admin
from .models import Birthday, Tag


class BirthdayAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    list_display_links = ('tag',)
    search_fields = ('tag',)


admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Tag, TagAdmin)
