from django.db import models

# Create your models here.

class User(models.Model):#i think Django already has a user model
    #personal info
    #username
    #email
    #Uuid // unique identifier should be a key

    pass
class Visitor(models.Model):
    Ip_address = models.CharField(max_length = 10)
    #pages_browsed = we need to get the list of pages that are accessible

class Client(models.Model):
    Uuid = models.CharField(max_length = 50,primary_key=True)
    #client_name = there is a way to refer the usermodel so we don't duplicate stuff
    current_sys_damand = models.CharField(max_length = 400)
    #current_balance
    #sys_demand_history
    #rating
class Developer(models.Model):
    Uuid = models.CharField(max_length = 50,primary_key=True)
    fullname = models.CharField(max_length=50)
    wallet = models.IntegerField()
    resume = models.FileField(upload_to="file path on system")
    sysdemand = models.CharField(max_length=500)
    Dev_since = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.fullname)
    #sysdemands taken
    #system delivered
class Bid(models.Model):
    system_demand_Details = models.CharField(max_length=500)
    bidder = models.CharField(max_length=50)#this needs review
    current_bid =  models.IntegerField()
    #time
    #is_chosen: what is this for?

class SysDemand(models.Model):

    NONE = "None"
    POSTED = "Posted"
    DELIVERED = "Delivered"
    TIMED_OUT = "Timed-out"
    STATUS = "Inprogress"
    CANCELED = "Canceled"

    status_list = ((POSTED,"Posted"),
                  (DELIVERED,"Delivered"),
                  (TIMED_OUT,"Timed-out"),
                  (STATUS,"Inprogress"),
                  (CANCELED,"Canceled"),
                   (NONE, "None"))
    time_posted = models.DateTimeField(auto_now_add=True)
    deadLine = models.DateTimeField(auto_now=True)
    #bids
    starting_price = models.IntegerField()
    #final_price
    summary = models.CharField(max_length=200)
    sysDemandName = models.CharField(max_length=20,blank=True)
    #owner = which client owns this SD
    status = models.CharField(
        max_length= 10,
        choices = status_list,
        default=NONE
    )
    def __str__(self):
        return str(self.sysDemandName)+"        [ "+str(self.status)+" ]"




