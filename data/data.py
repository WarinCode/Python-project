from typing import Dict, List
from random import shuffle

# ชื่อรายการอาหารทั้งหมด
# ข้างใน list เก็บ dictionary ทั้งหมด 171 อัน โดยเลข index อยู่ที่ 0 ถึง 170
# ข้างใน dictionary ประกอบด้วย properties 4 อันได้แก่
# name: เก็บชื่ออาหาร
# price: เก็บราคา
# id: เก็บรหัสสินค้า
# remain: จำนวนอาหาร


class Menu:
    __listMenu__ = [
        {"name": "สลัดผักมะเขือเทศและเนยสด", "price": 65, "id": 518, "remain": 30},
        {"name": "ข้าวผัดอเมริกัน", "price": 70, "id": 335, "remain": 30},
        {"name": "ปลาหมึกยักษ์", "price": 55, "id": 228, "remain": 30},
        {"name": "ลาซานญ่า", "price": 60, "id": 904, "remain": 30},
        {"name": "กุ้งสีชมพูอลาสก้า", "price": 75, "id": 636, "remain": 30},
        {"name": "ริซอตโต้เห็ด", "price": 55, "id": 322, "remain": 30},
        {"name": "ข้าวคลุกกะปิหมูกรอบ", "price": 55, "id": 975, "remain": 30},
        {"name": "ปลาทอดกระเทียม", "price": 75, "id": 806, "remain": 30},
        {"name": "ทูน่าซาซิมิ", "price": 90, "id": 683, "remain": 30},
        {"name": "แกงมัสมั่นไก่", "price": 70, "id": 302, "remain": 30},
        {"name": "ซุปผัก", "price": 80, "id": 600, "remain": 30},
        {"name": "ชีสเบอร์เกอร์", "price": 90, "id": 202, "remain": 30},
        {"name": "ปลาไหล", "price": 55, "id": 325, "remain": 30},
        {"name": "ปลากระพงทอดกระเทียมพริกไทย", "price": 80, "id": 320, "remain": 30},
        {"name": "แกงส้มชะอมหมู", "price": 60, "id": 721, "remain": 30},
        {"name": "ข้าวต้มกุ้ง", "price": 70, "id": 488, "remain": 30},
        {"name": "เฟตตูชินี่", "price": 90, "id": 515, "remain": 30},
        {"name": "ปลาอำพัน", "price": 55, "id": 477, "remain": 30},
        {"name": "ไส้กรอกหมู", "price": 80, "id": 265, "remain": 30},
        {"name": "แกงคั่วหมู", "price": 60, "id": 495, "remain": 30},
        {"name": "ก๋วยจั๊บ", "price": 45, "id": 202, "remain": 30},
        {"name": "หอยเป๋าฮื้อ", "price": 50, "id": 276, "remain": 30},
        {"name": "ด้งบุริไก่เทริยากิ", "price": 85, "id": 385, "remain": 30},
        {"name": "ไก่มิลานีส", "price": 55, "id": 943, "remain": 30},
        {"name": "แกงส้มปลากระป๋อง", "price": 65, "id": 796, "remain": 30},
        {"name": "ข้าวคลุกกะปิกุ้งสด", "price": 75, "id": 591, "remain": 30},
        {"name": "ไข่เจียว", "price": 25, "id": 495, "remain": 30},
        {"name": "กะหล่ำปลีผัดน้ำมันหอย", "price": 45, "id": 943, "remain": 30},
        {"name": "สลัดคาปรีส", "price": 70, "id": 119, "remain": 30},
        {"name": "บะหมี่เส้นใหญ่", "price": 40, "id": 506, "remain": 30},
        {"name": "ปลาเทราท์", "price": 40, "id": 113, "remain": 30},
        {"name": "ไก่ทอด", "price": 35, "id": 991, "remain": 30},
        {"name": "ข้าวคลุกกะปิหมึก", "price": 65, "id": 245, "remain": 30},
        {"name": "ข้าวหน้าเป็ด", "price": 50, "id": 255, "remain": 30},
        {"name": "ปลาอำพันเล็ก", "price": 65, "id": 611, "remain": 30},
        {"name": "ผัดผักบุ้งไข่เจียว", "price": 50, "id": 555, "remain": 30},
        {"name": "แกงส้มหมูต้ม", "price": 70, "id": 381, "remain": 30},
        {"name": "ผัดคะน้าหมูกรอบ", "price": 55, "id": 771, "remain": 30},
        {"name": "หมูสะเต๊ะ", "price": 35, "id": 763, "remain": 30},
        {"name": "ปลากระพงนึ่งมะนาว", "price": 75, "id": 488, "remain": 30},
        {"name": "เพนเน่คาลิฟลาวเวอร์", "price": 65, "id": 619, "remain": 30},
        {"name": "ปลาหมึกหิ่งห้อย", "price": 45, "id": 360, "remain": 30},
        {"name": "ปลาเก๋าลายจุด", "price": 50, "id": 845, "remain": 30},
        {"name": "ผัดไทยกุ้งสด", "price": 60, "id": 397, "remain": 30},
        {"name": "ข้าวผัดกระเพราไก่", "price": 45, "id": 456, "remain": 30},
        {"name": "พาสต้ากับมะเขือเทศและโหระพา", "price": 120, "id": 687, "remain": 30},
        {"name": "ปลากะพงสีดอกกุหลาบ", "price": 60, "id": 779, "remain": 30},
        {"name": "ลาบเป็ด", "price": 60, "id": 849, "remain": 30},
        {"name": "ก๋วยเตี๋ยวเส้นใหญ่น้ำตกหมู", "price": 65, "id": 313, "remain": 30},
        {"name": "ข้าวหมูทอดกระเทียม", "price": 50, "id": 190, "remain": 30},
        {"name": "ปลาจุดขาว", "price": 65, "id": 371, "remain": 30},
        {"name": "ฟาจิต้าไก่", "price": 95, "id": 354, "remain": 30},
        {"name": "พาสต้าและถั่ว", "price": 100, "id": 556, "remain": 30},
        {"name": "ชิลลี่คอนคาร์เน่", "price": 55, "id": 924, "remain": 30},
        {"name": "ข้าวขาหมู", "price": 55, "id": 742, "remain": 30},
        {"name": "ลาบปลาทู", "price": 75, "id": 366, "remain": 30},
        {"name": "ปลาทูม้าญี่ปุ่น", "price": 80, "id": 645, "remain": 30},
        {"name": "ไข่สก๊อต", "price": 80, "id": 450, "remain": 30},
        {"name": "สเต็กเนื้อ", "price": 75, "id": 169, "remain": 30},
        {"name": "ก๋วยเตี๋ยวเรือ", "price": 40, "id": 372, "remain": 30},
        {"name": "หอยลายเลือด", "price": 50, "id": 535, "remain": 30},
        {"name": "ลูกชิ้นพร้อมซอส", "price": 55, "id": 358, "remain": 30},
        {"name": "นิกิริปลาแซลมอน", "price": 90, "id": 607, "remain": 30},
        {"name": "หอยนางรมผัดฉ่า", "price": 60, "id": 754, "remain": 30},
        {"name": "ลิงกวินีกับหอย", "price": 85, "id": 894, "remain": 30},
        {"name": "สปาเก็ตตี้กุ้ง", "price": 75, "id": 924, "remain": 30},
        {"name": "ปลาแซลมอน", "price": 40, "id": 570, "remain": 30},
        {"name": "ผัดถั่วงอกกุ้ง", "price": 70, "id": 181, "remain": 30},
        {"name": "ปลากะพงทอดน้ำปลา", "price": 75, "id": 259, "remain": 30},
        {"name": "แกงเขียวหวานเต้าหู้หมู", "price": 75, "id": 406, "remain": 30},
        {"name": "ผ้าโพกศีรษะมีเขา", "price": 110, "id": 862, "remain": 30},
        {"name": "ปลาหมึก", "price": 80, "id": 243, "remain": 30},
        {"name": "ก๋วยเตี๋ยวเส้นใหญ่น้ำตกทะเล", "price": 80, "id": 696, "remain": 30},
        {"name": "แกงเขียวหวานหมูสับ", "price": 70, "id": 120, "remain": 30},
        {"name": "ยำมะม่วง", "price": 70, "id": 604, "remain": 30},
        {"name": "โอเรียนท์ หอย", "price": 60, "id": 680, "remain": 30},
        {"name": "ปลาทูน่า", "price": 70, "id": 949, "remain": 30},
        {"name": "แกงมัสมั่นเนื้อ", "price": 70, "id": 718, "remain": 30},
        {"name": "พิซซ่า", "price": 75, "id": 356, "remain": 30},
        {"name": "หมูผัดน้ำพริกเผา", "price": 60, "id": 657, "remain": 30},
        {"name": "ปลาเป้า", "price": 75, "id": 838, "remain": 30},
        {"name": "หอยรางน้ำ", "price": 60, "id": 766, "remain": 30},
        {"name": "ปลานึ่งมะนาว", "price": 75, "id": 415, "remain": 30},
        {"name": "ลาบหมู", "price": 60, "id": 961, "remain": 30},
        {"name": "ปาตองโก", "price": 30, "id": 781, "remain": 30},
        {"name": "ข้าวผัดปู", "price": 80, "id": 683, "remain": 30},
        {"name": "ผัดพริกแกงหมูกรอบ", "price": 55, "id": 689, "remain": 30},
        {"name": "ไก่นุ่มทอดกรอบ", "price": 50, "id": 270, "remain": 30},
        {"name": "ก๋วยเตี๋ยวเส้นเล็กต้มยำ", "price": 50, "id": 571, "remain": 30},
        {"name": "ผัดซีอิ๊ว", "price": 55, "id": 765, "remain": 30},
        {"name": "ปลาสำลีขาว", "price": 110, "id": 106, "remain": 30},
        {"name": "สปาเก็ตตี้ครีมซอสมะเขือเทศ", "price": 70, "id": 555, "remain": 30},
        {"name": "หอยนางรมนึ่งมะนาว", "price": 60, "id": 134, "remain": 30},
        {"name": "ซูฟลากี", "price": 65, "id": 593, "remain": 30},
        {"name": "น้ำพริกปลาทู", "price": 25, "id": 911, "remain": 30},
        {"name": "ผัดกระเพราหมูกรอบ", "price": 65, "id": 250, "remain": 30},
        {"name": "หอยมิรุไก", "price": 70, "id": 821, "remain": 30},
        {"name": "ข้าวหมูแดง", "price": 50, "id": 571, "remain": 30},
        {"name": "ไข่ปลาแซลมอน", "price": 45, "id": 682, "remain": 30},
        {"name": "ข้าวราดหน้าเนื้อ", "price": 65, "id": 625, "remain": 30},
        {"name": "ข้าวมันไก่หมู", "price": 55, "id": 894, "remain": 30},
        {"name": "หมูย่าง", "price": 80, "id": 633, "remain": 30},
        {"name": "ก๋วยเตี๋ยวเส้นใหญ่น้ำตก", "price": 40, "id": 847, "remain": 30},
        {"name": "ส้มตำไก่ย่าง", "price": 65, "id": 526, "remain": 30},
        {"name": "ซาลาเปาหมูสามชั้น", "price": 55, "id": 864, "remain": 30},
        {"name": "ริซอตโต้พร้อมอาหารทะเล", "price": 85, "id": 123, "remain": 30},
        {"name": "ปลาทูต้มราดข้าว", "price": 80, "id": 562, "remain": 30},
        {"name": "ปีกไก่", "price": 85, "id": 559, "remain": 30},
        {"name": "กุ้งแช่น้ำปลา", "price": 75, "id": 773, "remain": 30},
        {"name": "พาสต้าคาโบนาร่า", "price": 75, "id": 847, "remain": 30},
        {"name": "ไข่เจียวชิ้นหนาสไตล์ญี่ปุ่น", "price": 65, "id": 342, "remain": 30},
        {"name": "สปาเก็ตตี้บะหมี่", "price": 60, "id": 909, "remain": 30},
        {"name": "นมเปรี้ยว", "price": 40, "id": 737, "remain": 30},
        {"name": "แกงเขียวหวานไก่", "price": 70, "id": 333, "remain": 30},
        {"name": "ข้าวราดหน้าหมู", "price": 70, "id": 829, "remain": 30},
        {"name": "บรูเช็ตต์กับมะเขือเทศ", "price": 75, "id": 719, "remain": 30},
        {"name": "ขนมจีนนำยา", "price": 50, "id": 429, "remain": 30},
        {"name": "ทีรามิซู", "price": 110, "id": 569, "remain": 30},
        {"name": "หอยนางรมทอด", "price": 60, "id": 388, "remain": 30},
        {"name": "ผัดผักบุ้งไฟแดง", "price": 45, "id": 912, "remain": 30},
        {"name": "แกงเผ็ดหมู", "price": 65, "id": 227, "remain": 30},
        {"name": "ไก่ย่าง", "price": 35, "id": 208, "remain": 30},
        {"name": "ผัดกระเพราไก่ใส่ไข่ดาว", "price": 55, "id": 981, "remain": 30},
        {"name": "ปลาทูน่า Skipjack", "price": 70, "id": 154, "remain": 30},
        {"name": "สปาเก็ตตี้พริกสด", "price": 70, "id": 127, "remain": 30},
        {"name": "ข้าวผัดกะเพราหมู", "price": 50, "id": 608, "remain": 30},
        {"name": "ตำถั่วพลู", "price": 40, "id": 707, "remain": 30},
        {"name": "ซี่โครงบาร์บีคิว", "price": 70, "id": 127, "remain": 30},
        {"name": "ไข่เจียวมะระ", "price": 45, "id": 347, "remain": 30},
        {"name": "ข้าวต้ม", "price": 30, "id": 343, "remain": 30},
        {"name": "ก๋วยเตี๋ยวเส้นใหญ่น้ำตกไก่", "price": 60, "id": 424, "remain": 30},
        {"name": "ทรายแดงทะเล", "price": 80, "id": 609, "remain": 30},
        {"name": "ปลาทูสเปนญี่ปุ่น", "price": 50, "id": 701, "remain": 30},
        {"name": "ปัปปาร์เดลอัลลาโบโลเนส", "price": 55, "id": 680, "remain": 30},
        {"name": "ปลากะพงญี่ปุ่น", "price": 55, "id": 749, "remain": 30},
        {"name": "ต้มยำกุ้ง", "price": 80, "id": 255, "remain": 30},
        {"name": "หอยเชลล์", "price": 65, "id": 288, "remain": 30},
        {"name": "ฟิชแอนด์ชิป", "price": 55, "id": 564, "remain": 30},
        {"name": "ยำไข่ดาว", "price": 45, "id": 324, "remain": 30},
        {"name": "ข้าวมันไก่", "price": 45, "id": 961, "remain": 30},
        {"name": "ปลาเผา", "price": 70, "id": 399, "remain": 30},
        {"name": "ปลาฮาลิบัตไอ้สารเลว", "price": 70, "id": 638, "remain": 30},
        {"name": "ก๋วยเตี๋ยวต้มยำกุง", "price": 70, "id": 213, "remain": 30},
        {"name": "ปลาไวทิงญี่ปุ่น", "price": 45, "id": 443, "remain": 30},
        {"name": "ส้มตำ", "price": 40, "id": 448, "remain": 30},
        {"name": "ข้าวเหนียวหมูย่าง", "price": 40, "id": 701, "remain": 30},
        {"name": "ผัดถั่วงอกหมูกรอบ", "price": 55, "id": 229, "remain": 30},
        {"name": "ยำกุ้งสด", "price": 70, "id": 163, "remain": 30},
        {"name": "กุ้งโบตัน", "price": 75, "id": 728, "remain": 30},
        {"name": "ปลาแมคเคอเรล", "price": 55, "id": 306, "remain": 30},
        {"name": "ปลาสำลีใหญ่", "price": 40, "id": 451, "remain": 30},
        {"name": "ไข่เจียวน้ำเต้าหู้", "price": 55, "id": 426, "remain": 30},
        {"name": "ริคอตต้ายัดไส้ราวิโอลี่", "price": 90, "id": 388, "remain": 30},
        {"name": "ครึ่งบีก", "price": 65, "id": 484, "remain": 30},
        {"name": "เอบิเทนมากิ", "price": 80, "id": 967, "remain": 30},
        {"name": "แกงมัสมั่นหมู", "price": 65, "id": 272, "remain": 30},
        {"name": "ไก่ป่า", "price": 75, "id": 188, "remain": 30},
        {"name": "ยำสาหร่าย", "price": 60, "id": 893, "remain": 30},
        {"name": "ผัดซี่โครงหมูใบชะพลู", "price": 55, "id": 165, "remain": 30},
        {"name": "ยำกุนเชียง", "price": 40, "id": 728, "remain": 30},
        {"name": "ซีซาร์สลัด", "price": 80, "id": 978, "remain": 30},
        {"name": "แกงเขียวหวานปลาหมึก", "price": 70, "id": 215, "remain": 30},
        {"name": "แกงกะหรี่", "price": 45, "id": 900, "remain": 30},
        {"name": "หอยนางรม", "price": 55, "id": 703, "remain": 30},
        {"name": "สเต็กปลาหมึก", "price": 75, "id": 943, "remain": 30},
        {"name": "มากิแคลิฟอร์เนีย", "price": 70, "id": 457, "remain": 30},
        {"name": "ข้าวหน้าเนื้อตุ๋น", "price": 65, "id": 262, "remain": 30},
        {"name": "ข้าวไก่ทอด", "price": 55, "id": 458, "remain": 30},
        {"name": "ผัดเห็ดรวมหมู", "price": 60, "id": 997, "remain": 30},
        {"name": "เฟรนช์ฟรายกับไส้กรอก", "price": 105, "id": 290, "remain": 30},
        {"name": "ผัดกระเพรากุ้ง", "price": 70, "id": 384, "remain": 30},
    ]

    @classmethod
    def getMenu(cls, length: int = 171) -> List[Dict[str, str | int]]:
        shuffle(cls.__listMenu__)
        return cls.__listMenu__[:length]  # สามารถกำหนดจำนวนของข้อมูลที่จะส่งได้


