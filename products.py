import os # operating system

def read_file(filename):
    products = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue # 繼續
            name, price = line.strip().split(",")       
            products.append([name, price])
    return products   

# 讓使用者輸入商品資訊
def user_input(products):
    while True:
        name = input("請輸入商品名稱:")
        if name == "q":
            break
        price = int(input("請輸入商品價格:"))
        products.append([name, price])
    return products
        
#印出商品資訊
def print_products(products):
    for p in products:
        print(f"{p[0]}的價格是{p[1]}")

# 寫入檔案
def write_file(filename, products):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("商品,價格\n")
        for p in products:
            f.write(f"{p[0]},{p[1]}\n")

def main():
    filename = "menu.csv"
    if os.path.isfile(filename):# 檢查檔案在不在
        print("有找到檔案")
        products = read_file(filename)
    else:
        print("找不到檔案")  

    products = user_input(products) 
    print_products(products)
    write_file(filename, products)

main()
 
    

    
    
