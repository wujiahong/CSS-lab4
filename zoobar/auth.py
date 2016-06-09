from zoodb import *
from debug import *

import hashlib
import random
import pbkdf2
import bank_client

def newtoken(db, person):
    hashinput = "%s%.10f" % (person.password, random.random())
    person.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return person.token

def login(username, password):
    db = person_setup()
    person = db.query(Person).get(username)
    if not person:
        return None
    db_cred = cred_setup()
    cred = db_cred.query(Cred).get(username)
    if not cred:
        return None
    if cred.password == pbkdf2.PBKDF2(password, cred.salt).hexread(32) :
        return newtoken(db_cred, cred)
    else:
        return None

def register(username, password):
    db_person = person_setup()
    person = db_person.query(Person).get(username)
    if person:
        return None
    newperson = Person()
    newperson.username = username
    db_person.add(newperson)
    db_person.commit()
    bank_client.register(username)

    db_cred = cred_setup()
    cred = Cred()
    cred.username = username
    cred.salt = os.urandom(8).encode('base_64')
    cred.password = pbkdf2.PBKDF2(password, cred.salt).hexread(32)
    db_cred.add(cred)
    db_cred.commit()

    return newtoken(db_cred, cred)

def check_token(username, token):
    db = person_setup()
    person = db.query(Person).get(username)
    db_cred = cred_setup()
    cred = db_cred.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False

