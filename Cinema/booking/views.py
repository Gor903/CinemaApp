from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from . import models
from datetime import datetime


class Template_Books(TemplateView):
    template_name: str = "booking/rooms.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        rooms = models.Room.objects.all()

        context["rooms"] = rooms

        return context


class Template_Movies(TemplateView):
    template_name: str = "booking/movies.html"

    def get_context_data(self, room_id, **kwargs):
        context = super().get_context_data(**kwargs)

        room = models.Room.objects.get(id=room_id)

        schedule = models.Schedule.objects.filter(
            room=room,
            starts_at__gt=datetime.now(),
        )

        context["schedule"] = schedule

        return context


class Template_SeatPlace(LoginRequiredMixin, TemplateView):
    template_name: str = "booking/seats.html"
    login_url: str = "/auth/login/"

    def get_context_data(self, schedule_id, **kwargs):
        context = super().get_context_data(**kwargs)

        schedule = models.Schedule.objects.get(id=schedule_id)
        room = schedule.room

        context["seats"] = [
            [
                (
                    0
                    if models.Booking.objects.filter(
                        row=i,
                        seat=j,
                        schedule=schedule,
                    ).first()
                    else 1
                )
                for j in range(room.seats)
            ]
            for i in range(room.rows)
        ]
        context["schedule_id"] = schedule_id

        return context

    def post(self, request, schedule_id, *args, **kwargs):
        seat_index = request.POST.get("seat")

        if not seat_index:
            return HttpResponse("No seat selected.")

        row, seat = map(int, seat_index.split("-"))
        schedule = models.Schedule.objects.filter(id=schedule_id).first()

        temp = models.Booking.objects.filter(
            row=row,
            seat=seat,
            schedule=schedule,
        ).first()
        if not temp:
            models.Booking.objects.create(
                user=request.user,
                schedule=schedule,
                row=row,
                seat=seat,
            )

        return redirect("seat_selection", schedule_id=schedule_id)
