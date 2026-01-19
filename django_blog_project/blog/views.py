import random
import requests


from django.shortcuts import render
from .models import Post
from .wordle_guess_form import GuessForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def wordle(request):
    form = GuessForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            guess = form.cleaned_data["guess"]
            response = requests.get(
                "http://localhost:8081/score",
                params={
                    "guess": guess
                }
            )
            result = response.json().get("result")
        else:
            result = None
    else:
        result = None

    return render(request, 'blog/wordle.html', {'title': 'Wordle', 'result': result, 'form': form})

def projects(request):
    return render(request, 'blog/projects.html')