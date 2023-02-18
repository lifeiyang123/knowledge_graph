from question_classifier import *
from question_parser import *
from answer_search import *
import Global
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup

'''问答类'''
class ChatBotGraph:
    def clear(self):
        os.system('cls')
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent,lfy_answers):
        # answer = '没能理解您的问题，我数据量有限。。。能不能问的标准点'
        answer=''
        res_classify = self.classifier.classify(sent)
        # print(res_classify)
        if res_classify=={}:
            # if Global.num==0:
            #     print(answer)
            # Global.num=Global.num+1
            return
        if res_classify['question_types']=={} and Global.lfy_answers ==[]:
            # if Global.num==0:
            #     print(answer)
            # Global.num = Global.num + 1
            return
        # print('类别：',res_classify)
        res_sql = self.parser.parser_main(res_classify)

        # print('sql语句',res_sql)

        final_answers = self.searcher.search_main(res_sql,lfy_answers)
        # print(final_answers)
        if final_answers=='':
            print(answer)


            #return '\n'.join(final_answers)
class SearchPage:
    def __init__(self,master):
        self.root = master
        # root.attributes('-alpha', 0.3)
        photo = tk.PhotoImage(file=r"./背景图片/subbanner.gif"),
        label = tk.Label(self.root, image=photo, width=500, height=400)
        label.place(x=0)

        # label.pack()
        self.root.geometry('500x400')
        self.root.title('基于3E知识图谱的智能问答系统')
        shuru = tk.StringVar()

        def huoqu():
            neirong = shuru.get()
            lfy = neirong
            content = text.get(1.0, "end")
            if content != '':
                text.delete(1.0, "end")
            lfy_answers = []

            t = 0
            s = 0
            Global.lfy_answers = []
            Global.num = 0
            lfy_answers = []
            # print('')
            question = lfy

            # print('')
            a = cut(question)
            a.reverse()
            for i in pingying:
                    if i in question:
                        question = question.replace(i, hanzi[t])
                        break
                    t = t + 1
            for j in a:
                    for k in shuxing_list:
                        if j in k and j not in shuzi_list and len(j)>=2:
                            b = question
                            b = b.replace(j, k)
                            s = 1
                            handler.chat_main(b, lfy_answers)
                    if s == 1:
                        break
            if Global.lfy_answers != []:
                    for k in Global.lfy_answers:
                        text.insert(INSERT, k+'\n')
            else:
                    # text.insert(INSERT,'抱歉，我的数据库中没有相关内容！\n我将在百度百科中搜索该词条\n')
                    question=lfy
                    url = 'https://baike.baidu.com/item/' + question
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
                    }
                    # req = requests.get(url=url, headers=headers)
                    req = requests.get(url=url) #可以不用headers
                    # req.encoding = 'gbk'
                    html = req.text
                    bes = BeautifulSoup(html, "html.parser")
                    # print(bes)
                    # print(bes.get_text())
                    try:
                        texts = bes.find("div", class_="lemma-summary").get_text()
                    except AttributeError:
                        # print(f'抱歉，百度百科尚未收录词条 “{question}”')
                        text.insert(INSERT, f'抱歉，百度百科尚未收录词条 “{question}”')
                    else:
                        lfy1 = texts.replace(' ', '').replace('\n', '')
                        # text.insert(INSERT, '\n搜索内容如下：\n\n'+lfy1+'\n\n详情请查看网址'+url)
                        text.insert(INSERT,lfy1 + '\n\n详情请查看网址' + url)

















        def fanhui():
            self.root.destroy()
            self.root1 = tk.Tk()
            LoginPage(master=self.root1)

        lfy = ''
        c = tk.Button(self.root, text='查询', command=huoqu, width=4, height=1, bg='skyblue', fg='red')
        c.place(x=90, y=10)
        # c.pack()
        a = tk.Entry(self.root, textvariable=shuru, width=40, fg='red')  # .grid(row=1,column=2)
        a.place(x=130, y=10)

        b = tk.Label(self.root, text='结果', width=4, bg='skyblue')
        b.place(x=90, y=50)

        text = Text(self.root, width=40, height=5)
        text.place(x=130, y=50)

        g = tk.Button(self.root, text='返回登录页',command=fanhui, width=8, height=1, bg='skyblue', fg='red')
        g.place(x=430,y=150)

        self.root.mainloop()
