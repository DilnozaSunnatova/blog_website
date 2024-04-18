from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.name
    

class Project(models.Model):
    name = models.CharField(max_length = 80)
    description = models.TextField()
    poster = models.ImageField(upload_to="project/")
    link = models.URLField(max_length = 80)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    completed_at = models.DateField(null=True)

    def __str__(self) -> str:
        return self.name
    

class Profile(models.Model):
    full_name = models.CharField(max_length = 80,verbose_name="To'liq ism")
    bio = models.TextField()
    image = models.ImageField(upload_to="profile/")
    link = models.URLField()

    def __str__(self) -> str:
        return self.full_name

class Skill(models.Model):
    name = models.CharField(max_length=80)
    percentage = models.IntegerField(default=0)
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=80)
    icon = models.CharField(max_length=80)
    order = models.IntegerField(default=1)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    

class Blog(models.Model):
    title = models.CharField(max_length=80)
    published_at = models.DateField(auto_now=True)
    poster = models.ImageField(upload_to="blog/")
    author = models.CharField(max_length=80)
    description = models.TextField()

    view_count = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.title
    

class About(models.Model):
    body = models.TextField()
    amount = models.FloatField(default = 0)
    project_count = models.IntegerField(default=0)
    customer_count = models.IntegerField(default=0)



    def __str__(self) -> str:
        return str(self.id)




# Create your models here.
