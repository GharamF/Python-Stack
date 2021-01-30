import re
import bcrypt
from django.db import models
from datetime import date

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User_Manager(models.Manager):
    def user_validate(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name']= "First Name should be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name']= "Last Name should be at least 2 characters."
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email']= "Enter a valid e-mail address."
        if len(self.filter(email=postData['email']))>0:
            errors['email'] = "This email is already used!" 
        if postData['password'] != postData['repassword']:
            errors['repassword']= "The two password fields must match."
        if len(postData['password']) < 8:
            errors['password']= "Password should be at least 8 characters."
        return errors

    def log_validate(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['e-mail']):            
            errors['e-mail']= "Enter a valid e-mail address."
        if len(postData['e-mail']) < 1:
            errors["e-mail"] = "Please provide valid email"
        if len(postData['pass']) <1 :
            errors["pass"] = "Please provide the password"
        user=self.filter(email=postData['e-mail'])
        if(len(user)<1 or (len(user)>0 and not(bcrypt.checkpw(postData['pass'].encode(), user[0].password.encode())))):
            errors["user"] = "Email or password didn't match"
        return errors

class User(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=User_Manager()
    def __str__(self):
        return f"<User object: First Name: {self.firstname}  Last Name : {self.lastname} Email: {self.email} password: {self.password} ({self.id})>\n"
