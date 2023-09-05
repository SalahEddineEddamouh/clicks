from django.db import models
import requests
from django.utils.text import slugify
# from ckeditor.fields import RichTextField


class Meeting(models.Model):
    USER_TYPE_CHOICES = (
        ('new', 'New User'),
        ('client', 'Client'),
    )
    MEETING_CHOICES = (
        ('waiting', 'waiting'),
        ('success', 'success'),
        ('failed', 'failed'),
    )
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    market = models.CharField(max_length=250)
    note = models.TextField(blank=True)  # Note is not required
    objectif = models.CharField(max_length=255)
    userType = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='new')
    meetingStatus = models.CharField(max_length=10, choices=MEETING_CHOICES, default='waiting')
    date = models.DateField()
    time = models.TimeField()
    dateBooked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Adaccount(models.Model):
    USER_TYPE_CHOICES = (
        ('new', 'New User'),
        ('client', 'Client'),
    )
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    accountType = models.CharField(max_length=100)
    monthlySpend = models.IntegerField()
    userType = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='new')
    dateBooked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
    
    
    
    
def get_ip_location(ip_address):
    api_url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'ip': data.get('ip', ''),
            'city': data.get('city', ''),
            'region': data.get('region', ''),
            'country': data.get('country', ''),
            'loc': data.get('loc', ''),  # Latitude and longitude
        }
    else:
        return None




class VisitorLog(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    visit_date = models.DateTimeField()
    path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Article(models.Model):
    slug = models.SlugField(unique=True,max_length=200,blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()  
    Categories = models.ManyToManyField(Category)
    keywords = models.CharField(help_text='coma separeted every keyword',max_length=255,blank=True)
    meta = models.TextField()
    # image = models.ImageField(upload_to='articles_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    