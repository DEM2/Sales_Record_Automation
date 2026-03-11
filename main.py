from services import  record_sales, daily_summary, total_calculations

sales_register = []
summary=[]
to_continue = True

while to_continue != False :

    print("\n","-"*30)
    print("         Sales Record")
    print("-"*30)

    Product=input("\n Enter the product name: ")
    price=float(input("\n Enter the price per unit: "))
    sales=int(input("\n How many units?: "))

    record_sales(sales_register, Product, price, sales)
    option = input("\n Do you want to continue with the registration? Y for yes or N for no: ")
    if (option=="N"):  to_continue=False
    
summary=total_calculations(sales_register)
daily_summary(summary)
