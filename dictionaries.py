student_scores = {"Alice": 87, "Bob": 79, "Jerry": 94, "Sara": 90}
print(student_scores['Bob'])

#declare a car dictionary
car = {"make": "Mercury", "model": "Sable", "year": 1988, "value": 10000, "engine": 3.0}
#get all the keys, values from the student score dictionary
for student in student_scores:
    print(f"{student}: {student_scores[student]}")


#get all the keys and values from the car dictionary
print("\n")
for key, value in car.items():
    print(f"{key}: {value}")