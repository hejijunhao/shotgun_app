from django.db import models

class Session(models.Model):
    restaurant = models.ForeignKey(
        'Restaurant',
        on_delete=models.CASCADE,
        related_name='sessions'
    )
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.open_time.strftime('%H:%M')} - {self.close_time.strftime('%H:%M')}"