class LoginPage:
    def __init__(self,master):
        self.root = master
        self.root.geometry('300x200')
        self.root.title('登录页')
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.page=tk.Frame(self.root)
        self.page.pack()
        tk.Label(self.page).grid(row=1,column=1)
        tk.Label(self.page,text='账号：').grid(row=2,column=1)
        tk.Entry(self.page,textvariable=self.username).grid(row=2,column=2)

        tk.Label(self.page,text='密码：').grid(row=3,column=1,pady=10)
        tk.Entry(self.page,textvariable=self.password).grid(row=3,column=2)


        tk.Button(self.page,text='登录',command=self.login).grid(row=4,column=1,pady=10)
        tk.Button(self.page,text='退出',command=self.page.quit).grid(row=4,column=3)
        self.root.mainloop()

    def login(self):
        name = self.username.get()
        pwd = self.password.get()
        if name == '李飞扬' and pwd == '123456':
            self.page.destroy()
            SearchPage(self.root)
        elif name == '李辉' and pwd == '123456':
            self.page.destroy()
            SearchPage(self.root)
        elif name == '陈楚昕' and pwd == '123456':
            self.page.destroy()
            SearchPage(self.root)
        elif name == '肖婧雯' and pwd == '123456':
            self.page.destroy()
            SearchPage(self.root)
        else:
            messagebox.showwarning(title='警告', message='登录失败，请检查账号密码是否正确')

