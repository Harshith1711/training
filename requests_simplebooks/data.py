import random
def cred():

    num = str(random.randint(1001, 2001))

    credentials = {
            "clientName": "Harshith",
            "clientEmail": "Harshith" + num + "@gmail.com"
    }
    return credentials

def postOrder():

    return {"bookId": 1, "customerName": "John"}

def patchOrder():

    return {"customerName": "Harshith"}
