from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    stateProvince = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Authour(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=40)
    email = models.EmailField(blank=True,verbose_name="e-mail")

    def __unicode__(self):
        return u"%s %s" % (self.firstName,self.lastName)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Authour)
    publisher = models.ForeignKey(Publisher)
    publicationDate = models.DateField(blank=True,null=True)

    def __unicode__(self):
        return self.title
