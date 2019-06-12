class Member():
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def introduction(self):
        print('[Name]:' + self.name)
        print('[Status]:' + self.status)

    def is_paid(self):
        return self.status == 'Paid'


class PaidMember(Member):
    def __init__(self, name):
        status = 'Paid'
        super().__init__(name, status)


class FreeMember(Member):
    def __init__(self, name):
        status = 'Free'
        super().__init__(name, status)


class UnsubscribeMember(Member):
    def __init__(self, name):
        status = 'Unsubscribe'
        super().__init__(name, status)

    def introduction(self):
        print(self.name + 'は退会しています。自己紹介機能は提供しません。')

yamada = PaidMember('Yamada')
yamada.introduction()
print(yamada.is_paid())
suzuki = FreeMember('Suzuki')
suzuki.introduction()
print(suzuki.is_paid())
tanaka = UnsubscribeMember('Tanaka')
tanaka.introduction()
print(tanaka.is_paid())
