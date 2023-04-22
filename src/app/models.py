from django.db import models
# import datetime

# Create your models here.
class Person(models.Model):
    # id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email_address = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 30)
    bday = models.DateField()

class Position(models.Model):
#     id = models.IntegerField(primary_key = True)   
#     person_id = models.ForeignKey(Person, on_delete = models.CASCADE, related_name = 'id')
    position_title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 50)
    experience_required = models.CharField(max_length = 100)
    application_link = models.CharField(max_length = 100)
    applied = models.BooleanField()

    
    owner_user = models.CharField(max_length = 50)
    

    # if applied == 1 :
    #     date_applied = models.DateField()
    #     result = models.CharField(max_length = 10)
    #     interview_date = models.DateField()
            
    
    # if_applied = Person.objects.filter(applied = 1)
    # class HeardBack(models.HeardChoices):
    #     NO = 0, ("No")
    #     YES = 1, ("Yes")

    #     empty = ("(Unknown)")


    # class Result(models.ResultChocies):
    #     NO = 0, ("No")
    #     YES = 1, _("Yes")

    #     empty = _("(Unknown)")

instance_1 = Person(first_name='Anson', last_name='Burg', email_address='anson@gmail.com', address='123 Warner Ave', city='chico', bday= '1999-08-10')
instance_2 = Person(first_name = 'Sarah', last_name = 'Blotcky', email_address = 'scblotcky@cuschico.edu', address = '456 Warner Ave', city = 'Chico', bday = '1997-06-26')
instance_3 = Person(first_name = 'John', last_name = 'Doe', email_address = 'jdoe@csuchico.edu', address = '000 Warner Ave', city = 'Chico', bday = '2023-04-22')

instance_4 = Position(position_title = 'Data Analyst', description = 'Analyze data', experience_required = 'BA in CS', application_link = 'www.google.com', applied = 1)
instance_5 = Position(position_title = 'Drone Specialist', description = 'Program drones', experience_required = 'CSCI111', application_link = 'www.drones.com', applied = 0)
instance_6 = Position(position_title = 'CS teacher', description = 'Teach lower level', experience_required = 'BA in CS', application_link = 'csuchico.edu', applied = 1)