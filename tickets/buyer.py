from datetime import datetime
X = True
while(X == True):
    file_path = 'tickets.txt'  
    with open(file_path, 'r') as file:
        content = file.read()

    print(int(content))
    print(datetime.now())
    if int(content) > 0:
        newcontent = int(content) - 1
    elif int(content) <= 0:
        print('Sold Out')
        X = False

    with open(file_path, 'w') as file:
        file.write(str(newcontent))

    sales_filename = 'sales.db'
    with open(sales_filename, 'a') as file:
        file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + '\n')

    print("Archivo modificado exitosamente.")