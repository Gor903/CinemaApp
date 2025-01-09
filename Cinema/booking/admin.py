from django.contrib import admin
from .models import (
    Movie,
    Room,
    Schedule,
    Booking,
)

admin.site.register(Movie)
admin.site.register(Room)
# delete bellow
admin.site.register(Schedule)
admin.site.register(Booking)
