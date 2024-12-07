my_number = 21.5
#print("is int") if type(my_number) is int else print("is not int")

if type(my_number) is int:
    print("is int")
else: 
    print("is not int")

product_qty = 10 
print("in stock" if product_qty > 0 else "out of stock")

temp = +24
weather = "hot" if temp > 18 else "cold"
print(weather)

#send_img(img) if img.get['is_processed'] else process_and_send_img(img) 

my_img = ('1920', '1080')
#print(f"{my_img[0]}x{my_img[1]}") if len(my_img) == 2 else print("Incorrect image formatting")

#info = f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 else "Incorrect image formatting"
#print(info)

if len(my_img) == 2:
    info = f"{my_img[0]}x{my_img[1]}"
else:
    info = "Incorrect image formatting"
print(info)

my_str = "very, very, very, very, very, vere, very, very, very, vere, very, very, very, vere, very, very, very, very, very, very,very, verye, very, very,very, verye, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very long string"
res = "String is long" if len(my_str) > 79 else "String is short"
print(res)