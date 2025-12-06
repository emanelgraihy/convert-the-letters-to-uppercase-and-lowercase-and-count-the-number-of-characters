# ايمان ابراهيم الجرايحي محمد 

from tkinter import *

# إنشاء النافذة
myframe = Tk()
myframe.title("Text Tools")
myframe.geometry("500x450")

# عنوان الواجهة
title = Label( myframe, text="Simple Text Tools", fg="gray",font=("Tahoma", 18, "bold"))
title.pack(pady=20)

# Label للتعليمات
label1 = Label( myframe, text="اكتب النص هنا:", font=("Arial", 12))
label1.pack()

# Entry لإدخال النص
mytext = Entry( myframe, width=35, font=("Arial", 12))
mytext.pack(pady=10)

# صندوق Text لعرض النتائج
output = Text( myframe, width=45, height=5, font=("Arial", 12))
output.pack(pady=15)

# دالة مساعدة لمسح صندوق النتائج
def clear_output():
    output.delete("1.0", END)

# وظيفة 1: تحويل النص لكابيتال
def to_capital():
    text = mytext.get()
    clear_output()
    output.insert(END, text.upper())

# وظيفة 2: تحويل النص لسمول
def to_small():
    text = mytext.get()
    clear_output()
    output.insert(END, text.lower())

# وظيفة 3: حساب عدد الحروف
def count_chars():
    text = mytext.get()
    clear_output()
    output.insert(END, f"عدد الحروف هو: {len(text)}")

# الأزرار
btn1 = Button( myframe, text="تحويل لـ CAPITAL", bg="pink", fg="white",
              font=("Helvetica", 11, "bold"), command=to_capital)
btn1.pack(pady=5)

btn2 = Button( myframe, text="تحويل لـ small", bg="gray", fg="white",
              font=("Helvetica", 11, "bold"), command=to_small)
btn2.pack(pady=5)

btn3 = Button( myframe, text="عدد الحروف", bg="purple", fg="white",
              font=("Helvetica", 11, "bold"), command=count_chars)
btn3.pack(pady=5)

# تشغيل البرنامج
myframe.mainloop()
