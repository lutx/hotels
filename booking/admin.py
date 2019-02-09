from django.contrib import admin
from .models import *

class Hotel_ChainAdmin(admin.ModelAdmin):
    list_display = ('chain_name',)

admin.site.register(Booking)
admin.site.register(Hotel_Chain, Hotel_ChainAdmin)
admin.site.register(Hotel)
admin.site.register(Room_Type)
admin.site.register(Room)
admin.site.register(Payment)
admin.site.register(Comment)
admin.site.register(Rating)
