from django.contrib import admin
from .models import Cat, Feeding
# import your models here
from .models import Cat

# Register your models here
admin.site.register(Cat)
admin.site.register(Feeding)