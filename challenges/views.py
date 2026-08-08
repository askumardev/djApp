from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
monthly_challenges = {
    "january": "Hello January...",
    "february": "Hello February...",
    "march": "Hello March...",
    "april": "Hello April...",
    "may": "Hello May...",
    "june": "Hello June...",
    "july": "Hello July...",
    "august": "Hello August...",
    "september": "Hello September...",
    "october": "Hello October...",
    "november": "Hello November...",
    "december": "Hello December..."
}

# def january(request):
#     return HttpResponse("Hello January...")

# def any_month(request):
#     return HttpResponse("Hello Any Month...")

def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported...")
    return HttpResponse(text)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month < 1 or month > len(months):
        return HttpResponseNotFound("Month number out of range...")
    month = months[month - 1]
    return HttpResponseRedirect(f"/challenge/{month}")