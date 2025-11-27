#!/usr/bin/env python
# coding: utf-8

# In[2]:


# các biến thể hiện diện tích các phòng (m2)
hall=11.25
kit=18.0
liv=20.0
bed=10.75
bath=9.50

# khởi tạo danh sách areas
areas=[hall,kit,liv,bed,bath]

# in ra areas
print (areas)


# In[3]:


# các biến thể hiện diện tích các phòng (m2)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# sửa lại dòng khởi tạo danh sách areas
areas = [hall, kit, "living room", liv, bed, "bathroom", bath]

# in ra areas
print(areas)


# In[4]:


# các biến thể hiện diện tích các phòng (m2)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# thông tin về ngôi nhà, biểu diễn bởi danh sách của các danh sách
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv]]

# in ra giá trị của house
print(house)

# in ra kiểu dữ liệu của house
print(type(house))


# In[6]:


# Khởi tạo danh sách areas
areas=["hallway",11.25,"kitchen",18.0,"living room",20.0,"bedroom",10.75,"bathroom",9.50]
# in ra phần tử thứ hai của areas
print(areas[1])
#in ra phần tử cuối cùng của areas
print(areas[-1])
#in ra diện tích của phòng khách (living room)
print(areas[5])


# In[9]:


#Khởi tạo
areas = ["hallway",11.25,"kitchen",18.0,"living room", 20.0, "bedroom", 10.75,"bathroom",9.50]
# tổng diện tích của kitchen và bedroom:eat_sleep_ảea
eat_sleep_area=areas[3]+areas[-3]
#in ra giá trị của eat_sleep_area
print(eat_sleep_area)


# In[10]:


# khởi tạo
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# trích xuất các phần tử của areas để khởi tạo downstairs
downstairs = areas[0:6]

# trích xuất các phần tử của areas để khởi tạo upstairs
upstairs = areas[6:-1]

# in ra downstairs và upstairs
print(downstairs)
print(upstairs)


# In[11]:


# khởi tạo
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# trích xuất các phần tử của areas để khởi tạo downstairs (cách 2)
downstairs = areas[:6]

# trích xuất các phần tử của areas để khởi tạo upstairs (cách 2)
upstairs = areas[6:]

# in ra downstairs và upstairs
print(downstairs)
print(upstairs)


# In[12]:


x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]


# In[13]:


# khởi tạo
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# sửa lại diện tích của phòng tắm (bathroom)
areas[-1] = 10.50

# sửa "living room" thành "chill zone"
areas[4] = 'chill zone'

# in ra areas
print(areas)


# In[14]:


# khởi tạo
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# thêm dữ liệu của poolhouse vào areas, tạo danh sách mới tên areas_1
areas_1 = areas  + ["poolhouse", 24.5]

# thêm dữ liệu của garage vào areas_1, tạo danh sách mới tên areas_2
areas_2 = list(areas_1)
areas_2.extend(["garage", 15.45])

# in ra areas_1 và areas_2
print(areas_1)
print(areas_2)


# In[16]:


# khởi tạo 
areas = ["hallway",11.25,"kitchen",18.0,
        "chill zone",20.0,"bedroom",10.75,
        "bathroom",10.50,"poolhouse",24.5,
        "garage",15.45]
#Xóa "poolhouse"
del(areas[-4])

#Xóa diện tích của poolhouse
del(areas[-3])

#in ra areas
print(areas)


# In[17]:


# khởi tạo areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# tạo areas_copy
areas_copy = list(areas)

# thay đổi areas_copy
areas_copy[0] = 5.0

# in ra areas
print(areas)


# In[18]:


# khởi tạo
var1 = [1, 2, 3, 4]
var2 = True

# in ra kiểu của var1
print(type(var1))

# in ra số lượng phần tử của var1
print(len(var1))

# chuyển biến var2 sang số nguyên, kết quả lưu vào biến out2
out2 = int(var2)



# In[19]:


help(complex)


# In[20]:


help(sorted)


# In[21]:


# khởi tạo
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# ghép first và second vào danh sách full
full = first + second

# sắp xếp lại full theo thứ tự giảm dần, lưu vào biến full_sorted
full_sorted = sorted(full, reverse=True)

# in ra full_sorted
print(full_sorted)


# In[ ]:




