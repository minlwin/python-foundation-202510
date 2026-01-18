from .. model.dao.member_dao import get_all

def show_members():
    members = get_all()
    for member in members:
        print(member)