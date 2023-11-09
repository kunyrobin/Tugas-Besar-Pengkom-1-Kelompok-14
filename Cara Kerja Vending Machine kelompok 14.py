items = [
    {'code': 171, 'name': 'Nu Green Tea', 'price': 8000},
    {'code': 173, 'name': 'Cimory Yogurt', 'price': 7000},
    {'code': 284, 'name': 'Ultra Milk', 'price': 8000},
    {'code': 367, 'name': 'Pocari Sweat', 'price': 8000},
    {'code': 444, 'name': 'Nescafe', 'price': 7000},
    {'code': 541, 'name': 'Floridina', 'price': 3000},
    {'code': 733, 'name': 'Teh Kotak', 'price': 5000},
    {'code': 844, 'name': 'Le Minerale', 'price': 4000},
    {'code': 854, 'name': 'Sprite', 'price': 6000}
]

is_quit = False
item = ''

while is_quit == False:
    print("Selamat datang di vending machine!")
    for i in items:
        print(f"Nama Item: {i['name']} - Harga: {i['price']} - Kode: {i['code']}")
    price = int(input("Masukkan uang yang ingin Anda belanjakan: "))
    query = int(input("Masukkan kode item yang ingin Anda beli: "))
    for i in items:
        if query == i['code']:
            item = i
    if item == '':
        print('KODE TIDAK VALID')
    else:
        if price < item['price']:
            print(f"Uang Anda tidak cukup untuk membeli {item['name']}. Silakan masukkan uang lebih banyak.")
        elif price > item['price']:
            print(f"{item['name']} akan memakan biaya {item['price']} rupiah.")
            change = price - item['price']
            print(f"Ini {item['name']} Anda.")
        else:
            print(f"Terima kasih telah membeli, ini {item['name']} Anda.")
    query = input("Untuk keluar dari mesin, masukkan q dan untuk melanjutkan pembelian masukkan apa saja: ")
    if query == 'q':
        is_quit = True
    else:
        is_quit = False
    print('')
