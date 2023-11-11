<div align="center">
  <img src="./img/KU.png" width="300px" height="300px">
  <h1><b>มหาวิทยาลัยเกษตรศาสตร์วิทยาเขตศรีราชา</b></h1>
  <br>
</div>

> ส่งงาน project วิชา Fundamental Programming Concepts ปี 1 ภาคต้น 
<hr>

<div>
  <br>
  <h2>รายชื่อสมาชิกในกลุ่ม</h2>
  <p>นาย วรินทร์ สายปัญญา รหัสนิสิต 6630250435</p>
  <br>
</div>

<h1 align="center">โปรแกรมร้านอาหารขายอาหาร</h1>
<p align="center">โปรแกรมขายอาหารจัดการอาหารหรือสินค้าภายในโปรแกรมใช้งานโปรแกรมผ่าน command line โดยให้พิมพ์คำสั่งตามที่กำหนดไว้ในโปรแกรม</p>

[![wakatime](https://wakatime.com/badge/user/68e3e2dc-451c-45ef-bca8-9fc3ad60e2f9/project/018bbe78-641e-44df-a80b-173faa3d7148.svg)](https://wakatime.com/badge/user/68e3e2dc-451c-45ef-bca8-9fc3ad60e2f9/project/018bbe78-641e-44df-a80b-173faa3d7148)

<h2>ฟีเจอร์ของโปรแกรม</h2>
<ul>
  <li>เพิ่มสินค้า</li>
  <li>ลบสินค้า</li>
  <li>แก้ไขสินค้า</li>
  <li>สั่งซื้ออาหาร</li>
  <li>แสดงตารางเมนูอาหาร บิลใบเสร็จ และ รายละเอียดการสั่งซื้อ</li>
  <li>ระบบ login , logout , สมัครสมาชิก</li>
  <li>ระบบบันทึกการทำงานต่างๆของโปรแกรม</li>
  <li>ระบบเขียนข้อมูล อาหาร , ผู้ใช้งาน และ log file ลงในไฟล์ python</li>
  <li>กำหนดสิทธิ์การเข้าถึงคำสั่ง</li>
</ul>

## การติดตั้งและการนำโปรเจคไปใช้งาน

<div>
  <p>เครื่องมือที่ต้องมีก่อนนำไปใช้งาน</p>
  <ul>
    <li><a href="https://code.visualstudio.com/download">Visual Studio Code</a></li>   
    <li><a href="https://www.python.org/downloads/">python</a></li>    
    <li><a href="https://git-scm.com/downloads">git</a></li>
  </ul>
  <br>
</div>

<p>เปิด terminal แล้วพิมพ์คำสั่งตามขั้นตอนต่อไปนี้</p>

### 1. ดาวโหลด์ code ของโปรเจค
ถ้าไม่ได้ติดตั้ง git สามารถดาวโหลด์เป็น zip แล้วไปแตกไฟล์ได้
```
git clone https://github.com/VarinCode/Python-project.git
```

### 2. เข้าถึง directory
```
cd Python-project
```

### 3. สร้าง virtual environment
```
py -m venv .venv
```

### 4. เปิดใช้งานสภาพแวดล้อมจำลองที่สร้างขึ้น
```
.venv\Scripts\activate
```

### 5. ติดตั้ง libraries ที่อยู่ในโปรเจค
```
pip install -r requirements.txt
```

### 6. รันโปรแกรม
```
python main.py
```

### 6. ปิดใช้งาน
```
deactivate
```
