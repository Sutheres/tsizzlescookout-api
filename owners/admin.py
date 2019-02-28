from django.contrib import admin
from .models import Owner, Season
# Register your models here.


class SeasonInline(admin.TabularInline):
    model = Season
    extra = 0


class OwnerAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'phone_number', 'instagram_name', 'twitter_name', 'current_participant']
    inlines = [SeasonInline]
    list_display = ('name', 'current_participant')

admin.site.register(Owner, OwnerAdmin)