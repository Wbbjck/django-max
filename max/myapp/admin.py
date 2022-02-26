from django.contrib import admin
from myapp.models import (
    Protocols,
    ReestrTSZH,
    Scans
)

# Register your models here.
admin.site.register(Protocols)
admin.site.register(ReestrTSZH)
admin.site.register(Scans)