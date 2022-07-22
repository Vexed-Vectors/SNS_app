from urllib import request
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

'''
    ek groups management system banana tha.
It would have different channels where people can join and share their thoughts.
Channels can be two types public and private. Private channels can only be joined by invite.
something like discord but without the voice chat and meet features.
'''
# user ---> login/ signup

# public channels

# private channels ----> if invited

class Public_Channel(models.Model):
    pub_channel_name = models.CharField(max_length= 500, blank = False, null= True)
    channel_subject = models.CharField(max_length= 500, null =True)
    channel_members_count = models.IntegerField(default =1, null =True) 
    channel_members = models.ForeignKey(User,on_delete=models.CASCADE , null=True)
    channel_creator = models.CharField(max_length=500,null =True)
    # users, posts
    # channel creator = users[0]
    channel_date_created = models.DateTimeField(null=True)

    def __str__(self):
        return self.pub_channel_name

class Public_Posts(models.Model):
    channel = models.ForeignKey(Public_Channel, on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post_title = models.CharField(max_length= 500, null= True)
    post_date_created = models.DateTimeField(null=True)
    post_content = models.CharField(max_length=1000, null=True)
    upvotes = models.IntegerField(default =0, null=True)
    downvotes = models.IntegerField(default=0, null=True)
    def __str__(self):
        return self.post_title

class Post_Comments(models.Model):
    post = models.ForeignKey(Public_Posts, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200, null=True)
    comment_author = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self) :
        return self.comment_text
    




    

 