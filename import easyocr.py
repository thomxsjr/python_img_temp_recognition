import easyocr
import re
import pandas as pd
import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    popup.geometry("300x200")
    label = ttk.Label(popup, text="Average Temperature:", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Got It", command = popup.destroy)
    B1.pack()
    popup.mainloop()


reader = easyocr.Reader(['en'])

image_path = "./image.jpg"

results = reader.readtext(image_path)

extracted_text = []
extracted_numeric_values = []

for result in results:
    text = result[1]
    
    numeric_values = re.findall(r'-?\d+(\.\d*)?', text)
    
    extracted_text.append(text)
    
    extracted_numeric_values.extend(numeric_values)



for i in range (len(extracted_text)):
  if extracted_text[i].isdigit():
    extracted_text[i] = int(extracted_text[i])


data = extracted_text

if 40160 in data :
    data.remove(40160)
print(data)
temp=0;
print(len(data))
for i in range(0,len(data)):
    strtdata = str(data[i])
    # print(strtdata)
    if strtdata =='TEMP':
        print("Temperature :", data[i+1])
        temp+=float(data[i+1])
print("Average Temperature : " ,temp)   
popupmsg(temp)

# key_words = ['HR', 'T1']
# result_dict = {}
# flag = False
# for i,temp in enumerate(data):
#     if(temp in key_words):
#         for num in data[i:]:
#             if str(num).isnumeric():
#                 result_dict[T1] = [num]
#                 break
# print(result_dict)  

key_words = ['RESP', 'T1']
result_dict = {kw: [] for kw in key_words}
current_key = None
for num in extracted_numeric_values:
    if current_key is not None:
        result_dict[current_key].append(num)
    elif num in key_words:
        current_key = num

print(result_dict)
# df = pd.DataFrame(result_dict)
# df.to_csv('Data2.csv',index=False)
# df = pd.read_csv('./Data2.csv')
# df = df.append(result_dict,ignore_index=True)

# print(df)
# df.to_csv("Data2.csv")