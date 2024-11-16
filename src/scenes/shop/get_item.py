import re
import pandas as pd

# Load all items from the CSV file

with open(r"Python-studies\shop_shop_manager\assets\data\items\all_items.csv", "r") as file:
    all_items_df = pd.read_csv(file)

def get_item(input_string: str) -> tuple:
    """
    Replaces occurrences of the word 'ITEM' in the input string with a random item
    from the 'all_items.csv' file and returns additional details about the item.

    Parameters:
        input_string (str): The input string containing the word 'ITEM'.

    Returns:
        tuple: A tuple containing:
            - str: The updated string with 'ITEM' replaced by a random item.
            - list: A list containing the values [Item, Price, Type] for the chosen item.
    """
    # Check if the DataFrame is empty
    if all_items_df.empty:
        raise ValueError("The items CSV file is empty or not properly loaded.")

    # Select a random row
    random_row = all_items_df.sample(n=1).iloc[0]

    # Extract item details
    item = random_row['Item']
    price = float(random_row['Price'])
    type = random_row['Type']

    # Replace 'ITEM' in the input string with the random item
    new_string = re.sub(r"\bITEM\b", item, input_string)

    # Return the updated string and the details
    return new_string, [item, price, type]

if __name__ == "__main__":
    # Test the function
    test_string = "I want to buy ITEM, please!"
    updated_string, item_details = get_item(test_string)
    print("Updated String:", updated_string)
    print("Item Details:", item_details)