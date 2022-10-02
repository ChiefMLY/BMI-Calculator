#prompts the user to enter their heights in m and weight in kg
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#Calculates the users BMI and rounds it a whole number
bmi = weight/height ** 2
bmi_int = round(bmi)

#This then provide the user with additional information based on the rage their BMI falls in
if bmi_int < 18.5:
  print(f'Your BMI is {bmi_int}, you are underweight.')
elif bmi_int < 25:
  print(f'Your BMI is {bmi_int}, you have a normal weight.')
elif bmi_int < 30:
  print(f'Your BMI is {bmi_int}, you are slightly overweight.')
elif bmi_int < 35:
  print(f'Your BMI is {bmi_int}, you are obese.')
else:
  print(f'Your BMI is {bmi_int}, you are clinically obese.')
