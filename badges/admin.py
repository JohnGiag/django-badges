from django.contrib import admin

from badges.models import Badge,BadgeToUser

class BadgeAdmin(admin.ModelAdmin):
    list_display = ('id','level')


class BadgeToUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'badge','created')


admin.site.register(Badge, BadgeAdmin)
########################
admin.site.register(BadgeToUser,BadgeToUserAdmin)
