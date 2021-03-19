#source flaskapi/bin/activate
import pyrebase


firebaeconfig={
  "apiKey": "AIzaSyCVqajMEZRVDPABKg0G0wbcKTZC9rCpC6A",
  "authDomain": "even-ivy-256205.firebaseapp.com",
  "databaseURL": "https://even-ivy-256205.firebaseio.com",
  "projectId": "even-ivy-256205",
  "storageBucket": "even-ivy-256205.appspot.com",
  "messagingSenderId": "304328648235",
  "appId": "1:304328648235:web:b4c5ea61691b9a0750ec6e",
  "measurementId": "G-45ZKEK5R81"
}
try:
    firbase = pyrebase.initialize_app(firebaeconfig)
    # db=firbase.database()
    auth=firbase.auth()
    auth.sign_in_with_email_and_password("azeemarsal@gmail.com","12345678")
except Exception as e:
    print(e)
