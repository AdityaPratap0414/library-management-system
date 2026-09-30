def add_member(members):
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")

    for member in members:
        if member["id"] == member_id:
            print("Member ID already exists.")
            return

    members.append({
        "id": member_id,
        "name": name
    })

    print("Member added successfully.")


def view_members(members):
    if not members:
        print("No members found.")
        return

    for member in members:
        print(f'ID: {member["id"]} | Name: {member["name"]}')
