from .cat import Cat

class Tomcat(Cat):

    def __init__(self, name, age, gender=None):
        super().__init__(name, age, gender)
        self.gender = 'Male'


    @staticmethod
    def make_sound(): return 'Hiss'
