#!/usr/bin/env python 3

# initialize django

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'SiteOne.settings'
import django
django.setup()

#regular imports
import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess, sys

print(hmod)

#empty (or drop) db
cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")

#create db
cursor.execute("CREATE SCHEMA PUBLIC")

#Migrage db
subprocess.call([sys.executable, "manage.py", "migrate"])

#initialize tables


#initialize tables

##########################################################################################
#########Group

#Delete old groups

##########################################################################################
#########User

######################### -CREATE PERMISSIONS/GROUPS- #####################
Permission.objects.all().delete()
Group.objects.all().delete()

permission = Permission()
permission.codename = 'manager_rights'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Has Manager Rights'
permission.save()

group = Group()
group.name = "Managers"
group.save()
group.permissions.add(permission)


print('permissions initialized')
#Delete old users
hmod.SiteUser.objects.all().delete()

#create som users
############################### -ADD FIRST USER- ###############################
u = hmod.SiteUser()
u.name = "users"
u.first_name = "scott"
u.last_name = "romney"
u.set_password("mmc0911!")
u.username = "scottromney"
u.is_superuser= True
u.is_staff= True
u.save()


############################### -ARRAY OF USERS- ###############################
#Create new users: username, password, first_name, last_name, is_superuser, accountbalance
for data in [
  ['rodcox89', 'password', 'Rodney', 'Cox', True, True, '0', 'rodcox89@gmail.com'],
  ['stunna81', 'password', 'scott', 'romney', False, True, '0', 'romney81@gmail.com'],
  ['cody123', 'password', 'cody', 'anderson', False, True, '0', 'asdf@gmail.com'],
  ['csmith12', 'password', 'carter', 'Smith', False, True, '0', 'aa@gmail.com'],
]:

    #set attributes
    u = hmod.SiteUser()
    u.username = data[0]
    u.set_password(data[1])
    u.first_name = data[2]
    u.last_name = data[3]
    u.is_superuser = data[4]
    u.is_staff = data[5]
    u.account_balance = int(data[6])
    u.email = data[7]

    #save
    u.save()
    print(u.username)
    print(u.set_password)

############################### -EVENTS- #################################

#Delete old events
hmod.Event.objects.all().delete()

#Create new events: name, description, start, end, venue
for data in [
  ['Bread Making','Make bread using ovens they used back in the old days','2015-05-06','2015-05-06','Centenial Park'],
  ['LARP','Come join us in our exciteing Live Action Role Play ','2015-05-12','2015-05-12','Centenial Park'],
  ['Feather Pen Writing','Come and learn how to write like to used to with feathers and ink','2015-05-28','2015-05-28','Centenial Park'],
  ['Musket Shooting','Come give your aim a try with us as we practice shooting','2015-06-05','2015-06-05','Centenial Park'],
  ['Questival','The most intense magical journey you have every experienced','2015-04-06','2015-04-07','Energy Solutions'],

]:

    #set attributes
    e = hmod.Event()
    e.name = data[0]
    e.description = data[1]
    e.start_date = data[2]
    e.end_date = data[3]
    e.location = data[4]
    #save
    e.save()
    print(e)


############################### -RENTALS- ##############################

#Delete old rentals
hmod.Rentals.objects.all().delete()

#Create new Rentals: name, rental, due, person, damage, was_returned
for data in [
  ['Breeches','2015-02-03','2015-03-03', '2', ' ', False],
  ['Red Coat','2015-01-02','2015-03-03', '3', ' ', False],
  ['Blue Coat','2014-12-04','2015-01-01', '4', ' ', False],
  ['Hat','2015-05-02','2015-06-02', '5', ' ', False],
]:

    #set attributes
    rr = hmod.Rentals()
    rr.name = data[0]
    rr.rental_date = data[1]
    rr.due_date = data[2]
    rr.person = hmod.SiteUser.objects.get(id=data[3])
    rr.new_damage = data[4]
    rr.was_returned = data[5]
    #save
    rr.save()
    print(rr)


############################### -PURCHASES- ##############################

#Delete old rentals
hmod.Purchases.objects.all().delete()

