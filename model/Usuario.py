
class Usuario:
    def __init__(self, id, first_name, last_name, user_name, email, password, birth_date, role, is_active):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.role = role
        self.is_active = is_active

    
    def get_id(self):
        return self.id
    
    def set_id(self, value):
        self.id = value
    
    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, value):
        self.first_name = value

    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, value):
        self.last_name = value

    def get_user_name(self):
        return self.user_name
    
    def set_user_name(self, value):
        self.user_name = value
    
    def get_email(self):
        return self.email
    
    def set_email(self, value):
        self.email = value

    def get_password(self):
        return self.password
    
    def set_password(self, value):
        self.password = value

    def get_birth_date(self):
        return self.birth_date
    
    def set_birth_date(self, value):
        self.birth_date = value

    def get_role(self):
        return self.role
    
    def set_role(self, value):
        self.role = value

    def get_is_active(self):
        return self.is_active
    
    def set_is_active(self, value):
        self.is_active = value
