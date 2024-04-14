from django.db import models

class Track(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=220,null=True, blank=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=5, decimal_places=2)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=160)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Artist(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name    