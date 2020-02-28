dictions = {}
dictions["for"] = "循环、遍历"
dictions["if…in…"] = "判断、是否"
dictions["while"] ="当是什么时"
dictions[".insert"]= " 插入"
dictions["del"] = "删除"
for diction in dictions:
    print(diction+ " : " +dictions[diction])
for key , value in dictions.items():
    print(key+ " : \t"+value)
