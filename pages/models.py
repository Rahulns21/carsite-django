from django.db import models

class Teams(models.Model):
    class Meta:
        verbose_name_plural = 'Teams'
        ordering = ['created_date']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} - {self.designation}'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    instagram_link = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)