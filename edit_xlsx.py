import pandas as pd
from pandas import DataFrame
import random
data = pd.read_excel('C:\\Users\\Administrator\\Desktop\\整理后.xlsx',keep_default_na=False)
# pd.read_excel('test_excel.xlsx',sheet_name = 'AAA')#指定sheet名读取
# print(data.columns)
# print(data.values)#data.values不包含表头(第一行)
# print(data.values[0][0])
# DataFrame(data).to_excel('1.xlsx', sheet_name='Sheet1', index=False, header=True)#保存
# random_id = pd.read_excel('C:\\Users\\Administrator\\Desktop\\id.xlsx').values[0][1]
# print(random_id)
def random_hex(length):
    result = hex(random.randint(0,16**length)).replace('0x','').upper()
    if(len(result)<length):
        result = '0'*(length-len(result))+result
    return result
def random_id():
    return random_hex(8)+'-'+random_hex(4)+'-'+'4'+random_hex(3)+'-'+hex(random.randint(8,11)).replace('0x','').upper()+random_hex(3)+'-'+random_hex(8)+random_hex(4)
num_fjz=0
num_zr=0
num_zzaqy=0
num_fzr=0
num_jsy=0
num_qt=0
for lines in data.values:
    if(lines[1] != ''):
        lines[1] = int(lines[1])
    if('副局长' in lines[2]):
        num_fjz+=1
        print("insert into sec_user_role (id,delete_ts_nn,role_id,user_id) select '"+random_id()+"','1000-01-01 00:00:00.00000','113A20D5-70F0-9FE2-0158-D6E7A467700C',u.id from sec_user u where u.code='"+str(lines[1])+"';")
    elif('主任' in lines[2]):
        num_zr+=1
        print("insert into sec_user_role (id,delete_ts_nn,role_id,user_id) select '"+random_id()+"','1000-01-01 00:00:00.00000','33E3CED1-C3D4-0F6A-468D-7CC40990A8D6',u.id from sec_user u where u.code='"+str(lines[1])+"';")
    elif('专责' in lines[2] or '安全员' in lines[2]):
        num_zzaqy+=1
        print("insert into sec_user_role (id,delete_ts_nn,role_id,user_id) select '"+random_id()+"','1000-01-01 00:00:00.00000','074471CF-EBDD-0DD8-FF5A-1BE11BF179F8',u.id from sec_user u where u.code='"+str(lines[1])+"';")
        print("insert into sec_user_role (id,delete_ts_nn,role_id,user_id) select '"+random_id()+"','1000-01-01 00:00:00.00000','E19F2ED8-116C-EBFA-3CE4-087C311EB180',u.id from sec_user u where u.code='"+str(lines[1])+"';")
        print("insert into sec_user_role (id,delete_ts_nn,role_id,user_id) select '"+random_id()+"','1000-01-01 00:00:00.00000','46C66E6B-193A-B324-E963-AF9361AB6CF9',u.id from sec_user u where u.code='"+str(lines[1])+"';")
        print("insert into sec_user_role (id,delete_ts_nn,role_id,user_id) select '"+random_id()+"','1000-01-01 00:00:00.00000','599354AF-DBBB-1427-C9F7-ED3E5FB93DAC',u.id from sec_user u where u.code='"+str(lines[1])+"';")
    elif('负责人' in lines[2]):
        num_fzr+=1
        print("insert into sec_user_role (id,delete_ts_nn,role_id,user_id) select '"+random_id()+"','1000-01-01 00:00:00.00000','ACD1BB4F-EF5A-86EE-F7ED-29DFD7760F99',u.id from sec_user u where u.code='"+str(lines[1])+"';")
        print("insert into sec_user_role (id,delete_ts_nn,role_id,user_id) select '"+random_id()+"','1000-01-01 00:00:00.00000','24CBE26A-8CCB-5726-531C-A502696D6262',u.id from sec_user u where u.code='"+str(lines[1])+"';")
    elif('技术员' in lines[2]):
        num_jsy+=1
        print("insert into sec_user_role (id,delete_ts_nn,role_id,user_id) select '"+random_id()+"','1000-01-01 00:00:00.00000','074471CF-EBDD-0DD8-FF5A-1BE11BF179F8',u.id from sec_user u where u.code='"+str(lines[1])+"';")
        print("insert into sec_user_role (id,delete_ts_nn,role_id,user_id) select '"+random_id()+"','1000-01-01 00:00:00.00000','6988E4E8-A25E-42AB-F038-3BA2E9D98C4D',u.id from sec_user u where u.code='"+str(lines[1])+"';")
    else:
        num_qt+=1
        print(lines)

print("共生成sql脚本"+str(num_fjz*1+num_zr*1+num_zzaqy*4+num_fzr*2+num_jsy*2+num_qt*0)+"条")