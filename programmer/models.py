from django.db import models


# Create your models here.


class Programmer(models.Model):
    name = models.CharField(max_length=250)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'programmer/{0}/{1}'.format(instance.programmer.id, filename)


class Language(models.Model):
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to=user_directory_path)
