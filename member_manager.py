members = []

def am():  # Add members
    id = input("Enter Member ID: ")
    name = input("Enter your Name: ")

    members.append({
        "id": id,
        "name": name
    })

    print("Member added successfully!")


def vm():  # View Members
    if len(members) == 0:
        print("No Member found")
    else:
        for i in members:
            print(f'ID: {i["id"]} | Name: {i["name"]}')
