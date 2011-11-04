from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)

    def __str__(self):
        return '%s' % self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    state = models.ForeignKey(State)
    
    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name_plural= 'Cities'

class Site(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    xpath = models.CharField(max_length=200)
    searchtype_param = models.CharField(max_length=20)
    state_param = models.CharField(max_length=20)
    city_param = models.CharField(max_length=20)
    range_param = models.CharField(max_length=20)
    proptype_param = models.CharField(max_length=20)
    
    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name_plural = 'Websites'
	       
    
