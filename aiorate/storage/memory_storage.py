from typing import Optional
from datetime import datetime

from .abstract_storage import AbstractStorage



class StorageData:
     data: dict[str, datetime] = {}



class MemoryStorage(AbstractStorage):
     def __init__(self):
          self.storage_data = StorageData
          
     
     async def get_data(self, key: str) -> Optional[datetime]:
          return self.storage_data.data.get(key)
     
     
     async def update_data(self, key: str, value: datetime) -> None:
          self.storage_data.data.update({key: value})