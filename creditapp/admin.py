from django.contrib import admin
from .models import User,TransferHistory
# Register your models here.

admin.site.register(User)
admin.site.register(TransferHistory)
