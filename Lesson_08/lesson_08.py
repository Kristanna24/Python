lesson_08.py
# -------------------------------1---------------------------------
class Data:

    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def type(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            return f'Неправильный день'
        if 1 <= month <= 12:
            return f'Неправильный месяц'
        if 2019 >= year >= 0:
            return f'Неправильный год'


print(Data.valid(30, 11, 2022))
print(Data.type('30 - 11 - 2022'))

# -------------------------------2---------------------------------
class ZeroDivisionError(Exception):
   pass

try:
   div = int(input('Enter divisor: '))
   if div == 0:
      raise ZeroDivisionError
   num = 100 / div
   print(f'Your number: {num}')
except ValueError:
   print('Enter the number')
except ZeroDivisionError:
   print("Can't divide by zero")

 # -------------------------------3---------------------------------
 class Error(Exception):
   def __init__(self, text):
      self.text = text

   def __str__(self):
      return self.text

if __name__ == '__main__':
   my_list = []

   while True:
      user = input('Enter a number or stop to exit: ')

      if user == 'stop':
         break

      try:
         if not user.isdigit():
            raise Error(f'{user} enter a number')

         my_list.append(int(user))
      except Error as e:
         print(e)

   print(my_list)

# -------------------------------4---------------------------------
# -------------------------------5---------------------------------
# -------------------------------6---------------------------------
class OfficeEquipment:

   def __init__(self, name, price, quantity):
      self.name = name
      self.price = price
      self.quantity = quantity
      self.items = {'Model: ': self.name, 'Unit price: ': self.price, 'Quantity: ': self.quantity}

   def income(self):
      try:
         name = input(f'Enter model: ')
         price = int(input(f'Enter unit price: '))
         quantity = int(input(f'Enter quantity: '))
         item = {'Model': name, 'Unit price': price, 'Quantity': quantity}
         self.items.update(item)
         print(self.items)
      except ValueError as e:
         print(e)


class Printer(OfficeEquipment):
   pass

class Scanner(OfficeEquipment):
   pass

class Xerox(OfficeEquipment):
   pass


printer = Printer('Hp', 2000, 150)
scan = Scanner('Canon', 5000, 15)
xerox = Xerox('Xerox', 6200, 25)
printer.income()
scan.income()
xerox.income()

# -------------------------------7---------------------------------
class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%si)' % (self.a, self.b)

    def __add__(self, other):
        add_a = self.a + other.a
        add_b = self.b + other.b
        return ComplexNumber(add_a, add_b)

    def __mul__(self, other):
        mul_a = self.a * other.a - self.b * other.b
        mul_b = self.b * other.a + self.a * other.b
        return ComplexNumber(mul_a, mul_b)


c = ComplexNumber(2, 5)
d = ComplexNumber(3, 6)

print(f'{c} + {d} = ', c + d)
print(f'{c} * {d} = ', c * d)