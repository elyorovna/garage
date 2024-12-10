from django.db import models

# Create your models here

class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Joylashish(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Cars(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='cars/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    joylash = models.ForeignKey(Joylashish, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Email(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name















