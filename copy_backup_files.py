# coding: utf-8 

import os
import datetime
import shutil
import re
import time
import os.path

src_path1 = "/var/lib/vz/dump/"
src_path2 = "/mnt/pve/p2-data-nfs/dump/"
src_path3 = "/rpool/w/dump/"

dst_path1 = "/mnt/external2/W/"

backup_file = "(\.320|644+)"

pattern = "(320+)_\w*-\w*-\w*.(\.tgz)|" + backup_file + "-(\d*_\d*_\d*-\d*_\d*_\d*)+(\.tar.gz|lzo)"


# Удаляем все данные в подключенным HDD 
dst_path_backup = [element for element in os.listdir(dst_path1)]
for element in dst_path_backup:
    os.remove(os.path.join(dst_path1, element))

# Перенос данных с src_path3
files_list=os.listdir(src_path3)
i = 0
for lin in files_list:
     files_list[i] = src_path3 + lin
     i+=1
i = 0 
for i in files_list:
    if re.search(pattern, i):
        shutil.move(i, dst_path1)


# Перенос данных с src_path2
files_list=os.listdir(src_path2)
i = 0
for lin in files_list:
     files_list[i] = src_path2 + lin
     i+=1
i = 0 
for i in files_list:
    if re.search(pattern, i):
        shutil.move(i, dst_path1)

# Перенос данных с src_path1
today = datetime.datetime.today()
#print("Сегодняшняя дата: ", today.strftime("%d/%m/%Y") )
files_list=os.listdir(src_path1)
i = 0
for lin in files_list:
     files_list[i] = src_path1 + lin
     i+=1

# i = 0 
# for i in files_list:
#     if re.search(pattern, i):
#         createds = os.path.getctime(i)
#         year,month,day,hour,minute,second=time.localtime(createds)[:-3]
#         print(" Файл:\n", i,"\n","Создан:\n %02d/%02d/%d"%(day,month,year))
#         if "%02d/%02d/%d"%(day,month,year) == today.strftime("%d/%m/%Y"):
#             print("Даты соответствуют")
#             #shutil.move(i, dst_path1)
#         elif "%02d/%02d/%d"%(day,month,year) != today.strftime("%d/%m/%Y"):
#             print("Даты не соответствуют")