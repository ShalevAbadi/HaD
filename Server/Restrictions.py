
class Restrictions():

    def _init_(self,conn, id, min_age, max_age, sex, description):
        self.id = id
        self. min_age = min_age
        self.max_age = max_age
        self.sex = sex
        self.description = description

    def save_to_db(self):
        c