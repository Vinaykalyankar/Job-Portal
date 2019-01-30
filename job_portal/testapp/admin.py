from django.contrib import admin
from testapp.models import hydjobs,punejobs,chennaijobs,blorejobs
# Register your models here.

class HydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class BangJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(hydjobs, HydJobsAdmin)
admin.site.register(punejobs, PuneJobsAdmin)
admin.site.register(chennaijobs, ChennaiJobsAdmin)
admin.site.register(blorejobs, BangJobsAdmin)
