Pharmacy Order Processor

A Python automation project that reads pharmacy orders from CSV and JSON files, validates order information, separates valid and invalid orders, and saves processing results to output files.

Features

CSV Processing: Read pharmacy orders using Python's built-in csv module.

JSON Processing: Load and process structured order data using the json module.

Order Validation: Check patient names, medicine names, and quantities.

Error Handling: Handle missing files, invalid JSON, and incorrect quantity values.

Invalid Order Reporting: Store invalid orders along with the reasons for rejection.

Automated Output: Export valid and invalid orders to separate JSON files.

Modular Code: Keep validation logic separate from processing scripts.

Project Structure

pharmacy-order-processor/
├── main.py
├── validators.py
├── process_csv_orders.py
├── process_json_orders.py
├── orders.csv
├── orders.json
├── valid_orders.json
├── invalid_orders.json
├── requirements.txt
├── .gitignore
└── README.md
