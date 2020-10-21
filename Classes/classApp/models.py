from django.db import models

# Create your models here.
TITTLE_CHOICES = (
    ('Math', 'Math'),
    ('Physics', 'Physics'),
    ('Biology', 'Biology'),
    ('English', 'English'),
)



class djangoClasses(models.Model):
    title = models.CharField(max_length=60, choices=TITTLE_CHOICES)
    courseNumber = models.IntegerField(default="", blank=True, null=False)
    instructorName = models.CharField(max_length=60, default="", blank=True)
    duration = models.FloatField(default=0, null=True, blank=True)


    objects = models.Manager()

    def __str__(self):
        return self.title
