import csv
import json

from validators import validate_order


def process_csv_orders(input_file):
    valid_orders = []
    invalid_orders = []

    try:
        with open(input_file, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for order in reader:
                errors = validate_order(order)

                if errors:
                    invalid_orders.append({
                        "order": order,
                        "errors": errors
                    })
                else:
                    order["quantity"] = int(order["quantity"])
                    valid_orders.append(order)

    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return

    except csv.Error as error:
        print(f"CSV error: {error}")
        return

    print("Valid orders:", len(valid_orders))
    print("Invalid orders:", len(invalid_orders))

    with open("valid_orders.json", "w", encoding="utf-8") as file:
        json.dump(valid_orders, file, indent=4)

    with open("invalid_orders.json", "w", encoding="utf-8") as file:
        json.dump(invalid_orders, file, indent=4)

    print("Results saved successfully.")


if __name__ == "__main__":
    process_csv_orders("orders.csv")
