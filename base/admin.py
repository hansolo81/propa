from django.contrib import admin
from propa.base.models import *

class StateAdmin(admin.ModelAdmin):
    pass

class CityAdmin(admin.ModelAdmin):
    pass

class SiteAdmin(admin.ModelAdmin):
    pass


admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Site, SiteAdmin)

