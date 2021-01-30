from django.db import models


# Create your models here.
class dojo(models.Model):
    name = models.CharField(max_length=255)
    city =models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    desc=models.TextField()
    def __str__(self):
        return f"<dojo object: Name: {self.name} City: {self.city} State: {self.state}  Description : {self.desc}  ({self.id})>\n"
class ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo_id = models.ForeignKey(dojo, related_name="ninjas", on_delete = models.CASCADE)
    def __str__(self):
        return f"<Ninja object: First Name: {self.first_name}  Last Name: {self.last_name} Dojo: {self.dojo_id} ({self.id})>\n"
