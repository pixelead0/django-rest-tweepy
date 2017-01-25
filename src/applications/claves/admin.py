from django.contrib import admin
from .models import Customer, Board, Command, Vehicle

admin.site.register(Customer)
admin.site.register(Board)
admin.site.register(Command)
admin.site.register(Vehicle)
