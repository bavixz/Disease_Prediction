name = input("Enter your name:\n")
print(f'Oh welcome {name}')

Pregnancies = input(f'{name}, what\'s your Pregnancies count:\n')
print("okay")

Glucose = input(f'{name}, what\'s your Glucose level:\n')
print("okay")

BloodPressure = input(f'{name}, what\'s your Blood Pressure:\n')
print("okay")

SkinThickness = input(f'{name}, what\'s your Skin Thickness:\n')
print("okay")

Insulin = input(f'{name}, what\'s your Insulin level:\n')
print("okay")

BMI = input(f'{name}, what\'s your BMI:\n')
print("okay")

DiabetesPedigreeFunction = input(f'{name}, what\'s your Diabetes Pedigree Function:\n')
print("okay")

age = input(f'{name}, what\'s your age:\n')
print(f'{age} - that\'s great, {name}!')

# Creating the tuple with the input data
input_data = (
    int(Pregnancies),
    int(Glucose),
    int(BloodPressure),
    int(SkinThickness),
    int(Insulin),
    float(BMI),
    float(DiabetesPedigreeFunction),
    int(age)
)

# Making the prediction
prediction = make_prediction(input_data)

# Output the prediction
if prediction == 0:
    print('The person is not diabetic')
else:
    print('The person is diabetic')
