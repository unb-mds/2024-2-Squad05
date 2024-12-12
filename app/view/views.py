from django.shortcuts import render
import sys
from app.manipulation.sentiment_analysys import analyze_sentiment, str_response


def index(request):
    if request.method == "POST":
        # Get the form data
        form_data = request.POST.get("comment")

        # Do something with the form data
        result = analyze_sentiment(form_data)
        if result == -1:
            result = "Invalid comment"

        # Return the response
        return render(request, "index.html", {"sentiment_result": str_response(result)})

    # If the request is not POST, render the index.html template
    return render(request, "index.html")
