from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

items = []

# Create your views here.

class NewFoodItemForm(forms.Form):
    food_item = forms.CharField(label="Food Item")

class NewAmountForm(forms.Form):
    amount = forms.CharField(label="Amount")

class NewExpirForm(forms.Form):
    expir = forms.DateField(label="Expiration Date")

def index(request):
    return render(request, 'pantry/index.html', {
        "items": items
    })

# add a new food item:

def add(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form1 = NewFoodItemForm(request.POST)
        form2 = NewAmountForm(request.POST)
        form3 = NewExpirForm(request.POST)

        # Check if form data is valid (server-side)
        if (form1.is_valid() and form2.is_valid() and form3.is_valid()):

            # Isolate the item from the 'cleaned' version of form data
            food_item = form1.cleaned_data["food_item"]
            amount = form2.cleaned_data["amount"]
            expir = form3.cleaned_data["expir"]

            # Add the new food item to our list of items
            new_row = {'item': food_item, 'amount': amount, 'expir': expir}
            items.append(new_row)

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("pantry:index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "pantry/add.html", {
                "form1": form1,
                'form2': form2,
                'form3': form3
            })

    return render(request, "pantry/add.html", {
        "form1": NewFoodItemForm(),
        'form2': NewAmountForm(),
        'form3': NewExpirForm()
    })

# remove a food item:

def remove(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form1 = NewFoodItemForm(request.POST)

        # Check if form data is valid (server-side)
        if (form1.is_valid()):

            # Isolate the item from the 'cleaned' version of form data
            food_item = form1.cleaned_data["food_item"]

            # Remove the food item from our list of items
            for row in items:
                if row['item'].lower() == food_item.lower():
                    items.remove(row)
                    break

            # Redirect user to list of items
            return HttpResponseRedirect(reverse("pantry:index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "pantry/remove.html", {
                "form1": form1
            })

    return render(request, "pantry/remove.html", {
        "form1": NewFoodItemForm()
    })