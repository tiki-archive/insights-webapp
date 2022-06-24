#
#  Lets make 100 companies
#  With 1 - 5 emails each
#  On 3 different dates
#  With 3 - 5 subjects each
#  sent to 15 - 200 people each
#
import random
import string

from pyArango.connection import *
from datetime import date, timedelta

def loadCompanies():
    print("Loading 100 companies")
    companiesTemp = []
    for line in open("samples/companies.txt", "r"):
        line = line.strip()
        if line:
            companiesTemp.append(line)
    return companiesTemp

conn = Connection(username="root", password="password")

db = conn["kgraph"]

companies = db["company"]
occurrences = db["occurrence"]
actions = db["action"]
dates = db["date"]
subjects = db["subject"]
edges = db["edge"]

# Clear current collections
companies.truncate()
occurrences.truncate()
actions.truncate()
dates.truncate()
subjects.truncate()
edges.truncate()

emailSubjects = ["New Specials for you!", "Reset Your Password",
                 "Your Order Was Confirmed", "Summer Deals For You",
                 "Account Created Confirmation", "Self-manage or hire it out?",
                 "Pre-market summary on your portfolio", "Here is today's Wordle",
                 "Must Reads: 2 Best ETFs to Buy Now", "Wall Street Breakfast:  Stressed Out"]
companiesToAdd = loadCompanies()
dateDocs = []

# Put last 9 days as date documents in arango
for i in range(10):
    myDate = (date.today() - timedelta(days=i)).strftime("%m/%d/%Y")
    dateDoc = dates.createDocument()
    dateDoc["date"] = myDate
    dateDoc.save()
    dateDocs.append(dateDoc)

# Put email action as document in  actions
emailActionDoc = actions.createDocument()
emailActionDoc["action"] = "email"
emailActionDoc.save()

totalEmailsAdded = 0

for company in companiesToAdd:
    random.shuffle(emailSubjects)
    emailAmount = random.randrange(6, 9)

    companyDoc = companies.createDocument()
    companyDoc["name"] = company
    companyDoc.save()

    print("Adding " + str(emailAmount) + " emails to " + company)
    for i in range(emailAmount):
        # Each email subject
        subject = emailSubjects[i]
        edgeWeight = random.randrange(15, 1000)

        totalEmailsAdded += edgeWeight

        occurrenceDoc = occurrences.createDocument()
        occurrenceDoc["occurrence"] = "occ" + ''.join(random.choices(string.ascii_lowercase, k=5))
        occurrenceDoc.save()

        subjectDoc = subjects.createDocument()
        subjectDoc["subject"] = subject
        subjectDoc.save()

        # Get a random date for this email
        sentDate = dateDocs[random.randrange(0, 9)]

        companyEdge = edges.createDocument()
        companyEdge["_from"] = "company/" + companyDoc._key
        companyEdge["_to"] = "occurrence/" + occurrenceDoc._key
        companyEdge["weight"] = edgeWeight
        companyEdge.save()

        actionEdge = edges.createDocument()
        actionEdge["_from"] = "occurrence/" + occurrenceDoc._key
        actionEdge["_to"] = "action/" + emailActionDoc._key
        actionEdge["weight"] = edgeWeight
        actionEdge.save()

        dateEdge = edges.createDocument()
        dateEdge["_from"] = "occurrence/" + occurrenceDoc._key
        dateEdge["_to"] = "date/" + sentDate._key
        dateEdge["weight"] = edgeWeight
        dateEdge.save()

        subjectEdge = edges.createDocument()
        subjectEdge["_from"] = "occurrence/" + occurrenceDoc._key
        subjectEdge["_to"] = "subject/" + subjectDoc._key
        subjectEdge["weight"] = edgeWeight
        subjectEdge.save()



print("Added " + str(totalEmailsAdded) + " dummy emails to " + str(len(companiesToAdd)) + " companies")

