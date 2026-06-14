#Asynchronous execution means a program can start a slow task, pause it while it waits, and continue doing other work instead of sitting idle.

import asyncio
from pickle import APPEND
from fastapi import FastAPI
from pydantic import BaseModel

async def make_tea():
    print('Boiling water...')
    await asyncio.sleep(3)
    print('Tea Ready')
    
async def reply():
    print('Replying to messages...')
    
    
async def main():
    await asyncio.gather(
        make_tea(),
        reply()
    )
    
asyncio.run(main())



#In fastAPI
# @app.get('/users')
# async def get_users():
#     users = await fetch_users_from_database()
#     return users


#Type-Hinting
# name: str = "Harsh"
# age: int = 25
# is_active: bool = True

# def greet(name: str) -> str:
#     return f"Hello, {name}"

# print(greet(123)


#Example for object-oriented programming
# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
        
#     def greet(self)-> str:
#         return f"Hello, my name is {self.name} and I am {self.age} years old"
    
# user = User('Harsh', 25)
# print(user.greet())



class UserService:
    def __init__(self):
        self.users = []
        
    def add_user(self, name: str):
        user = {'id': len(self.users) + 1, 'name': name}
        self.users.append(user)
        return user
    
    def list_users(self):
        return self.users
    
    
service = UserService()
service.add_user('Harsh')
service.add_user('Panwar')
print(service.list_users())


async def task_one():
    await asyncio.sleep(2)
    return f"Task One Completed"
    
async def task_two():
    await asyncio.sleep(2)
    return f"Task Two Completed"
    
async def main():
    result1, result2 = await asyncio.gather(task_one(), task_two())
    print(result1)
    print(result2)

asyncio.run(main())



class Product(BaseModel):
    name: str
    price: float
    

@APPEND.post('/create-product')
async def create_product(product: Product):
    return {"message": f"Product '{product.name}' was created with price {product.price}"}