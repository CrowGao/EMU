from asyncore import write
import re
import time
readfilepath = "emu.txt"
writefilepath = "stats.txt"

readf = open(readfilepath,"r")
lines = readf.readlines()
readf.close()



data = ""
cycle = 0
num = 0 
for line in lines:
    # print(line)
    result = []
    result = line.split(",")
    if len(result)!=3:
        continue
    # 调正cycle
    CYCLE = result[0].replace(" ","")
    nowcycle = (int(CYCLE)+20)//100*100
    result[0] = str(nowcycle)
    if cycle == 0:
        data =line
        cycle = nowcycle
        continue
    if cycle == nowcycle:
        line = result[0] + "," + result[1] + "," + result[2]
        data = data + line
        # num = num + 1
    elif cycle != nowcycle: #   and num != 0:
        # print(data)
        writef = open(writefilepath,"a")
        writef.write(data)
        writef.close()
        cycle = nowcycle
        line = result[0] + "," + result[1] + "," + result[2]
        data = line
        # time.sleep(1)
    # elif cycle != nowcycle and num == 0:
    #     data = ""
    #     line = result[0] + "," + result[1] + "," + result[2]
    #     data = data + line
    #     cycle = nowcycle
    #     num = num + 1


    