#Create new Rentals: name, rental, due, person, damage, was_returned
for data in [
  ['2','100','2015-03-10', 'asdf'],
  ['3','200','2015-03-06', 'asdff'],
  ['4','150','2015-02-02', 'asdfff'],
  ['5','175','2015-02-02', 'asdffff'],
]:

    #set attributes
    pu = hmod.Purchases()
    pu.customer = hmod.SiteUser.objects.get(id=data[0])
    pu.total = data[1]
    pu.purchase_date = data[2]
    pu.charge_id = data[3]
    #save
    pu.save()
    print(pu)

############################### -ITEMS- ###############################
#Delete old items
hmod.Item.objects.all().delete()

#Create new items: name, description, value
for data in [
  ['Blue Coat' , 'Original blue coat of the colonial army', '129','chf'],
  ['Red Coat' , 'Original red coat of the colonial army', '129'],
  ['Backpack' , 'From deep within the cotopaxi warehouse', '29','chf'],
  ['Canteen' , '12 oz canteen thats sure to keep your thirst quenched', '5','chf'],
]:

    i = hmod.Item()
    i.name = data[0]
    i.description = data[1]
    i.value = data[2]
    i.organization = [3]

    i.save()
    print(i)

############################### -PRODUCTS- ###############################
#
# #Delete old Products
hmod.Product.objects.all().delete()

#Create new Products: name, description, category, current_price
for data in [
  ['Musket', 'This non-functional replica is as real as it gets', 'Crafts', '14'],
  ['Mayflower', 'Cool Mayflower Replica that will be sure to impress those who see it', 'Crafts', '2'],
  ['Quil', 'An exact replica of a feather quil used in the colonial era', 'Collectors', '8'],
  ['Abacus', 'This authentic Abacus is what they used to count', 'Business', '13'],

]:

    p = hmod.Product()
    p.name = data[0]
    p.description = data[1]
    p.category = data[2]
    p.current_price = data[3]

    p.save()
    print(p)




############################### -LOCATIONS- ###############################

hmod.Location.objects.all().delete()

#create new Locations: name, description, city, state

for data in [
    ['Kiwanis Park','decent tree coverage, close to the creamery','Provo','Utah'],
    ['Veterans Memorial Park','Two pavillions with basketball courts','Provo','Utah'],
    ['Larsen Park','Attached to larsen Elementary school','SF','Utah'],
    ['Brookhollow Park','a bit colder, but tons of open space','Evanston','Wyoming'],

]:

    l = hmod.Location()
    l.name = data[0]
    l.description = data[1]
    l.city = data[2]
    l.state = data[3]

    l.save()
    print(l)


############################### -AREAS- ###############################

hmod.Area.objects.all().delete()

#create new Area: name, description

for data in [
    ['Knead The Dough','Knead the dough before we start the cookin!'],
    ['Shooting Range','Safe area located on the far end of the park'],
    ['Pen Writing Station','Pen writing desks that lets us write'],
    ['Fake Village','Fake village located in the soutwest corner'],

]:

    ar = hmod.Area()
    ar.name = data[0]
    ar.description = data[1]

    ar.save()
    print(ar)


############################### -VENUES- ###############################
#delete previous venues

hmod.Venue.objects.all().delete()

#create new Venue: name, Description, address, city, state, zip

for data in [

    ['usana ampitheatre','nice outdoor venue, great for concerts','332 pleasant way','West Valley','Utah','84669'],
    ['The great saltair','Old open warehouse at the edge of the great salt Lake','55 e I-80','Magna','Utah','84667'],
    ['Scera Parl','Awesome ampitheatre seats close to 4000 people, great for movies','800 north state street','Orem','Utah','84664'],
    ['Jordan towns','Has a splashpad for kids, with a nice barbeque pit','455 e main','Springville','Utah','84661'],

]:

    v = hmod.Venue()
    v.name = data[0]
    v.description = data[1]
    v.address = data[2]
    v.city = data[3]
    v.state = data[4]
    v.zip_code = data[5]

    v.save()
    print(v)


#runs server
############################### -RUN SERVER- ###############################
subprocess.call([sys.executable, "manage.py", "runserver"])
