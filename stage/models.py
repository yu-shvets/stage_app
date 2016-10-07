from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Events(models.Model):

    EVENT_CHOICES = (
        ('CONCERT', 'Concert'),
        ('THEATRE', 'Theatre'),
        ('CIRCUS', 'Circus'),
    )

    class Meta(object):
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['event_date']

    event_date = models.DateField(
        blank=False,
        verbose_name="Date of event",
        null=True)

    artist_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Artist's name")

    event_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name="Name of event",
        default='')

    event_place = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Place of event",
        default='')

    event_time = models.TimeField(
        blank=False,
        verbose_name=u"Time of event",
        null=True)

    poster = models.ImageField(
        blank=True,
        verbose_name="Poster",
        null=True)

    event_type = models.CharField(
        max_length=7,
        choices=EVENT_CHOICES,
        default='CONCERT')

    price = models.CharField(
        max_length=256,
        blank=True,
        verbose_name="Price",
        null=True,
    )

    notes = models.TextField(
        blank=True,
        verbose_name="Notes")

    def __unicode__(self):
        return "%s %s" % (self.artist_name, self.event_name)


class Email(models.Model):

    class Meta(object):
        verbose_name = "Email"
        verbose_name_plural = "Emails"

    mail = models.EmailField(
        max_length=254,
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return "%s" % (self.mail)