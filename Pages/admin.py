from django.contrib import admin
from .models import AboutUsPage ,Team,Work
# Register your models here.
@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    '''Admin View for AboutUsPage'''

    list_display = ('about',)
   
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    '''Admin View for Team'''

    list_display = ('fname','lname','role','created')
    list_filter = ('role',)
    
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    '''Admin View for Work'''

    list_display = ('title','content','created')
    