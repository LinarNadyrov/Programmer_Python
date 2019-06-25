# coding: utf-8 
# 

import os
import datetime
import shutil
import re
import time
import os.path

src_path1 = "/Users/7bit/Documents/GeekBrains/src_path1/"
dst_path1 = "/mnt/external2/W/"

backup_file = "(\.320|640+)"

pattern = "(320+)_\w*-\w*-\w*.(\.tgz)|" + backup_file + "-(\d*_\d*_\d*-\d*_\d*_\d*)+(\.tar.gz|lzo)"



# Перенос данных с src_path1
today = datetime.datetime.today()
#print("Сегодняшняя дата: ", today.strftime("%d/%m/%Y") )

files_list=os.listdir(src_path1)
i = 0
for lin in files_list:
     files_list[i] = src_path1 + lin
     i+=1


last_name = ' '
last_update = 0

i = 0 
for i in files_list:
     if re.search(pattern, i):
          #print(i)
          #last_name = i
          if last_update < os.path.getctime(i):
               #last_name = i
               last_update = os.path.getctime(i)
               print(last_update)
               #print(last_name)
               #shutil.move(last_name, dst_path1)


#     if re.search(pattern, i):
#          print("Файлы до функции last_update: ", i)
     #     if last_update < os.path.getctime(i):
     #          print(i)
               #last_update = os.path.getctime(i)
               #print(last_update)
     #    createds = os.path.getctime(i)
     #    year,month,day,hour,minute,second=time.localtime(createds)[:-3]
     #    print(" Файл:\n", i,"\n","Создан:\n %02d/%02d/%d"%(day,month,year))
     #    if "%02d/%02d/%d"%(day,month,year) == today.strftime("%d/%m/%Y"):
     #        print("Даты соответствуют")
     #        #shutil.move(i, dst_path1)
     #    elif "%02d/%02d/%d"%(day,month,year) != today.strftime("%d/%m/%Y"):
     #        print("Даты не соответствуют")