from django.shortcuts import render
from app.forms import MadlibForm


def Madlib_view(request):
    if request.method == "POST":
        form = MadlibForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            name = form.cleaned_data["name"]
            noun = form.cleaned_data["noun"]
            adjective = form.cleaned_data["adjective"]
            signed_by = form.cleaned_data["signed_by"]
            context = {
                "form": form,
                "date": date,
                "name": name,
                "noun": noun,
                "adjective": adjective,
                "signed_by": signed_by,
            }

        return render(request, "madlib.html", context)
    else:
        form = MadlibForm()
        return render(request, "madlib.html", {"form": form})
