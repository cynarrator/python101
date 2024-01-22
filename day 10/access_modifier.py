class Person:
    def __init__(self, name, age, password):
        self.__name = name
        self.__password = password
        self.__age = age

# password vanne eauta property banyo ra tesle __password lai reference garyo
        # Step 1: Property vanera banaune eauta function jun chai attribute jastai tara arko attribute lai reference garxa
    @property
    def password(self):
        return self.__password
        # Tyao @property decorator lagako lai getter ra setter lagaune
    @password.setter
    def password(self, password):
        self.__password = password

    @password.getter
    def provide_password(self):
        return self.__password
    
    @property
    def name(self, new_name):
        return self.__name

    # def get_password(self):
    #     return self.__password
    
    # def set_password(self, password):
    #     self.__password = password

    # password = property(get_password, set_password)
        
binit = Person("binit", 23, "binit@123")
print(binit.name)
print(binit.password)