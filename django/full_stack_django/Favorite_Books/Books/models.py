from django.db import models
from LogAndReg.models import User

# Create your models here.

class manger(models.Manager):
    def Book_valdate(self , postData):
        errors = {}
        if len(postData['title'])==0:
            errors['title'] = 'Title is Required'
        if len(postData['descrption'])<5:
            errors['descrption']= "descrption Should be at least 2 characters." 
        return errors

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uplouded_By=models.ForeignKey(User,related_name="books_uploaded", on_delete = models.CASCADE)    
    users_who_like = models.ManyToManyField(User, related_name = "liked_books" )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=manger()

    def __str__(self):
            return f"<book object: Title: {self.title}  descrption : {self.desc} , {self.uplouded_By}  {self.users_who_like} ({self.id})>\n"