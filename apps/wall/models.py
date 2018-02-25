from __future__ import unicode_literals
from django.db import models
from ..secrets.models import User

class SecretManager(models.Manager):
    def like(self, this_secret, user_id):
        if this_secret.likes.filter(id=user_id): # if they have already liked it?
            the_user = User.objects.get(id=user_id)
            this_secret.likes.remove(the_user)
            this_secret.likes.remove(the_user)
            this_secret.like_count = this_secret.like_count - 1
            this_secret.save()
            return False
        else: # no - add like
            the_user = User.objects.get(id=user_id)
            this_secret.likes.add(the_user)
            this_secret.like_count = this_secret.like_count + 1
            this_secret.save()
            return True

    def if_liked(self, this_secret, user): # for printitng to the template
        try:
            this_secret.likes.filter(id=user.id) # if they have already liked it?
            return True
        except : # no
            return False



    def delete(self, this_secret, user_id):
        the_user = User.objects.get(id=user_id)
        if this_secret.the_user == the_user:
            this_secret.delete()
            return "DELETED"
        else: # no - add like
            return "Something went wrong in secret.delete"

    def tell_validator(self, postData):
        errors = {}
        if len(postData['the_secret'] < 5):
            errors['longer']='You need at least characters to create a secret!'
        if len(postData['the_secret'] > 255):
            errors['longer']='Too long! You need to have under 255 characters to create a secret!'
        return errors


class Secret(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    the_secret = models.CharField(max_length=255)
    the_user = models.ForeignKey(User, related_name="secrets")
    likes = models.ManyToManyField(User, related_name="liked_secret")
    like_count = models.IntegerField(default=0)
    liked_by_this_user= models.BooleanField(default=False)
    objects = SecretManager()
