age = int(input("Enter your age: "))
price = int(input("Enter your price: "))
studentStatus = input("Are you a student? (yes/no): ")

if (age > 65 and studentStatus == "no"):
    discount = price * 0.10
    print("Seniour Citison: You will get discount of 10%: final amount is =>", price-discount)

elif (studentStatus == "yes"):
    discount = price * 0.05
    print("You are student 5% discount: final amount is =>", price-discount)
else:
    discount = price * 0.02
    print("No discount available for your age group so basic discount 2%: final amount is =>", price-discount)
