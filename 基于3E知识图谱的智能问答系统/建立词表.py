import csv
#资源与环境
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/1-土地面积.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/1-土地面积.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/2-河流面积.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/2-河流面积.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/3-流域面积.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/3-流域面积.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/4-矿产产量.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/4-矿产产量.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/5-城市温度.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/5-城市温度.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/6-城市湿度.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/6-城市湿度.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/7-城市降水量.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/7-城市降水量.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/8-城市日照时间数.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/8-城市日照时间数.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/9-1-不同地区水资源总量.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/9-1-不同地区水资源总量.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/9-不同年份水资源总量.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/9-不同年份水资源总量.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/10-1-不同地区供水总量.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/10-1-不同地区供水总量.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/10-不同年份供水总量.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/10-不同年份供水总量.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/11-不用地区废水污染物含量.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/11-不用地区废水污染物含量.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/12-不同城市废水污染物含量.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/12-不同城市废水污染物含量.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/13-不同地区废气污染物含量.csv' ,'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     l_genre=[]
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         #print("当前行数：",reader.line_num,"当前内容",item)
#         #只要类别
#         print("当前行数：", reader.line_num, "当前内容", item[0])
#         if item[0] not in l_genre:
#             l_genre.append(item[0])
# f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/13-不同地区废气污染物含量.txt', 'w+',encoding='utf-8')
# f_genre.write('\n'.join(list(l_genre)))
# f_genre.close()
with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/3-能源/C09-16万元国内生产总值能源消费量.csv' ,'r', encoding='utf-8') as f:
    #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
    l_genre=[]
    reader=csv.reader(f)
    for item in reader:
        #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
        if reader.line_num==1:
            continue
        #print("当前行数：",reader.line_num,"当前内容",item)
        #只要类别
        print("当前行数：", reader.line_num, "当前内容", item[0])
        if item[0] not in l_genre:
            l_genre.append(item[0])
f_genre = open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/3-能源/C09-16万元国内生产总值能源消费量.txt', 'w+',encoding='utf-8')
f_genre.write('\n'.join(list(l_genre)))
f_genre.close()