from django.db import models
from django.contrib import admin
from homepage import models as hmod


admin.site.register(hmod.SiteUser)
admin.site.register(hmod.Product)
admin.site.register(hmod.Area)
admin.site.register(hmod.Item)
admin.site.register(hmod.Event)
