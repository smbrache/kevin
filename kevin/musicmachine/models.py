from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date


class Song(models.Model):
    """Model representing a single saved song"""

    # Fields
    title = models.CharField(max_length=30, help_text='Enter song title')
    creator = models.CharField('Creator', max_length=16, help_text='<a href="https://www.kevin.com/musicmachine/creators/creator_id">Creator profile</a>')# TODO: make this link to creator profile
    tempo = models.IntegerField('Tempo', validators=[MaxValueValidator(300)])
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the song')
    file = models.FileField()
    creation_date = models.DateField(null=True, blank=True)

    # Metadata
    class Meta: 
        ordering = ['creator', 'title']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Song."""
        return reverse('song-detail', args=[str(self.id)])

   	# TODO: add get_creator_url for above creator field link?
    
    def __str__(self):
        """String for representing the Song object (in Admin site etc.)."""
        return self.title