# สมมุติโครงสร้างข้อมูลผูใช้งานโปรแกรมนี้ในร้านอาหาร
# ข้อมูลผู้ใช้งานในโปรแกรมนี้จะถูกเก็บไว้ใน list userData
# ข้างใน list เก็บ dictionary ของข้อมูลผู้ใช้งานแต่ละคน
# โดย properties ที่จะใช้งานหลักๆในโปรแกรมจะมี 4 อันประกอบด้วย
# name : ชื่อผู้ใชงาน
# email : บัญชีอีเมลที่ใช้งาน
# password : รหัสผ่านผู้ใช้งาน
# position : ตำแหน่งงานที่ทำงานอยู่ในร้านอาหาร


class Users:
    __usersData__ = [
        {
            "name": "john",
            "email": "john@gmail.com",
            "password": "111",
            "position": "ผู้จัดการ",
        },
        {
            "name": "david",
            "email": "david@gmail.com",
            "password": "222",
            "position": "ผู้ดูแลระบบ",
        },
        {
            "name": "jane",
            "email": "jane@gmail.com",
            "password": "333",
            "position": "แคชเชียร์",
        },
        {
            "name": "jack",
            "email": "jack@gmail.com",
            "password": "444",
            "position": "แคชเชียร์",
        },
        {
            "name": "elizabeth",
            "email": "elizabeth@gmail.com",
            "password": "555",
            "position": "พนักงานบาร์",
        },
        {
            "name": "robert",
            "email": "robert@gmail.com",
            "password": "666",
            "position": "ซอมเมลิเยร์",
        },
        {
            "name": "jill",
            "email": "jill@gmail.com",
            "password": "777",
            "position": "ผู้จัดการครัว",
        },
        {
            "name": "jame",
            "email": "james@gmail.com",
            "password": "888",
            "position": "กุ๊ก",
        },
        {
            "name": "william",
            "email": "william@gmail.com",
            "password": "999",
            "position": "ผู้ช่วยกุ๊ก",
        },
        {
            "name": "linda",
            "email": "linda@gmail.com",
            "password": "000",
            "position": "บริกร",
        },
        {
            "name": "jennifer",
            "email": "jennifer@gmail.com",
            "password": "001",
            "position": "พนักงานต้อนรับ",
        },{
            "name": "mary",
            "email": "mary@gmail.com",
            "password": "102",
            "002": "พนักงานต้อนรับ",
        },
    ]

    # ? method ในการให้ข้อมูลผู้ใช้งาน
    @classmethod
    def getUser(cls) -> List[Dict[str, str]]:
        return cls.__usersData__

    # ? method ในการข้อมูลผู้ใช้งาน
    @classmethod
    def addUser(cls, newUser: Dict[str, str]) -> None:
        cls.__usersData__.append(newUser)