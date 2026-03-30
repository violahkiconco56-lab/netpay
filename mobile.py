def menu():
    print("welcome to Mobile Money")
    print("1.Send Money")
    print("2.Buy Airtime")
    print("3.ChecK Balance")

menu()
choice = input("select your option (1, 2, 3): ")

if choice == "1":
   phone = input("Enter phone number: ")
   amount = int(input("Enter amount: "))

   if amount > 50000:
         print("Insufficient Funds")

   elif amount <= 50000:
         print(f"You have sent{amount} to {phone}")

   else:
         print("Invalid amount")

else:
     print("Invalid option")

#buy airtime
choice = input("Enter your choice (1, 2, or 3): ")

if choice == "2":
    amount = int(input("Enter airtime is 500"))

    if amount < 500:
         print("Minimum airtime is 500")

    elif amount >= 500:
         print("Airtime purchase successful")

    else:
          print("Invalid amount")

else:
    print("Invalid option")
#invalid option
choice = input("Enter your choice (1, 2, or 3): ")

if choice == "3":
    print("Your balance is 50,000 UGX")

elif choice == "1":
    print("Send Money option selected")

elif choice == "2":
    print("Buy Airtime option selected")

else:
    print("Invalid option selected")
