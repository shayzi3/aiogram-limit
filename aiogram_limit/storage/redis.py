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
     def sync_set_data(cls, callback_name, callback_data):
          ...
          
          
     @classmethod
     def sync_get_data(cls, callback_name):
          ...
                          
                    
     @classmethod
     async def get_data(cls, callback_name):
          ...
          
          
          
     @classmethod
     async def update_data_users(cls, callback_name, field, data):
          ...