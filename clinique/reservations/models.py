from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Show(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    available_seats = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, related_name='shows', null=True, blank=True)

    def __str__(self):
        return f"{self.name} on {self.date.strftime('%Y-%m-%d %H:%M')}"

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    video_url = models.CharField(unique=True, max_length=30)
    show = models.ForeignKey(Show, on_delete=models.PROTECT, related_name='videos')

    def __str__(self):
        return self.title

