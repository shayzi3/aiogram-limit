from enum import Enum


class Language(Enum):
     RU = "Осталось времени до следующего использования:"
     EN = "Time left until next use:"
     
     def __str__(self):
          return self.value