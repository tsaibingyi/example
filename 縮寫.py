sentence = input("請輸入一句句子：")
output = ""

for word in sentence.split(): #.spilt可以把句子拆分成多個字
    output = output + word[0].upper() #word[0]代表word的第一個字母 #.upper代表大寫

print(output)

