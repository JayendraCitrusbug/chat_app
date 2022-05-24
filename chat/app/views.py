from django.shortcuts import redirect, render
from django.views import View
from .models import Room, Message
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class CheckView(View):
    def post(self, request):
        room_name = request.POST['room_name']
        username = request.POST['username']

        if Room.objects.filter(name=room_name).exists():
            return redirect('/room/'+room_name+'/?username='+username)
        else:
            return redirect('home')


class RoomView(View):
    def get(self, request, room):
        username = request.GET.get('username')
        room_details = Room.objects.get(name=room)
        return render(request, 'room.html', {'username': username, 'room': room, 'room_details': room_details})


class SendView(View):
    def post(self, request):
        message = request.POST['message']
        username = request.POST['username']
        room_id = request.POST['room_id']

        new_message = Message.objects.create(
            value=message, user=username, room=room_id)
        new_message.save()
        return HttpResponse(f'{message} sent successfully...!')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
