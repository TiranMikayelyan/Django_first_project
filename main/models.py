from django.db import models

# Create your models here.


class Main(models.Model):
    name = models.CharField('Site name', max_length=50)
    text = models.TextField("Enter your text")
    button1 = models.CharField('main button name', max_length=30)
    button2 = models.CharField('Home button name', max_length=30)
    button3 = models.CharField('what we do button name', max_length=30)
    button4 = models.CharField('testimionals button name', max_length=30)
    button5 = models.CharField('Gallery  button name', max_length=30)
    button6 = models.CharField('Contact button name', max_length=30)

    def __str__(self) -> str:
        return self.name
    
class Testimonials(models.Model):
    image = models.ImageField('Worker image', upload_to='image')
    about = models.TextField('CV Worker')
    names = models.TextField('worker name')
    def __str__(self) -> str:
        return self.names
    
class Gallery(models.Model):
    image = models.ImageField(' image', upload_to='image')
    button = models.TextField('button name', max_length=50)
    
    def __str__(self) -> str:
        return self.button
    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

class Gall(models.Model):
    name = models.CharField('Gallery name', max_length=50)
    text = models.TextField("Enter your text")

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    name = models.CharField('Contact name', max_length=50)
    email = models.CharField('Contact email', max_length=50)
    message = models.TextField('Contact message')
    def __str__(self) -> str:
        return self.name



class last(models.Model):
    pname = models.CharField('page name', max_length=50)
    text = models.TextField("Enter your text")
    button = models.CharField('chat name',max_length=30)
    button2 = models.CharField('location name',max_length=30)
    button1 = models.CharField('mail name',max_length=30)
    button3 = models.CharField('number ',max_length=30)
    def __str__(self) -> str:
        return self.pname
    
