import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {}
    for arg in sys.argv[1:]:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}")
            continue
        parts = arg.split(':', 1)
        item_name = parts[0]
        qty_str = parts[1]
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            qty = int(qty_str)
            inventory[item_name] = qty
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
    if len(inventory) == 0:
        print("Got inventory: {}")
        return
    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")
    total_items = len(inventory)
    total_qty = sum(inventory.values())
    print(f"Total quantity of the {total_items} items: {total_qty}")
    for item in inventory.keys():
        qty = inventory[item]
        pct = round((qty / total_qty) * 100, 1)
        print(f"Item {item} represents {pct}%")
    most_item = item_list[0]
    most_qty = inventory[most_item]
    least_item = item_list[0]
    least_qty = inventory[least_item]
    for item in item_list:
        qty = inventory[item]
        if qty > most_qty:
            most_qty = qty
            most_item = item
        if qty < least_qty:
            least_qty = qty
            least_item = item
    print(f"Item most abundant: {most_item} with quantity {most_qty}")
    print(f"Item least abundant: {least_item} with quantity {least_qty}")
    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
