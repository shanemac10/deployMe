from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt

class UserManager(models.Manager):
    def hash_new_PW(self, password_in):
        return bcrypt.hashpw(password_in.encode(), bcrypt.gensalt())

    def check_PW_DB(self, password_in, hashed_DB_password):
        return bcrypt.checkpw(password_in.encode(), hashed_DB_password.encode())

    def user_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be more than 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be more than 2 characters"

        if len(postData['email']) < 7:
            errors['email'] = "Please enter an email address"
        else:
            try:
                validate_email(postData['email'])
                email_valid = True
            except ValidationError:
                print ValidationError
                email_valid = False
                errors['email'] = "That email address does not appear to be valid"
            if email_valid:
                try:
                    User.objects.get(email=postData['email'])
                    errors['email_exists'] = "Sorry, that email address is aleady associated with an existing account"
                except :
                    email_valid = True

        if len(postData['password']) < 8:
            errors['password_len'] = "Passwords need to be at least 8 characters"
            if postData['password'] != postData['password_conf']:
                errors['passwords'] = "Your password and confirmation didn't match"

        return errors

    def try_by_email(self, postData):
        errors = {}
        if len(postData['email']) < 7:
            errors['email'] = "Please enter an email address"
        else:
            try:
                validate_email(postData['email'])
            except ValidationError:
                print ValidationError
                errors['email'] = "That email address does not appear to be valid"

        if len(postData['password']) < 8:
            errors['password_len'] = "Passwords need to be at least 8 characters"

        if len(errors):
            return errors
        else:
            try:
                tryMe = User.objects.get(email=postData['email']) # existing email?
            except :
                errors["nope"] = "Sorry, that email password combination was not recognized"
                return errors
            if User.objects.check_PW_DB( postData['password'], tryMe.password ):  #postData['password'] != tryMe.password
                return tryMe # password match success returns the User object
            else:
                errors["nope"] = "Sorry, that email password combination was not recognized"
                return errors

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
