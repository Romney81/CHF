from django.db import models
from django.contrib import admin
from homepage import models as hmod


admin.site.register(hmod.SiteUser)
admin.site.register(hmod.Organization)
admin.site.register(hmod.Artisan)
admin.site.register(hmod.Agent)
admin.site.register(hmod.Product)
admin.site.register(hmod.IndividualProduct)
admin.site.register(hmod.Participant)
admin.site.register(hmod.Area)
admin.site.register(hmod.SaleItem)
admin.site.register(hmod.Item)
admin.site.register(hmod.WardrobeItem)
admin.site.register(hmod.PublicEvent)
admin.site.register(hmod.Event)
admin.site.register(hmod.Venue)
admin.site.register(hmod.Order)
admin.site.register(hmod.BulkProduct)
admin.site.register(hmod.PersonalProduct)
admin.site.register(hmod.ProductPicture)
admin.site.register(hmod.BulkDetail)
admin.site.register(hmod.RentedItem)
admin.site.register(hmod.Rental)
admin.site.register(hmod.Return)
admin.site.register(hmod.PersonalDetail)
