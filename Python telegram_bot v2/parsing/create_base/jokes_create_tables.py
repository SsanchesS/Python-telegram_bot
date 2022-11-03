from parsing.create_base.sql import check_base, create_base
BASE_PATH = 'jokes.db'
def check_create_base():
    if not check_base(BASE_PATH):
        print("БД не существует")
        create_base(BASE_PATH, "parsing/create_base/sql/base.sql")
        return True
    else:
        print("БД существует")
        return False
    
if __name__ == '__main__':
    check_create_base()