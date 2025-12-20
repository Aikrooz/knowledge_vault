from django.contrib import admin
from .models import EntryModel
# Register your models here.
class EntryModelAdmin(admin.ModelAdmin):
    list_display=(("title","user","published","status","category"))

admin.site.register(EntryModel,EntryModelAdmin)