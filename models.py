from django.db import models

# Create your models here.

class Users(models.Model):
    #user_id = models.IntegerField(primary_key) fiaxnei mono to to primary key (id)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "Users"

            
class Group(models.Model):
    #group_id = models.IntegerField(primary_key) fiaxnei mono to to primary key (id)
    group_name = models.CharField(max_length=50)
    group_owner = models.CharField(max_length=50)
    group_description = models.CharField(max_length=250, help_text="Enter field description")
    group_members = models.CharField(max_length=500)

    class Meta:
        ordering = ['group_name']

        



    
