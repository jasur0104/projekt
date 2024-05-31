from db import cur, conn
from moduls import User
from sessions import Session
import utils

session = Session()


def login(username: str, password: str):
    user: Session | None = session.check_session()
    if user:
        return utils.BadRequest('You already logged in', status_code=401)

    get_user_by_username = '''select * from users where username = %s;'''
    cur.execute(get_user_by_username, (username,))
    user_data = cur.fetchone()
    if not user_data:
        return utils.BadRequest('Username not found in my DB')
    _user = User(username=user_data[1], password=user_data[2], role=user_data[3], status=user_data[4],
                 login_try_count=user_data[5])

    if password != _user.password:
        update_count_query = """update users set login_try_count = login_try_count + 1 where username = %s;"""
        cur.execute(update_count_query, (_user.username,))
        conn.commit()

    user.add_session(_user)
    return utils.ResponseData('User Successfully Logged in')

def login_():
    a=0
    while True:
        username = input('Username: ')
        password = input('Password: ')
        if not username or not password:
            utils.BadRequest('Username or password not found in my DB')
        if username == 'admin' and password == '123':
            return utils.ResponseData('Login Successful')
            print('Login Successful')
            return login(username, password)
        a+=1
        if a>3:
            utils.BadRequest('Too many logins')
            print("is bloked")
            break
if __name__ == '__main__':
    login_()








