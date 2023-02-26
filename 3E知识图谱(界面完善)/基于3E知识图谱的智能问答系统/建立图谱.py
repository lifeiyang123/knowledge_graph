import csv
from py2neo import Graph,Node,Relationship,NodeMatcher,NodeMatcher
import py2neo
#graph直接写账号密码会不安全
g=Graph('http://localhost:7474/browser/',auth=('neo4j','2020011720'),name='neo4j')
#资源与环境
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/1-土地面积.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("土地面积",土地类型=item[0],面积=item[1])
#         g.merge(test_node_1, "土地面积", "土地类型")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/2-河流面积.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("河流面积",河流名称=item[0],流域面积=item[1],河长=item[2],年径流量=item[3])
#         g.merge(test_node_1, "河流面积", "河流名称")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/3-流域面积.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("流域面积",流域名称=item[0],流域面积=item[1],占外流河和内陆河流域面积合计=item[2])
#         g.merge(test_node_1, "流域面积", "流域名称")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/4-矿产产量.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("矿产产量",矿产名称=item[0],年产量2020年=item[1],年产量2021年=item[2])
#         g.merge(test_node_1, "矿产产量", "矿产名称")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/5-城市温度.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("城市温度",城市名称=item[0],温度1月=item[1],温度2月=item[2],温度3月=item[3],温度4月=item[4],温度5月=item[5],温度6月=item[6],温度7月=item[7],温度8月=item[8],温度9月=item[9],温度10月=item[10],温度11月=item[11],温度12月=item[12],年平均温度=item[13])
#         g.merge(test_node_1, "城市温度", "城市名称")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/6-城市湿度.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("城市湿度",城市名称=item[0],湿度1月=item[1],湿度2月=item[2],湿度3月=item[3],湿度4月=item[4],湿度5月=item[5],湿度6月=item[6],湿度7月=item[7],湿度8月=item[8],湿度9月=item[9],湿度10月=item[10],湿度11月=item[11],湿度12月=item[12],年平均湿度=item[13])
#         g.merge(test_node_1, "城市湿度", "城市名称")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/7-城市降水量.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("城市降水量",城市名称=item[0],降水量1月=item[1],降水量2月=item[2],降水量3月=item[3],降水量4月=item[4],降水量5月=item[5],降水量6月=item[6],降水量7月=item[7],降水量8月=item[8],降水量9月=item[9],降水量10月=item[10],降水量11月=item[11],降水量12月=item[12],全年降水量=item[13])
#         g.merge(test_node_1, "城市降水量", "城市名称")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/8-城市日照时间数.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("城市日照时间数",城市名称=item[0],日照时数1月=item[1],日照时数2月=item[2],日照时数3月=item[3],日照时数4月=item[4],日照时数5月=item[5],日照时数6月=item[6],日照时数7月=item[7],日照时数8月=item[8],日照时数9月=item[9],日照时数10月=item[10],日照时数11月=item[11],日照时数12月=item[12],全年日照时数=item[13])
#         g.merge(test_node_1, "城市日照时间数", "城市名称")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/9-不同年份水资源总量.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同年份水资源总量",年份=item[0],水资源总量=item[1],地表水资源量=item[2],地下水资源量=item[3],地表水与地下水资源重复量=item[4],人均水资源量=item[5])
#         g.merge(test_node_1, "不同年份水资源总量", "年份")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/10-1-不同地区供水总量.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同地区供水总量",地区=item[0],供水总量=item[1],地表水供水量=item[2],地下水供水量=item[3],其他供水量=item[4],用水总量=item[5],农业用水量=item[6],工业用水量=item[7],生活用水量=item[8],人工生态环境补水用水量=item[9],人均用水量=item[10])
#         g.merge(test_node_1, "不同地区供水总量", "地区")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/11-不用地区废水污染物含量.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不用地区废水污染物含量11",地区=item[0],废水中化学需氧量排放量=item[1],废水中氨氮排放量=item[2],废水中总氮排放量=item[3],废水中总磷排放量=item[4],废水中石油类排放量=item[5],废水中挥发酚排放量=item[6],废水中总铅排放量=item[7],废水中总汞排放量=item[8],废水中总镉排放量=item[9],废水中六价铬排放量=item[10],废水中总铬排放量=item[11],废水中总砷排放量=item[12])
#         g.merge(test_node_1, "不用地区废水污染物含量11", "地区")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/14-不同城市废气污染物含量.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同城市废气污染物含量14",城市=item[0],工业二氧化硫排放量=item[1],工业氮氧化物排放量=item[2],工业颗粒物排放量=item[3],生活及其他二氧化硫排放量=item[4],生活及其他氮氧化物排放量=item[5],生活及其他颗粒物排放量=item[6])
#         g.merge(test_node_1, "不同城市废气污染物含量14", "城市")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/24-不同地区草原建设情况.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同地区草原建设情况24",地区=item[0],种草面积=item[1],草原改良面积=item[2],草原鼠害发生面积=item[3],草原鼠害防治面积=item[4],草原虫害发生面积=item[5],草原虫害防治面积=item[6],草原火灾受害面积=item[7])
#         g.merge(test_node_1, "不同地区草原建设情况24", "地区")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/25-不同地区自然保护情况.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同地区自然保护情况25",地区=item[0],国家级自然保护区个数=item[1],国家级自然保护区面积=item[2])
#         g.merge(test_node_1, "不同地区自然保护情况25", "地区")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/26-不同地区自然灾害情况.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同地区自然灾害情况26",地区=item[0],农作物受灾面积合计=item[1],农作物绝收面积合计=item[2],旱灾受灾面积=item[3],旱灾绝收面积=item[4],洪涝地质灾害和台风受灾面积=item[5],洪涝地质灾害和台风绝收面积=item[6],风雹灾害受灾面积=item[7],风雹灾害绝收面积=item[8],低温冷冻和雪灾受灾面积=item[9],低温冷冻和雪灾绝收面积=item[10],受灾人口=item[11],死亡人口=item[12],直接经济损失=item[13])
#         g.merge(test_node_1, "不同地区自然灾害情况26", "地区")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/27-1-不同地区地质灾害情况.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同地区地质灾害情况27_1",地区=item[0],发生地质灾害数量=item[1],滑坡次数=item[2],崩塌次数=item[3],泥石流次数=item[4],地面塌陷次数=item[5],人员伤亡数量=item[6],死亡人数=item[7],直接经济损失=item[8])
#         g.merge(test_node_1, "不同地区地质灾害情况27_1", "地区")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/27-不同年份地质灾害情况.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同年份地质灾害情况27",年份=item[0],发生地质灾害数量=item[1],滑坡次数=item[2],崩塌次数=item[3],泥石流次数=item[4],地面塌陷次数=item[5],人员伤亡数量=item[6],死亡人数=item[7],直接经济损失=item[8])
#         g.merge(test_node_1, "不同年份地质灾害情况27", "年份")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/28-不同地区森林火灾情况.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同地区森林火灾情况28",地区=item[0],森林火灾次数=item[1],一般火灾次数=item[2],较大火灾次数=item[3],重大火灾次数=item[4],特别重大火灾次数=item[5],火场总面积=item[6],受害森林面积=item[7],伤亡人数=item[8],其它损失折款=item[9])
#         g.merge(test_node_1, "不同地区森林火灾情况28", "地区")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/29-不同年份生物灾害情况.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同年份生物灾害情况29",年份=item[0],林业有害生物发生面积=item[1],林业有害生物防治面积=item[2],林业有害生物防治率=item[3],森林病害发生面积=item[4],森林病害防治面积=item[5],森林虫害发生面积=item[6],森林虫害防治面积=item[7],森林鼠害发生面积=item[8],森林鼠害防治面积=item[9],有害植物发生面积=item[10],有害植物防治面积=item[11])
#         g.merge(test_node_1, "不同年份生物灾害情况29", "年份")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/30-不同地区突发环境事件次数.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同地区突发环境事件次数30",地区=item[0],突发环境事件次数=item[1],特别重大环境事件次数=item[2],重大环境事件次数=item[3],较大环境事件次数=item[4],一般环境事件次数=item[5])
#         g.merge(test_node_1, "不同地区突发环境事件次数30", "地区")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/31-1-不同地区地震情况.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同地区地震情况31_1",地区=item[0],地震次数=item[1],地震次数5点0_5点9级=item[2],地震次数6点0_6点9级=item[3],地震次数7点0_7点9级=item[4],人员伤亡数量=item[5],死亡人数=item[6],直接经济损失=item[7])
#         g.merge(test_node_1, "不同地区地震情况31_1", "地区")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/31-不同年份地震情况.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同年份地震情况31",年份=item[0],地震次数=item[1],地震次数5点0_5点9级=item[2],地震次数6点0_6点9级=item[3],地震次数7点0_7点9级=item[4],人员伤亡数量=item[5],死亡人数=item[6],直接经济损失=item[7])
#         g.merge(test_node_1, "不同年份地震情况31", "年份")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/32-海洋灾害情况.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("海洋灾害情况32",灾种=item[0],发生次数=item[1],人员死亡失踪=item[2],直接经济损失=item[3])
#         g.merge(test_node_1, "海洋灾害情况32", "灾种")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/33-海域不同水质面积.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("海域不同水质面积33",海域=item[0],第二类水质海域面积=item[1],第三类水质海域面积=item[2],第四类水质海域面积=item[3],劣于第四类水质海域面积=item[4])
#         g.merge(test_node_1, "海域不同水质面积33", "海域")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/34-不同地区基础建设投资.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不同地区基础建设投资34",地区=item[0],城镇环境基础设施建设投资=item[1],燃气建设投资=item[2],集中供热建设投资=item[3],排水建设投资=item[4],园林绿化建设投资=item[5],市容环境卫生建设投资=item[6])
#         g.merge(test_node_1, "不同地区基础建设投资34", "地区")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/资源与环境/36-林业草原投资完成情况.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("林业草原投资完成情况36",地区=item[0],本年完成林业草原投资总计=item[1],林业草原国家投资=item[2],林业草原生态修复治理投资=item[3],林业草原林产品加工制造投资=item[4],林业草原林业草原服务保障和公共管理投资=item[5])
#         g.merge(test_node_1, "林业草原投资完成情况36", "地区")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/2-国民经济核算/C03-01国民生产总值.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("国民生产总值2_1",年份=item[0],国民总收入=item[1],国内生产总值=item[2],第一产业=item[3],第二产业=item[4],第三产业=item[5],农林牧渔业=item[6],工业=item[7],建筑业=item[8],批发和零售业=item[9],交通运输仓储和邮政业=item[10],住宿和餐饮业=item[11],金融业=item[12],房地产业=item[13],其他=item[14],人均国民总收入=item[15],人均国内生产总值=item[16])
#         g.merge(test_node_1, "国民生产总值2_1", "年份")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/2-国民经济核算/C03-03不变价国内生产总值.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("不变价国内生产总值2_3",年份=item[0],国内生产总值=item[1],第一产业=item[2],第二产业=item[3],第三产业=item[4],农林牧渔业=item[5],工业=item[6],建筑业=item[7],批发和零售业=item[8],交通运输仓储和邮政业=item[9],住宿和餐饮业=item[10],金融业=item[11],房地产业=item[12],其他=item[13])
#         g.merge(test_node_1, "不变价国内生产总值2_3", "年份")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/2-国民经济核算/C03-06分行业增加值.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("分行业增加值2_6",年份=item[0],国内生产总值=item[1],农林牧渔业=item[2],采矿业=item[3],制造业=item[4],电力热力燃气及水=item[5],建筑业=item[6],批发和零售业=item[7],交通运输仓储和邮政业=item[8],住宿和餐饮业=item[9],信息传输软件和信息=item[10],金融业=item[11],房地产业=item[12],租赁和商务服务业=item[13],科学研究和技术服务业=item[14],水利环境和公共设施管理业=item[15],居民服务修理和其他服务业=item[16],教育=item[17],卫生和社会工作=item[18],文化体育和娱乐业=item[19],公共管理社会保障=item[20])
#         g.merge(test_node_1, "分行业增加值2_6", "年份")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/2-国民经济核算/C03-16资金流量表 (金融交易，2020年).csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("资金流量表_金融交易_2020年_2_16",交易项目=item[0],净金融投资=item[1],资金运用合计=item[2],资金来源合计=item[3],通货=item[4],存款=item[5],活期存款=item[6],定期存款=item[7],财政存款=item[8],外汇存款=item[9],其他存款=item[10],证券公司客户保证金=item[11],贷款=item[12],短期贷款与票据融资=item[13]
#                          ,中长期贷款=item[14],外汇贷款=item[15],委托贷款=item[16],其他贷款=item[17],未贴现的银行承兑汇票=item[18],保险准备金=item[19],金融机构往来=item[20],存款准备金=item[21],债券=item[22],政府债券=item[23],金融债券=item[24],中央银行债券=item[25],企业债券=item[26],股票=item[27]
#                          ,证券投资基金份额=item[28],库存现金=item[29],中央银行贷款=item[30],其他=item[31],直接投资=item[32],其他对外债权债务=item[33],国际储备资产=item[34],国际收支错误与遗漏=item[35])
#         g.merge(test_node_1, "资金流量表_金融交易_2020年_2_16", "交易项目")

# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/3-能源/C09-16万元国内生产总值能源消费量.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("国内生产总值能源消费量3_16",年份=item[0],国内生产总值能源消费量=item[1],国内生产总值煤炭消费量=item[2],国内生产总值焦炭消费量=item[3],国内生产总值石油消费量=item[4],国内生产总值原油消费量=item[5],国内生产总值燃料油消费量=item[6],国内生产总值电力消费量=item[7])
#         g.merge(test_node_1, "国内生产总值能源消费量3_16", "年份")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/4-联系/1-能源.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("能源_4_1",id=item[0],name=item[1],定义=item[2])
#         g.merge(test_node_1, "能源_4_1", "id")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/4-联系/2-能源分类.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("能源分类_4_2",id=item[0],name=item[1],定义=item[2])
#         g.merge(test_node_1, "能源分类_4_2", "id")
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/4-联系/3-环境/9','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("环境具体分类_4_3_4",id=item[0],name=item[1],定义=item[2])
#         g.merge(test_node_1, "环境具体分类_4_3_4", "id")



matcher = NodeMatcher(g)
with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/4-联系/1-能源/8-能源分类-不同年份数据.csv', 'r', encoding='utf-8') as f:
    #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
    reader=csv.reader(f)
    for item in reader:
        #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
        if reader.line_num==1:
            continue
        # print("当前行数：", reader.line_num, "当前内容", item)
        findnode = matcher.match('能源分类_4_2', id=item[0]).first()
        endnode = matcher.match('原油不同年份相关数据_4_18', id=item[1]).first()
        # print(findnode,endnode)
        relationships = Relationship(findnode, '原油不同年份相关数据', endnode)
        g.merge(relationships, "", "id")

# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/4-联系/1-能源/9-发电方式.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("发电方式_4_9",id=item[0],name=item[1],定义=item[2])
#         g.merge(test_node_1, "发电方式_4_9", "id")

# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/4-联系/19-能源不同年份相关数据.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("能源不同年份相关数据_4_19",id=item[0],年份=item[1],可供消费的能源总量=item[2],一次能源生产总量=item[3],能源进口量=item[4],能源出口量=item[5],能源消费总量=item[6],农林牧渔业能源消费总量=item[7],工业能源消费总量=item[8],建筑业能源消费总量=item[9],交通运输仓储和邮政业能源消费总量=item[10],批发和零售业住宿和餐饮业能源消费总量=item[11],其他能源消费总量=item[12],居民生活能源消费总量=item[13])
#         g.merge(test_node_1, "能源不同年份相关数据_4_19", "id")

# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/4-联系/15-燃料油不同年份相关数据.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("燃料油不同年份相关数据_4_15",id=item[0],年份=item[1],燃料油可供量=item[2],燃料油生产量=item[3],燃料油进口量=item[4],燃料油出口量=item[5],燃料油消费量=item[6],农林牧渔业燃料油消费量=item[7],工业燃料油消费量=item[8],建筑业燃料油消费量=item[9],交通运输仓储和邮政业燃料油消费量=item[10],批发和零售业住宿和餐饮业燃料油消费量=item[11],其他燃料油消费量=item[12])
#         g.merge(test_node_1, "燃料油不同年份相关数据_4_15", "id")





# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/个人—爱好知识图谱问答/data/爱好类型.csv','r',encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：",reader.line_num,"当前内容",item)
#         test_node_1=Node("爱好类型",id=item[0],name=item[1])
#         g.merge(test_node_1, "爱好类型", "id")
matcher = NodeMatcher(g)
# with open('D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/个人—爱好知识图谱问答/data/关系.csv', 'r', encoding='utf-8') as f:
#     #数据集除了第一行代表属性外，第一列为实体1，第二列为实体2，第三列是两者英文关系，第四列为两者中文关系
#     reader=csv.reader(f)
#     for item in reader:
#         #第一行的标签不是咱们需要的内容，line_num表示文件的第几行
#         if reader.line_num==1:
#             continue
#         # print("当前行数：", reader.line_num, "当前内容", item)
#         findnode = matcher.match('个人信息', id=item[0]).first()
#         endnode = matcher.match('爱好类型', id=item[1]).first()
#         # print(findnode,endnode)
#         relationships = Relationship(findnode, '爱好是', endnode)
#         g.merge(relationships, "", "id")