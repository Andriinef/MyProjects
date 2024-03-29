# chat/views.py
from chat.models import Room
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    room, created = Room.objects.get_or_create(id=room_name)
    # messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(
        request,
        "chat/room.html",
        {
            "room_name": room_name,
            # 'messages': messages,
        },
    )
