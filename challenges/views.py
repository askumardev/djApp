from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

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
        # resp = render_to_string("challenges/challenge.html", {
        #     "text": text,
        #     "month_name": month.capitalize()
        # })
        return render(request, "challenges/challenge.html", {
            "text": text,
            "month_name": month.capitalize()})
    except:
        return HttpResponseNotFound("This month is not supported...")
    return HttpResponse(resp)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month < 1 or month > len(months):
        return HttpResponseNotFound("Month number out of range...")
    month = months[month - 1]
    return HttpResponseRedirect(reverse("monthly-challenge", args=[month]))

def index(request):
    list_items = ""
    for month in monthly_challenges:
        month_url = reverse("monthly-challenge", args=[month])
        list_items += f"<li><a href=\"{month_url}\">{month.capitalize()}</a></li>\n"

    data = f"""
    <h1>Monthly Challenges</h1>
    <ul>
        {list_items}
    </ul>
    """
    return HttpResponse(data)
