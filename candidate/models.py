from djongo import models
from django.forms import widgets
from django.contrib.auth.models import User
from django.conf import settings


class Candidate(models.Model):

    #Choices
    source_choices = (('RF','Referral'),('JP','Job Portal'))
    status_choices = (('pending','Pending'),('hired','Hired'),('reject','Reject'))
    skill_choices = (('python','Python'),('java','Java'))
    rating_choices = ((1,1),(2,2),(3,3),(4,4),(5,5))
    sex_choices=(('m', 'Male'), ('f', 'Female'))

    #fields
    #user = models.ForeignKey(User, related_name='User', null=True,on_delete=models.CASCADE)
    First_name = models.CharField(max_length=20,null = False,blank = False)
    Last_name = models.CharField(max_length=20,null = False,blank = False)
    Sex = models.CharField(max_length = 1,choices = sex_choices)
    Phone = models.BigIntegerField(null = False,blank = False)
    Experience = models.IntegerField(default = 2,blank = False,null =False)
    Notice_period = models.IntegerField(default = 0,blank = False,null =False)
    Skill = models.SlugField(default = 'Python',choices = skill_choices)
    Source = models.CharField(max_length = 10,choices = source_choices)

    #admin
    Status = models.CharField(default = 'Pending',max_length = 10,choices = status_choices)
    Rating = models.IntegerField(null = True,blank = True,choices = rating_choices)
    feedback = models.TextField(null = True,blank = True)
    Created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-Created_at','-Updated_at']
    
    # def get_absolute_url(self):
    #     return f"/blog/{self.slug}"

    # def __str__(self):
    #     Name = First_name + ' ' + Last_name
    #     return self.Name