from django.contrib import admin

from .models import RescueInfo, SocialMedia
# Register your models here.
class RescueInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', 'website', 'email', 'nonprofit_ein')
        }),
        ('PO Box Address',{
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('display_poboxaddress','pobox_number', 'poboxcity', 'poboxstate', 'poboxzip')
        }),
        ('Street Address',{
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('display_regaddress','address1','address2', 'city', 'state', 'zipcode')
        }),
    )
admin.site.register(SocialMedia)
admin.site.register(RescueInfo, RescueInfoAdmin)