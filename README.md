# ISM3232 Midterm: RidgeLine Tool Rental

- **Name:** Yusra Batool
- **Version:** ALPHA
- **Date:** 10/23/2026

## What This Program Does
This program is built for Ridgeline Tool Rental, a company that rents equipment to customers with certain discounts and waivers. This program contains logic to calculate essential business functions such as the rental cost, discount, quote, etc. It also places rentals into categories such as whether or not they require inspection or a deposit. Overall, this program allows the business to streamline its processes and organize its data in a way that is automated and non-repetitive. 

## Business Rules
The first business rule defines the rental cost, which is the daily rate multiplied by the number of days the equipment is rented. The second rule specifies the discounts. Any item rented for fewer than 3 days gets no discount. An item rented between 3 to 6 days gets a 10% discount. Finally, an item rented for 7 or more days gets a 20% discount. The third rule defines an exception for licensed contractors, who always get a 10% discount whether they meet the 3-day condition or not. The fourth rule adds a $25 damage waiver to any rental with a cost below $150 after all discounts are applied. The fifth rule requires that any quote going over $1000 requires a deposit. Finally, the last rule defines the criteria for when a rental needs an inspection, stating that an inspection is required when the rental runs 5 days or over, and when its quote is over $800. 

## How to Run
To run the program, you must first open the virtual environment and then access the rental report through the main.py file. 

python3 -m venv .venv
source .venv/bin/activate
python main.py

## How to Test
To test this program, I wrote 22 pytest tests to verify my functions defining the business rules. I used ruff check . to check my code for errors. 

ruff check . 
pytest -v

## Files in This Repository
The files in this repository are as follows: 
1. .gitignore: Lists files and folders that Git should ignore.
2. README.md: Explains how to run and test program. 
3. business_rules.py: Contains eight functions that define the business rules.
4. main.py: Contains the rental list and prints the final report.
5. commands.md: Documents the commands and outputs used during the project.
6. requirements.txt: Lists the packages required for this project.
7. tests/__init__.py: Marks the tests folder as a Python package.
8. tests/test_business_rules.py: Contains 22 tests used to check the functions in business_rules.py. 

## AI Use Statement
I did not use AI for this project. 