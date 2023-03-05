import os # operating system

# 讀取檔案
products = []
if os.path.isfile("menu.csv"):# 檢查檔案在不在
    print("有找到檔案")
    with open("menu.csv", "r", encoding="utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue # 繼續
            name, price = line.strip().split(",")       
            products.append([name, price])
    print(products)      
else:
    print("找不到檔案")


# 讓使用者輸入商品資訊
while True:
    name = input("請輸入商品名稱:")
    if name == "q":
        break
    price = int(input("請輸入商品價格:"))
    products.append([name, price])

# 寫入檔案
with open("menu.csv", "w", encoding="utf-8") as f:
    f.write("商品,價格\n")
    for p in products:
        f.write(f"{p[0]},{p[1]}\n")
    
    
    