import json
import sys
import time

def compute_total_cost(price_catalogue, sales_record):
    try:
        with open(price_catalogue, 'r') as f:
            prices = json.load(f)
        with open(sales_record, 'r') as f:
            sales = json.load(f)
    except FileNotFoundError:
        print("Error: One or both files not found.")
        return

    price_dict = {product["title"]: product["price"] for product in prices}

    total_cost = 0
    for sale in sales:
        product_name = sale["Product"]
        if product_name in price_dict:
            total_cost += price_dict[product_name] * sale["Quantity"]
        else:
            print(f"Error: Price not found for product '{product_name}'")

    return total_cost

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    start_time = time.time()
    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]
    total_cost = compute_total_cost(price_catalogue_file, sales_record_file)
    end_time = time.time()

    if total_cost is not None:
        print(f"Total cost of sales: ${total_cost:.2f}")
        print(f"Time elapsed: {end_time - start_time:.2f} seconds")

        with open("SalesResults.txt", "w") as f:
            f.write(f"Total cost of sales: ${total_cost:.2f}\n")
            f.write(f"Time elapsed: {end_time - start_time:.2f} seconds\n")