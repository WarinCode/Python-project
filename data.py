from typing import Any, Dict , List
# สมมุติโครงสร้างข้อมูลผูใช้งานโปรแกรมนี้ในร้านอาหาร
# ข้อมูลผู้ใช้งานในโปรแกรมนี้จะถูกเก็บไว้ใน list userData
# ข้างในมี dictionary ของผู้ใช้งานแต่ละคน

class Users:
    __usersData__ = [
        {
            "name": "test",
            "email": "test@email.com",
            "password": "1",
            "position": "ผู้จัดการ",
        },
        {
            "name": "john",
            "email": "john@email.com",
            "password": "111",
            "position": "ผู้จัดการ",
        },
        {
            "name": "david",
            "email": "david@email.com",
            "password": "222",
            "position": "ผู้ดูแลระบบ",
        },
        {
            "name": "jane",
            "email": "jane@email.com",
            "password": "333",
            "position": "แคชเชียร์",
        },
        {
            "name": "jack",
            "email": "jack@email.com",
            "password": "444",
            "position": "แคชเชียร์",
        },
        {
            "name": "elizabeth",
            "email": "elizabeth@email.com",
            "password": "555",
            "position": "พนักงานบาร์",
        },
        {
            "name": "robert",
            "email": "robert@email.com",
            "password": "666",
            "position": "ซอมเมลิเยร์",
        },
        {
            "name": "jill",
            "email": "jill@email.com",
            "password": "777",
            "position": "ผู้จัดการครัว",
        },
        {
            "name": "jame",
            "email": "james@email.com",
            "password": "888",
            "position": "กุ๊ก",
        },
        {
            "name": "william",
            "email": "william@email.com",
            "password": "999",
            "position": "ผู้ช่วยกุ๊ก",
        },
        {
            "name": "linda",
            "email": "linda@email.com",
            "password": "123",
            "position": "บริกร",
        },
        {
            "name": "jennifer",
            "email": "jennifer@email.com",
            "password": "456",
            "position": "พนักงานต้อนรับ",
        },
        {
            "name": "mary",
            "email": "mary@email.com",
            "password": "695",
            "position": "พนักงานต้อนรับ",
        },
    ]
    
    #? method ในการให้ข้อมูลผู้ใช้งาน
    def getUser(self) -> List[Dict[str , str]]:
        return self.__usersData__
    
    #? method ในการตั้งค่าข้อมูลผู้ใช้งาน
    def setUser(self) -> None:
        pass
    
    #? method ในการข้อมูลผู้ใช้งาน
    def addUser(self, newUser: Dict[str, str]) -> None:
        self.__userData__.append(newUser)