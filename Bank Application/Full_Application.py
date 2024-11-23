class Mybank:
    ROI = 0.07
    def __init__(self, name, dob, mob, Aadhar, Pan, balance, pin):
        self.name    = name
        self.dob     = dob
        self.mob     = mob
        self.Aadhar  = Aadhar
        self.Pan     = Pan
        self.balance = balance
        self.pin     = pin

    def details(self):
        print(f'name    = {self.name}')
        print(f'dob     =  {self.dob}')
        print(f'mob     = {self.mob}')
        print(f'Aadhar  = {self.Aadhar}')
        print(f'Pan     = {self.Pan}')
        print(f'balance = {self.balance}')
    def withdraw(self):
        if self.checkpin() == self.pin:
            amount = int(input("Enter The Amount To Withdraw : "))
            if self.balance >= amount:
                self.balance -= amount
                print(f'Your amount of rs {amount} Is Debited Successfully...')
                print(f'Your Current Account Balance Is {self.balance}')
            else:
                print('Insufficient Funds...')
        else:
            print('Invalid Pin...')

    def deposite(self):
        amount = int(input('Enter The Amount To Deposite : '))
        self.balance += amount
        print(f'Your amount of rs {amount} Is Credited Successfully...')
        print(f'Your Current Account Balance IS {self.balance}')
    def checkbal(self):
        if self.checkpin() == self.pin:
            print(f'Your Current Account Balance Is {self.balance}')
        else:
            print('Invalid pin...')

    @staticmethod
    def checkpin():
        return int(input("Enter Your Pin : "))
    
    @classmethod
    def changeROI(cls):
         var = float(input('Enter The New ROI : '))
         cls.ROI = var
    def changepin(self):
        oldpin = int(input('Enter Your old pin :  '))
        if self.pin == oldpin:
            newpin = int(input('Enter The New pin : '))
            self.pin = newpin
            print("Your Pin Is Successfully Changed...")
cust1 = Mybank('Abhinaba', '31-AUG-2001', 7001171223, 123456789101, 'ABCD1234', 10000, 1234)
cust2 = Mybank('Pradip', '01-JAN-2002', 88972156386, 56789101112, 'EFGH5678', 20000, 5678)

# cust1.withdraw()
# cust2.checkbal()
# cust2.deposite()
# cust1.checkbal()
cust2.changepin()
cust2.withdraw()