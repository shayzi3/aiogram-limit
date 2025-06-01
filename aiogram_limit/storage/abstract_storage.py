from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from ..schema import CallbackData



class AbstractStorage(ABC):
     storage: dict[str, CallbackData]
     
     
     @classmethod
     def sync_set_data(
          cls,
          callback_name: str,
          callback_data: CallbackData
     ) -> None:
          ...
          
          
     @classmethod
     @abstractmethod
     def sync_get_data(
          cls, 
          callback_name: str
     ) -> bool | CallbackData:
          ...
          
     
     @classmethod
     @abstractmethod
     async def get_data(
          cls, 
          callback_name: str
     ) -> bool | CallbackData:
          ...
          
     
          
     @classmethod
     @abstractmethod
     async def update_data_users(
          cls, 
          callback_name: str, 
          data: dict[str, datetime]
     ) -> None:
          ...