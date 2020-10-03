from django.contrib import admin
from .models import (Cuboid,FilterLength,FilterWidth,FilterHeight,FilterArea,FilterVolume)

# Register your models here.

register_model = [Cuboid,FilterLength,FilterWidth,FilterHeight,FilterArea,FilterVolume]

admin.site.register(register_model)
