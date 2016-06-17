import pymongo
import sys
from pymongo.message import query

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
grades = db.grades

def printInSortedWay():

    print("find, reporting for duty Find and Delete")
    query = {'type': 'homework'}
    projection = {'type' : 1, 'student_id':1,'score':1, '_id': 0}

    try:
        cursor = grades.find(query, projection).sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)])
        #grades.delete_one({'student_id' : 0})

    except Exception as e:
        print ("Unexpected error:", type(e), e)
    
    count =0
    prev_record = 999   
    for doc in cursor:
        if prev_record == doc['student_id']:
            continue
        grades.delete_one(doc)
        prev_record = doc['student_id']
    
    print (count)

printInSortedWay()