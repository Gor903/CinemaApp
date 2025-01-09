from django.urls import path
from . import views

urlpatterns = [
    path("rooms/", views.Template_Books.as_view(), name="rooms"),
    path("movies/<int:room_id>/", views.Template_Movies.as_view(), name="movies"),
    path(
        "rooms/<int:schedule_id>",
        views.Template_SeatPlace.as_view(),
        name="seat_selection",
    ),
]
