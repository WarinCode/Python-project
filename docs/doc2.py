# คู่มือการใช้งาน rich library : https://rich.readthedocs.io/
# การติดตั้ง : pip install rich

from rich.console import Console
console = Console()

console.rule('เส้นบรรทัด') # สร้างเส้นบรรทัด
# การแสดงข้อความใน terminal จะเรียกใช้ object console แล้วใช้งาน method print เป็นหลัก
console.print('Hello World!')

# การใส่สี และพื้นหลัง ในข้อความโดยทำได้หลายแบบดังนี้
#* ชื่อสีที่ใช้งานได้ -> https://rich.readthedocs.io/en/latest/appendix/colors.html#appendix-colors
# แบบที่ 1: การส่งค่า argument(ชื่อสี) ไปให้ parameter style
console.print('red' , style='red')
console.print('yellow' , style='yellow')
console.print('purple' , style='purple')
console.print('green' , style='green')
console.print('blue' , style='blue')
console.rule()
# แบบที่ 2: การแทรกค่า [ชื่อสี] ใน string 
console.print('[red]red')
console.print('[yellow]yellow')
console.print('[purple]purple')
console.print('[green]green')
console.print('[blue]blue')
console.rule()
# เราสามารถให้สีของข้อความอยู่ในระยะได้โดย การใส่ tag เปิด และ tag ปิด เหมือน html
# ตัวอย่าง: [ชื่อสี ชนิดฟ้อน พื้นหลัง] content [/]
console.print('[sky_blue3]sky_blue [/sky_blue3] [magenta]magenta[/]')
console.print('[bold cyan1]cyan1[/] , ข้อความที่ไม่มีสี')
console.print('[dark_red italic on white] dark_red [/]') # การใช้ on หมายถึง ให้มีสีพื้นหลังของข้อความเป็นสีอะไร เช่น: ชนิดฟ้อน สี บน พื้นหลัง
console.rule()

# การใส่ชนิดของฟ้อน (บางคำสั่งไม่สามารถใช้งานได้หรือรันใน terminal แล้วจะเป็น ข้อความธรรมดา)
console.print("blink", style="blink")
console.print("blink2", style="blink2")
console.print("bold", style="bold") # ฟ้อนตัวหนา
console.print("conceal", style="conceal") # ไม่สามารถเห็นข้อความได้
console.print("italic", style="italic") # หรือ style="i" ฟ้อนตัวเอียง
console.print("reverse", style="reverse") # หรือ style="r" สลับสีกับพื้นหลังสีจะตรงข้ามกัน
console.print("strike", style="strike") # หรือ style="s" ขีดฆ่าข้อความ
console.print("underline", style="underline") # หรือ style="u"  เส้นใต้ข้อความ



