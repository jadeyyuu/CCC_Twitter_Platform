from django.shortcuts import render


def WC_current(request):
    img = 'WC_current.png'
    return render(request, './test_tmp/WC_current.html', {"WC_current": img})


def WC_previous(request):
    img = 'WC_previous.png'
    return render(request, './test_tmp/WC_previous.html', {"WC_previous": img})


def WC_before_the_previous(request):
    img = 'WC_before_the_previous.png'
    return render(request, './test_tmp/WC_before_the_previous.html', {"WC_before_the_previous": img})
