from django.db import models

# Create your models here.
# id(pk) 자동으로 생성됨
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]