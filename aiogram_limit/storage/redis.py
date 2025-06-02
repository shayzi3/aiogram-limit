from redis.asyncio.client import Redis
from datetime import datetime

from asgiref.sync import async_to_sync

from .abstract_storage import AbstractStorage
from ..schema import CallbackData



class RedisStorage(AbstractStorage):
     def __init__(self, redis: Redis):
          self.name = "aiogram_limit"
          self.redis = redis
        
          
     @async_to_sync
     async def sync_set_data(
          self, 
          callback_name: str, 
          callback_data: CallbackData
     ) -> None:
          async with self.redis as session:
               await session.hset(
                    name=self.name,
                    key=callback_name,
                    value=callback_data.to_redis()
               )
          
         
     @async_to_sync 
     async def sync_get_data(
          self, 
          callback_name: str
     ) -> CallbackData | bool:
          async with self.redis as session:
               data = await session.hget(
                    name=self.name,
                    key=callback_name
               )
               if data is None:
                    return False
          return CallbackData.from_redis(data.decode())
                          
           
                    
     async def get_data(
          self, 
          callback_name
     ) -> CallbackData | bool:
          async with self.redis as session:
               data = await session.hget(
                    name=self.name,
                    key=callback_name
               )
               if data is None:
                    return False
          return CallbackData.from_redis(data.decode())
          
          
          
     async def update_data_users(
          self, 
          callback_name: str, 
          data: dict[str, datetime]
     ) -> None:
          async with self.redis as session:
               redis_data = await session.hget(
                    name=self.name,
                    key=callback_name
               )
               if redis_data is None:
                    return None
               
               callback_data = CallbackData.from_redis(redis_data.decode())
               callback_data.users.update(data)
               await session.hset(
                    name=self.name,
                    key=callback_name,
                    value=callback_data.to_redis()
               )
               