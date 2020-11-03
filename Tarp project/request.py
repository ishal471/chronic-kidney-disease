import requests

url = 'http://localhost=5000/predict_api'
r= requests.post(url,json={'Pregnancies' : 2 , 'Glucose' : 45 , 'BloodPressure' : 120 , 'SkinThickness' : 20 , 'Insulin' : 10 ,'BMI': 20 ,'DiabetesPedigreeFunction' : 40 , 'Age':30  })
print(r.json())