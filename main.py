from services import  record_sales, daily_summary, total_calculations

sales_register = []
summary=[]
to_continue = True

while to_continue :

    print("\n","-"*30)
    print("         Sales Record")
    print("-"*30)

    record_sales(sales_register)

    validate = True
    while validate:
        try:
            option = input("\n Do you want to continue with the registration? Y for yes or N for no: ").upper()
            if option not in ["Y", "N"]:
                raise ValueError("Invalid option")
            validate=False
        except ValueError :
         print("\n Please enter Y or N")

    if (option=="N"):  to_continue=False
    
summary=total_calculations(sales_register)
daily_summary(summary)
