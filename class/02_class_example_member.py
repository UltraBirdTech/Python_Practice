class Member():
    def __init__(self, name, status):
       self.name = name
       self.status = status

    def introduction(self):
       print('[Name]:' + self.name)
       print('[Status]:' + self.status)

class PaidMember(Member):
    def __init__(self, name):
        self.status = 'Paid'
        super().__init__(name, self.status)

class FreeMember(Member):
    def __init__(self, name):
        self.status = 'Free'
        super().__init__(name, self.status)

yamada = PaidMember('Yamada')
yamada.introduction()
suzuki = FreeMember('Suzuki')
suzuki.introduction()
