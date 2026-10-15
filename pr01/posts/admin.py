from django.contrib import admin

from posts.models import Object, Galaxy, System

# Register your models here.

class GalaxyModelAdmin(admin.ModelAdmin):
    list_display=['galaxy_name', 'radius', 'age']
    list_display_links=['galaxy_name']
    list_filter=['radius', 'age']
    search_fields=['galaxy_name']
    class Meta:
        model=Galaxy

class SystemModelAdmin(admin.ModelAdmin):
    list_display=['system_name', 'radius', 'age']
    list_display_links=['system_name']
    list_filter=['radius', 'age']
    search_fields=['system_name']
    class Meta:
        model=System

class ObjectModelAdmin(admin.ModelAdmin):
    list_display=['id','object_name', 'mass', 'radius','system_name', 'galaxy_name']
    list_display_links=['object_name']
    list_filter=['id','mass', 'radius']
    search_fields=['id', 'object_name']
    class Meta:
        model=Object

admin.site.register(Galaxy, GalaxyModelAdmin)
admin.site.register(System, SystemModelAdmin)
admin.site.register(Object, ObjectModelAdmin)
