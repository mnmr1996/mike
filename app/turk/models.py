from django.db import models

# Create your models here.

class user(models.Model):#i think Django already has a user model
    #username
    #email
    #Uuid // unique identifier

    pass
class visitor(models.Model):
    Ip_address = models.CharField(max_length = 10)
    #pages_browsed = we need to get the list of pages that are accessible

class client(models.Model):
    Uuid = models.CharField(max_length = 50)
    #client_name = there is a way to refer the usermodel so we don't duplicate stuff
    current_sys_damand = models.CharField(max_length = 400)
    #current_balance
    #sys_demand_history
    #rating
class developer(models.Model):
    pass
class bid(models.Model):
    pass

class SYSDEMANDS(models.Model):
    pass

class REQUESTS(models.Model):
    pass



