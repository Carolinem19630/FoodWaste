from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
import datetime

items = []
user_email = ''
now = datetime.date.today()
one_week = now + datetime.timedelta(days=7)



# Create your views here.

class NewFoodItemForm(forms.Form):
    food_item = forms.CharField(label="Food Item")

class NewAmountForm(forms.Form):
    amount = forms.CharField(label="Amount")

class NewExpirForm(forms.Form):
    expir = forms.DateField(label="Expiration Date")

class NewEmailForm(forms.Form):
    email = forms.CharField(label="Email")

def index(request):
    return render(request, 'pantry/index.html', {
        "items": sorted(items, key = lambda i: i['expir']),
	'now': now,
        'one_week': one_week
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

            # Add the new item to our list of items
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

def remove(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form1 = NewFoodItemForm(request.POST)

        # Check if form data is valid (server-side)
        if (form1.is_valid()):

            # Isolate the item from the 'cleaned' version of form data
            food_item = form1.cleaned_data["food_item"]

            # Remove the item to our list of items
            for row in items:
                if row['item'].lower() == food_item.lower():
                    items.remove(row)
                    break

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("pantry:index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "pantry/remove.html", {
                "form1": form1
            })

    return render(request, "pantry/remove.html", {
        "form1": NewFoodItemForm()
    })

def email(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form1 = NewEmailForm(request.POST)

        # Check if form data is valid (server-side)
        if (form1.is_valid()):

            # Isolate the item from the 'cleaned' version of form data
            email = form1.cleaned_data["email"]

            # save the email
            user_email = email

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("pantry:index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "pantry/email.html", {
                "form1": form1
            })

    return render(request, "pantry/email.html", {
        "form1": NewEmailForm()
    })

def change(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form1 = NewFoodItemForm(request.POST)
        form2 = NewAmountForm(request.POST)

        # Check if form data is valid (server-side)
        if (form1.is_valid() and form2.is_valid()):

            # Isolate the item from the 'cleaned' version of form data
            food_item = form1.cleaned_data["food_item"]
            amount = form2.cleaned_data["amount"]

            # change the amount of the item in our items
            for row in items:
                if row['item'].lower() == food_item.lower():
                    row['amount'] = amount
                    break

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("pantry:index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "pantry/change.html", {
                "form1": form1,
                'form2': form2
            })

    return render(request, "pantry/change.html", {
        "form1": NewFoodItemForm(),
        'form2': NewAmountForm()
    })