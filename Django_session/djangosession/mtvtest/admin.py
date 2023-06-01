from django.contrib import admin
from .models import COUNT_TB

# Register your models here.
class CountAdmin(admin.ModelAdmin):
    list_display=(
        'count_num',
    )
    
admin.site.register(COUNT_TB,CountAdmin)