import json

from validators import validate_order


def process_json_orders(input_file):
    valid_orders = []
    invalid_orders = []

    try:
        with open(
            input_file,
            "r",
            encoding="utf-8"
        ) as file:
            orders = json.load(file)

    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return

    except json.JSONDecodeError as error:
        print(f"Invalid JSON format: {error}")
        return

    if not isinstance(orders, list):
        print("The JSON file must contain a list of orders.")
        return

    for order in orders:
        errors = validate_order(order)

        if errors:
            invalid_orders.append({
                "order": order,
                "errors": errors
            })
        else:
            order["quantity"] = int(order["quantity"])
            valid_orders.append(order)

    with open(
        "valid_orders.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(valid_orders, file, indent=4)

    with open(
        "invalid_orders.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(invalid_orders, file, indent=4)

    print("Valid orders:", len(valid_orders))
    print("Invalid orders:", len(invalid_orders))
    print("Results saved successfully.")


if __name__ == "__main__":
    process_json_orders("orders.json")
