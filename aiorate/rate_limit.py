from typing import Optional, Callable

from .filter import RateLimitFilter
from .storage import AbstractStorage, MemoryStorage
from .enums import Language




class RateLimit:
     def __init__(
          self,
          answer_callnack: Optional[Callable] = None,
          answer_language: Language = Language.EN,
          storage: AbstractStorage = MemoryStorage()
     ):
          self.storage = storage
          self.answer_callback = answer_callnack
          self.answer_language = answer_language
          
          
     def __call__(
          self,
          answer_callback: Optional[Callable] = None,
          answer_language: Optional[Language] = None,
          seconds: float = 0,
          minutes: float = 0,
          hours: float = 0,
          days: float = 0,
          weeks: float = 0,
          all_users: bool = False
     ) -> RateLimitFilter:
          
          return RateLimitFilter(
               answer_callback=(
                    self.answer_callback 
                    if answer_callback is None
                    else answer_callback
               ),
               answer_language=(
                    self.answer_language
                    if answer_language is None
                    else answer_language
               ),
               storage=self.storage,
               seconds=seconds,
               minutes=minutes,
               hours=hours,
               days=days,
               weeks=weeks,
               all_users=all_users
          )