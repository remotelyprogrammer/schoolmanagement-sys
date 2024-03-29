from django.contrib import admin
from .models import PersonalInfo, Address, Contact

admin.site.register(PersonalInfo)
admin.site.register(Address)
admin.site.register(Contact)