from datetime import datetime
from typing import Callable, Any, Awaitable
from aiogram.types import Message
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from loguru import logger

from ..limit import Limits
from ..schema import CallbackData



class MiddlewareLimit(BaseMiddleware):
     def __init__(self, limits: Limits):
          self.limits = limits
          
          
     async def __call__(
          self, 
          handler: Callable[[Message, dict[str, Any]], Awaitable], 
          event: Message, 
          data: dict[str, Any]
     ) -> Any:
          handler = data.get("handler")
          if handler is None:
               logger.warning("handler object not found in data")
               
          callback_name: str = handler.callback.__name__
          callback_data: CallbackData = await self.limits._get(callback_name)
          
          if callback_data is False:
               return await handler(event, data)
          
          
          if callback_data.all_users is True:
               usertime = callback_data.users.get("usertime")
               if usertime is None:
                    await self.limits._update_users(
                         name=callback_name,
                         data={"usertime": datetime.utcnow() + callback_data.expire}
                    )
                    return await handler(event, data)
               
               if usertime >= datetime.utcnow():
                    return await event.answer(self.limits.message) # отдавать время, которое ещё нужно ждать
               
               await self.limits._update_users(
                    callback_name=callback_name,
                    data={"usertime": datetime.utcnow() + callback_data.expire}
               )
               return await handler(event, data)
               
               
          user = str(event.from_user.id)
          if callback_data.users.get(user) is None:
               await self.limits._update_users(
                    callback_name=callback_name,
                    data={user: datetime.utcnow() + callback_data.expire}
               )
               return await handler(event, data)
          
          if callback_data.users.get(user) >= datetime.utcnow():
               return await event.answer(self.limits.message)
          
          await self.limits._update_users(
               callback_name=callback_name,
               data={user: datetime.utcnow() + callback_data.expire}
          )
          await handler(event, data)
          
          
          
          
          
          