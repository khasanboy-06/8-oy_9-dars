from django.db import models


class Like(models.Model):
    like = models.BooleanField()

    
    
class Comment(models.Model):
    comment = models.TextField()
    
    def __str__(self):
        return self.comment


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    like = models.ForeignKey(Like, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

