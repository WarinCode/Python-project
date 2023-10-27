<div align="center">
  <img src="https://thaimooc.org/sites/default/files/2022-09/ku_11.png" width="300px" height="300px">
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

<h1 align="center">โปรแกรมร้านอาหารขายอาหาร จัดการสินค้าในร้านอาหาร</h1>

<h2>ฟีเจอร์ของโปรแกรม</h2>
<ul>
  <li>เพิ่มสินค้า</li>
  <li>ลบสินค้า</li>
  <li>แก้ไขสินค้า</li>
  <li>คำนวณการสั่งซื้ออาหาร</li>
  <li>แสดงบิลใบเสร็จรายละเอียดการสั่งซื้ออาหาร</li>
  <li>ระบบ login , logout , สมัครสมาชิก</li>
  <li>ดูบันทึกของโปรแกรม</li>
</ul>

## การติดตั้งและการนำโปรเจคไปใช้งาน

<div>
  <p>เครื่องมือที่ต้องมีก่อนนำไปใช้งาน</p>
  <ul>
    <li><a href="https://code.visualstudio.com/download">Visual Studio Code</a></li>
    <li><a href="https://git-scm.com/downloads">git</a></li>
    <li><a href="https://www.python.org/downloads/">python</a></li>
  </ul>
  <br>
</div>

<p>เปิด terminal แล้วพิมพ์คำสั่งตามขั้นตอนต่อไปนี้</p>

### 1. ดาวโหลด์ code ของโปรเจค
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

### 4. เปิดใช้งาน
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
