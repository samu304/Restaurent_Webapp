from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.fname
    
    class Meta:
        verbose_name_plural = "Contact Table"

class AboutUs(models.Model):
    title1 = models.CharField(max_length=100)
    desc1 = models.TextField()
    title2 = models.CharField(max_length=100,default=None)
    desc2 = models.TextField(default=None)
    title3 = models.CharField(max_length=100,default=None)
    desc3 = models.TextField(default=None)

    ceo_name = models.CharField(max_length=100,default=None)
    ceo_desc = models.TextField(default=None)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title1

    class Meta:
        verbose_name_plural = 'About Us'