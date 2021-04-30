from django.db import models


class Control(models.Model):
    name = models.CharField(max_length=20)
    state = models.BooleanField()

    def __str__(self):
        return self.name + " : " + str(self.state)
