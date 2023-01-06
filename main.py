import json
import time
import datetime

# Load the data from the JSON file, or initialize an empty list if the file doesn't exist
filename = 'data.json'
try:
    with open(filename, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

# ID counter
id_counter = max([obj['id'] for obj in data], default=0)


def add_object():
    global id_counter
    id_counter += 1
    now = datetime.datetime.now()
    date = f"{now.day:02d}-{now.month:02d}-{now.year:02d} {now.hour:02d}:{now.minute:02d}"
    pressure = float(input("Pressure: "))
    mass_flow = float(input("Mass flow: "))
    temperature = float(input("Temperature: "))
    data.append({
        'id': id_counter,
        'date': date,
        'pressure': pressure,
        'mass flow': mass_flow,
        'temperature': temperature
    })
    print(f"Object added with ID {id_counter}")
    check_ids()
    save_data()


def search_objects():
    search_term = input("Enter search term: ")
    search_results = []
    for obj in data:
        if search_term in str(obj.values()):
            search_results.append(obj)
    if search_results:
        print("Search results:")
        for obj in search_results:
            print(obj)
    else:
        print("No results found")


def delete_object():
    id_to_delete = input("Enter ID(s) of object(s) to delete (comma-separated or 'all'): ")
    if id_to_delete == 'all':
        confirm = input("Are you sure you want to delete all objects? (y/n) ")
        if confirm == 'y':
            data.clear()
            print("All objects deleted")
            check_ids()
            save_data()
        else:
            print("Deletion cancelled")
        return
    ids_to_delete = [int(x) for x in id_to_delete.split(',')]
    delete_count = 0
    not_found = 0
    for id_to_delete in ids_to_delete:
        for i, obj in enumerate(data):
            if obj['id'] == id_to_delete:
                del data[i]
                delete_count += 1
                shift_ids(id_to_delete)
                print(f"Object with ID {id_to_delete} deleted")
                break
        else:
            not_found += 1
            print(f"Object with ID {id_to_delete} not found")
    if delete_count or not_found:
        check_ids()
        save_data()


def shift_ids(id_to_delete):
    for obj in data:
        if obj['id'] > id_to_delete:
            obj['id'] -= 1


def check_ids():
    for i, obj in enumerate(data):
        if obj['id'] != i + 1:
            obj['id'] = i + 1


def sort_data():
    keys = list(data[0].keys())
    print("Enter key to sort by:")
    for i, key in enumerate(keys):
        print(f"{i + 1}. {key}")
    choice = int(input("> "))
    key = keys[choice - 1]
    data.sort(key=lambda x: x[key])


def list_all_data():
    print("All data:")
    for obj in data:
        print(obj)


def save_data():
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def edit_object():
    id_to_edit = input("Enter ID of object to edit: ")
    for obj in data:
        if obj['id'] == int(id_to_edit):
            print("Enter new values or leave blank to keep current value")
            for key in obj.keys():
                if key == 'id':
                    continue
                obj[key] = input(f"{key}: ") or obj[key]
            save_data()
            print("Object updated")
            return
    print("Object not found")


# Main loop
while True:
    print("\nEnter a command:")
    print("1. Add object")
    print("2. Search objects")
    print("3. Delete object")
    print("4. Sort data")
    print("5. List all data")
    print("6. Edit object")
    print("7. Quit")
    command = input("> ")
    if command == '1':
        add_object()
    elif command == '2':
        search_objects()
    elif command == '3':
        delete_object()
    elif command == '4':
        sort_data()
    elif command == '5':
        list_all_data()
    elif command == '6':
        edit_object()
    elif command == '7':
        break
    else:
        print("Invalid command")

# Save the data to the JSON file
save_data()
