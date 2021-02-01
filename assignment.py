class Patient:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = None

    def get_bmi(self):
        if not self.bmi:
            self.bmi = self.height/self.weight
        return self.bmi

jeremiah = Patient(name='jeremiah', height=10, weight=50)
marvelous = Patient(name='marvelous', height=50, weight=10)