if __name__ == '__main__':
    handler = ChatBotGraph()
    t=0
    # 执行结果：
    # 以“1234”为例，结果为– > [‘1’, ‘2’, ‘3’, ‘4’, ‘12’, ‘23’, ‘34’, ‘123’, ‘234’, ‘1234’]
    # 分析
    # 子字符串中并没有“24”，“124”，说明分的效果并不是这么好
    def cut(s: str):
        results = []
        num = 0
        # x + 1 表示子字符串长度
        for x in range(len(s)):
            # i 表示偏移量
            for i in range(len(s) - x):
                results.append(s[i:i + x + 1])
        return results


    # 执行结果：
    # 还是输入字符串“1234”，所有子字符串为：
    # ['1', '2', '3', '4', '12', '13', '14', '23', '24', '34', '123', '124', '234', '1234']
    def cut2(s: str):
        results = []
        num = 0

        # x + 1 表示子字符串长度
        for x in range(len(s)):
            # i 表示偏移量
            for i in range(len(s) - x):
                if x == 0:
                    results.append(s[i:i + x + 1])
                elif x < 2:
                    for j in range(len(s) - x - i):
                        results.append(s[i] + s[j + x + i])
                else:
                    for j in range(len(s) - x - i):
                        results.append(s[i:i + x] + s[j + x + i])
        # 判断子字符串中能被n整除的个数
        # for y in results:
        #     if int(y) % int(n) == 0:
        #         num = num + 1

        return results
    hanzi=['全国','北京','北京','天津','天津','河北','河北','山西','山西','内蒙古','内蒙古','辽宁','辽宁','吉林','吉林','黑龙江','黑龙江','上海','上海','江苏','江苏','浙江','浙江','安徽','安徽','福建','福建','江西','江西','山东','山东','河南','河南','湖北','湖北','湖南','湖南','广东','广东','广西','广西','海南','海南',
           '重庆','重庆','四川','四川','贵州','贵州','云南','云南','西藏','西藏','陕西','陕西','甘肃','甘肃','青海','青海','宁夏','宁夏','新疆','新疆','石家庄',
           '太原','呼和浩特','沈阳','长春','哈尔滨','南京','杭州','合肥','福州','南昌','济南','郑州','武汉','长沙','广州','南宁','海口','成都','贵阳','昆明','拉萨',
           '西安','兰州','西宁','银川','乌鲁木齐','大连','长春','青岛','桂林','贵阳']
    pingying=['quanguo','beijing','京','tianjin','津','hebei','冀','shanxi','晋','neimenggu','蒙','liaoning','辽','jilin','吉','heilongjiang','黑','shanghai','沪','jiangsu','苏','zhejiang','浙','anhui','皖','fujian','闽','jiangxi','赣','shandong','鲁','henan','豫','hubei','鄂','hunan','湘','guangdong','粤','guangxi','桂','hainan','琼',
           'chongqin','渝','sichuang','川','guizhou','贵','yunnan','云','xizang','藏','shaanxi','陕','gansu','甘','qinghai','青','ningxia','宁','xinjiang','新','shijiazhuang',
           'taiyuan','huhehaote','shenyang','changchun','haerbin','nanjing','hangzhou','hefei','fuzhou','nanchang','jinan','zhengzhou','wuhan','changsha','guangzhou','nanning','haikou','chengdu','guiyang','kunming','lasa',
           'xian','lanzhou','xining','yinchuan','wulumuqi','dalian','changchun','qingdao','guilin','guiyang']
    shuxing_list=['面积','流域面积','河长','年径流量','流域面积','面积占比','2020年产量','2021年产量','2021年的1月温度','2021年的2月温度','2021年的3月温度','2021年的4月温度','2021年的5月温度',
                  '2021年的6月温度','2021年的7月温度','2021年的8月温度','2021年的9月温度','2021年的10月温度','2021年的11月温度','2021年的12月温度','2021年的年平均温度','2021年的1月湿度','2021年的2月湿度','2021年的3月湿度','2021年的4月湿度','2021年的5月湿度',
                  '2021年的6月湿度','2021年的7月湿度','2021年的8月湿度','2021年的9月湿度','2021年的10月湿度','2021年的11月湿度','2021年的12月湿度','2021年的年平均湿度','2021年的1月降水量','2021年的2月降水量','2021年的3月降水量','2021年的4月降水量','2021年的5月降水量',
                  '2021年的6月降水量','2021年的7月降水量','2021年的8月降水量','2021年的9月降水量','2021年的10月降水量','2021年的11月降水量','2021年的12月降水量','2021年的全年降水量','2021年的1月日照时数','2021年的2月日照时数','2021年的3月日照时数','2021年的4月日照时数','2021年的5月日照时数',
                  '2021年的6月日照时数','2021年的7月日照时数','2021年的8月日照时数','2021年的9月日照时数','2021年的10月日照时数','2021年的11月日照时数','2021年的12月日照时数','2021年的全年日照时数','水资源总量','地表水资源量','地下水资源量','地表水与地下水资源重复量','人均水资源量','供水总量','地表水供水量',
                  '地下水供水量','其他供水量','用水总量','农业用水量','工业用水量','生活用水量','人工生态环境补水用水量','人均用水量','废水中化学需氧量排放量','废水中氨氮排放量','废水中总氮排放量','废水中总磷排放量','废水中石油类排放量','废水中挥发酚排放量','废水中总铅排放量','废水中总汞排放量','废水中总镉排放量','废水中六价铬排放量',
                  '废水中总铬排放量','废水中总砷排放量','城市废水中工业化学需氧量排放量','城市废水中工业氨氮排放量','城市废水中生活化学需氧量排放量','城市废水中生活氨氮排放量','二氧化硫排放量','氮氧化物排放量','颗粒物排放量','工业二氧化硫排放量','工业氮氧化物排放量','工业颗粒物排放量','生活及其他二氧化硫排放量','生活及其他氮氧化物排放量','生活及其他颗粒物排放量',
                  '一般工业固体废物产生量','一般工业固体废物综合利用量','一般工业固体废物处置量','一般工业固体废物贮存量','一般工业固体废物倾倒丢弃量','危险废物产生量','危险废物利用处置量','危险废物本年末贮存量','二氧化硫年平均浓度','二氧化氮年平均浓度','可吸入颗粒物年平均浓度','一氧化碳日均值第95百分位浓度','臭氧日最大8小时第90百分位浓度','细颗粒物年平均浓度','空气质量优良天数比例','生活垃圾清运量','垃圾无害化处理厂数','卫生填埋厂数','垃圾焚烧厂数',
                  '其他厂数','垃圾无害化处理能力','卫生填埋处理能力','垃圾焚烧处理能力','其他处理能力','垃圾无害化处理量','卫生填埋处理量','垃圾焚烧处理量','其他处理量','生活垃圾无害化处理率','道路交通噪声等效声级','区域环境噪声等效声级','2013年的耕地面积','2014年的耕地面积','2015年的耕地面积','2016年的耕地面积','2017年的耕地面积','2019年的耕地面积','耕地面积','园地面积','林地面积','草地面积','湿地面积','城镇村及工矿用地面积','交通运输用地面积','水域及水利设施用地面积',
                  '林业用地面积','森林面积','人工林面积','森林覆盖率','活立木总蓄积量','森林蓄积量','造林总面积','人工造林面积','飞播造林面积','封山育林面积','退化林修复面积','人工更新面积','种草面积','草原改良面积','草原鼠害发生面积','草原鼠害防治面积','草原虫害发生面积','草原虫害防治面积','草原火灾受害面积','国家级自然保护区个数','国家级自然保护区面积','农作物受灾面积','农作物绝收面积','旱灾受灾面积','旱灾绝收面积','洪涝地质灾害和台风受灾面积','洪涝地质灾害和台风绝收面积',
                  '风雹灾害受灾面积','风雹灾害绝收面积','低温冷冻和雪灾受灾面积','低温冷冻和雪灾绝收面积','受灾人口','死亡人口','自然灾害导致的直接经济损失','发生地质灾害数量','地质灾害导致的滑坡次数','地质灾害导致的崩塌次数','地质灾害导致的泥石流次数','地质灾害导致的地面塌陷次数','地质灾害导致的人员伤亡数量','地质灾害导致的死亡人数','地质灾害导致的直接经济损失','森林火灾次数','一般火灾次数','较大火灾次数','重大火灾次数','特别重大火灾次数','火场总面积','受害森林面积','森林火灾导致的伤亡人数','森林火灾导致的其它损失折款',
                  '林业有害生物发生面积','林业有害生物防治面积','林业有害生物防治率','森林病害发生面积','森林病害防治面积','森林虫害发生面积','森林虫害防治面积','森林鼠害发生面积','森林鼠害防治面积','有害植物发生面积','有害植物防治面积','突发环境事件次数','特别重大环境事件次数','重大环境事件次数','较大环境事件次数','一般环境事件次数','地震次数','5.0-5.9级地震次数','6.0-6.9级地震次数','7.0级以上地震次数','地震导致的人员伤亡数量','地震导致的死亡人数','地震导致的直接经济损失','发生次数','导致的人员死亡失踪','导致的直接经济损失',
                  '第二类水质海域面积','第三类水质海域面积','第四类水质海域面积','劣于第四类水质海域面积','城镇环境基础设施建设投资','燃气建设投资','集中供热建设投资','排水建设投资','园林绿化建设投资','市容环境卫生建设投资','工业污染治理完成投资','治理废水投资','治理废气投资','治理固体废物投资','治理噪声投资','治理其他投资','本年完成林业草原投资总计','林业草原国家投资','林业草原生态修复治理投资','林业草原林产品加工制造投资','林业草原服务保障和公共管理投资','国民总收入','国内生产总值','第一产业','第二产业','第三产业','农林牧渔业','工业','建筑业','批发和零售业',
                  '交通运输仓储和邮政业','住宿和餐饮业','金融业','房地产业','其他','人均国民总收入','人均国内生产总值','国内生产总值的占比','第一产业的占比','第二产业的占比','第三产业的占比','农林牧渔业的占比','工业的占比','建筑业的占比','批发和零售业的占比','交通运输仓储和邮政业的占比','住宿和餐饮业的占比','金融业的占比','房地产业的占比','其他的占比','不变价国内生产总值','不变价第一产业','不变价第二产业','不变价第三产业','不变价农林牧渔业','不变价工业','不变价建筑业','不变价批发和零售业','不变价交通运输仓储和邮政业','不变价住宿和餐饮业','不变价金融业','不变价房地产业','不变价其他',
                  '国民总收入的指数','国内生产总值的指数','第一产业的指数','第二产业的指数','第三产业的指数','农林牧渔业的指数','工业的指数','建筑业的指数','批发和零售业的指数','交通运输仓储和邮政业的指数','住宿和餐饮业的指数','金融业的指数','房地产业的指数','其他的指数','人均国民总收入的指数','人均国内生产总值的指数','国内生产总值的增加值','农林牧渔业的增加值','采矿业的增加值','制造业的增加值','电力热力燃气及水的增加值','建筑业的增加值','批发和零售业的增加值','交通运输仓储和邮政业的增加值','住宿和餐饮业的增加值','信息传输软件和信息的增加值','金融业的增加值','房地产业的增加值','租赁和商务服务业的增加值',
                  '科学研究和技术服务业的增加值','水利环境和公共设施管理业的增加值','居民服务修理和其他服务业的增加值','教育的增加值','卫生和社会工作的增加值','文化体育和娱乐业的增加值','公共管理社会保障的增加值','国内生产总值的贡献率','第一产业的贡献率','第二产业的贡献率','第三产业的贡献率','工业的贡献率','批发和零售业的贡献率','金融业的贡献率','国内生产总值对国内生产总值增长的拉动','第一产业对国内生产总值增长的拉动','第二产业对国内生产总值增长的拉动','第三产业对国内生产总值增长的拉动','工业对国内生产总值增长的拉动','批发和零售业对国内生产总值增长的拉动','金融业对国内生产总值增长的拉动','地区生产总值','第一产业增加值','第二产业增加值','第三产业增加值','农林牧渔业增加值','工业增加值','建筑业增加值','批发和零售业增加值','交通运输仓储和邮政业增加值',
                  '住宿和餐饮业增加值','金融业增加值','房地产业增加值','其他增加值','人均地区生产总值','第一产业构成占比','第二产业构成占比','第三产业构成占比','地区生产总值指数','第一产业指数','第二产业指数','第三产业指数','人均地区生产总值指数','生产总值','最终消费','资本形成总额','货物和服务净出口','最终消费率','资本形成率','居民消费中居民消费支出占比','居民消费中政府消费支出占比','居民消费支出','城镇居民支出','农村居民支出','政府消费支出','最终消费中居民消费支出占比','最终消费中政府消费支出占比','出口','进口','固定资本形成总额','存货变动','固定资本形成总额占比','存货变动占比','居民实际最终消费占比','政府实际最终消费占比','居民实际最终消费','政府实际最终消费','全体居民绝对数','城镇居民绝对数','农村居民绝对数','城镇居民消费水平与农村居民消费水平的比值',
                  '全体居民指数','城镇居民消费指数','农村居民消费指数','最终消费支出贡献率','最终消费支出拉动','资本形成总额贡献率','资本形成总额拉动','货物和服务净出口贡献率','货物和服务净出口拉动','净金融投资','资金运用合计','资金来源合计','通货','存款','活期存款','定期存款','财政存款','外汇存款','其他存款','证券公司客户保证金','贷款','短期贷款与票据融资','中长期贷款','外汇贷款','委托贷款','其他贷款','未贴现的银行承兑汇票','保险准备金','金融机构往来','存款准备金','债券','政府债券','金融债券','中央银行债券','企业债券','股票','证券投资基金份额','库存现金','中央银行贷款','其他','直接投资','其他对外债权债务','国际储备资产','国际收支错误与遗漏','企业部门初次分配总收入','企业部门占比','广义政府部门初次分配总收入','广义政府部门占比','住户部门初次分配总收入','住户部门占比',
                  '企业部门调整后可支配总收入','企业部门调整后占比','广义政府部门调整后可支配总收入','广义政府部门调整后占比','住户部门调整后可支配总收入','住户部门调整后占比','农林牧渔产品和服务','采掘产品','食品和烟草','纺织服装鞋及皮革羽绒制品','木材加工家具造纸印刷和文教工美用品','炼油炼焦和化学产品','非金属矿物制品','金属冶炼加工及制品','机械设备和交通运输设备及电子电气及其他设备','其他各类制造产品','电力热力燃气和水的生产和供应','建筑','批发零售运输仓储邮政','信息传输软件和信息技术服务','金融和房地产','科学研究和技术服务','其他服务','中间投入合计','一次能源生产总量','原煤占一次能源生产总量的比重','原油占一次能源生产总量的比重','天然气占一次能源生产总量的比重','一次电力及其他能源占一次能源生产总量的比重','能源消费总量','煤炭占能源消费总量的比重','石油占能源消费总量的比重',
                  '天然气占能源消费总量的比重','一次电力及其他能源占能源消费总量的比重','可供消费的能源总量','一次能源生产总量','回收量','进口量','出口量','年初年末库存差额','能源消费总量','渔业','工业','建筑业','邮政业','住宿和餐饮业','其他','居民生活','终端消费','加工转换损失量','炼焦','炼油及煤制油','损失量','平衡差额','石油可供量','石油生产量','石油进口量','石油出口量','石油年初年末库存差额','石油消费量','农林牧渔业中石油消费量','工业中石油消费量','建筑业中石油消费量','交通运输仓储和邮政业中石油消费量','批发和零售业住宿和餐饮业中石油消费量','其他中石油消费量','居民生活中石油消费量','终端消费中石油消费量','中间消费中石油消费量','火力发电中石油消费量','供热中石油消费量','制气中石油消费量','炼油损失量中石油消费量','损失量中石油消费量','石油平衡差额','煤炭可供量','煤炭生产量','煤炭进口量',
                  '煤炭出口量','煤炭年初年末库存差额','煤炭消费量','农林牧渔业中煤炭消费量','工业中煤炭消费量','建筑业中煤炭消费量','交通运输仓储和邮政业中煤炭消费量','批发和零售业住宿和餐饮业中煤炭消费量','其他中煤炭消费量','居民生活中煤炭消费量','终端消费中煤炭消费量','中间消费中煤炭消费量','火力发电中煤炭消费量','供热中煤炭消费量','炼焦中煤炭消费量','煤制油中煤炭消费量','制气中煤炭消费量','洗选损耗中煤炭消费量','煤炭平衡差额','可供量','电力生产量','水电生产量','火电生产量','核电生产量','风电生产量','电力进口量','电力出口量','电力消费量','农林牧渔业中电力消费量','工业中电力消费量','建筑业中电力消费量','交通运输仓储和邮政业中电力消费量','批发和零售业住宿和餐饮业中电力消费量','其他中电力消费量','居民生活中电力消费量','终端消费中电力消费量','输配电损失量','能源生产比上年增长','电力生产比上年增长',
                  '国内生产总值比上年增长','能源生产弹性系数','电力生产弹性系数','能源消费比上年增长','电力消费比上年增长','国内消费总值比上年增长','能源消费弹性系数','电力消费弹性系数','能源消费总量','煤炭','焦炭','原油','汽油','煤油','柴油','燃料油','天然气','电力','总效率','发电及供热','炼焦','炼油及煤制油','平均每天能源消费合计','平均每天煤炭消费','平均每天焦炭消费','平均每天原油消费','平均每天燃料油消费','平均每天汽油消费','平均每天煤油消费','平均每天柴油消费','平均每天天然气消费','平均每天电力消费','居民能源消费合计','居民煤炭消费','居民煤油消费','居民液化石油气消费','居民天然气消费','居民煤气消费','居民热力消费','居民电力消费','人均生活能源消费量','人均煤炭消费','人均电力消费','人均液化石油气消费','人均天然气消费','人均煤气消费','北京电力消费','天津电力消费','河北电力消费','山西电力消费',
                  '内蒙古电力消费','辽宁电力消费','吉林电力消费','黑龙江电力消费','上海电力消费','江苏电力消费','浙江电力消费','安徽电力消费','福建电力消费','江西电力消费','山东电力消费','河南电力消费','湖北电力消费','湖南电力消费','广东电力消费','广西电力消费','海南电力消费','重庆电力消费','四川电力消费','贵州电力消费','云南电力消费','西藏电力消费','陕西电力消费','甘肃电力消费','青海电力消费','宁夏电力消费','新疆电力消费','发电装机容量','火发电量','水发电量','核发电量','风发电量','太阳能发电量','其他','国内生产总值能源消费量','国内生产总值煤炭消费量','国内生产总值焦炭消费量','国内生产总值石油消费量','国内生产总值原油消费量','国内生产总值燃料油消费量','国内生产总值电力消费量']
    shuzi='20020201971981990123456789'
    shuzi_list=cut2(shuzi)

    #可视化
    root = tk.Tk()
    LoginPage(master=root)


    # root = tk.Tk()
    # # root.attributes('-alpha', 0.3)
    # photo = tk.PhotoImage(file=r"C:\Users\Administrator\Desktop\python编程\subbanner.gif"),
    # label = tk.Label(root, image=photo, width=500, height=400)
    # label.place(x=0)
    #
    # # label.pack()
    # root.geometry('500x400')
    # root.title('基于3E知识图谱的智能问答系统')
    # shuru = tk.StringVar()
    #
    #
    # def huoqu():
    #     neirong = shuru.get()
    #     lfy = neirong
    #     content = text.get(1.0, "end")
    #     if content != '':
    #         text.delete(1.0, "end")
    #
    #     lfy_answers = []
    #
    #     t = 0
    #     s = 0
    #     Global.lfy_answers = []
    #     Global.num = 0
    #     lfy_answers = []
    #     # print('')
    #     question = lfy
    #     # print('')
    #     a = cut(question)
    #     a.reverse()
    #     for i in pingying:
    #             if i in question:
    #                 question = question.replace(i, hanzi[t])
    #                 break
    #             t = t + 1
    #     for j in a:
    #             for k in shuxing_list:
    #                 if j in k and j not in shuzi_list:
    #                     b = question
    #                     b = b.replace(j, k)
    #                     s = 1
    #                     handler.chat_main(b, lfy_answers)
    #             if s == 1:
    #                 break
    #     if Global.lfy_answers != []:
    #             for k in Global.lfy_answers:
    #                 text.insert(INSERT, k+'\n')
    #     else:
    #             text.insert(INSERT,'没能理解您的问题，请您问的标准一点')
    #
    #
    #
    # lfy = ''
    # c = tk.Button(root, text='查询', command=huoqu, width=4, height=1, bg='skyblue', fg='red')
    # c.place(x=110, y=10)
    # # c.pack()
    # a = tk.Entry(root, textvariable=shuru, width=40, fg='red')  # .grid(row=1,column=2)
    # a.place(x=150, y=10)
    #
    # b = tk.Label(root, text='结果', width=4, bg='skyblue')
    # b.place(x=110, y=50)
    #
    # text = Text(root, width=40, height=5)
    # text.place(x=150, y=50)
    #
    # root.mainloop()
    #测试-start
    # problems=["十面埋伏和功夫的评分","十面埋伏和功夫的上映时print(Global.lfy_answers)间","十面埋伏和功夫的风格","十面埋伏和功夫的简介","十面埋伏和功夫的演员","李连杰和成龙的简介",
    #          "成龙和李连杰和周星驰合作的电影","成龙和李连杰和周星驰总共演了多少的电影","成龙和李连杰合作的电影","周星驰和李连杰的生日是？","我女朋友是谁？"]
    # for id,problem in enumerate(problems):
    #     print("第{0}个问题是{1}：".format(id,problem))
    #     handler.chat_main(problem)
    #     print("\n")
    # print("测试结束")
    # 测试-end
    # lfy_answers = []
    # while 1:
    #     t = 0
    #     s = 0
    #     Global.lfy_answers = []
    #     Global.num=0
    #     lfy_answers = []
    #     print('')
    #     question = input('咨询:')
    #     print('')
    #     a=cut(question)
    #     a.reverse()
    #     for i in pingying:
    #         if i in question:
    #             question = question.replace(i, hanzi[t])
    #             break
    #         t=t+1
    #     for j in a:
    #         for k in shuxing_list:
    #             if j in k and j not in shuzi_list:
    #                 b=question
    #                 b=b.replace(j,k)
    #                 s=1
    #                 handler.chat_main(b,lfy_answers)
    #         if s==1:
    #             break
    #     if Global.lfy_answers == []:
    #         print('没能理解您的问题，请您问的标准一点')
        # handler.chat_main(question)




