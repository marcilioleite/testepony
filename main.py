from pony.orm import *

db = Database('mysql', host='127.0.0.1', user='root', passwd='', db='pony', charset="utf8")

class Person(db.Entity):
    name = Required(unicode)
    age = Required(int)
    places = Set("Place")

class Place(db.Entity):
    name = Required(unicode)
    lat = Required(float)
    long = Required(float)
    person = Required(Person)

#sql_debug(True)
db.generate_mapping(create_tables=True)

#place = Place(name='Trabalho', lat=3.2312, long=230.30, person=p2)
#commit()

''' Get by Id '''
#person = Person[1]

# Select all
persons = select(p for p in Person)[:]

for person in persons:
    print "Name: %s, Age: %d" % (person.name, person.age)
    #for place in person.places:
        #print "\tPlace: %s" % place.name
