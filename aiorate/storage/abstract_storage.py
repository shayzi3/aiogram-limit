from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional



class AbstractStorage(ABC):
     
     @abstractmethod
     async def get_data(self, key: str) -> Optional[datetime]:
          raise NotImplementedError
     
     
     @abstractmethod
     async def update_data(self, key: str, value: datetime) -> None:
          raise NotImplementedError