from django.contrib import admin
from .models import Candidate

# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['First_name','Last_name','Phone','Experience','Notice_period','Skill','Source','Created_at','Updated_at']

admin.site.register(Candidate,CandidateAdmin)