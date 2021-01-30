from django.db import models

# Create your models here.
class tvshow_Manager(models.Manager):
    def basic_validator(self ,value):
        errors = {}
        if len(value['title'])<=2:
            errors["title"] = "Title should be at least 2 characters"
        if len(value['network'])<=3:
            errors['network'] = 'Network Should be at least3 characters'
        if len(value['descrption'])<=10:
            errors['descrption'] = 'Descrption shold be at least 10 characters'
        return errors

class tvshow(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    releasedate=models.DateTimeField()
    descrption = models.TextField()
    objects=tvshow_Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"<tvshpw object: Title: {self.title}  NetWork : {self.network} Release Date: {self.releasedate} Descrption: {self.descrption} ({self.id})>\n"
