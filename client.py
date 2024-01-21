class Client: 
    def __init__(self, name, surname, telNumber, birthday, category, exam_type):
        self.name = name
        self.surname = surname
        self.telNumber = telNumber
        self.birthday = birthday
        self.category = category
        self.exam_type = exam_type

    def __str__(self):
        return f"Client({self.name}, {self.surname}, {self.telNumber}, {self.birthday}, {self.category}, {self.exam_type})"

