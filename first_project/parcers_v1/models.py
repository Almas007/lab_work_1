from django.db import models


class Resource(models.Model):
    resource_name = models.CharField(max_length=255)
    resource_url = models.CharField(max_length=255)
    top_tag = models.CharField(max_length=255)
    bottom_tag = models.CharField(max_length=255)
    title_cut = models.CharField(max_length=255)
    date_cut = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} {self.resource_name}'
    

class Items(models.Model):
    res = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True, related_name='resource_id')
    link = models.CharField(max_length=255)
    title = models.TextField()
    content = models.TextField()
    nd_date = models.CharField(max_length=255)
    s_date = models.CharField(max_length=255)
    not_date = models.CharField(max_length=255)

    
