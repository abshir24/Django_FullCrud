from django.db import models

import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    def register(self,request_object):
        errors = []

        if len(request_object['firstname']) < 2:
            errors.append('First name must be at least 2 characters long')
        
        if len(request_object['lastname']) < 2:
            errors.append('Last name must be at least 2 characters long')

        if not len(request_object['email']):
            errors.append("Email is required")
        else:
            if not EMAIL_REGEX.match(request_object['email']):
                errors.append("Enter a valid email")
        
        if len(request_object['password']) < 8:
            errors.append("Password must be at least 8 characters long")
        
        if not request_object['password'] == request_object['confirm_password']:
            errors.append("Confirm Password doesn't match Password")
        
        if self.filter(email = request_object['email']):
            errors.append("This email already belongs to a user")

        response_to_views = {}

        if len(errors) == 0:
            user = self.create(firstname = request_object['firstname'], lastname = request_object['lastname'],email = request_object['email'],password = request_object['password'])
            response_to_views['user'] =  user
            response_to_views['status'] = True
        else:
            response_to_views['errors'] = errors
            response_to_views['status'] = False
        
        return response_to_views

    def login(self,request_object):
        user = self.filter(email = request_object['email'])
        response_to_views = {}

        if not user:
            response_to_views['status'] = False
            response_to_views['errors'] = 'Email address not found'
        else:
            
            if user[0].password == request_object['password']:
                response_to_views['status'] = True
                response_to_views['user'] = user.first()

            else:
                response_to_views['status'] = False
                response_to_views['errors'] = 'Invalid Email/password combination'

        return response_to_views


class User(models.Model):
    firstname = models.CharField(max_length = 45)
    lastname = models.CharField(max_length = 45)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()


