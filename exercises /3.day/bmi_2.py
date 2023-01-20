eight = float(input("Enter your height in m:"))
weight = int(input("Enter your height in KG:"))

bmi = weight / (height**2)

int_bmi= int(bmi)

if bmi < 18.5:
   print(f"Your BMI is {int_bmi},you are underweught")
elif bmi < 25:
   print(f"Your BMI is {int_bmi},you are normal weight")
elif bmi < 30:
   print(f"Your BMI is {int_bmi},you are slightly overweight")
elif bmi < 35:
   print(f"Your BMI is {int_bmi},you are obese")
else :
    print(f"Your BMI is {int_bmi}, you are clinically obese ")           