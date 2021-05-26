from django.shortcuts import render


def main_page(request):
    return render(request, 'main.html')


def emotion(request):
    return render(request, 'emotion.html')


def timeline(request):
    return render(request, 'timeline.html')


def live_tweets(request):
    return render(request, 'live_tweets.html')


def social_impact(request):
    return render(request, 'social_impact.html')

