__author__ = "Teeraphat Kullanankanjana"
__version__ = "Prototype2.1.2"

from tkinter import *
from tkinter import ttk
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from PIL import ImageTk, Image


class CreateGUI(Tk):
    def __init__(self):
        super(CreateGUI, self).__init__()
        self.province = StringVar()
        self.title("Temperature Data V2.1.2")
        self.minsize(500, 400)
        self.wm_iconbitmap("Temp Logo.ico")
        self.resizable(width=FALSE, height=FALSE)
        self.create_menu_bar()
        self.autocompleteList = (
            "เชียงราย", "เชียงใหม่", "แม่ฮ่องสอน", "ตาก", "น่าน", "อุตรดิตถ์", "พิษณุโลก", "กำแพงเพชร", "พิจิตร",
            "สุโขทัย",
            "พะเยา", "ลำพูน", "ลำปาง", "แพร่", "เพชรบูรณ์", "หนองคาย", "เลย", "ขอนแก่น", "อุบลราชธานี", "นครราชสีมา",
            "ร้อยเอ็ด", "มุกดาหาร", "อุดรธานี",
            "หนองบัวลำภู", "นครพนม", "สกลนคร", "มหาสารคาม", "กาฬสินธุ์", "ชัยภูมิ", "ศรีสะเกษ", "ยโสธร", "สุรินทร์",
            "บุรีย์รัมย์", "อำนาจเจริญ", "กาญจนบุรี", "นครสวรรค์", "กรุงเทพมหานคร", "สุพรรณบุรี", "ชัยนาท", "ลพบุรี",
            "พระนครศรีอยุธยา",
            "ราชบุรี", "ปทุมธานี", "สระบุรี", "สิงห์บุรี", "สมุทรสงคราม", "อ่างทอง", "อุทัยธานี", "นนทบุรี", "นครปฐม",
            "สมุทรปราการ",
            "สมุทรสาคร", "สระแก้ว", "ชลบุรี", "ระยอง", "ปราจีนบุรี", "ตราด", "จันทรบุรี", "ฉะเชิงเทรา", "นครนายก",
            "ชลบุรี(พัทยา)",
            "ประจวบคีรีขันธ์",
            "ชุมพร", "นครศรีธรรมราช", "นราธิวาส", "สุราษฎร์ธานี", "ยะลา", "ปัตตานี", "สงขลา", "เพชรบุรี",
            "ประจวบคีรีขันธ์(หัวหิน)",
            "สุราษฎร์ธานี(เกาะสมุย)",
            "พัทลุง", "ระนอง",
            "ภูเก็ต", "กระบี่", "ตรัง", "พังงา", "สตูล", "สงขลา(หาดใหญ่)", "บึงกาฬ")
        # tab create
        tab_control = ttk.Notebook(self)
        # tab 1 definition
        self.tab1 = ttk.Frame(tab_control)
        tab_control.add(self.tab1)
        # tab 2 definition
        self.tab2 = ttk.Frame(tab_control)
        tab_control.add(self.tab2)
        # display all tab
        tab_control.pack(expan=1, fill="both")
        # for switching tab
        self.tab_control = tab_control
        # add object to all tab
        self.add_object2tab1()
        self.add_object2tab2()

    def add_object2tab1(self):
        # TAB1
        head_frame1 = LabelFrame(self.tab1)  # Title
        head_frame1.grid(column=0, row=0)
        head_label1 = Label(head_frame1, text="ยินดีต้อนรับเข้าสู่โปรแกรมข้อมูลอุตุนิยมวิทยา")
        head_label1.config(font=("Bangna New", 22, "bold"), bg="black", fg="#4ee44e")
        head_label1.grid(column=0, row=0)
        # -----
        canvas_frame1 = Canvas(self.tab1, height=200, width=200)  # Picture
        canvas_frame1.grid(column=0, row=1)
        image1 = Image.open("logo_TMD.png")
        canvas_frame1.image = ImageTk.PhotoImage(image1)
        canvas_frame1.create_image(0, 0, image=canvas_frame1.image, anchor="nw")
        # ------
        bu_frame1 = LabelFrame(self.tab1, height=100, width=200)  # Button
        bu_frame1.grid(column=0, row=2, rowspan=1)
        bu_click1 = Button(bu_frame1, text="Get Start", command=self.switch_tab)
        bu_click1.config(font=("Bangna New", 10, "bold"), bg="black", fg="#4ee44e")
        bu_click1.grid(column=0, row=1)

    def add_object2tab2(self):
        part_frame1 = Label(self.tab2, text="กรุณาป้อนชื่อจังหวัดของคุณ")
        part_frame1.config(font=("THSarabunNew", 16))
        part_frame1.grid(column=0, row=0, sticky=W)

        combo = ttk.Combobox(self.tab2, width=20, textvariable=self.province)
        combo["values"] = self.autocompleteList
        combo.config(font=("THSarabunNew", 10))
        combo.grid(column=2, row=0, sticky=W)

        button = Button(self.tab2, text="ยืนยัน", command=self.confirm)
        button.config(font=("THSarabunNew", 15))
        button.grid(column=5, row=0, sticky=W)

        part_frame3 = Label(self.tab2, text="ผลลัพธ์")
        part_frame3.config(font=("THSarabunNew", 16))
        part_frame3.grid(column=0, row=1, sticky=W)

        part_frame4 = Label(self.tab2, text="จังหวัด:")
        part_frame4.config(font=("THSarabunNew", 16))
        part_frame4.grid(column=0, row=2, sticky=W)

        part_frame5 = Label(self.tab2, text="อุณหภูมิ: ")
        part_frame5.config(font=("THSarabunNew", 16))
        part_frame5.grid(column=0, row=3, sticky=W)

    def close_gui(self):
        self.quit()
        self.destroy()
        exit()

    def create_menu_bar(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Exit", command=self.close_gui)

        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Help")
        help_menu.add_command(label="About")

    def switch_tab(self):
        self.tab_control.select(self.tab2)

    def confirm(self):
        province_tag = self.province.get()
        index = self.autocompleteList.index(province_tag)
        index += 1
        url = "https://www.tmd.go.th/province.php?id=" + str(index)
        web_open = req(url)
        page_html = web_open.read()
        web_open.close()
        data = soup(page_html, "html.parser")
        temp = data.findAll("td", {"class": "strokeme"})
        province = data.findAll("span", {"class": "title"})
        pv = province[0].text.replace(" ", " ")
        result = temp[0].text

        part_frame4 = Label(self.tab2)
        part_frame4.config(text="จังหวัด:" + str(pv), font=("THSarabunNew", 16))
        part_frame4.grid(column=0, row=2, sticky=W)

        part_frame5 = Label(self.tab2)
        part_frame5.config(text="อุณหภูมิ: " + str(result), font=("THSarabunNew", 16))
        part_frame5.grid(column=0, row=3, sticky=W)


if __name__ == "__main__":
    window = CreateGUI()
    window.mainloop()
