from django.shortcuts import render, HttpResponse, render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Events, Email
from django.views.generic import ListView, View, DetailView
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms import widgets

# Create your views here.


def index(request):
    if request.method == 'POST':
        email = Email(mail=request.POST['email'])
        try:
            validate_email(email)
        except Exception:
            return HttpResponseRedirect('%s?mail_message=Please, enter a valid email!' % reverse('index'))
        else:
            email.save()

            return HttpResponseRedirect('%s?mail_message=Bingo!' % reverse('events'))

    else:
        return render(request, 'index.html', {})


def search(request):
    if 'q' in request.GET and request.GET['q'].strip():
        q = request.GET['q'].strip()
        events = Events.objects.filter(artist_name__icontains=q)
        if not events:
            events = Events.objects.filter(event_place__icontains=q)
        return render_to_response('search_result.html', {'events': events, 'query': q})
    else:
        return HttpResponseRedirect('%s?search_message=Please, submit a search term' % reverse('index'))


def events(request):

    form = DateForm(request.GET, auto_id=False)
    date = form['date'].data

    if date:
        events = Events.objects.filter(event_date=date)

    else:
        events = Events.objects.all()

    return render(request, 'events.html', {'events': events, 'form': form})


def concerts(request):

    events = Events.objects.filter(event_type='CONCERT')

    return render(request, 'concerts.html', {'events': events})


def theatre(request):

    events = Events.objects.filter(event_type='THEATRE')

    return render(request, 'theatre.html', {'events': events})


def circus(request):

    events = Events.objects.filter(event_type='CIRCUS')

    return render(request, 'circus.html', {'events': events})


def contact(request):
    return render(request, 'contact.html', {})


class EventDetail(DetailView):
    model = Events
    template_name = "info.html"
    slug_field = "artist_name"
    slug_url_kwarg = 'event_artist_name'


class DateForm(forms.Form):
    date = forms.DateField(required=False,
        widget=SelectDateWidget
    )
