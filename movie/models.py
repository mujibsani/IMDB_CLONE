from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

CATEGORY_CHOICES = (
    ('action', 'ACTIONS'),
    ('drama', 'DRAMA',),
    ('comedy', 'COMEDY'),
    ('romance', 'ROMANCE')
)

LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('germany', 'GERMAN')
)

STATUS_CHOICES = (
    ('RA', 'RECENTLY'),
    ('MW', 'MOST WATCHES'),
    ('TR', 'TOP RATED'),
    ('CS', 'COMING SOON'),
)
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    banner=models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    years_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    cast = models.CharField(max_length=250)
    movie_trailer = models.URLField()
    slug = models.SlugField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super(Movie, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

LINK_CHOICES = (
    ('D', 'DOWNLOAD LINK'),
    ('W', 'WATCH LINK'),
)

class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return str(self.movie) + ' ' + str(self.movie)

class DownloadLink(models.Model):
    pass