def step(message, i , j, way,source,target):
                if(way == "way1"):
                    message[i][j] =  message[i-1][j] + f'Xoa ky tu {source[i]} \n'
                elif(way == "way2"):
                    message[i][j] = message[i][j-1] + f'Chen ky tu {target[j]} \n'
                else:
                    if way == "way3.0":
                        message[i][j] = message[i-1][j-1] + f'Thay ky tu {source[i]} bang {target[j]} \n'
                    else:
                        message[i][j] = message[i-1][j-1] + f'Giu  nguyen ky tu {source[i]} \n'
                
source = input("Nhap chuoi bat dau : ")
target = input("Nhap chuoi ket thuc : ")
source = "#" + source
target = "#" + target
D = [[0 for _ in range(len(target))] for _ in range(len(source))]
message = [['' for _ in range(len(target))]for _ in range(len(source))]
for i in range(len(source)):
    if i == 0:
        for j in range(len(target)):
            D[0][j] = j
            if j != 0:
                message[0][j] = f"Chen ky tu {target[j]} \n"
    else:
        D[i][0] = i
        message[i][0] = f'Xoa kt tu {source[i]} \n'
        for j in range(1, len(target)):
            way1 = D[i-1][j] + 1
            way2 = D[i][j-1] + 1
            way3 = D[i-1][j-1] + (1 if source[i] != target[j] else 0)
            D[i][j] = min(way1, way2, way3)
            way = ''
            if(D[i][j] == way1): way = "way1"
            elif(D[i][j] == way2):  way = "way2"
            else:
                    if(D[i][j] == D[i-1][j-1] + 1): way = "way3.0"
            step(message,i,j,way, source,target)
                
print(D)
print(f'Khoang cach can chinh sua tu {source} thanh {target} la : {D[len(source)-1][len(target)-1]}')
print("Cac buoc thuc hien : ")
print(message[len(source)-1][len(target)-1])
    



