# admin.py
from django.contrib import admin
from models import MyModel

# ... export functions will go here ...

class Data1Admin(admin.ModelAdmin):
    actions = [export_csv]

admin.site.register(Data1, Data1Admin)