# import json
#
# file_name = 'test.txt'
# # nums = [3, 4, 5, 7, 1, 9]
# nums = {"name": "Mike", "age": 12}
# with open(file_name, 'w') as file_obj:
#     '''写入json文件'''
#     json.dump(nums, file_obj)
#     print("写入json文件：", nums)
#
# dic={"商家名称": "井格老灶火锅(望京新世界店)", "评分": 26.2, "地址": "火锅望京广顺南大街路16号", "人均消费": 105, "评论数量": 1387}
# with open(filename+'.json','a') as outfile:
#     json.dump(dic,outfile,ensure_ascii=False)
#     outfile.write('\n')
# import json
# data = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
# js = json.dumps(data)
# with open('test.txt','w') as f:
#     f.write(js)
#     f.close()
# with open('test.txt') as f:
#     data=f.read()
#     f.close()
# x=json.loads(data)
# print(x)
import json
a={"啊哈哈":111}
with open('test.txt','w') as f:
    f.write(json.dumps(a))
with open('test.txt') as f:
    x=json.loads(f.read())
print(x)
