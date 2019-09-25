from django.db import models
class Musician(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=50)
    def __str__(self):
        return self.first_name
class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE,related_name='album_musician',null=True)
    name=models.CharField(max_length=50)
    release_date=models.DateField()
    rating=models.IntegerField()
    def __str__(self):
        return self.name
