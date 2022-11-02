from parsing.create_base.sql import check_base, create_base
BASE_PATH = 'jokes.db'
def check_create_base():
    if not check_base(BASE_PATH):
        create_base(BASE_PATH, "parsing/create_base/sql/base.sql")
if __name__ == '__main__':
    check_create_base()