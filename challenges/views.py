from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

# def january(request):
#     return HttpResponse("Hello January...")

# def any_month(request):
#     return HttpResponse("Hello Any Month...")

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

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
