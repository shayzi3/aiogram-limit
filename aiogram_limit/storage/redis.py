from .abstract_storage import AbstractStorage



class RedisStorage(AbstractStorage):
     def __init__(
          self,
          host: str = "localhost",
          port: int = 6379,
          password: str = ""
     ):
          self.redis = ...
          
          
     @classmethod
     async def get_data(cls, callback_name):
          ...
          
     @classmethod
     async def set_data(cls, callback_name, callback_data):
          ...
          
     @classmethod
     async def update_data_users(cls, callback_name, field, data):
          ...