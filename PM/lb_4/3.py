class Emplovee(ABC):
    def __init__(self, name, base_rate, position):
        self.name = name
        self.base_rate = base_rate
        self.position = position

    @abstractmethod
    def calculate_salary(self):
        pass

    def get_info(self):
        return f'Employer: {self.name} ({self.position}).  salary: {self.base_rate}.'


class Manager(Emplovee):
    def __init__(self, name, base_rate, position):
        super().__init__(name, base_rate, position)

    def calculate_salary(self):
        return self.base_rate * 1.5

    def promote(self, val):
        self.base_rate += val

    def work(self):
        return f'{super().get_info()} Organizes the teams work'


class Developer(Emplovee):
    def __init__(self, name, base_rate, position):
        super().__init__(name, base_rate, position)

    def calculateSalary(self):
        return self.base_rate + 500

    def promote(self, val):
        self.base_rate += val

    def work(self):
        return f'{super().get_info()} Writes code and fixes bugs'
