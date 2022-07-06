class Date:
     def __init__(self, *args):
          self.day, self.month, self.year = args

     @classmethod
     def parse_date_str(cls, str_date):
          return tuple(map(int, str_date.split('-')))

     @classmethod
     def is_date_valid(cls, str_date):
          d, m, y = cls.parse_date_str(str_date)
          return 0 < d <= 31 and 0 < m <= 12 and y > 0

     @classmethod
     def from_string(cls, str_date):

