from django.contrib import admin
from .models import Persons, State


# Register your models here.
class PersonsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'state')
    list_display_links = ('name',)
    search_fields = ('name', 'address', 'phone', 'state')


admin.site.register(Persons, PersonsAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(State, StateAdmin)
