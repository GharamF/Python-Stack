from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return f"<book object: Title: {self.title}  decrption : {self.desc} Author: {self.authors} ({self.id})>\n"
class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    book = models.ManyToManyField(Books, related_name="authors")
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return f"<author object: First Name : {self.first_name}  Last Name : {self.last_name} Books: {self.book} ({self.id})>\n"
