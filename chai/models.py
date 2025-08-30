from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE =[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELAYCHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name

# one to many relationship
# the one chai will have multiple reviews so one to many
class ChaiReveiw(models.Model):
    REVIEW_CHOICES = [
        (5, 'AMAZING'),
        (4, 'EXCELLENT'),
        (3, 'GOOD'),
        (2, 'COULD HAVE BEEN BETTER'),
        (1, 'NOT SURE'),
    ]
    chai = models.ForeignKey(ChaiVarity,on_delete=models.CASCADE,related_name="reviews")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.IntegerField(choices=REVIEW_CHOICES)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
# many to many
# same chai can have multiple store like it can be present in multiple store and 
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVarity,related_name='store')
    
    def __str__(self):
        return self.name


# one to one
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity,on_delete=models.CASCADE,related_name="certificate")
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now())
    valid_until = models.DateTimeField
    
    def __str__(self):
        return f'Certificate for {self.name.chai}'

    