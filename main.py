
from process_csv_orders import process_csv_orders
from process_json_orders import process_json_orders


def main():
    print("Pharmacy Order Processor")
    print("1. Process CSV orders")
    print("2. Process JSON orders")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        process_csv_orders("orders.csv")
    elif choice == "2":
        process_json_orders("orders.json")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
