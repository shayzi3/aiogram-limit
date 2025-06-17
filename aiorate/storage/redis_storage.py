from typing import Optional
from datetime import datetime
from redis.asyncio import Redis

from .abstract_storage import AbstractStorage



class RedisStorage(AbstractStorage):
     def __init__(self, redis: Redis):
          self.name = "aiorate"
          self.redis = redis
     
     
     async def get_data(self, key: str) -> Optional[datetime]:
          async with self.redis as session:
               result = await session.hget(
                    name=self.name,
                    key=key
               )
          return (
               datetime.fromisoformat(result.decode()) 
               if result 
               else None
          )
               
               
     async def update_data(self, key: str, value: datetime) -> None:
          async with self.redis as session:
               await session.hset(
                    name=self.name,
                    key=key,
                    value=value.isoformat()
               )