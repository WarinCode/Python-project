from abc import abstractmethod 
from datetime import datetime as dt
from random import randint , random , choice
from math import floor
# นำเข้า module (ข้อมูลเมนู)
from menu import list_menu as data
from data import userData , addUser
# pip install prettytable
from prettytable import PrettyTable 
# pip install typing
from typing import List , Dict , Union , Any , Tuple
from statistics import mean , mode

# |ขั้นตอนการใช้งาน|                 |คำสั่ง|
# ดาวโหลด์:                        git clone -b oop https://github.com/VarinCode/Python-project.git
# เข้าถึง directory ของ project:     cd Python-project
# ติดตั้ง virtual environment:       py -m venv .venv
# เปิดใช้งาน venv:                  .venv\Scripts\activate
# ติดตั้ง library ที่อยู่ใน project:     pip install -r requirement.txt
# คำสั่งรันโปรแกรม:                   py main.py หรือ py "C:\Users\ชื่อผู้ใช้งานคอมพิวเตอร์\Desktop\Python-project\main.py"
# ปิดใช้งาน venv:                   deactivate

# The Configuration class defines the structure and abstract methods for a program.
class Configuration: #? กำหนดโครงสร้างของ Program
    #? กำหนด methods ที่สำคัญดังนี้
    
    #* ตำแหน่งต่างๆในร้านอาหาร
    POSITIONS = ("ผู้บริหาร" , "พนักงานครัว" , "ผู้ดูแลระบบ" , "ผู้จัดการ" , "แคชเชียร์" , "ผู้ใช้งานทั่วไป")
    
    #* กำหนดการตั้งค่าพื้นฐานของโปรแกรม 
    __DEFAULTSETTING__ = {
        "LoginSystem": True,
        "PriceIsDecimalNumber": False
    }
    
    #* สิทธิ์ในการใช้งานคำสั่งต่างๆในโปรแกรม 
    # อธิบายค่า value ที่อยู่ใน Properties
    # None ค่า None ยังไม่ได้กำหนดสิทธิ์ใช้งาน
    # True ค่า True อณุญาติให้มีสิทธิ์ในการใช้งานคำสั่งนั้นได้ 
    # False ค่า False ไม่อณุญาติให้มีสิทธิ์ใช้งานคำสั่งนั้น
    __PERMISSIONS__ = {
        "AddDataPermission": None,       # สิทธิ์ในการเพิ่มข้อมูล
        "DeleteDataPermission": None,    # สิทธิ์ในการลบข้อมูล
        "EditDataPermission": None,      # สิทธิ์ในการแก้ไขข้อมูล
        "DeleteAllDataPermission": None, # สิทธิ์ในการลบข้อมูลทั้งหมด
        "ViewLogPermission": None        # สิทธิ์ในการดูข้อมูล
    }
    
    MIN = 1
    MAX = 1000
    PRODUCTCODE_LENGTH = 3
    WORD_LENGTH = 28
    NAME_LENGTH = 3
    PASSWORD_LENGTH = 6
    __LOG__:List[str] = []
    
    #* ข้อมูลผู้ใช้งาน
    __user__ = {
        "name": None,
        "email": None,
        "password": None,
        "position": None,
        "AccessPermissions": __PERMISSIONS__
    }
    
    __saveUser__ = None
    __activeUser__ = None
    
    #? method ในการ login 
    def __login__(self) -> Dict[str , str]:    
        #? function ในการ login 
        def loginFunction():
            userLogin = {
                "nameOrEmail": None,
                "password": None
            }
            print('\n\tLogin')
            while not bool(userLogin["nameOrEmail"]) or not bool(userLogin["password"]):
                while not bool(userLogin["nameOrEmail"]):
                    try:
                        nameOrEmail = input("ชื่อผู้ใช้งานหรืออีเมล : ").strip()
                        if self.isEmpty(nameOrEmail):
                            raise UserWarning('❌ ชื่อผู้ใช้งานไม่ถูกต้องโปรดลองใหม่อีกครั้ง')
                        elif len(nameOrEmail) > self.WORD_LENGTH:
                            raise UserWarning('❌ ชื่อผู้ใช้งานของคุณมีความยาวมากเกินไป')
                        else:
                            userLogin['nameOrEmail'] = nameOrEmail
                    except UserWarning as err:
                        print(err)
                while not bool(userLogin["password"]):
                    try:
                        password = input("รหัสผ่าน : ").strip()
                        if self.isEmpty(password):
                            raise UserWarning('❌ รหัสผ่านผู้ใช้งานไม่ถูกต้องโปรดลองใหม่อีกครั้ง')
                        elif len(password) < self.PASSWORD_LENGTH:
                            raise UserWarning(f'❌ ความยาวของรหัสผ่านต้องมีความยาว {self.PASSWORD_LENGTH} ตัวขึ้นไป')
                        else:
                            userLogin['password'] = password
                    except UserWarning as err:
                        print(err)
            return {
                "status": bool(userLogin),
                "user": userLogin
            }
        
        #? function ในการตรวจสอบข้อมูลผู้ใช้งาน 
        def verifyUser(status: bool , validateUser: Dict[str , str]) -> bool:
            isCorrectName = False # ชื่อผู้ใช้งานถูกต้อง
            isCorrectPassword = False # รหัสผ่านถูกต้อง
            isCorrectEmail = False # อีเมลถูกต้อง
            isValid = False # ชื่อและรหัสผ่านถูกต้อง
            try:
                if status:
                    for user in userData:
                        if validateUser["nameOrEmail"] == user["name"]:
                            isCorrectName = True
                        else:
                            isCorrectName = False
                        if validateUser["nameOrEmail"] == user["email"]:
                            isCorrectEmail = True
                        else:
                            isCorrectEmail = False
                        if validateUser["password"] == user["password"]:
                            isCorrectPassword = True
                        else:
                            isCorrectPassword = False
                        # ตรวจสอบแล้วว่ามีผู้ใช้งาน    
                        if (isCorrectName or isCorrectEmail) and isCorrectPassword: 
                            isValid = True
                            del validateUser["nameOrEmail"]
                            validateUser["name"] = user["name"]
                            validateUser["email"] = user["email"]
                            validateUser["position"] = user["position"]
                            break
                        if isCorrectName and not isCorrectPassword:
                            raise Warning('❗ รหัสผ่านไม่ถูกต้องโปรดใส่รหัสผ่านให้ถูกต้อง')
                        elif not isCorrectName and isCorrectPassword:
                            raise Warning('❗ ชื่อผู้ใช้งานไม่ถูกต้องโปรดใส่ชื่อผู้ใช้งานให้ถูกต้อง')
                        elif not isCorrectName and not isCorrectPassword:
                            raise Warning('❗ ไม่มีบัญชีผู้ใช้งานนี้อยู่ในฐานข้อมูล')
                else:
                    raise Warning('เกิดข้อผิดพลาดขึ้นโปรดลองใหม่อีกครั้ง!')
            except Warning as err:
                print(err)
            else:
                self.__saveUser__ = validateUser
                print(validateUser)
            return isValid
        
        errorCounter = 0
        while not verifyUser(*loginFunction().values()):
            errorCounter += 1
            if errorCounter >= 3:
                if input('การ Login ล้มเหลวจำนวนหลายครั้งคุณต้องการ สมัครบัญชีผู้ใช้งานใหม่ไหม (y) : ').lower().strip() == "y":
                    self.__signup__()
                    break
        return self.__saveUser__
    
    #? method ในการ สมัครบัญชีผู้ใช้งานใหม่
    def __signup__(self) -> Dict[str , str]:
        print('\n','สมัครบัญชีผู้ใช้งานใหม่')
        newUser = self.__user__.copy()
        while (not bool(newUser["name"])) or (not bool(newUser["password"])) or (not bool(newUser["position"])) or (not bool(newUser["email"])):
            while not bool(newUser["name"]):
                try:
                    name = input("ตั้งชื่อผู้ใช้งาน : ").strip()
                    if self.isEmpty(name):
                        raise UserWarning('❌ ชื่อผู้ใช้งานไม่ถูกต้องโปรดลองใหม่อีกครั้ง')
                    elif len(name) > self.WORD_LENGTH:
                        raise UserWarning('❌ ชื่อผู้ใช้งานของคุณมีความยาวมากเกินไป')
                    elif len(name) <= self.NAME_LENGTH:
                        raise UserWarning('❌ ชื่อผู้ใช้งานของคุณมีสั้นน้อยเกินไป')
                    else:
                        newUser['name'] = name
                except UserWarning as err:
                    print(err)
            while not bool(newUser["email"]):
                try:
                    email = input("ใส่อีเมลที่ใช้ในบัญชีนี้ : ").strip()
                    if self.isEmpty(email):
                        raise UserWarning('❌ อีเมลไม่ถูกต้องโปรดลองใหม่อีกครั้ง')
                    elif "@" not in list(email) or "." not in list(email):
                        raise UserWarning(f'❌ {email} ไม่ใช้อีเมลโปรดลองใหม่อีกครั้ง')
                    else:
                        newUser['email'] = email
                except UserWarning as err:
                    print(err)
            while not bool(newUser["password"]):
                symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@' , '{', '|', '}', '~' , '[', '\\', ']', '^', '_', '`']
                isSymbol = False
                try:
                    password = input("ตั้งรหัสผ่าน : ").strip()
                    for letter in password:
                        if letter in symbols:
                            isSymbol = True
                    if not isSymbol:
                        raise UserWarning(f'❗ ต้องมีสัญลักษณ์อย่างน้อย 1 ตัว: {" ".join(symbols)}')
                    if self.isEmpty(password):
                        raise UserWarning('❌ รหัสผ่านผู้ใช้งานไม่ถูกต้องโปรดลองใหม่อีกครั้ง')
                    elif len(password) < self.PASSWORD_LENGTH:
                        raise UserWarning(f'❌ ความยาวของรหัสผ่านต้องมีความยาว {self.PASSWORD_LENGTH} ตัวขึ้นไป')
                    else:
                        confirmPassword = input("ยืนยันรหัสผ่าน : ").strip()
                        if confirmPassword == password:
                            newUser['password'] = password
                        elif confirmPassword != password:
                            raise UserWarning(f'รหัสผ่านที่ยืนยันไม่ถูกต้องกับรหัสผ่านที่ตั้ง')
                except UserWarning as err:
                    print(err)
            while not bool(newUser["position"]):
                print(f'💬 ตำแหน่งงานในร้านอาหาร :' , " , ".join(self.POSITIONS))
                try:
                    position = input("ตำแหน่งงานหรือหน้าที่ของคุณคือ : ").strip()
                    if self.isEmpty(position):
                        raise UserWarning('❌ คุณไม่ได้ใส่ตำแหน่งงานของคุณโปรดกรอกตำแหน่งงานของคุณ')
                    elif position not in self.POSITIONS:
                        raise UserWarning(f'❌ ตำแหน่ง "{position}" ไม่มีอยู่ในร้านอาหารของเราโปรดลองใหม่อีกครั้ง')
                    else:
                        newUser['position'] = password
                except UserWarning as err:
                    print(err)
        else:
            print('สมัครบัญชีผู้ใช้งานใหม่นสำเร็จโปรด Login เพื่อเข้าใช้งานโปรแกรม')
            # เพื่มผู้ใช้งาน
            addUser(newUser)
            return self.__login__()
    
    #? method เอาบัญชีผู้ใช้งานออกจากระบบ
    def __logout__(self):
        if input('คุณต้องการออกจากบัญชีผู้ใช้งานนี้ (y) : ').lower().strip() == "y":
            if bool(self.__activeUser__):
                self.__activeUser__ = None
                self.__setUser__(user=self.__user__ , isNone=True)
        else:
            print('คุณยกเลิกการออกจากบัญชีนี้')

    def __setUser__(self , user:Dict[str , str] , isNone: bool = False) -> None:
        if isNone:
            for key in user:
                self.__user__[key] = None
        else:
            for key in user:
                self.__user__[key] = user[key]
        
    def __getUser__(self) -> Dict[str , str | Any] | None:
        user = None
        while not bool(user):
            try:
                print(*('พิมพ์ (1) เพื่อ Login เข้าสู่ระบบ' , 'พิมพ์ (2) เพื่อสมัครบัญชีผู้ใช้งาน') , sep='\n')
                ask = int(input('โปรดเลือกตัวเลือก : '))
                if ask == 1:
                    user = self.__login__()
                elif ask == 2:
                    user = self.__signup__()
                else:
                    raise Warning(f'❌ ไม่มี "{ask}" ในตัวเลือกของการถาม โปรดพิมพ์แค่ 1 หรือ 2 เท่านั้น')
            except ValueError:
                print('♦ โปรดพิมพ์เป็นตัวเลขเท่านั้น')
            except Warning as err:
                print(err)
        return user

    #     "AddDataPermission": None,       # สิทธิ์ในการเพิ่มข้อมูล
    #     "DeleteDataPermission": None,    # สิทธิ์ในการลบข้อมูล
    #     "EditDataPermission": None,      # สิทธิ์ในการแก้ไขข้อมูล
    #     "DeleteAllDataPermission": None, # สิทธิ์ในการลบข้อมูลทั้งหมด
    #     "ViewLogPermission": None        # สิทธิ์ในการดูข้อมูล
    def __setPermissions__(self , user: Dict[str , Any]) -> None:
        position = user["position"]
        if position == "ผู้บริหาร" and position == "ผู้ดูแลระบบ":
            for key in self.__user__["AccessPermissions"]: # loop การเข้าถึงสิทธิ์ทั้งหมด อณุญาติสิทธิ์ทั้งหมด
                self.__user__["AccessPermissions"][key] = True
        elif position == "ผู้จัดการ":
            self.__user__["AccessPermissions"]["AddDataPermission"] = True
            self.__user__["AccessPermissions"]["EditDataPermission"] = True
            self.__user__["AccessPermissions"]["DeleteDataPermission"] = False
            self.__user__["AccessPermissions"]["DeleteAllDataPermission"] = False
            self.__user__["AccessPermissions"]["ViewLogPermission"] = False
        # print(user)
    
    #? method ในการแปลงชนิดค่าข้อมูลที่ส่งมา 
    def convertValue(self , value: str) -> Union[int , float]:
        if self.__DEFAULTSETTING__["PriceIsDecimalNumber"]:
            typeOf = int
        elif not self.__DEFAULTSETTING__["PriceIsDecimalNumber"]:
            typeOf = float
        return typeOf(value)
    
    def isEmpty(self , var: str) -> bool:
        return var == "" or var.__len__() == 0
    
    #? method ในการบันทึกข้อมูลการทำงานต่างๆของโปรแกรม 
    def __log__(self , text:str , Type:None | str = None , Item: None | Any = None) -> None:
        if bool(text) and (Type is None and Item is None):
            formatStr = f"{self.getTime(milliseconds=True)}\t {text}"
            
        if Type == "บันทึก":
            formatStr = f"{self.getTime(milliseconds=True)}\t ✓ เพิ่มสินค้า \"{Item}\" ในรายการเมนูสำเร็จ"
        elif Type == "ลบ":
            formatStr = f"{self.getTime(milliseconds=True)}\t ลบสินค้า \"{Item}\" ในรายการเมนู"
        elif Type == "แก้ไข":
            formatStr = f"{self.getTime(milliseconds=True)}\t 🔧 แก้ไขข้อมูลสินค้า \"{Item}\" ในรายการเมนู"
        elif Type == "ล้มเหลว":
            formatStr = f"{self.getTime(milliseconds=True)}\t เกิดปัญหาขึ้น {text} "
        elif Type == "สั่งซื้อ":
            formatStr = f"{self.getTime(milliseconds=True)}\t สั่งซื้ออาหาร \"{Item}\" จำนวน {Item} อย่าง"
        self.__LOG__.append(formatStr)
    
    #? ใช้ abstract method และเป็น private method
    
    @abstractmethod
    def __setElements__(self) -> None:
        pass
    
    @abstractmethod
    def __search__(self , param: str) -> int:
        pass
    
    @abstractmethod
    def __placeOrder__(self) -> None:
        pass
    
    @abstractmethod
    def __addItems__(self) -> None:
        pass
    
    @abstractmethod
    def __addItems__(self) -> None:
        pass
    
    @abstractmethod
    def __removeItems__(self) -> None:
        pass
    
    @abstractmethod
    def __editItems__(self) -> None:
        pass
    
    @abstractmethod
    def __deleteMenu__(self) -> None:
        pass
    
    @abstractmethod
    def __exitProgram__(self) -> None:
        pass
                
# The class Program inherits from the Configuration class.
class Program(Configuration):
    #? กำหนด attributes
    
    #* วันที่
    days = ("จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์" , "อาทิตย์")
    months = ("มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม")
    #* วันเวลาปัจจุบัน
    now = dt.now()
    time = now.time()
    year = now.date().year + 543
    today = now.date().strftime('%d/%m/%Y') 
    
    #* ตัวแปรไว้เป็นค่าอ้างอิงเลข index ในการหาอาหารสินค้าในรายการเมนู
    __foodList__: List[str] = []
    __idList__: List[str] = []
    
    #* รายการที่ผู้ใช้สั่งเมนูอาหารจะเก็บไว้ในตัวแปร order
    currentOrder: Dict[str , int] = {} # key คือ ชื่ออาหาร , value คือ จำนวนสินค้าที่สั่ง
    __allOrders__: List[Dict[str , int]] = []    # order ทั้งหมดจะเก็บไว้ใน list 
    result = 0          # ยอดเงินรวมจำนวนล่าสุดของ currentOrder
    __totalMoney__ = []    # ยอดเงินรวมทั้งหมดใน 1วัน เก็บเป็นยอดสั่งอาหารเรียงแต่ละรายการ
    orderNumber = 0   # หมายเลขจำนวนครั้งในการสั่ง order
    
    #* ค่าสถานะทุกอย่างของโปรแกรม
    __programStatus__ = {
       "isDeleted": None,  # สถานะการลบสินค้า -> True: มีการลบสินค้าแล้ว , False: ไม่มีการลบสินค้า
       "isWorking": None,  # สถานะการทำงานของ method (EXECUTE) หลัก -> True: กำลังทำงาน , False: ไม่ได้ทำงาน
       "programeIsRunning" : False, # สถานะการทำงานอยู่ของโปรแกรม -> True: กำลังทำงาน , False: ไม่ได้ทำงาน
       "isInvokeMethods": None, # สถานะการทำงานของ method ->  True: method กำลังทำงาน , False: method หยุดทำงาน
       "isError": None, # สถานะการเกิดข้อผิดพลาดขึ้นใน method ที่กำลังทำงาน -> True: เกิดข้อผิดพลาด , False: ไม่เกิดข้อผิดพลาด
       "isContinue": None, # สถานะการดำเนินการต่อใน method -> True: ทำต่อ , Falnionse: หยุดทำ
    }
    
    #* ชื่อคำสั่งที่ใช้งานในโปรแกรม
    __KEYWORDS__ = ("e" , "c", "m" , "b", "a" , "d" , "l" , "ed" , "cl" , "exit" , "commands", "menu" , "buy" ,"add" , "delete" , "log" , "edit" , "clear")
    
    #* เช็คคำที่ใส่มาว่าเป็นคำสั่งหรือไม่
    def isKeyword(self , param: str) -> bool:
        return param in self.__KEYWORDS__
    
    #? รันคำสั่งโปรแกรมตอนเริ่มต้น
    def __init__(self , menu:List[Dict[str , Union[int , str]]] , Table: Any) -> None:
        self.__log__(text="เริ่มต้นทำงานโปรแกรม")
        # print(self.__user__)
        if self.__DEFAULTSETTING__["LoginSystem"]:
            user = super().__getUser__()
            super().__setUser__(user)
            super().__setPermissions__(user)
            self.__activeUser__ = user
        # เรียกใช้ method จาก superclass 
        # เริ่มสถานะการทำงานของโปรแกรม
        self.__programStatus__["programeIsRunning"] = True 
        # รับค่า parameter(menu) มาเก็บไว้ใน attribute menu
        self.__menu__ = menu
        # สร้างตาราง
        self.__menuTable__ = Table() # ตารางอาหาร
        self.__commandsTable__ = Table() # ตารางคำสั่ง
        # สร้างเลข id(รหัสสินค้า)
        for item in self.__menu__: 
            item["id"] = self.createId(self.PRODUCTCODE_LENGTH)
        # เพิ่มคำสั่งแต่ละ columns
        self.__commandsTable__.add_column('คำสั่ง', self.__KEYWORDS__[:9]) # index ที่ 0 - 8
        self.__commandsTable__.add_column('ชื่อคำสั่งเต็ม', self.__KEYWORDS__[9:]) # index ที่ 9 ขึ้นไป
        self.__commandsTable__.add_column("ความหมายของคำสั่ง" , ("ออกจากโปรแกรม" , "แสดงคำสั่ง" , "แสดงเมนูอาหาร" , "สั่งซื้อสินค้า" , "เพิ่มรายการสินค้า" , "ลบรายการสินค้า" , "แสดง log ของโปรแกรม" ,"แก้ไขชื่อรายการสินค้า" , "ลบรายการสินค้าทั้งหมด"))
        # นำเข้า property(value) ใน dict เรียงเก็บไว้ใน list ตอนเริ่มโปรแกรม
        self.__setElements__() 
        self.greeting(self.time.hour) # ทักทายผู้ใช้งาน
        self.showCommands() # แสดงคำสั่ง
    
    def getTime(self , milliseconds: bool = False) -> str:
        if milliseconds:
            return f"{dt.now().time()}"
        elif not milliseconds:
            return f"{self.time.hour}:{f'0{self.time.minute}' if self.time.minute < 10 else self.time.minute}:{f'0{self.time.second}' if self.time.second < 10 else self.time.second}"
    
    #? method สวัสดีในแต่ละช่วงเวลา
    def greeting(self , h: int) -> None:
        hi = ''
        if 12 > h >= 0: hi = 'สวัสดีตอนเช้า'
        elif 18 >= h >= 12: hi = 'สวัสดีตอนบ่าย'
        elif 23 >= h >= 19: hi = 'สวัสดีตอนเย็น'
        # แสดงข้อความ
        if self.__DEFAULTSETTING__["LoginSystem"]:
            print(f'🙏 {hi} คุณ {self.__user__["name"]} วันนี้ วัน{self.days[self.now.date().weekday()]} ที่ {self.now.date().day} เดือน {self.months[self.now.date().month - 1]} ปี พ.ศ. {self.year} ({self.today})')
        else:
            print(f'🙏 {hi} วันนี้ วัน{self.days[self.now.date().weekday()]} ที่ {self.now.date().day} เดือน {self.months[self.now.date().month - 1]} ปี พ.ศ. {self.year} ({self.today})')
        print(f"🕓 เวลา {self.time.hour}:{f'0{self.time.minute}' if self.time.minute < 10 else self.time.minute}:{f'0{self.time.second}' if self.time.second < 10 else self.time.second}")
        print('โปรแกรมพร้อมให้บริการ 🙂')
        
    #? method สร้างเลข id
    def createId(self , length: int = 7) -> int:
        numbers:List[str] = []  # เก็บตัวเลขที่สุ่มมาได้ไว้ใน list
        rand = lambda: str(floor(random() * randint(1,10000)))  # สุ่มเลขส่งคืนกลับมาเป็น string 
        while True:
            num = choice(rand()) # สุ่มเลือก 1 element เลขของผลลัพธ์ 
            if len(numbers) == length: break # ถ้าเท่ากับความยาวที่ตั้งไว้ให้หยุด loop ซ้ำ
            else: 
                numbers.append(num)  # เก็บตัวเลขเข้าใน list
                if numbers[0] == '0': numbers.remove('0') # ไม่เอาเลข 0 นำหน้า
        newId = str("".join(numbers))  # รวม element ใน list ให้เป็นข้อความ
        numbers.clear()
        return newId
    
    #? method ในการเปลี่ยนค่าข้อมูลใน foodList , idList เมื่อในรายการในเมนู (menu) มีการเปลี่ยนแลง ตัวแปรทั้ง 2 ตัวนี้จะเปลี่ยนตามด้วย
    def __setElements__(self) -> None:
        # method getValue จะวน loop ดึง value ที่อยู่ใน dict ของ menu
        def getValue(setInitialValue: List[str] , keyName: str) -> List[str]: 
            setInitialValue.clear() # ล้างค่า elements เก่าทุกครั้ง
            for item in self.__menu__: setInitialValue.append(item[keyName]) # เพิ่ม element ใหม่ให้ parameter
            newValue = setInitialValue 
            return newValue
        # ถ้าไม่มีรายการสินค้าอะไรในเมนูให้ลบข้อมูล li อันเก่าทั้งหมด 
        if self.__menu__ == []:
            self.__foodList__.clear()
            self.__idList__.clear()
        else:
            # เก็บค่า list ที่ได้ให้ 2 ตัวแปร
            self.__foodList__ = getValue(setInitialValue=self.__foodList__ , keyName="name") 
            self.__idList__ = getValue(setInitialValue=self.__idList__ , keyName="id")
        
    #? method ในการค้นหา dictionary ที่อยู่ใน foodList , idList (อ่านค่าใน list) ส่งคืนกลับเป็นเลข index หรือ None 
    def __search__(self , param: str) -> int | None:
        # เช็ค parameter ที่ส่งมา 
        checked =  param.strip() # ตัดเว้นว่างออก
        # มีข้อมูลใน รายการอาหาร
        if checked in self.__foodList__:
            idx = self.__foodList__.index(checked)
        # มีข้อมูลใน รายการรหัสสินค้า
        elif checked in self.__idList__:
            idx = self.__idList__.index(checked)
        # ถ้าไม่มีข้อมูลอยู่ในทั้ง 2 รายการให้ส่งค่า None
        elif (checked not in self.__foodList__) and (checked not in self.__idList__): 
            return None 
        return idx

    #? method แสดงเมนูอาหาร
    def showMenu(self):
        # ตัวอย่างประกอบการใช้งาน Library: https://pypi.org/project/prettytable
        self.__menuTable__.clear() # reset ข้อมูลตารางใหม่ทุกครั้งเมื่อเรียกใช้ function
        self.__menuTable__.field_names = ('ลำดับ' , 'อาหาร' , 'ราคา(บาท)' , 'รหัสสินค้า') # สร้าง field
        n = 1 
        for item in self.__menu__:
            # print(f'{n}. {item["name"]} ราคา {item["price"]} บาท รหัสสินค้า {item["id"]}')
            self.__menuTable__.add_row((n , item["name"] , item["price"] , int(item["id"])) , divider=True) # เพิ่ม row ใหม่ตามเมนูที่มีอยู่ในปัจจุบัน
            n += 1
        # แสดงตารางเมนูถ้าไม่พบข้อมูลสินค้าไม่ต้องแสดงตาราง (เขียนในรูแบบ ternary operator)
        print(f'🌟 ตอนนี้ไม่มีรายการสินค้าใดๆโปรดเพิ่มสินค้าก่อนแสดงรายการเมนู!') if self.__menu__.__len__() == 0 else print('\n',self.__menuTable__ , '\n')
    
    #? method แสดงคำสั่ง
    def showCommands(self) -> None:
        print('\nเลือกพิมพ์คำสั่งเหล่านี้เพื่อดำเนินการ'.center(50))
        print(self.__commandsTable__,'\n')
    
    #? แสดงข้อความแจ้งเตือนทุกครั้งตอนเรียกใช้ methods
    def notify(self , context: str , *args: Tuple[str] | None) -> None: # แสดงข้อความเมื่อเรียกคำสั่งที่พิมพ์ไป
        print(f'❔ พิมพ์ตัว "m" หรือ "menu เพื่อแสดงเมนู\n❔ พิมพ์ตัว "e" หรือ "end" {context}')
        # การส่งค่า parameter ตัวที่ 2 เป็น None คือไม่ต้องการแสดงข้อความอย่างอื่นเพิ่ม
        if args[0] == None: pass
        else: print(*args, sep='\n')
                                                                                                                                                                                                                 
    #? method สั่งซื้อรายการสินค้า
    def __placeOrder__(self) -> None:  
        # แสดงแจ้งเตือน
        self.notify("เพื่อออกจากการสั่งซื้อ" , "❔ พิมพ์ตัว \"c\" หรือ \"cancel\" เพื่อยกเลิก order ที่สั่งไปทั้งหมด"
        , "❔ พิมพ์ตัว \"s\" หรือ \"show\" เพื่อแสดงรายการที่สั่งไปทั้งหมด")
        
        # เมื่อหยุดการทำงานของ method นี้ให้คำนวณยอดเงินรวม order ที่สั่งไป
        def calculateOrder() -> None:
            # มีการสั่งอาหาร = ข้อมูลใน dict จะไม่เป็น 0
            if (self.currentOrder.__len__() != 0) or self.currentOrder != {}: 
                priceList:List[int] = [] # เก็บราคาอาหาร(ราคาจานละ)
                showOrder = self.currentOrder.copy() # dict ที่จะแสดงใน print                
                self.__allOrders__.append(self.currentOrder.copy()) # เก็บ order
                for item in self.currentOrder:  # loop รายชื่ออาหารที่ทำการสั่งมาทั้งหมด
                    idx = self.__search__(item) # หาเลข index แต่ละรายการมาอ้างอิงข้อมูลในเมนู
                    # จำนวนสินค้า X กับราคาสินค้าที่อยู่ในเมนู = ราคาอาหารทั้งหมดของอาหารนั้น
                    # currentOrder{ Key: แต่ละรายชื่ออาหาร , Value: แต่ละราคาอาหารรวมทั้งหมด }
                    self.currentOrder[item] = (self.currentOrder[item] * self.__menu__[idx]["price"])
                    # ราคารียงชื่ออาหารตามลำดับของ currentOrder
                    priceList.append(self.__menu__[idx]["price"])
                # ผลรวมจำนวนเงินที่ต้องจ่าย
                self.result = sum(self.currentOrder.values())
                # เก็บ li จำนวนแต่ละราคาอาหารที่สั่งไป
                self.__totalMoney__.extend(self.currentOrder.values())
                self.orderNumber += 1
                print(f"\nหมายเลขรายการสั่งอาหารที่ {self.orderNumber}. รายการอาหารที่สั่งไปคือ : ")
                for number, key in enumerate(showOrder):
                    print(f"🍽 {number + 1}. {key} จำนวน {showOrder[key]:,} อย่าง ราคาจานละ {priceList[number]} บาท รวมเป็นเงิน {self.currentOrder[key]:,} บาท")
                print(f"💸 ยอดเงินรวมท้งหมด {self.result:,} บาท")
                # เริ่มสั่งรายการใหม่ให้ set ค่าเริ่มใหม่หมด (ลบสินค้า order ปัจจุบันออก)
                self.result = 0
                self.currentOrder.clear()
                # ถ้าไม่ได่สั่งอะไรไม่ต้องแสดงรายการ
            else: 
                print('ไม่มีการสั่งอาหารรายการใดๆ')
                
        # infinity loop จนกว่าจะพิมพ์คำสั่ง "e" หรือ "end" เพื่อออกจาก loop
        while self.__programStatus__["isInvokeMethods"]:
            try:
                foodName = input("ชื่ออาหารหรือรหัสสินค้า : ")
                foodName = foodName.lower().strip()
                # แสดงรายการเมนู
                if foodName == 'm' or foodName == 'menu': 
                    self.showMenu()
                    continue
                # ออกจาการทำงานของ method
                elif foodName == "e" or foodName == "end":
                    # ! เมื่อหยุดการทำงานของ function __placeOrder__ ให้เรียกใช้ method คำนวณสินค้า
                    calculateOrder()
                    self.__programStatus__["isInvokeMethods"] = False
                # ยกเลิกอาหารที่สั่ง
                elif foodName == "c" or foodName == "cancel":
                    self.currentOrder.clear()
                    print('✔ ลบรายการ order ที่ทำการสั่งไปเรียบร้อย')
                # แสดง order ที่สั่งไป
                elif foodName == 's' or foodName == 'show':
                    if self.currentOrder == {}:
                        print('❗ ยังไม่มีการสั่งเมนูอาหารโปรดสั่งอาหารเพื่อทำการแสดงรายการที่สั่ง')
                    count = 0
                    print('อาหารที่คุณสั่งไป')
                    for key , valaue in self.currentOrder.items():
                        count += 1
                        print(f'{count}.) {key} จำนวน {valaue} อย่าง')
                elif (foodName in self.__foodList__) or (foodName in self.__idList__):
                    self.__programStatus__["isContinue"] = True
                    while self.__programStatus__["isContinue"]:
                        try:
                            amount = int(input("จำนวน : ")) # จำนวนอาหาร
                            if amount <= 0 or amount >= 30:
                                raise UserWarning("❌ จำนวนอาหารไม่ถูกต้องโปรดใส่จำนวนใหม่อีกครั้ง!")
                        except ValueError:
                            print("❌ โปรดใส่เป็นเลขจำนวนเต็มเท่านั้น!")
                        except UserWarning as err:
                            print(err)
                        else:
                            self.__programStatus__["isContinue"] = False
                    # แปลงรหัสสินค้าให้เป็นชื่ออาหาร
                    if foodName in self.__idList__: 
                        idx = self.__search__(foodName)
                        foodName = self.__menu__[idx]["name"]
                    # เพิ่มสินค้าที่สั่งลง order
                    # ถ้าเป็นชื่ออาหารที่ยังไม่มี key อยู่ใน dict    
                    if foodName not in self.currentOrder: 
                        # key: ชื่ออาหาร , value: จำนวนอาหาร
                        self.currentOrder[foodName] = amount # เก็บจำนวนอาหาร
                    # ถ้ามีชื่อ key ซ้ำเป็นอยู่แล้วให้เพิ่มจำนวนอาหารเท่ากับของใหม่     
                    elif foodName in self.currentOrder: 
                        self.currentOrder[foodName] += amount # เพิ่มจำนวนอาหารที่มีอยู่แล้ว
                # ไม่มีชื่ออาหารอยู่ในเมนู    
                elif (foodName not in self.__foodList__) and (foodName not in self.__foodList__): 
                    raise UserWarning(f'❌ ไม่มีชื่อ "{foodName}" อยู่ในเมนูอาหาร!')
                else:
                    raise UserWarning(f'❌ ไม่มีชื่อ "{foodName}" อยู่ในเมนูอาหาร!')
            except UserWarning as err:
                print(err)
                
    #? method เพิ่มรายการสินค้า
    def __addItems__(self) -> None:
        # แสดงแจ้งเตือน
        self.notify('เพิ่อออกจาการเพิ่มสินค้า' , None)
        # infinity loop จนกว่าจะพิมพ์คำสั่ง "e" หรือ "end" เพื่อออกจาก loop
        while self.__programStatus__["isInvokeMethods"]:
            try:
                newProduct = input('ชื่ออาหารใหม่ : ') 
                newProduct = newProduct.strip().lower()
                # ออกจาการทำงานของ method
                if newProduct == "e" or newProduct == "end": 
                    self.__programStatus__["isInvokeMethods"] = False
                # แสดงรายการเมนู    
                elif newProduct == "m" or newProduct == "menu": 
                    self.showMenu()
                    continue
                else:
                    # ห้ามมีชื่ออาหารที่ตั้งมาใหม่ซ้ำกับข้อมูลในเมนู
                    if newProduct in self.__foodList__:
                        raise UserWarning(f'❌ ไม่สามารถใช้ชื่อ "{newProduct}" ในการตั้งเมนูใหม่ได้เนื่องจากมีชื่อซ้ำอยู่ในเมนูโปรดตั้งชื่อใหม่!')
                    # ห้ามเกินความยาวในการตั้งชื่ออาหารที่กำหนด
                    elif len(newProduct) >= self.WORD_LENGTH: 
                        raise UserWarning('❌ ไม่สามารถตั้งชื่ออาหารที่มีความยาวเกินได้')
                    # ห้ามตั้งชื่ออาหารขึ้นต้นเป็นตัวเลขหรือตั้งชื่อเป็นตัวเลข
                    elif newProduct.isdigit() or newProduct[0].isdigit():
                        raise UserWarning(f'❌ ไม่สามารถตั้งชื่ออาหารที่เป็นเลขขึ้นต้นได้')
                    # ตรวจแล้วไม่มีเงื่อนไข error ใดๆให้ดำเนินการต่อ
                    else:
                        self.__programStatus__["isContinue"] = True # set ค่าสถานะให้ดำเนินการต่อ
            except UserWarning as err:
                print(err)
            # เช็คแล้วว่าไม่ใช้คำสั่งหรือใส่ชื่อเรียบร้อยให้ใช้เงื่อนไขเพิ่มราคาสินค้า
            else:
                while self.__programStatus__["isContinue"]:
                    try:
                        print('💬 ราคาสินค้าสามารถตั้งอยู่ในช่วงราคา 1 ถึง 1,000 บาท')
                        price = self.convertValue(input('ราคาอาหาร : '))  
                        # ห้ามตั้งเกินราคาที่ตั้งไว้ 
                        if price > self.MAX: 
                            raise UserWarning('❌ ไม่สามารถตั้งราคาอาหารเกิน 1,000 บาทได้')
                        # ห้ามตั้งน้อยกว่าราคาที่ตั้งไว้ 
                        elif price <= self.MIN: 
                            raise UserWarning('❌ ไม่สามารถตั้งราคาอาหารติดลบหรือเป็นศูนย์ได้')
                        else:
                            # เมื่อชื่ออาหารที่ไม่มีอยู่ในเมนู (เช็คแล้วว่าไม่มีชื่อสินค้าซ้ำ) ให้เพิ่มสินค้าใหม่
                            if newProduct not in self.__foodList__:
                                # สร้างรายการอาหารใหม่
                                self.__menu__.append({ 
                                    "name": newProduct,
                                    "price": price,
                                    "id": self.createId(self.PRODUCTCODE_LENGTH)
                                })          
                                print('✔ เพิ่มรายการอาหารใหม่เสร็จสิ้น')
                                print(f'🍖 จำนวนรายการอาหารมีทั้งหมดตอนนี้ {len(self.__menu__)} รายการ')
                                self.__setElements__()   
                            else: 
                                raise UserWarning(f'❌ ไม่สามารถใช้ชื่อ "{newProduct}" ในการตั้งเมนูใหม่ได้เนื่องจากมีชื่อซ้ำอยู่ในเมนูโปรดตั้งชื่อใหม่!')
                    except UserWarning as err:
                        print(err)
                    except ValueError:
                        print('❌ ไม่สามารถตั้งราคาสินค้าได้ราคาสินค้าต้องตั้งเป็นตัวเลขจำนวนเต็มเท่านั้น!')
                    else: 
                        self.__programStatus__["isContinue"] = False

    # ? method ลบรายการสินค้า
    def __removeItems__(self) -> None:
        # แสดงแจ้งเตือน
        self.notify("เพื่อออกจากการลบเมนู" , None)
        # function ลบสินค้า
        def deleteElements(param: str) -> None:
            findIndex = self.__search__(param) # หาสินค้าที่ต้องการลบส่งกลับเป็นเลข index
            del self.__menu__[findIndex] # ลบสินค้า่โดยอ้างอิงเลข index
            self.__setElements__() # แก้ไข element ใน foodList และ idList เมื่อมีการลบสินค้าในเมนู
            self.__programStatus__["isDeleted"] = True
        # infinity loop จนกว่าจะพิมพ์คำสั่ง "e" หรือ "end" เพื่อออกจาก loop
        while self.__programStatus__["isInvokeMethods"]:
            self.__programStatus__["isDeleted"] = False
            try:
                item = input('ใส่ชื่ออาหารหรือรหัสสินค้าเพื่อทำการลบ : ')
                item = item.lower().strip() 
                # ออกจาการทำงานของ method
                if item == 'e' or item == 'end':  
                    self.__programStatus__["isInvokeMethods"] = False
                # แสดงรายการเมนู    
                elif item == 'm' or item == 'menu': 
                    self.showMenu()
                    continue
                # ลบข้อมูลเป็นหลายๆอย่างโดยใส่ , 
                # จะใช่เงื่อนไขนี้ได้เมื่อใส่ข้อมูลตรงตามนี้: a , b , c ,...
                elif ',' in item or ',' in [*item]: # ถ้าใส่ , ให้ทำเงิอนไขนี้
                    formatList = item.split(',') # ลบ , ออกจะได้ ข้อมูลเป็น list
                    # จัดระเบียบข้อความ
                    for i in range(formatList.__len__()): 
                        formatList[i] = formatList[i].strip() # ลบทุก elements ทุกตัวให้เอาเว้นว่างออก
                    # ถ้าใส่ , แล้วไม่มีชื่ออาหารหรือเลข id ต่อท้ายให้ลบช่องว่างเปล่าที่เกิดขึ้น
                    if '' in formatList:
                        count = formatList.count('') 
                        for j in range(count):
                            formatList.remove('') # ลบ sting เปล่าออก
                    # ลบสินค้าที่ละชิ้น
                    for element in formatList: 
                        if element in self.__foodList__: 
                            deleteElements(element)
                        elif element in self.__idList__: 
                            deleteElements(element)
                        elif (element not in self.__foodList__) and (element not in self.__idList__):
                            self.__programStatus__["isError"] = True
                            raise UserWarning(f"❌ ไม่มี \"{element}\" อยู่ในเมนูอาหารโปรดกรอกชื่อหรือเลข id ใหม่")
                # เมื่อมีข้อมูลให้ลบออก
                elif (item in self.__foodList__) or (item in self.__idList__): 
                    deleteElements(item)
                elif (item not in self.__foodList__) and (item not in self.__idList__):
                    raise UserWarning(f"❌ ไม่มี \"{item}\" อยู่ในเมนูอาหารโปรดกรอกชื่อหรือเลข id ใหม่")
                else: 
                    raise UserWarning(f"❌ ไม่มี \"{item}\" อยู่ในเมนูอาหารโปรดกรอกชื่อหรือเลข id ใหม่")
            except UserWarning as err:
                print(err)
                if self.__programStatus__["isError"]:
                    print('ยกเลิกการดำเนินการลบสินค้าล่าสุด')
            except ValueError:
                print(f"❌ ไม่มี \"{item}\" อยู่ในเมนูอาหาร")
            else:
                if self.__programStatus__["isDeleted"]:
                    print('✔ ลบรายการอาหารเสร็จสิ้น')
                    print(f'🍖 จำนวนรายการอาหารมีทั้งหมดตอนนี้ {len(self.__menu__)} รายการ')

    # ? method แก้ไขรายการสินค้า
    def __editItems__(self) -> None:
        # แสดงแจ้งเตือน
        self.notify("เพิ่อออกจาการแก้ไข" , None)
        # infinity loop จนกว่าจะพิมพ์คำสั่ง "e" หรือ "end" เพื่อออกจาก loop
        while self.__programStatus__["isInvokeMethods"]:
            try:
                self.__programStatus__["isError"] = False # set ค่าสถานะ
                # ถามข้อมูล
                product = input('ใส่ชื่ออาหารหรือรหัสสินค้าเพื่อทำการแก้ไข : ')
                product = product.lower().strip()
                # ออกจาการทำงานของ method
                if product == 'e' or product == 'end': 
                    self.__programStatus__["isInvokeMethods"] = False
                # แสดงรายการเมนู    
                elif product == 'm' or product == 'menu': 
                    self.showMenu()
                    continue
                else:
                    # หาเลข index ของเมนูอาหาร
                    findIndex = self.__search__(product)
                    idx = findIndex # เลข index
                    if idx == None: # ใส่ข้อมูลไม่ถูกต้อง
                        raise UserWarning(f'❌ "{product}" ไม่ค้นพบชื่ออารและรหัสสินค้าอยู่ในรายการสินค้าโปรดลองใหม่อีกครั้ง!')
                    else:
                        # แสดงข้อความ
                        print(f'คุณเลือกรายการสินค้าที่จะแก้ไข คือ {self.__menu__[idx]["name"]} ราคา {self.__menu__[idx]["price"]} บาท รหัสสินค้าคือ {self.__menu__[idx]["id"]}')
                        # ชื่ออาหารที่จะแก้ไขใหม่
                        changeFoodName = input(f'แก้ไขชื่อ จาก "{self.__menu__[idx]["name"]}" เป็น --> ')
                        #! ตรวจสอบความถูกต้อง
                        assert changeFoodName not in self.__foodList__ # ชื่อห้ามซ้ำกับรายการอื่นๆ
                        assert not(changeFoodName == '' or changeFoodName.__len__() == 0) # ไม่ใส่ชื่อ
                        if changeFoodName.isdigit() or changeFoodName[0].isdigit():
                            raise UserWarning('❌ ไม่สามารถตั้งชื่อขึ้นต้นด้วยตัวเลขได้หรือตั้งชื่อเป็นตัวเลขได้!')
                        print('💬 ราคาสินค้าสามารถตั้งอยู่ในช่วงราคา 1 ถึง 1,000 บาท') # แสดงข้อความ
                        # ราคาที่จะแก้ไขใหม่
                        changePrice = int(input(f'แก้ไขราคา จาก {self.__menu__[idx]["price"]} บาท เป็น --> '))
                        # ยอดเงินต้องไม่เกิน 1000 บาท และ ต้องไม่ติดลบและไม่เป็นศูนย์
                        if (changePrice > self.MAX or changePrice <= self.MIN) or (changePrice not in range(self.MIN , self.MAX)): 
                            raise UserWarning('❌ ราคาสินค้าต้องตั้งอยู่ในราคาไม่เกิน 1,000 บาทเท่านั้น!')
                        print(f'💬 รหัสสินค้าต้องตั้งเป็นเลขจำนวนเต็มจำนวน {self.PRODUCTCODE_LENGTH} ตัว')
                        # เลข id ที่จะแก้ไข
                        changeId = int(input(f'แก้ไขรหัสสินค้า จากรหัส {self.__menu__[idx]["id"]} เป็น --> '))
                        if str(changeId).__len__() != self.PRODUCTCODE_LENGTH:
                            raise UserWarning(f'❌ ต้องตั้งความของรหัสสินค้าเป็น {self.PRODUCTCODE_LENGTH} เท่านั้น!')
                        #* แก้ไขข้อมูล dictionary ในเมนู
                        self.__menu__[idx]["name"] = changeFoodName
                        self.__menu__[idx]["price"] = changePrice
                        self.__menu__[idx]["id"] = changeId
                        print('✔ แก้ไขรายการอาหารเสร็จสิ้น')          
                        # เปลี่ยนแปลงค่า li ใหม่   
                        self.__setElements__()
            except ValueError:
                self.__programStatus__["isError"] = True
                print('🔴 Error: ราคาสินค้าและรหัสสินค้าต้องตั้งเป็นตัวเลขจำนวนเต็มเท่านั้น!')
            except AssertionError:
                self.__programStatus__["isError"] = True
                print('🔴 Error: ชื่อที่คุณทำการแก้ไขนั้นเป็นชื่อซ้ำอยู่ในเมนูอาหารโปรดแก้ไขชื่อที่ไม่เหมือนกัน หรือ ห้ามชื่อว่างเปล่า!')
            except UserWarning as err:
                self.__programStatus__["isError"] = True
                print(err)
            finally:
                self.__programStatus__["isError"] and print('❗ เกิดข้อผิดพลาดขึ้นเริ่มทำรายการใหม่ตั้งแต่เริ่มต้น')

    # ? method สรุปจำนวนเงินและการสั่งซื้อสินค้า
    def conclusion(self , total: List[int] , orders: List[Dict[str , int]]) -> str:
        quantity = 0 # จำนวนอาหารที่สั่งไปทั้งหมด
        me:List[int] = mean(total) # หาค่าเฉลี่ย
        mo:List[str] = [] # ฐานนิยม
        for i in range(len(orders)):
            element = orders[i] # dict แต่ละอันใน list 
            for j in element: # เข้าถึง dist แล้วดึง key มาใช้ , ตัวแปร j คือชื่ออาหารทำการเก็บจำนวนรายการเอาไว้ 
                key = j # ชื่ออาหาร
                value = element[j] # จำนวนของอาหารที่สั่ง
                li = [key for k in range(value)] # loop ตามจำนวนครั้ง ของ value ทุกๆครั้งที่ loop จะคืนค่า(เพิ่ม) ชื่ออาหารให้ li
                mo.extend(li) # เพิ่ม li ให้ mo เพื่อนำไปหาฐานนิยมต่อไป
                quantity += value # บวกจำนวนเพิ่มแต่ละอาหาร
        mo = mode(mo) # หาฐานนิยม: return ชื่ออาหารที่มีชื่อนั้นมากสุด ถ้าไม่มีชื่ออาหารตัวไหนมากกว่ากันจะคืน element ตัวแรก
        return f"""🔷 จำนวนสั่งซื้ออาหารวันนี้ {len(orders):,} รายการ {quantity:,} อย่าง ทำจำนวนเงินรวมไปได้ {sum(total):,} บาท 
มีค่าเฉลี่ยการสั่งซื้ออาหารอยู่ที่ {me:,.2f}
อาหารที่สั่งบ่อยหรือสั่งเยอะที่สุดในวันนี้คือ {mo}
        """
                
    #? method ในการแสดงข้อมูลการทำงานต่างๆของโปรแกรม 
    def __showLog__(self) -> None:
        print('\n\tบันทึกของโปรแกรม')
        for i in self.__LOG__:
            print(i)
        print('\n')

    #? method ในการลบเมนูสินค้า
    def __deleteMenu__(self) -> None:
        if input('คุณแน่ใจว่าต้องการลบสินค้าทั้งหมดถ้าต้องการให้พิมพ์ "y" แต่โปรดรู้ไว้ข้อมูลสินค้าจะถูกลบถาวรและไม่สามารถกู้คืนได้ : ').lower().strip() == "y":
            self.__menu__.clear()
            print('✔ ลบรายการสินค้าทั้งหมดเสร็จสิ้น')
        else: print('❗ คุณยกเลิกการดำเนินการลบสินค้าทั้งหมด')

    #? method ออกจากโปรแกรม
    def __exitProgram__(self) -> None:
        self.__log__(text="จบการทำงานโปรแกรม")
        self.__programStatus__["isWorking"] = False
        #* ถ้ามีการสั่งอาหารให้แสดงรายการสรุปสินค้าที่ซื้อไปภายใน 1 วัน ถ้าไม่ได้สั่งซื้อไม่ต้องแสดง
        self.__allOrders__.__len__() != 0 and print(self.conclusion(total=self.__totalMoney__ , orders=self.__allOrders__))
        print('🙏 ขอบคุณที่มาใช้บริการของเรา')
        self.__programStatus__["programeIsRunning"] = False

    #? method ในการดำเนินการหลักของโปรแกรม
    def EXECUTE(self) -> None:
        self.__log__(text="เริ่มทำงาน function หลัก")
        # infinity loop จนกว่าจะพิมพ์คำสั่ง "e" หรือ "exit" เพื่อออกจาก loop
        while self.__programStatus__["programeIsRunning"]:
            self.__programStatus__["isWorking"] = True
            self.__programStatus__["isWorking"] and self.__log__(text="โปรแกรมรอคำสั่งเพื่อเริ่มดำเนินการทำงาน")
            try:
                command = input("🟢 พิมพ์คำสั่งเพื่อดำเนินการต่อไป >>> ")
                command = command.lower().strip()
                #! ตรวจสอบความถูกต้อง
                assert command != "" or len(command) == 0 # ถ้าไม่ได้พิมพ์คำสั่งอะไรมา
                #? ค้นหาชื่อคำสั่ง
                if self.isKeyword(command):
                    # เปลี่ยนสถานะ attribute ตัวนี้ให้เป็น True หมายถึงกำลังทำการเรียกใช้ methods ของโปรแกรม
                    self.__programStatus__["isInvokeMethods"] = True
                    #* ออกจากโปรแกรม
                    if command == "e" or command == "exit":
                        self.__log__(text="มีการเรียกใช้คำสั่ง ออกจากโปรแกรม")
                        self.__exitProgram__()
                    #* แสดงคำสั่ง
                    elif command == "c" or command == "commands": 
                        self.__log__(text="มีการเรียกใช้คำสั่ง แสดงคำสั่ง")
                        self.showCommands()
                    #* แสดงรายการเมนู
                    elif command == "m" or command == "menu": 
                        self.__log__(text="มีการเรียกใช้คำสั่ง แสดงเมนู")
                        self.showMenu()
                    #* ซื้ออาหาร
                    elif command == "b" or command == "buy":
                        self.__log__(text="มีการเรียกใช้คำสั่ง สั่งซื้อสินค้า")
                        self.__placeOrder__()
                    #* เพิ่มสินค้า
                    elif command == "a" or command == "add": 
                        self.__log__(text="มีการเรียกใช้คำสั่ง เพิ่มสินค้า")
                        self.__addItems__()
                    #* ลบสินค้า
                    elif command == "d" or command == "delete":
                        self.__log__(text="มีการเรียกใช้คำสั่ง ลบสินค้า")
                        self.__removeItems__()
                    #* แก้ไขสินค้า
                    elif command == "ed" or command == "edit": 
                        self.__log__(text="มีการเรียกใช้คำสั่ง แก้ไขสินค้า")
                        self.__editItems__()
                    #* ลบรายการสินค้าทั้งหมด
                    elif command == "cl" or command == "clear":
                        self.__log__(text="มีการเรียกใช้คำสั่ง ล้างรายการสินค้าทั้งหมด")
                        self.__deleteMenu__()
                    #* แสดงกิจกรรมการทำงานต่างๆของโปรแกรม
                    elif command == "l" or command == "log":
                        self.__showLog__()
                #* ไม้มีคำสั่งที่ค้นหา
                else: 
                    raise UserWarning(f'🔴 Error: ไม่รู้จำคำสั่ง "{command}" โปรดเลือกใช้คำสั่งที่มีระบุไว้')
            except UserWarning as err:
                print(err)
                self.__log__(Type='ล้มเหลว' , text="ไม่พบคำสั่งที่มีอยู่ในโปรแกรม")
            except AssertionError:
                print("🔴 Error: คุณไม่ได้ป้อนคำสั่งโปรดพิมพ์คำสั่ง")
                self.__log__(Type='ล้มเหลว' , text="ไม่พบคำสั่งที่มีอยู่ในโปรแกรม")
            finally:
                self.__programStatus__["isWorking"] and print('โปรดเลือกพิมพ์คำสั่ง')

# สร้าง instance(object) เพื่อนำไปใช้งาน
program = Program(menu=data[:20] , Table=PrettyTable)
program.EXECUTE() # เรียกใช้ method เพื่อดำเนินการทำงานหลักของ program