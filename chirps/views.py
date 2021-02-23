from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Chirp
from .forms import ChirpForm


def main(request):
    return render(request, 'chirps/main.html')


def index(request):
    latest_chirp_list = Chirp.objects.order_by('-id')
    context = {'latest_chirp_list': latest_chirp_list}
    return render(request, 'chirps/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ChirpForm(request.POST)
        if form.is_valid():
            text = form['text']
            # id = form['id']
            chirp = Chirp(text=text)
            chirp.save()
            requests.post("https://bellbird.joinhandshake-internal.com/push", data={'chirp_id': chirp.id})
            return render(request, 'chirps/confirm.html')
    else:
        form = ChirpForm()
        return render(request, 'chirps/create.html', {'form': form})


# def upvote(request):
#     if request.method == 'POST':
