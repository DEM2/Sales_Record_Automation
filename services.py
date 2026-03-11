from collections import defaultdict


def  record_sales (record):
    validate = True
    Product=input("\n Enter the product name: ").strip()
    while validate:
        try:
           
            price=float(input("\n Enter the price per unit: "))
            quantity=int(input("\n How many units?: "))

            record.append({
                'Product': Product,
                'Price_per_unit': price,
                'Amount': quantity
            })
            print("\n Registros Exitoso ✅")
            validate=False 
        except ValueError:
            print("Price or Quantity are invalid")


def total_calculations(record):
    summary= defaultdict(lambda: {'units_sold': 0, 'total': 0})
    for sale in record:
        product = sale['Product']

        summary[product]['units_sold']+=sale['Amount']
        summary[product]['total']+=sale['Price_per_unit']*sale['Amount']
        
    return summary

def daily_summary (summary):
    print("="*30)
    print("\n Daily Sales Summary")
    total=0
    for product, info in summary.items():
        print(f"\n Product: {product}")
        print(f" Total Quantity Sold: {info['units_sold']}")
        total+=info['total']
    print(f"\n Total Collected: ${total}")
    