from datetime import datetime as dt
from math import floor
from random import choice
from random import randint
from random import shuffle

from prettytable import PrettyTable

from menu import list_menu
# pip install prettytable
# นำเข้าข้อมูลรายการเมนู


class Program:
    """ """
    # * ตัวแปรไว้เป็นค่าอ้างอิงเลข index ในการหาอาหารสินค้าในรายการเมนู
    foodList = []
    idList = []
    # * รายการที่ผู้ใช้สั่งเมนูอาหารจะเก็บไว้ในตัวแปร order
    currentOrder = {}  # key คือ ชื่ออาหาร , value คือ จำนวนสินค้าที่สั่ง
    allOrders = []  # order ทั้งหมดจะเก็บไว้ใน list
    _sum = 0  # ยอดเงินรวมจำนวนล่าสุดของ currentOrder
    totalMoney = 0  # ยอดเงินรวมทั้งหมดใน 1วัน
    orderNumber = 0  # หมายเลขจำนวนครั้งในการสั่ง order
    # * เก็บค่าสถานะทุกอย่างของโปรแกรม
    programStatus = {
        "isDeleted": False,  # สถานะการลบสินค้า
        "isWorking": None,  # สถานะการทำงาน
        "programeIsRunning": False,  # สถานะการทำงานอยู่ของโปรแกรมหลัก
        # สถานะการทำงานของ method , True: method กำลังทำงาน , False: method หยุดทำงาน
        "isInvokeMethods": None,
    }
    KEYWORDS = (
        "e",
        "c",
        "m",
        "b",
        "a",
        "d",
        "ed",
        "cl",
        "exit",
        "commands",
        "menu",
        "buy",
        "add",
        "delete",
        "edit",
        "clear",
    )

    def isKeyword(self, param):
        """

        :param param:

        """
        return param in self.KEYWORDS

    # ? ตั้งค่าโปรแกรมเริ่มต้น
    def __init__(self, menu, table):
        self.programStatus["programeIsRunning"] = True
        self.menu = menu
        # ? สร้างตาราง
        self.menuTable = table()  # ตารางอาหาร
        self.commandsTable = table()  # ตารางคำสั่ง
        # สร้างเลข id
        for item in self.menu:
            item["id"] = self.createID()
        shuffle(self.menu)
        # เพิ่มแต่ละ columns
        self.commandsTable.add_column("คำสั่ง", self.KEYWORDS[:8])
        self.commandsTable.add_column("ชื่อคำสั่งเต็ม", self.KEYWORDS[8:])
        self.commandsTable.add_column(
            "ความหมายของคำสั่ง",
            (
                "ออกจากโปรแกรม",
                "แสดงคำสั่ง",
                "แสดงเมนูอาหาร",
                "สั่งซื้อสินค้า",
                "เพิ่มรายการสินค้า",
                "ลบรายการสินค้า",
                "แก้ไขชื่อรายการสินค้า",
                "ลบรายการสินค้าทั้งหมด",
            ),
        )
        self.setElements()
        self.showCommands()

    # ? function สวัสดีในแต่ละช่วงเวลา
    def greeting(self):
        """ """
        # * วันที่
        days = ("จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์",
                "อาทิตย์")
        months = (
            "มกราคม",
            "กุมภาพันธ์",
            "มีนาคม",
            "เมษายน",
            "พฤษภาคม",
            "มิถุนายน",
            "กรกฎาคม",
            "สิงหาคม",
            "กันยายน",
            "ตุลาคม",
            "พฤศจิกายน",
            "ธันวาคม",
        )
        # * วันเวลาปัจจุบัน
        now = dt.now()
        time = now.time()
        today = now.date().strftime("%d/%m/%Y")
        h = time.hour
        hi = ""
        if 12 > h >= 0:
            hi = "สวัสดีตอนเช้า"
        elif 18 >= h >= 12:
            hi = "สวัสดีตอนบ่าย"
        elif 23 >= h >= 19:
            hi = "สวัสดีตอนเย็น"
        print(
            f"""{hi} วัน{days[now.date().weekday()]} ที่ {now.date().day} เดือน {months[now.date().month - 1]} ปี พ.ศ. {now.year + 543} ({today})
        เวลา {time.hour}:{f'0{time.minute}' if time.minute < 10 else time.minute}:{f'0{time.second}' if time.second < 10 else time.second}
        โปรแกรมพร้อมให้บริการ 🙂""")

    # ? function สร้างเลข id
    def createID(self, length=4):
        """

        :param length:  (Default value = 4)

        """
        numbers = []  # เก็บตัวเลขที่สุ่มมาได้

        # สุ่มเลขส่งคืนกลับมาเป็น string ก้อนใหญ่
        def rand():
            """ """
            return str(floor(id({}) * randint(1, 100)))

        while True:
            ran = choice(rand())  # สุ่ม 1 เลขของผลลัพธ์
            if len(numbers) == length:
                break
            else:
                numbers.append(ran)  # เก็บตัวเลขเข้าใน list
                if numbers[0] == "0":
                    numbers.remove("0")
        _id = "".join(numbers)  # รวม element ใน list ให้เป็นข้อความ
        _id = int(_id)
        numbers.clear()
        return _id

    # ? function ในการเปลี่ยนค่าข้อมูลใน foodLi , idLi เมื่อในรายการในเมนู (menu) มีการเปลี่ยนแลง ตัวแปรทั้ง 2 ตัวนี้จะเปลี่ยนตามด้วย
    def setElements(self):
        """ """

        # function getValue จะวน loop ดึง value ที่อยู่ใน dict ของ menu
        def getValue(setInitialValue, keyName):
            """

            :param setInitialValue:
            :param keyName:

            """
            setInitialValue.clear()  # ล้างค่า elements เก่าทุกครั้ง
            for item in self.menu:
                # เพิ่ม element ใหม่ให้ parameter
                setInitialValue.append(item[keyName])
            newValue = setInitialValue
            return newValue

        # เก็บค่า tuple ให้ 2 ตัวแปร
        self.foodList = getValue(setInitialValue=self.foodList, keyName="name")
        self.idList = getValue(setInitialValue=self.idList, keyName="id")

    # ? function ในการค้นหา dictionary ที่อยู่ใน foodLi , idLi ส่งกลับเป็นเลข index
    def searchMenu(self, param):
        """

        :param param:

        """
        try:
            if param == "m" or param == "menu":
                pass
            if param in self.foodList:
                idx = self.foodList.index(param)
            elif int(param) in self.idList:
                idx = self.idList.index(int(param))
            elif (param not in self.foodList) or (int(param)
                                                  not in self.idList):
                raise Warning(
                    f'❌ "{param}" ไม่อยู่ในเมนูอาหารโปรดใส่ชื่ออาหารหรือรหัสสินค้าใหม่อีกครั้ง!'
                )
            return idx
        except ValueError:  # เมื่อใส่ชื่อหรือ id ที่ไม่อยู่ในเมนู
            print(
                f'❌ "{param}" ไม่อยู่ในเมนูอาหารโปรดใส่ชื่ออาหารหรือรหัสสินค้าใหม่ให้ถูกต้อง!'
            )
        except Warning as err:
            print(err)

    # ? function แสดงเมนูอาหาร
    def showMenu(self):
        """ """
        # documentation: https://pypi.org/project/prettytable/
        self.menuTable.clear(
        )  # reset ข้อมูลตารางใหม่ทุกครั้งเมื่อเรียกใช้ function
        self.menuTable.field_names = ("ลำดับ", "อาหาร", "ราคา(บาท)",
                                      "รหัสสินค้า")
        n = 1
        for item in self.menu:
            # print(f'{n}. {item["name"]} ราคา {item["price"]} บาท รหัสสินค้า {item["id"]}')
            self.menuTable.add_row(
                (n, item["name"], item["price"], item["id"]), divider=True)
            n += 1
        print(f"🌟 ตอนนี้ไม่มีรายการสินค้าใดๆโปรดเพิ่มสินค้าก่อนแสดงรายการเมนู!"
              ) if self.menu.__len__() == 0 else print("\n", self.menuTable,
                                                       "\n")

    # ? function แสดงคำสั่ง
    def showCommands(self):
        """ """
        print("\nเลือกพิมพ์คำสั่งเหล่านี้เพื่อดำเนินการ".center(50))
        print(self.commandsTable, "\n")

    def notify(self, text):  # แสดงข้อความเมื่อเรียกคำสั่งที่พิมพ์ไป
        """

        :param text:

        """
        print(
            f'❔ พิมพ์ตัว "m" หรือ "menu เพื่อแสดงเมนูอาหาร\n❔ พิมพ์ตัว "e" หรือ "end" {text}'
        )

    # ? function สั่งซื้อรายการสินค้า
    def placeOrder(self):
        """ """
        showOrder = {}
        self.notify("เพื่อออกจากการสั่งซื้อ")
        while self.programStatus["isInvokeMethods"]:
            try:
                foodName = input("ชื่ออาหาร : ")
                foodName = foodName.lower().strip()
                if foodName == "m" or foodName == "menu":  # แสดงรายการเมนู
                    self.showMenu()
                    continue
                elif foodName in self.foodList:
                    while True:
                        try:
                            amount = int(input("จำนวน : "))  # จำนวนอาหาร
                            if (amount <= 0) and not (foodName.isdigit()):
                                raise UserWarning(
                                    "❌ จำนวนอาหารไม่ถูกต้องโปรดใส่จำนวนใหม่อีกครั้ง!"
                                )
                        except ValueError:
                            print("❌ โปรดใส่เป็นเลขจำนวนเต็มเท่านั้น!")
                        except UserWarning as err:
                            print(err)
                        else:
                            break
                    if (foodName not in self.currentOrder
                        ):  # ถ้าเป็นชื่ออาหารที่ยังไม่มี key อยู่ใน dict
                        self.currentOrder[foodName] = amount  # เก็บจำนวนอาหาร
                    elif (
                            foodName in self.currentOrder
                    ):  # ถ้ามีชื่อ key ซ้ำเป็นอยู่แล้วให้เพิ่มจำนวนอาหารเท่ากับของใหม่
                        self.currentOrder[foodName] += amount
                # ไม่มีชื่ออาหารอยู่ในเมนู
                elif (foodName not in self.foodList) and (
                        not (foodName == "end" or foodName == "e")):
                    raise UserWarning(
                        f'❌ ไม่มีชื่อ "{foodName}" อยู่ในเมนูอาหาร!')
            except ValueError:
                print("❌ โปรดใส่เป็นเลขจำนวนเต็มเท่านั้น!")
            except UserWarning as err:
                print(err)
            # ! เมื่อหยุดการทำงานของ function placeOrder
            if foodName == "end" or foodName == "e":
                priceList = []  # เก็บราคาอาหาร
                self.allOrders.append(self.currentOrder.copy())  # เก็บ order
                showOrder = self.currentOrder.copy()  # dict ที่จะแสดงใน print
                for item in self.currentOrder:  # loop รายชื่ออาหารที่ทำการสั่งหมด
                    idx = self.searchMenu(item)
                    # จำนวนสินค้า คูณ กับราคาสินค้าที่อยู่ในเมนู
                    self.currentOrder[item] = (self.currentOrder[item] *
                                               self.menu[idx]["price"])
                    priceList.append(self.menu[idx]["price"])
                self._sum = sum(self.currentOrder.values())
                self.totalMoney += self._sum
                self.orderNumber += 1
                # ถ้าไม่ได่สั่งอะไรไม่ต้องแสดงรายการ
                if self.currentOrder.__len__() != 0:
                    print(
                        f"\nหมายเลขรายการสั่งอาหารที่ {self.orderNumber}. รายการอาหารที่สั่งไปคือ : "
                    )
                    for number, key in enumerate(self.currentOrder):
                        print(
                            f"🍽 {number + 1}. {key} จำนวน {showOrder[key]:,} อย่าง ราคาจานละ {priceList[number]} บาท รวมเป็นเงิน {self.currentOrder[key]:,} บาท"
                        )
                    print(f"💸 ยอดเงินรวมท้งหมด {self._sum:,} บาท")
                    #  เริ่มสั่งรายการใหม่ให้ set ค่าใหม่หมด (ลบสินค้า order ปัจจุบันออก)
                    self._sum = 0
                    self.currentOrder.clear()
                    showOrder.clear()
                self.programStatus["isInvokeMethods"] = False

    # ? function เพิ่มรายการสินค้า
    def addItems(self):
        """ """
        self.notify("เพิ่อออกจาการเพิ่มสินค้า")
        while True:
            try:
                newItem = input("ชื่ออาหารใหม่ : ")
                newItem = newItem.strip().lower()
                if newItem == "e" or newItem == "end":  # ออกจาการทำงานของ function
                    break
                elif newItem == "m" or newItem == "menu":  # แสดงรายการเมนู
                    self.showMenu()
                    continue
                elif ((newItem in self.foodList)
                      and not (newItem == "e" or newItem == "end")
                      and not (newItem == "m" or newItem == "menu")):
                    raise UserWarning(
                        f'❌ ไม่สามารถใช้ชื่อ "{newItem}" ในการตั้งเมนูใหม่ได้เนื่องจากมีชื่อซ้ำอยู่ในเมนูโปรดตั้งชื่อใหม่!'
                    )
            except UserWarning as err:
                print(err)
            else:
                while True:
                    try:
                        price = int(input("ราคาอาหาร : "))
                        if len(newItem) >= 28:
                            raise UserWarning(
                                "❌ ไม่สามารถตั้งชื่ออาหารที่มีความยาวเกินได้")
                        elif price > 1000:
                            raise UserWarning(
                                "❌ ไม่สามารถตั้งราคาอาหารเกิน 1,000 บาทได้")
                        elif price <= 0:
                            raise UserWarning(
                                "❌ ไม่สามารถตั้งราคาอาหารติดลบหรือเป็นศูนย์ได้"
                            )
                        else:
                            if newItem not in self.foodList:
                                # สร้างรายการอาหารใหม่
                                self.menu.append({
                                    "name": newItem,
                                    "price": price,
                                    "id": self.createID(),
                                })
                                print("✔ เพิ่มรายการอาหารใหม่เสร็จสิ้น")
                                print(
                                    f"🍖 จำนวนรายการอาหารมีทั้งหมดตอนนี้ {len(self.menu)} รายการ"
                                )
                                self.setElements()
                            else:
                                raise UserWarning(
                                    f'❌ ไม่สามารถใช้ชื่อ "{newItem}" ในการตั้งเมนูใหม่ได้เนื่องจากมีชื่อซ้ำอยู่ในเมนูโปรดตั้งชื่อใหม่!'
                                )
                    except UserWarning as err:
                        print(err)
                    except ValueError:
                        print(
                            "❌ ไม่สามารถตั้งราคาสินค้าได้ราคาสินค้าต้องตั้งเป็นตัวเลขจำนวนเต็มเท่านั้น!"
                        )
                    else:
                        break

    # ? function ลบรายการสินค้า
    def removeItems(self):
        """ """
        self.notify("เพื่อออกจากการลบเมนู")

        def deleteElements(param):
            """

            :param param:

            """
            findIndex = self.searchMenu(param)  # ส่งกลับเป็นเลข index
            del self.menu[findIndex]
            self.setElements()
            self.programStatus["isDeleted"] = True

        while True:
            self.programStatus["isDeleted"] = False
            try:
                item = input("ใส่ชื่ออาหารหรือรหัสสินค้าเพื่อทำการลบ : ")
                item = item.lower().strip()
                if item == "e" or item == "end":  # ออกจาการทำงานของ function
                    break
                elif item == "m" or item == "menu":  # แสดงรายการเมนู
                    self.showMenu()
                elif "," in item or "," in [*item]:  # ถ้าใส่ , ให้ทำเงิอนไขนี้
                    formatList = item.split(",")  # ลบ , ออก
                    # จัดระเบียบข้อความ
                    for i in range(formatList.__len__()):
                        formatList[i] = formatList[i].strip()
                        # ถ้าใส่ , แล้วไม่มีชื่ออาหารหรือเลข id ต่อท้ายให้ลบช่องว่างเปล่าที่เกิดขึ้น
                    if "" in formatList:
                        count = formatList.count("")
                        for j in range(count):
                            formatList.remove("")
                    # ลบสินค้าที่ละชิ้น
                    for element in formatList:
                        if element in self.foodList:
                            deleteElements(element)
                        elif int(element) in self.idList:
                            deleteElements(element)
                        elif (element
                              not in self.foodList) and (int(element)
                                                         not in self.idList):
                            raise UserWarning(
                                f'❌ ไม่มี "{item}" อยู่ในเมนูอาหารโปรดกรอกชื่อหรือเลข id ใหม่'
                            )
                elif (item in self.foodList) or (int(item) in self.idList):
                    deleteElements(item)
                elif (item not in self.foodList) and (int(item)
                                                      not in self.idList):
                    raise UserWarning(
                        f'❌ ไม่มี "{item}" อยู่ในเมนูอาหารโปรดกรอกชื่อหรือเลข id ใหม่'
                    )
                else:
                    raise UserWarning(
                        f'❌ ไม่มี "{item}" อยู่ในเมนูอาหารโปรดกรอกชื่อหรือเลข id ใหม่'
                    )
            except UserWarning as err:
                print(err)
            except ValueError:
                print(f'❌ ไม่มี "{item}" อยู่ในเมนูอาหาร')
            else:
                if self.programStatus["isDeleted"]:
                    print("✔ ลบรายการอาหารเสร็จสิ้น")
                    print(
                        f"🍖 จำนวนรายการอาหารมีทั้งหมดตอนนี้ {len(self.menu)} รายการ"
                    )

    # ? function แก้ไขรายการสินค้า
    def editItems(self):
        """ """
        self.notify("เพิ่อออกจาการแก้ไข")
        while True:
            try:
                item = input("ใส่ชื่ออาหารหรือรหัสสินค้าเพื่อทำการแก้ไข : ")
                item = item.lower()
                if item == "end" or item == "e":  # ออกจาการทำงานของ function
                    break
                if item == "menu" or item == "m":  # แสดงรายการเมนู
                    self.showMenu()
                    continue
                else:
                    findIndex = self.searchMenu(item)
                    idx = findIndex
                    print(
                        f'คุณเลือกรายการสินค้าที่จะแก้ไข คือ {self.menu[idx]["name"]} ราคา {self.menu[idx]["price"]} บาท'
                    )
                    changeFoodName = input(
                        f'แก้ไขชื่อ จาก "{self.menu[idx]["name"]}" เป็น -> : ')
                    assert not (changeFoodName in self.foodList)
                    assert not (changeFoodName == ""
                                or changeFoodName.__len__() == 0)
                    price = int(
                        input(
                            f'แก้ไขราคา จาก {self.menu[idx]["price"]} บาท เป็น -> : '
                        ))
                    if price > 1000 or price <= 0:
                        raise UserWarning(
                            "❌ ราคาสินค้าต้องตั้งอยู่ในราคาไม่เกิน 1,000 บาทเท่านั้น!"
                        )
                    # แก้ไขข้อมูล dict
                    self.menu[idx]["name"] = changeFoodName
                    self.menu[idx]["price"] = price
                    print("✔ แก้ไขรายการอาหารเสร็จสิ้น")
                    self.setElements()
            except ValueError:
                print(
                    "🔴 Error:\nราคาสินค้าต้องตั้งเป็นตัวเลขจำนวนเต็มเท่านั้น!")
            except AssertionError:
                print(
                    "🔴 Error:\nชื่อที่คุณทำการแก้ไขนั้นเป็นชื่อซ้ำอยู่ในเมนูอาหารโปรดแก้ไขชื่อที่ไม่เหมือนกัน หรือ ห้ามชื่อว่างเปล่า!"
                )
            except UserWarning as err:
                print(err)

    # ? function สรุปจำนวนเงินและการสั่งซื้อสินค้า
    def conclusion(self, total, orders):
        """

        :param total:
        :param orders:

        """
        quantity = 0
        for i in range(len(orders)):
            element = orders[i]  # เข้าถึง dict แต่ละอันใน list
            for j in element:  # เข้าถึง dist แล้วดึง key มาใช้
                quantity += element[j]  # บวกจำนวนเพิ่มแต่ละอาหาร
        return f"🔵 จำนวนสั่งซื้ออาหารวันนี้ {len(orders):,} รายการ {quantity:,} อย่าง ทำจำนวนเงินรวมไปได้ {total:,} บาท"

    # ? function ในการลบเมนูสินค้า
    def deleteMenu(self):
        """ """
        if (input(
                'คุณแน่ใจว่าต้องการลบสินค้าทั้งหมดถ้าต้องการให้พิมพ์ "y" แต่โปรดรู้ไว้ข้อมูลสินค้าจะถูกลบถาวรและไม่สามารถกู้คืนได้ : '
        ).lower() == "y"):
            self.menu.clear()
            print("✔ ลบรายการเมนูทั้งหมดเสร็จสิ้น")
        else:
            print("❗ คุณยกเลิกการดำเนินการลบเมนูทั้งหมด")

    # ? function ออกจากโปรแกรม
    def exitProgram(self):
        """ """
        self.programStatus["isWorking"] = False
        # * ถ้ามีการสั่งอาหารให้แสดงรายการสรุปสินค้าที่ซื้อไปภายใน 1 วัน ถ้าไม่ได้สั่งซื้อไม่ต้องแสดง
        self.allOrders.__len__() != 0 and print(
            self.conclusion(total=self.totalMoney, orders=self.allOrders))
        print("<------ จบการทำงานโปรแกรม ------>")
        self.programStatus["programeIsRunning"] = False

    def exitMethods(self):
        """ """
        pass

    # ? function ในการดำเนินการหลักของโปรแกรม
    def PROGRESS(self):
        """ """
        while self.programStatus["programeIsRunning"]:
            self.programStatus["isWorking"] = True
            try:
                command = input("🟢 พิมพ์คำสั่งเพื่อดำเนินการต่อไป >>> ")
                command = command.lower().strip()
                # ! ตรวจสอบความถูกต้อง
                assert command != "" or len(command) == 0
                # ? ค้นหาชื่อคำสั่ง
                if self.isKeyword(command):
                    self.programStatus["isInvokeMethods"] = True
                    if command == "e" or command == "exit":
                        self.exitProgram()
                    # แสดงคำสั่ง
                    elif command == "c" or command == "commands":
                        self.showCommands()
                    # แสดงรายการเมนู
                    elif command == "m" or command == "menu":
                        self.showMenu()
                    # ซื้ออาหาร
                    elif command == "b" or command == "buy":
                        self.placeOrder()
                    # เพิ่มสินค้า
                    elif command == "a" or command == "add":
                        self.addItems()
                    # ลบสินค้า
                    elif command == "d" or command == "delete":
                        self.removeItems()
                    # แก้ไขสินค้า
                    elif command == "ed" or command == "edit":
                        self.editItems()
                    # ลบรายการสินค้าทั้งหมด
                    elif command == "cl" or command == "clear":
                        self.deleteMenu()
                # ไม้มีคำสั่งที่ค้นหา
                else:
                    raise UserWarning(
                        f'🔴 Error: ไม่รู้จำคำสั่ง "{command}" โปรดเลือกใช้คำสั่งที่มีระบุไว้ให้'
                    )
            except UserWarning as err:
                print(err)
            except ValueError:
                print(
                    f"🔴 Error: สิ่งที่ท่านหาไม่มีอยู่ในเมนูอาหารโปรดใส่ชื่ออาหารหรือรหัสสินค้าใหม่อีกครั้ง!"
                )
            except AssertionError:
                print("🔴 Error: คุณไม่ได้ป้อนคำสั่งโปรดพิมพ์คำสั่ง")
            finally:
                self.programStatus["isWorking"] and print(
                    "โปรดเลือกพิมพ์คำสั่ง")


#  สร้าง instance(object) ของ program
program = Program(menu=list_menu[:30], table=PrettyTable)
program.PROGRESS()  # เรียกใช้ method เพื่อดำเนินการทำงานของ program
