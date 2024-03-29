smoke = float(input("Do You Smoke? (Yes:1 & No:0) : "))
age = float(input("Enter your age: "))
bmi = float(input("Enter Your BMI: "))
print("Your Predicted Insurance Charges is : "+str(-1760.3160521+39.8080191*age+23558.1282*smoke+7.08703539*age*bmi))