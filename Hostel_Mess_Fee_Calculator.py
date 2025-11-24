#Hostel Mess Fee Calculator

print("\nHOSTEL MESS FEE CALCULATOR\n")

#Student Details
name = input("Enter Student Name:")
registration_no = input("Enter Registration Number:")

#Mess Fee Structure(Monthly)
veg_fee = int(input("Enter monthly Veg Mess Fee:"))
non_veg_fee = int(input("Enter monthly Non-Veg Fee:"))
jain_fee = int(input("Enter monthly Jain Mess Fee:"))

#Extra Charges
milk_charge = int(input("Enter milk charge:"))
special_meal_charge = int(input("Enter Special meal charge:"))

#Mess Options
print("Mess Options:")
print("1: Veg Mess")
print("2: Non-Veg Mess")
print("3: Jain Mess")

choice = int(input("Enter your mess type (1/2/3):"))

#Determine Base Fess
if choice == 1:
    base_fee = veg_fee
    mess_name = "Veg Mess"
elif choice == 2:
    base_fee = non_veg_fee
    mess_name = "Non-Veg Mess"
elif choice == 3:
    base_fee = jain_fee
    mess_name = "Jain Mess"
else:
    print("Invalid Option Selected")

#Asking for Optional Extras
print("\nOptional Add-ons")
print("1: Milk","(",milk_charge,"/month)")
print("2: Special Meal","(",special_meal_charge,"/month)")
print("3: Both")
print("4: None")

addon = int(input("Select your add-ons(1/2/3/4):"))
extra = 0
if addon == 1:
    extra += milk_charge
elif addon == 2:
    extra += special_meal_charge
elif addon == 3:
    extra += milk_charge + special_meal_charge

#Ask if student recieves discount
print("\nPerformence based Discount Categories:")
print("1: Excellent (20%_off)")
print("2: Good (10%_off)")
print("3: Average (No discount)")

performance = int(input("Enter your performance Category (1/2/3):"))
if performance == 1:
    discount_percent = 20
elif performance == 2:
    discount_percent = 10
else:
    discount_percent = 0

#Calculate Final Fee
gross_fee = base_fee + extra
discount_amount = (gross_fee * discount_percent)/100
net_fee = gross_fee - discount_amount

#Fee Summary & Calculation
print("\n------------------------------------------------------------")
print("FEE SUMMARY")
print("\n------------------------------------------------------------")
print(f"Mess Name:{mess_name}")
print(f"Base Mess Fee (per month): {base_fee}")
print(f"Base Mess Annual Fee (1 year): {base_fee * 12}")

if extra>0:
    print(f"Extra Add-ons:{extra}")
else:
    print("Extra Add-Ons None")

print(f"Gross Monthly Fee: {gross_fee}")
print(f"Performence Discount: {discount_percent}%")
print(f"Discount Amount: {discount_amount}")
print(f"Final Monthly Mess Fee: {net_fee}")
print(f"Final Annual Mess Fee: {net_fee * 12}")
print("--------------------------------------------------------------")