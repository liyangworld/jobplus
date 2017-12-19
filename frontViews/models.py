from flask_login import UserMixin
import requests

from .apis import apis

class User(UserMixin):

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    def __init__(self):
        self.id = ''
        self.name = ''
        self.email = ''
        self.role = None
        self.company_id = None


    def get_id(self):
        """overwrite, 此方法将在login_user(user)时被调用，作为存储在session中的user_id, 必须为unicode,int得转
        """
        return str(self.id)

    def is_admin(self):
        return self.role == User.ROLE_ADMIN

    def is_company(self):
        return self.role == User.ROLE_COMPANY

    def is_user(self):
        return self.role == User.ROLE_USER

    @staticmethod
    def get(user_id):
        """try to return user_id corresponding User object.
        This method is used by load_user callback function
        """
        r = requests.get(apis.get('getUserById').format(int(user_id)), params=None)
        resData = r.json()
        if resData['Success']:
            user_data = resData['data']
            user = User()
            user.id = user_data['id']
            user.name = user_data['name']
            user.email = user_data['email']
            user.role = user_data['role']
            return user




