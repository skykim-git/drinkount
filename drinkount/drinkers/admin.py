from django.contrib import admin
from .models import Drinker

# Register your models here.

class DrinkerAdmin(admin.ModelAdmin):
      list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Drinker, DrinkerAdmin)

