from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Booking(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        related_name="bookings",
    )
    schedule = models.ForeignKey(
        to="Schedule",
        on_delete=models.CASCADE,
        null=False,
        related_name="bookings",
    )
    row = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=False,
    )
    seat = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=False,
    )

    def __str__(self):
        return f"{self.user} - {self.schedule}"

    def clean(self):
        room = self.schedule.room
        if self.row > room.rows:
            raise ValidationError({"row": f"Row must not be gt {room.rows}"})
        if self.seat > room.seats:
            raise ValidationError({"seat": f"Seat must not be gt {room.seats}"})

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        unique_together = ["schedule", "row", "seat"]


class Schedule(models.Model):
    movie = models.ForeignKey(
        to="Movie",
        on_delete=models.CASCADE,
        related_name="schedules",
    )
    room = models.ForeignKey(
        to="Room",
        on_delete=models.CASCADE,
        related_name="schedules",
    )
    starts_at = models.DateTimeField()

    def __str__(self):
        return f"{self.movie} - {self.room}"

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"


class Movie(models.Model):
    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    poster = models.ImageField(
        null=False,
        upload_to="movie_posters",
    )
    duration = models.DurationField(
        null=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class Room(models.Model):
    TITLES = (
        ("Red", "Red"),
        ("Blue", "Blue"),
        ("Green", "Green"),
        # etc.
    )
    title = models.CharField(
        max_length=30,
        choices=TITLES,
        null=False,
        blank=False,
    )
    rows = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=False,
    )
    seats = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
