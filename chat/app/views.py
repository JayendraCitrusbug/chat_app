from django.shortcuts import redirect, render
from django.views import View

# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class RoomView(View):
    def get(self, request, room):
        return render(request, 'room.html')


class CheckView(View):
    def get(self, request, room):
        return redirect('room')

    def post(self, request):
        room_name = request.POST['room_name']
        username = request.POST['username']

        print(room_name, username)
