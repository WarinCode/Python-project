from typing import Dict

userData = [
    {
        "name": "john",
        "email": "john@email.com",
        "password": "123456",
        "position": "ผู้บริหาร"
    },
    {
        "name": "jane",
        "email": "jane@email.com",
        "password": "000000",
        "position": "แคชเชียร์"
    }
]

def addUser(newUser: Dict[str , str]) -> None:
    userData.append(newUser)   