from Usuario import Usuario
class Cliente(Usuario):
    def __init__(self, id, first_name, last_name, user_name, email, password, birth_date, role, is_active, company, department, client_type):
        super().__init__(id, first_name, last_name, user_name, email, password, birth_date, role, is_active)
        
        self.company = company
        self.department = department
        self.client_type = client_type


    def get_company(self):
        return self.company
    
    def set_company(self, value):
        self.company = value

    def get_department(self):
        return self.department
    
    def set_department(self, value):
        self.department = value
    
    def get_client_type(self):
        return self.client_type
    
    def set_client_type(self, value):
        self.client_type = value
