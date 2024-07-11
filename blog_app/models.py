from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    

    def __str__(self):
        return self.title

class Like(models.Model):
    like = models.BooleanField()
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.comment