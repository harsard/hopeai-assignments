print("Welcome to Assignment-1")

num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

print("Num1= ", num1)
print("Num2= ", num2)
print("Add= ", num1 + num2)

bmi_index = float(input("Enter the BMI Index: "))

if bmi_index < 18.5:
    print("Underweight")
elif bmi_index < 25:
    print("Normal")
elif bmi_index < 30:
    print("Overweight")
else:
    print("Very overweight")
