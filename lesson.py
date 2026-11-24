class Shahs:
    count_shahs = 0

    def __init__(self, name, password, tyil, account, bio):
        self.name = name
        self.__password = password
        self.tyil = tyil
        self.__account = account
        self.bio = bio
        Shahs.count_shahs += 1

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_account(self):
        return self.__account

    @classmethod
    def get_count(cls):
        return cls.count_shahs


class Talaba(Shahs):
    def __init__(self, name, password, tyil, account, bio, kurs=1):
        super().__init__(name, password, tyil, account, bio)
        self.kurs = kurs

    def get_info(self):
        return f"{self.name}'s bio:\n{self.bio}"

    def set_bio(self, bio):
        self.bio = bio


talaba1 = Talaba('alisher', '1112@', '2011', 'aaalli1', 'im backend engineer')

print(talaba1.get_info())
print("Password:", talaba1.get_password())
print("Account:", talaba1.get_account())
print("all users:", Shahs.get_count())