import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCOCahH_fKyUjtxKRFBtmXyHd4fPMy-bio",
    "authDomain": "python400-16c06.firebaseapp.com",
    "projectId": "python400-16c06",
    "storageBucket": "python400-16c06.firebasestorage.app",
    "messagingSenderId": "773938144010",
    "appId": "1:773938144010:web:9d2468e12553b15ca8d0f3",
    "measurementId": "G-WF57KJEXQD",
    "databaseURL": "https://python400-16c06-default-rtdb.asia-southeast1.firebasedatabase.app",
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
