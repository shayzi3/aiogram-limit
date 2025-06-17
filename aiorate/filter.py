from asyncio import iscoroutinefunction
from typing import Callable, Optional
from datetime import datetime, timedelta
from aiogram.filters import Filter
from aiogram.types import Message

from .storage import MemoryStorage, AbstractStorage
from .exception import StorageError, CoroutineError
from .enums import Language




class RateLimitFilter(Filter):
     def __init__(
          self,
          answer_callback: Optional[Callable] = None,
          answer_language: Language = Language.EN,
          storage: AbstractStorage = MemoryStorage(),
          seconds: float = 0,
          minutes: float = 0,
          hours: float = 0,
          days: float = 0,
          weeks: float = 0,
          all_users: bool = False
     ) -> None:
          if (
               iscoroutinefunction(answer_callback) is False
               and 
               answer_callback is not None
          ):
               raise CoroutineError("answer_callback must be coroutine")
          
          if isinstance(all_users, bool) is False:
               raise ValueError("all_user must be a bool type")
          
          if issubclass(type(storage), AbstractStorage) is False:
               raise StorageError("invalid storage")
          
          if isinstance(answer_language, Language) is False:
               raise ValueError("invalid answer_language")
          
          self.time = timedelta(
               seconds=seconds,
               minutes=minutes,
               hours=hours,
               days=days,
               weeks=weeks
          )
          self.storage = storage
          self.all_users = all_users
          self.answer_callback = answer_callback
          self.answer_language = answer_language
     
     
     async def __call__(self, message: Message, **kwargs) -> bool:
          user = str(message.from_user.id)
          if self.all_users is True:
               user = "users"
               
          usertime = await self.storage.get_data(user)
          if usertime is None:
               await self.storage.update_data(
                    key=user,
                    value=datetime.utcnow() + self.time
               )
               return True
          
          if usertime > datetime.utcnow():
               if self.answer_callback is not None:
                    return await self.answer_callback(
                         message, 
                         usertime, 
                         self.time 
                         **kwargs
                    )
               await message.answer(f"{self.answer_language} {(usertime - datetime.utcnow()).seconds}s")
               return False
          
          await self.storage.update_data(
               key=user,
               value=datetime.utcnow() + self.time
          )
          return True          
          