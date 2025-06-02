from datetime import datetime
from typing import Protocol

from asgiref.sync import async_to_sync

from ..schema import CallbackData



class AbstractStorage(Protocol):
     
     @async_to_sync
     async def get_data(
          cls, 
          callback_name: str
     ) -> bool | CallbackData:
          ...
          
     @async_to_sync
     async def update_data_users(
          cls, 
          callback_name: str, 
          data: dict[str, datetime]
     ) -> None:
          ...
     
     
     async def get_data(
          cls, 
          callback_name: str
     ) -> bool | CallbackData:
          ...
          
          
     async def update_data_users(
          cls, 
          callback_name: str, 
          data: dict[str, datetime]
     ) -> None:
          ...