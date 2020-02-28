'''使用count（）方法   圈定特定的单词或短语在字符串中出现的次数，'''
s = "dsfa,"
if ',' in s:
    s = s.replace(',','')
print(s)
'''split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都储存到一个列表。
    判断两端消息有多少个字母相同
'''
def count(filemessage,word):
    i = 0
    lists = filemessage.spilt()
    for list in lists:
        if  ',' in list:
            list = list.replace(',','')
        if '.' in list:
            list = list.replace('.', '')
        if  '!' in list:
            list = list.replace('!','')
        if  '~' in list:
            list = list.replace('~','')
        if  '?' in list:
            list = list.replace('?','')

        if list.lower() == word:
            i = i+1
    return i


