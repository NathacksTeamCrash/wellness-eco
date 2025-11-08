import firebase_admin
from firebase_admin import credentials, firestore

#Only initialize once
if not firebase_admin._apps:
    cred = credentials.Certificate("crash-29061-firebase-adminsdk-fbsvc-8d1421967f.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

def get_db():
    return db