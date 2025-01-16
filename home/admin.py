from django.contrib import admin
from home.models import feedback
from home.models import Company_profile
from home.models import tender
from home.models import create_progress
from home.models import applications
# Register your models here.
admin.site.register(feedback)
admin.site.register(Company_profile)
admin.site.register(tender)
admin.site.register(create_progress)
admin.site.register(applications)