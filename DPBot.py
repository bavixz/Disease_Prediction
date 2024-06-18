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
input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = lr.predict(std_data)
print(prediction)

if (prediction[0] == 0):
    print('The person is not at risk of a heart attack')
else:
    print('The person is at risk of a heart attack')
