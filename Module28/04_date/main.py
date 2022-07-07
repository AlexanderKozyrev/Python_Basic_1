class Date:
     def __init__(self, *args) -> None:
          self.day, self.month, self.year = args

     @classmethod
     def parse_date_str(cls, str_date: str) -> int:
          return tuple(map(int, str_date.split('-')))

     @classmethod
     def is_date_valid(cls, str_date: str) -> int:
          d, m, y = cls.parse_date_str(str_date)
          return 0 < d <= 31 and 0 < m <= 12 and y > 0

     @classmethod
     def from_string(cls, str_date: str) -> int:
          assert cls.is_date_valid(str_date), 'Ошибка'
          return cls(*cls.parse_date_str(str_date))

     def __str__(self) -> str:
          return f'День {self.day} Месяц {self.month} Год {self.year}'


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))