from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, id, first_name, last_name, user_name, email, password, birth_date, role, is_active):
        super().__init__(id, first_name, last_name, user_name, email, password, birth_date, role, is_active)