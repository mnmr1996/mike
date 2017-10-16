from django.db import models

# Create your models here.

class User(models.Model):#i think Django already has a user model
    #username
    #email
    #Uuid // unique identifier

    pass


class Visitor(models.Model):
    Ip_address = models.CharField(max_length = 10)
    #pages_browsed = we need to get the list of pages that are accessible


class Client(models.Model):
    Uuid = models.CharField(max_length = 50)
    #client_name = there is a way to refer the usermodel so we don't duplicate stuff
    current_sys_damand = models.CharField(max_length = 400)
    #current_balance
    #sys_demand_history
    #rating


class Developer(models.Model):
    pass


class Bid(models.Model):
    pass


class SYSDEMANDS(models.Model):
    pass

class REQUESTS(models.Model):
    pass



