docs = input("Hujjat topshirganmisiz? (ha/yo'q): ")
interview = input("Suhbatdan o'tdingizmi? (ha/yo'q): ")
test = input("Testdan o'tdingizmi? (ha/yo'q): ")

if docs == "ha" and interview == "ha" and test == "ha":
    print("Siz ishga qabul qilindingiz!")
elif docs == "yo'q":
    print("Avvalo hujjatlaringizni topshiring.")
elif docs == "ha" and interview == "yo'q":
    print("Suhbatdan o'tmagansiz.")
elif docs == "ha" and interview == "ha" and test == "yo'q":
    print("Test natijalari yetarli emas.")
else:
    print("Jarayon davom etmoqda.")
