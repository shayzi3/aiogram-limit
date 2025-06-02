from datetime import datetime
from asgiref.sync import async_to_sync

from .abstract_storage import AbstractStorage
from ..schema import CallbackData



class MemoryStorage(AbstractStorage):
     def __init__(self):
          self.storage: dict[str, CallbackData] = {}
     
     
     @async_to_sync
     async def sync_set_data(
          self, 
          callback_name: str, 
          callback_data: CallbackData
     ) -> None:
          self.storage.update({callback_name: callback_data})
          
          
     @async_to_sync
     async def sync_get_data(
          self, 
          callback_name: str
     ) -> bool:
          data = self.storage.get(callback_name)
          return True if data else False
          
     
     
     async def get_data(
          self, 
          callback_name: str
     ) -> bool | CallbackData:
          data = self.storage.get(callback_name)
          return data if data else False
     
     
     
     async def update_data_users(
          self, 
          callback_name: str, 
          data: dict[str, datetime]
     ) -> None:
          self.storage[callback_name].users.update(data)