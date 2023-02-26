from py2neo import Graph
from chatbot_graph import *
import py2neo
import Global
import socket
class AnswerSearcher:
    def __init__(self):

        self.g = Graph("http://yidaproserver.ltd:7019/browser/",auth=('neo4j','2020011720'),name='neo4j')
        # self.g=Graph('http://localhost:7474/browser/',auth=('neo4j','2020011720'),name='neo4j')
        self.num_limit = 1000

    '''执行cypher查询，并返回相应结果'''
    def search_main(self, sqls,lfy_answers):
        final_answers = []
        for sql_ in sqls:
            question_type = sql_['question_type']
            queries = sql_['sql']
            answers = []
            for query in queries:
                ress = self.g.run(query).data()
                answers += ress
            # print(answers)
            final_answer = self.answer_prettify(question_type, answers,lfy_answers)
            
            if final_answer:
                final_answers.append(final_answer)
        # print(final_answers)
        return final_answers

    '''根据对应的qustion_type，调用相应的回复模板'''
    def answer_prettify(self, question_type, answers,lfy_answers):

        final_answer = []
        if not answers:
            return ''
        #十面埋伏和功夫的评分（测试完成，单个和多个）
        #可以完成多个电影查询评分，取第一个评分，不知道为啥返回好多评分。。。

        no_data="统计年鉴中该属性无具体数据"

        if question_type == '资源与环境-1-面积':
            l_=[]
            for i in answers:
                if i['m.土地类型'] not in l_:
                    l_.append(i['m.土地类型'])
                    final_answer = '中国{0}的面积是：{1}'.format(i['m.土地类型'], i['m.面积'])
                    if i['m.面积']=='':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-2-流域面积':
            l_=[]
            for i in answers:
                if i['m.河流名称'] not in l_:
                    l_.append(i['m.河流名称'])
                    final_answer = '{0}的流域面积是：{1}'.format(i['m.河流名称'], i['m.流域面积'])
                    if i['m.流域面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-2-河长':
            l_=[]
            for i in answers:
                if i['m.河流名称'] not in l_:
                    l_.append(i['m.河流名称'])
                    final_answer = '{0}的河长是：{1}'.format(i['m.河流名称'], i['m.河长'])
                    if i['m.河长'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-2-年径流量':
            l_=[]
            for i in answers:
                if i['m.河流名称'] not in l_:
                    l_.append(i['m.河流名称'])
                    final_answer = '{0}的年径流量是：{1}'.format(i['m.河流名称'], i['m.年径流量'])
                    if i['m.年径流量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-3-流域面积':
            l_=[]
            for i in answers:
                if i['m.流域名称'] not in l_:
                    l_.append(i['m.流域名称'])
                    final_answer = '{0}的流域面积是：{1}'.format(i['m.流域名称'], i['m.流域面积'])
                    if i['m.流域面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-3-面积占比':
            l_=[]
            for i in answers:
                if i['m.流域名称'] not in l_:
                    l_.append(i['m.流域名称'])
                    final_answer = '{0}的面积占比是：{1}'.format(i['m.流域名称'], i['m.占外流河和内陆河流域面积合计'])
                    if i['m.占外流河和内陆河流域面积合计'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-4-2020年产量':
            l_=[]
            for i in answers:
                if i['m.矿产名称'] not in l_:
                    l_.append(i['m.矿产名称'])
                    final_answer = '{0}的2020年产量是：{1}'.format(i['m.矿产名称'], i['m.年产量2020年'])
                    if i['m.年产量2020年'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-4-2021年产量':
            l_=[]
            for i in answers:
                if i['m.矿产名称'] not in l_:
                    l_.append(i['m.矿产名称'])
                    final_answer = '{0}的2021年产量是：{1}'.format(i['m.矿产名称'], i['m.年产量2021年'])
                    if i['m.年产量2021年'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-1月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的1月温度是：{1}'.format(i['m.城市名称'], i['m.温度1月'])
                    if i['m.温度1月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-2月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的2月温度是：{1}'.format(i['m.城市名称'], i['m.温度2月'])
                    if i['m.温度2月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-3月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的3月温度是：{1}'.format(i['m.城市名称'], i['m.温度3月'])
                    if i['m.温度3月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-4月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的4月温度是：{1}'.format(i['m.城市名称'], i['m.温度4月'])
                    if i['m.温度4月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-5月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的5月温度是：{1}'.format(i['m.城市名称'], i['m.温度5月'])
                    if i['m.温度5月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-6月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的6月温度是：{1}'.format(i['m.城市名称'], i['m.温度6月'])
                    if i['m.温度6月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-7月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的7月温度是：{1}'.format(i['m.城市名称'], i['m.温度7月'])
                    if i['m.温度7月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-8月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的8月温度是：{1}'.format(i['m.城市名称'], i['m.温度8月'])
                    if i['m.温度8月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-9月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的9月温度是：{1}'.format(i['m.城市名称'], i['m.温度9月'])
                    if i['m.温度9月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-10月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的10月温度是：{1}'.format(i['m.城市名称'], i['m.温度10月'])
                    if i['m.温度10月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-11月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的11月温度是：{1}'.format(i['m.城市名称'], i['m.温度11月'])
                    if i['m.温度11月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-12月温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的12月温度是：{1}'.format(i['m.城市名称'], i['m.温度12月'])
                    if i['m.温度12月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-5-年平均温度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的年平均温度是：{1}'.format(i['m.城市名称'], i['m.年平均温度'])
                    if i['m.年平均温度'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-6-1月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的1月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度1月'])
                    if i['m.湿度1月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-2月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的2月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度2月'])
                    if i['m.湿度2月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-3月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的3月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度3月'])
                    if i['m.湿度3月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-4月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的4月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度4月'])
                    if i['m.湿度4月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-5月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的5月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度5月'])
                    if i['m.湿度5月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-6月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的6月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度6月'])
                    if i['m.湿度6月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-7月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的7月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度7月'])
                    if i['m.湿度7月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-8月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的8月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度8月'])
                    if i['m.湿度8月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-9月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的9月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度9月'])
                    if i['m.湿度9月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-10月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的10月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度10月'])
                    if i['m.湿度10月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-11月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的11月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度11月'])
                    if i['m.湿度11月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-12月湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的12月湿度是：{1}'.format(i['m.城市名称'], i['m.湿度12月'])
                    if i['m.湿度12月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-6-年平均湿度':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的年平均湿度是：{1}'.format(i['m.城市名称'], i['m.年平均湿度'])
                    if i['m.年平均湿度'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-7-1月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的1月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量1月'])
                    if i['m.降水量1月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-2月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的2月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量2月'])
                    if i['m.降水量2月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-3月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的3月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量3月'])
                    if i['m.降水量3月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-4月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的4月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量4月'])
                    if i['m.降水量4月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-5月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的5月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量5月'])
                    if i['m.降水量5月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-6月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的6月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量6月'])
                    if i['m.降水量6月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-7月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的7月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量7月'])
                    if i['m.降水量7月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-8月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的8月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量8月'])
                    if i['m.降水量8月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-9月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的9月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量9月'])
                    if i['m.降水量9月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-10月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的10月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量10月'])
                    if i['m.降水量10月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-11月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的11月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量11月'])
                    if i['m.降水量11月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-12月降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的12月降水量是：{1}'.format(i['m.城市名称'], i['m.降水量12月'])
                    if i['m.降水量12月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-7-全年降水量':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的全年降水量是：{1}'.format(i['m.城市名称'], i['m.全年降水量'])
                    if i['m.全年降水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-8-1月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的1月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数1月'])
                    if i['m.日照时数1月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-2月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的2月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数2月'])
                    if i['m.日照时数2月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-3月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的3月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数3月'])
                    if i['m.日照时数3月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-4月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的4月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数4月'])
                    if i['m.日照时数4月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-5月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的5月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数5月'])
                    if i['m.日照时数5月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-6月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的6月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数6月'])
                    if i['m.日照时数6月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-7月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的7月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数7月'])
                    if i['m.日照时数7月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-8月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的8月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数8月'])
                    if i['m.日照时数8月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-9月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的9月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数9月'])
                    if i['m.日照时数9月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-10月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的10月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数10月'])
                    if i['m.日照时数10月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-11月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的11月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数11月'])
                    if i['m.日照时数11月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-12月日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的12月日照时数是：{1}'.format(i['m.城市名称'], i['m.日照时数12月'])
                    if i['m.日照时数12月'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-8-全年日照时数':
            l_=[]
            for i in answers:
                if i['m.城市名称'] not in l_:
                    l_.append(i['m.城市名称'])
                    final_answer = '{0}2021年的全年日照时数是：{1}'.format(i['m.城市名称'], i['m.全年日照时数'])
                    if i['m.全年日照时数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-9-水资源总量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的水资源总量是：{1}'.format(i['m.地区'], i['m.水资源总量'])
                    if i['m.水资源总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-9-地表水资源量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的地表水资源量是：{1}'.format(i['m.地区'], i['m.地表水资源量'])
                    if i['m.地表水资源量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-9-地下水资源量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的地下水资源量是：{1}'.format(i['m.地区'], i['m.地下水资源量'])
                    if i['m.地下水资源量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-9-地表水与地下水资源重复量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的地表水与地下水资源重复量是：{1}'.format(i['m.地区'], i['m.地表水与地下水资源重复量'])
                    if i['m.地表水与地下水资源重复量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-9-人均水资源量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的人均水资源量是：{1}'.format(i['m.地区'], i['m.人均水资源量'])
                    if i['m.人均水资源量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-9-1-水资源总量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的水资源总量是：{1}'.format(i['m.年份'], i['m.水资源总量'])
                    if i['m.水资源总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-9-1-地表水资源量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的地表水资源量是：{1}'.format(i['m.年份'], i['m.地表水资源量'])
                    if i['m.地表水资源量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-9-1-地下水资源量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的地下水资源量是：{1}'.format(i['m.年份'], i['m.地下水资源量'])
                    if i['m.地下水资源量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-9-1-地表水与地下水资源重复量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的地表水与地下水资源重复量是：{1}'.format(i['m.年份'], i['m.地表水与地下水资源重复量'])
                    if i['m.地表水与地下水资源重复量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-9-1-人均水资源量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均水资源量是：{1}'.format(i['m.年份'], i['m.人均水资源量'])
                    if i['m.人均水资源量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-10-1-供水总量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的供水总量是：{1}'.format(i['m.地区'], i['m.供水总量'])
                    if i['m.供水总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-1-地表水供水量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的地表水供水量是：{1}'.format(i['m.地区'], i['m.地表水供水量'])
                    if i['m.地表水供水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-1-地下水供水量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的地下水供水量是：{1}'.format(i['m.地区'], i['m.地下水供水量'])
                    if i['m.地下水供水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-1-其他供水量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的其他供水量是：{1}'.format(i['m.地区'], i['m.其他供水量'])
                    if i['m.其他供水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-1-用水总量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的用水总量是：{1}'.format(i['m.地区'], i['m.用水总量'])
                    if i['m.用水总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-1-农业用水量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的农业用水量是：{1}'.format(i['m.地区'], i['m.农业用水量'])
                    if i['m.农业用水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-1-工业用水量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的工业用水量是：{1}'.format(i['m.地区'], i['m.工业用水量'])
                    if i['m.工业用水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-1-生活用水量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的生活用水量是：{1}'.format(i['m.地区'], i['m.生活用水量'])
                    if i['m.生活用水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-1-人工生态环境补水用水量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的人工生态环境补水用水量是：{1}'.format(i['m.地区'], i['m.人工生态环境补水用水量'])
                    if i['m.人工生态环境补水用水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-1-人均用水量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的人均用水量是：{1}'.format(i['m.地区'], i['m.人均用水量'])
                    if i['m.人均用水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-10-供水总量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的供水总量是：{1}'.format(i['m.年份'], i['m.供水总量'])
                    if i['m.供水总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-地表水供水量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的地表水供水量是：{1}'.format(i['m.年份'], i['m.地表水供水量'])
                    if i['m.地表水供水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-地下水供水量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的地下水供水量是：{1}'.format(i['m.年份'], i['m.地下水供水量'])
                    if i['m.地下水供水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-其他供水量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的其他供水量是：{1}'.format(i['m.年份'], i['m.其他供水量'])
                    if i['m.其他供水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-用水总量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的用水总量是：{1}'.format(i['m.年份'], i['m.用水总量'])
                    if i['m.用水总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-农业用水量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的农业用水量是：{1}'.format(i['m.年份'], i['m.农业用水量'])
                    if i['m.农业用水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-工业用水量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的工业用水量是：{1}'.format(i['m.年份'], i['m.工业用水量'])
                    if i['m.工业用水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-生活用水量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的生活用水量是：{1}'.format(i['m.年份'], i['m.生活用水量'])
                    if i['m.生活用水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-人工生态环境补水用水量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人工生态环境补水用水量是：{1}'.format(i['m.年份'], i['m.人工生态环境补水用水量'])
                    if i['m.人工生态环境补水用水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-10-人均用水量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均用水量是：{1}'.format(i['m.年份'], i['m.人均用水量'])
                    if i['m.人均用水量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-11-废水中化学需氧量排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中化学需氧量排放量是：{1}'.format(i['m.地区'], i['m.废水中化学需氧量排放量'])
                    if i['m.废水中化学需氧量排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-11-废水中氨氮排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中氨氮排放量是：{1}'.format(i['m.地区'],
                                                                              i['m.废水中氨氮排放量'])
                    if i['m.废水中氨氮排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-11-废水中总氮排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中总氮排放量是：{1}'.format(i['m.地区'],
                                                                              i['m.废水中总氮排放量'])
                    if i['m.废水中总氮排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-11-废水中总磷排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中总磷排放量是：{1}'.format(i['m.地区'],
                                                                              i['m.废水中总磷排放量'])
                    if i['m.废水中总磷排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-11-废水中石油类排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中石油类排放量是：{1}'.format(i['m.地区'],
                                                                              i['m.废水中石油类排放量'])
                    if i['m.废水中石油类排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-11-废水中挥发酚排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中挥发酚排放量是：{1}'.format(i['m.地区'],
                                                                              i['m.废水中挥发酚排放量'])
                    if i['m.废水中挥发酚排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-11-废水中总铅排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中总铅排放量是：{1}'.format(i['m.地区'],
                                                                              i['m.废水中总铅排放量'])
                    if i['m.废水中总铅排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-11-废水中总汞排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中总汞排放量是：{1}'.format(i['m.地区'],
                                                                              i['m.废水中总汞排放量'])
                    if i['m.废水中总汞排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-11-废水中总镉排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中总镉排放量是：{1}'.format(i['m.地区'],
                                                                              i['m.废水中总镉排放量'])
                    if i['m.废水中总镉排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-11-废水中六价铬排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中六价铬排放量是：{1}'.format(i['m.地区'],
                                                                              i['m.废水中六价铬排放量'])
                    if i['m.废水中六价铬排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-11-废水中总铬排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中总铬排放量是：{1}'.format(i['m.地区'],
                                                                              i['m.废水中总铬排放量'])
                    if i['m.废水中总铬排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-11-废水中总砷排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的废水中总砷排放量是：{1}'.format(i['m.地区'],
                                                                              i['m.废水中总砷排放量'])
                    if i['m.废水中总砷排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-12-城市废水中工业化学需氧量排放量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的城市废水中工业化学需氧量排放量是：{1}'.format(i['m.城市'],
                                                                              i['m.城市废水中工业化学需氧量排放量'])
                    if i['m.城市废水中工业化学需氧量排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-12-城市废水中工业氨氮排放量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的城市废水中工业氨氮排放量是：{1}'.format(i['m.城市'],
                                                                              i['m.城市废水中工业氨氮排放量'])
                    if i['m.城市废水中工业氨氮排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-12-城市废水中生活化学需氧量排放量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的城市废水中生活化学需氧量排放量是：{1}'.format(i['m.城市'],
                                                                              i['m.城市废水中生活化学需氧量排放量'])
                    if i['m.城市废水中生活化学需氧量排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-12-城市废水中生活氨氮排放量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的城市废水中生活氨氮排放量是：{1}'.format(i['m.城市'],
                                                                              i['m.城市废水中生活氨氮排放量'])
                    if i['m.城市废水中生活氨氮排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-13-二氧化硫排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的二氧化硫排放量是：{1}'.format(i['m.地区'],
                                                                        i['m.二氧化硫排放量'])
                    if i['m.二氧化硫排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-13-氮氧化物排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的氮氧化物排放量是：{1}'.format(i['m.地区'],
                                                                        i['m.氮氧化物排放量'])
                    if i['m.氮氧化物排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-13-颗粒物排放量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的颗粒物排放量是：{1}'.format(i['m.地区'],
                                                                        i['m.颗粒物排放量'])
                    if i['m.颗粒物排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-14-工业二氧化硫排放量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的工业二氧化硫排放量是：{1}'.format(i['m.城市'],
                                                                        i['m.工业二氧化硫排放量'])
                    if i['m.工业二氧化硫排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-14-工业氮氧化物排放量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的工业氮氧化物排放量是：{1}'.format(i['m.城市'],
                                                                        i['m.工业氮氧化物排放量'])
                    if i['m.工业氮氧化物排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-14-工业氮氧化物排放量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的工业氮氧化物排放量是：{1}'.format(i['m.城市'],
                                                                        i['m.工业氮氧化物排放量'])
                    if i['m.工业氮氧化物排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-14-生活及其他二氧化硫排放量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的生活及其他二氧化硫排放量是：{1}'.format(i['m.城市'],
                                                                        i['m.生活及其他二氧化硫排放量'])
                    if i['m.生活及其他二氧化硫排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-14-生活及其他氮氧化物排放量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的生活及其他氮氧化物排放量是：{1}'.format(i['m.城市'],
                                                                        i['m.生活及其他氮氧化物排放量'])
                    if i['m.生活及其他氮氧化物排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-14-生活及其他颗粒物排放量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的生活及其他颗粒物排放量是：{1}'.format(i['m.城市'],
                                                                        i['m.生活及其他颗粒物排放量'])
                    if i['m.生活及其他颗粒物排放量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-15-一般工业固体废物产生量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的一般工业固体废物产生量是：{1}'.format(i['m.地区'],
                                                                        i['m.一般工业固体废物产生量'])
                    if i['m.一般工业固体废物产生量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-15-一般工业固体废物综合利用量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的一般工业固体废物综合利用量是：{1}'.format(i['m.地区'],
                                                                        i['m.一般工业固体废物综合利用量'])
                    if i['m.一般工业固体废物综合利用量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-15-一般工业固体废物处置量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的一般工业固体废物处置量是：{1}'.format(i['m.地区'],
                                                                        i['m.一般工业固体废物处置量'])
                    if i['m.一般工业固体废物处置量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-15-一般工业固体废物贮存量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的一般工业固体废物贮存量是：{1}'.format(i['m.地区'],
                                                                        i['m.一般工业固体废物贮存量'])
                    if i['m.一般工业固体废物贮存量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-15-一般工业固体废物倾倒丢弃量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的一般工业固体废物倾倒丢弃量是：{1}'.format(i['m.地区'],
                                                                        i['m.一般工业固体废物倾倒丢弃量'])
                    if i['m.一般工业固体废物倾倒丢弃量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-15-危险废物产生量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的危险废物产生量是：{1}'.format(i['m.地区'],
                                                                        i['m.危险废物产生量'])
                    if i['m.危险废物产生量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-15-危险废物利用处置量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的危险废物利用处置量是：{1}'.format(i['m.地区'],
                                                                        i['m.危险废物利用处置量'])
                    if i['m.危险废物利用处置量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-15-危险废物本年末贮存量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的危险废物本年末贮存量是：{1}'.format(i['m.地区'],
                                                                        i['m.危险废物本年末贮存量'])
                    if i['m.危险废物本年末贮存量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-16-一般工业固体废物产生量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的一般工业固体废物产生量是：{1}'.format(i['m.城市'],
                                                                                i['m.一般工业固体废物产生量'])
                    if i['m.一般工业固体废物产生量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-16-一般工业固体废物综合利用量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的一般工业固体废物综合利用量是：{1}'.format(i['m.城市'],
                                                                                i['m.一般工业固体废物综合利用量'])
                    if i['m.一般工业固体废物综合利用量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-16-一般工业固体废物处置量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的一般工业固体废物处置量是：{1}'.format(i['m.城市'],
                                                                                i['m.一般工业固体废物处置量'])
                    if i['m.一般工业固体废物处置量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-16-一般工业固体废物贮存量':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的一般工业固体废物贮存量是：{1}'.format(i['m.城市'],
                                                                                i['m.一般工业固体废物贮存量'])
                    if i['m.一般工业固体废物贮存量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-17-二氧化硫年平均浓度':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的二氧化硫年平均浓度是：{1}'.format(i['m.城市'],
                                                                              i['m.二氧化硫年平均浓度'])
                    if i['m.二氧化硫年平均浓度'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-17-二氧化氮年平均浓度':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的二氧化氮年平均浓度是：{1}'.format(i['m.城市'],
                                                                              i['m.二氧化氮年平均浓度'])
                    if i['m.二氧化氮年平均浓度'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-17-可吸入颗粒物年平均浓度':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的可吸入颗粒物年平均浓度是：{1}'.format(i['m.城市'],
                                                                              i['m.可吸入颗粒物年平均浓度'])
                    if i['m.可吸入颗粒物年平均浓度'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-17-一氧化碳日均值第95百分位浓度':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的一氧化碳日均值第95百分位浓度是：{1}'.format(i['m.城市'],
                                                                              i['m.一氧化碳日均值第95百分位浓度'])
                    if i['m.一氧化碳日均值第95百分位浓度'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-17-臭氧日最大8小时第90百分位浓度':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的臭氧日最大8小时第90百分位浓度是：{1}'.format(i['m.城市'],
                                                                              i['m.臭氧日最大8小时第90百分位浓度'])
                    if i['m.臭氧日最大8小时第90百分位浓度'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-17-细颗粒物年平均浓度':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的细颗粒物年平均浓度是：{1}'.format(i['m.城市'],
                                                                              i['m.细颗粒物年平均浓度'])
                    if i['m.细颗粒物年平均浓度'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-17-空气质量优良天数比例':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的空气质量优良天数比例是：{1}'.format(i['m.城市'],
                                                                              i['m.空气质量优良天数比例'])
                    if i['m.空气质量优良天数比例'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-18-生活垃圾清运量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的生活垃圾清运量是：{1}'.format(i['m.地区'],
                                                                          i['m.生活垃圾清运量'])
                    if i['m.生活垃圾清运量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-无害化处理厂数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的垃圾无害化处理厂数是：{1}'.format(i['m.地区'],
                                                                      i['m.无害化处理厂数'])
                    if i['m.无害化处理厂数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-卫生填埋厂数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的卫生填埋厂数是：{1}'.format(i['m.地区'],
                                                                      i['m.卫生填埋厂数'])
                    if i['m.卫生填埋厂数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-焚烧厂数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的垃圾焚烧厂数是：{1}'.format(i['m.地区'],
                                                                      i['m.焚烧厂数'])
                    if i['m.焚烧厂数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-其他厂数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的其他厂数是：{1}'.format(i['m.地区'],
                                                                      i['m.其他厂数'])
                    if i['m.其他厂数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-无害化处理能力':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的垃圾无害化处理能力是：{1}'.format(i['m.地区'],
                                                                      i['m.无害化处理能力'])
                    if i['m.无害化处理能力'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-卫生填埋处理能力':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的卫生填埋处理能力是：{1}'.format(i['m.地区'],
                                                                      i['m.卫生填埋处理能力'])
                    if i['m.卫生填埋处理能力'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-焚烧处理能力':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的垃圾焚烧处理能力是：{1}'.format(i['m.地区'],
                                                                      i['m.焚烧处理能力'])
                    if i['m.焚烧处理能力'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-其他处理能力':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的其他处理能力是：{1}'.format(i['m.地区'],
                                                                      i['m.其他处理能力'])
                    if i['m.其他处理能力'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-无害化处理量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的垃圾无害化处理量是：{1}'.format(i['m.地区'],
                                                                      i['m.无害化处理量'])
                    if i['m.无害化处理量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-卫生填埋处理量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的卫生填埋处理量是：{1}'.format(i['m.地区'],
                                                                      i['m.卫生填埋处理量'])
                    if i['m.卫生填埋处理量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-焚烧处理量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的垃圾焚烧处理量是：{1}'.format(i['m.地区'],
                                                                      i['m.焚烧处理量'])
                    if i['m.焚烧处理量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-其他处理量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的其他处理量是：{1}'.format(i['m.地区'],
                                                                      i['m.其他处理量'])
                    if i['m.其他处理量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-18-生活垃圾无害化处理率':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的生活垃圾无害化处理率是：{1}'.format(i['m.地区'],
                                                                      i['m.生活垃圾无害化处理率'])
                    if i['m.生活垃圾无害化处理率'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-19-道路交通噪声等效声级':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的道路交通噪声等效声级是：{1}'.format(i['m.城市'],
                                                                            i['m.道路交通噪声等效声级'])
                    if i['m.道路交通噪声等效声级'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-19-区域环境噪声等效声级':
            l_ = []
            for i in answers:
                if i['m.城市'] not in l_:
                    l_.append(i['m.城市'])
                    final_answer = '{0}的区域环境噪声等效声级是：{1}'.format(i['m.城市'],
                                                                            i['m.区域环境噪声等效声级'])
                    if i['m.区域环境噪声等效声级'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-20-2013耕地面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的2013年耕地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.耕地面积2013'])
                    if i['m.耕地面积2013'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-20-2014耕地面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的2014年耕地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.耕地面积2014'])
                    if i['m.耕地面积2014'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-20-2015耕地面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的2015年耕地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.耕地面积2015'])
                    if i['m.耕地面积2015'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-20-2016耕地面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的2016年耕地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.耕地面积2016'])
                    if i['m.耕地面积2016'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-20-2017耕地面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的2017年耕地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.耕地面积2017'])
                    if i['m.耕地面积2017'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-20-2019耕地面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的2019年耕地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.耕地面积2019'])
                    if i['m.耕地面积2019'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-21-耕地':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的耕地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.耕地'])
                    if i['m.耕地'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-21-园地':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的园地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.园地'])
                    if i['m.园地'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-21-林地':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的林地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.林地'])
                    if i['m.林地'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-21-草地':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的草地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.草地'])
                    if i['m.草地'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-21-湿地':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的湿地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.湿地'])
                    if i['m.湿地'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-21-城镇村及工矿用地':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的城镇村及工矿用地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.城镇村及工矿用地'])
                    if i['m.城镇村及工矿用地'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-21-交通运输用地':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的交通运输用地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.交通运输用地'])
                    if i['m.交通运输用地'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-21-水域及水利设施用地':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的水域及水利设施用地面积是：{1}'.format(i['m.地区'],
                                                                    i['m.水域及水利设施用地'])
                    if i['m.水域及水利设施用地'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-22-林业用地面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的林业用地面积是：{1}'.format(i['m.地区'],
                                                                          i['m.林业用地面积'])
                    if i['m.林业用地面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-22-森林面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的森林面积是：{1}'.format(i['m.地区'],
                                                                          i['m.森林面积'])
                    if i['m.森林面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-22-人工林':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的人工林面积是：{1}'.format(i['m.地区'],
                                                                          i['m.人工林'])
                    if i['m.人工林'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-22-森林覆盖率':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的森林覆盖率是：{1}'.format(i['m.地区'],
                                                                          i['m.森林覆盖率'])
                    if i['m.森林覆盖率'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-22-活立木总蓄积量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的活立木总蓄积量是：{1}'.format(i['m.地区'],
                                                                          i['m.活立木总蓄积量'])
                    if i['m.活立木总蓄积量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-22-森林蓄积量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的森林蓄积量是：{1}'.format(i['m.地区'],
                                                                          i['m.森林蓄积量'])
                    if i['m.森林蓄积量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-23-1-造林总面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的造林总面积是：{1}'.format(i['m.地区'],
                                                                  i['m.造林总面积'])
                    if i['m.造林总面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-23-1-人工造林面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的人工造林面积是：{1}'.format(i['m.地区'],
                                                                  i['m.人工造林面积'])
                    if i['m.人工造林面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-23-1-飞播造林面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的飞播造林面积是：{1}'.format(i['m.地区'],
                                                                  i['m.飞播造林面积'])
                    if i['m.飞播造林面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-23-1-封山育林面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的封山育林面积是：{1}'.format(i['m.地区'],
                                                                  i['m.封山育林面积'])
                    if i['m.封山育林面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-23-1-退化林修复面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的退化林修复面积是：{1}'.format(i['m.地区'],
                                                                  i['m.退化林修复面积'])
                    if i['m.退化林修复面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-23-1-人工更新面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的人工更新面积是：{1}'.format(i['m.地区'],
                                                                  i['m.人工更新面积'])
                    if i['m.人工更新面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-23-造林总面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的造林总面积是：{1}'.format(i['m.年份'],
                                                                  i['m.造林总面积'])
                    if i['m.造林总面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-23-人工造林面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人工造林面积是：{1}'.format(i['m.年份'],
                                                                  i['m.人工造林面积'])
                    if i['m.人工造林面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-23-飞播造林面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的飞播造林面积是：{1}'.format(i['m.年份'],
                                                                  i['m.飞播造林面积'])
                    if i['m.飞播造林面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-23-封山育林面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的封山育林面积是：{1}'.format(i['m.年份'],
                                                                  i['m.封山育林面积'])
                    if i['m.封山育林面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-23-退化林修复面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的退化林修复面积是：{1}'.format(i['m.年份'],
                                                                  i['m.退化林修复面积'])
                    if i['m.退化林修复面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-23-人工更新面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人工更新面积是：{1}'.format(i['m.年份'],
                                                                  i['m.人工更新面积'])
                    if i['m.人工更新面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-24-种草面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的种草面积是：{1}'.format(i['m.地区'],
                                                                      i['m.种草面积'])
                    if i['m.种草面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-24-草原改良面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的草原改良面积是：{1}'.format(i['m.地区'],
                                                                      i['m.草原改良面积'])
                    if i['m.草原改良面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-24-草原鼠害发生面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的草原鼠害发生面积是：{1}'.format(i['m.地区'],
                                                                      i['m.草原鼠害发生面积'])
                    if i['m.草原鼠害发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-24-草原鼠害防治面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的草原鼠害防治面积是：{1}'.format(i['m.地区'],
                                                                      i['m.草原鼠害防治面积'])
                    if i['m.草原鼠害防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-24-草原虫害发生面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的草原虫害发生面积是：{1}'.format(i['m.地区'],
                                                                      i['m.草原虫害发生面积'])
                    if i['m.草原虫害发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-24-草原虫害防治面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的草原虫害防治面积是：{1}'.format(i['m.地区'],
                                                                      i['m.草原虫害防治面积'])
                    if i['m.草原虫害防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-24-草原火灾受害面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的草原火灾受害面积是：{1}'.format(i['m.地区'],
                                                                      i['m.草原火灾受害面积'])
                    if i['m.草原火灾受害面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-25-国家级自然保护区个数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的国家级自然保护区个数是：{1}'.format(i['m.地区'],
                                                                        i['m.国家级自然保护区个数'])
                    if i['m.国家级自然保护区个数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-25-国家级自然保护区面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的国家级自然保护区面积是：{1}'.format(i['m.地区'],
                                                                        i['m.国家级自然保护区面积'])
                    if i['m.国家级自然保护区面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-26-农作物受灾面积合计':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的农作物受灾面积是：{1}'.format(i['m.地区'],
                                                                            i['m.农作物受灾面积合计'])
                    if i['m.农作物受灾面积合计'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-农作物绝收面积合计':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的农作物绝收面积是：{1}'.format(i['m.地区'],
                                                                            i['m.农作物绝收面积合计'])
                    if i['m.农作物绝收面积合计'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-旱灾受灾面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的旱灾受灾面积是：{1}'.format(i['m.地区'],
                                                                            i['m.旱灾受灾面积'])
                    if i['m.旱灾受灾面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-旱灾绝收面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的旱灾绝收面积是：{1}'.format(i['m.地区'],
                                                                            i['m.旱灾绝收面积'])
                    if i['m.旱灾绝收面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-洪涝地质灾害和台风受灾面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的洪涝地质灾害和台风受灾面积是：{1}'.format(i['m.地区'],
                                                                            i['m.洪涝地质灾害和台风受灾面积'])
                    if i['m.洪涝地质灾害和台风受灾面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-洪涝地质灾害和台风绝收面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的洪涝地质灾害和台风绝收面积是：{1}'.format(i['m.地区'],
                                                                            i['m.洪涝地质灾害和台风绝收面积'])
                    if i['m.洪涝地质灾害和台风绝收面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-风雹灾害受灾面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的风雹灾害受灾面积是：{1}'.format(i['m.地区'],
                                                                            i['m.风雹灾害受灾面积'])
                    if i['m.风雹灾害受灾面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-风雹灾害绝收面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的风雹灾害绝收面积是：{1}'.format(i['m.地区'],
                                                                            i['m.风雹灾害绝收面积'])
                    if i['m.风雹灾害绝收面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-低温冷冻和雪灾受灾面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的低温冷冻和雪灾受灾面积是：{1}'.format(i['m.地区'],
                                                                            i['m.低温冷冻和雪灾受灾面积'])
                    if i['m.低温冷冻和雪灾受灾面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-低温冷冻和雪灾绝收面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的低温冷冻和雪灾绝收面积是：{1}'.format(i['m.地区'],
                                                                            i['m.低温冷冻和雪灾绝收面积'])
                    if i['m.低温冷冻和雪灾绝收面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-受灾人口':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的受灾人口是：{1}'.format(i['m.地区'],
                                                                            i['m.受灾人口'])
                    if i['m.国家级自然保护区面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-死亡人口':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的死亡人口是：{1}'.format(i['m.地区'],
                                                                            i['m.死亡人口'])
                    if i['m.死亡人口'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-26-直接经济损失':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}自然灾害导致的直接经济损失是：{1}'.format(i['m.地区'],
                                                                            i['m.直接经济损失'])
                    if i['m.直接经济损失'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-27-1-发生地质灾害数量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}发生地质灾害数量是：{1}'.format(i['m.地区'],
                                                                    i['m.发生地质灾害数量'])
                    if i['m.发生地质灾害数量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-1-滑坡次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由地质灾害导致的滑坡次数是：{1}'.format(i['m.地区'],
                                                                    i['m.滑坡次数'])
                    if i['m.滑坡次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-1-崩塌次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由地质灾害导致的崩塌次数是：{1}'.format(i['m.地区'],
                                                                    i['m.崩塌次数'])
                    if i['m.崩塌次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-1-泥石流次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由地质灾害导致的泥石流次数是：{1}'.format(i['m.地区'],
                                                                    i['m.泥石流次数'])
                    if i['m.泥石流次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-1-地面塌陷次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由地质灾害导致的地面塌陷次数是：{1}'.format(i['m.地区'],
                                                                    i['m.地面塌陷次数'])
                    if i['m.地面塌陷次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-1-人员伤亡数量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由地质灾害导致的人员伤亡数量是：{1}'.format(i['m.地区'],
                                                                    i['m.人员伤亡数量'])
                    if i['m.人员伤亡数量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-1-死亡人数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由地质灾害导致的死亡人数是：{1}'.format(i['m.地区'],
                                                                    i['m.死亡人数'])
                    if i['m.死亡人数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-1-直接经济损失':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由地质灾害导致的直接经济损失是：{1}'.format(i['m.地区'],
                                                                    i['m.直接经济损失'])
                    if i['m.直接经济损失'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-27-发生地质灾害数量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}发生地质灾害数量是：{1}'.format(i['m.年份'],
                                                                    i['m.发生地质灾害数量'])
                    if i['m.发生地质灾害数量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-滑坡次数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}由地质灾害导致的滑坡次数是：{1}'.format(i['m.年份'],
                                                                    i['m.滑坡次数'])
                    if i['m.滑坡次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-崩塌次数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}由地质灾害导致的崩塌次数是：{1}'.format(i['m.年份'],
                                                                    i['m.崩塌次数'])
                    if i['m.崩塌次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-泥石流次数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}由地质灾害导致的泥石流次数是：{1}'.format(i['m.年份'],
                                                                    i['m.泥石流次数'])
                    if i['m.泥石流次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-地面塌陷次数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}由地质灾害导致的地面塌陷次数是：{1}'.format(i['m.年份'],
                                                                    i['m.地面塌陷次数'])
                    if i['m.地面塌陷次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-人员伤亡数量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}由地质灾害导致的人员伤亡数量是：{1}'.format(i['m.年份'],
                                                                    i['m.人员伤亡数量'])
                    if i['m.人员伤亡数量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-死亡人数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}由地质灾害导致的死亡人数是：{1}'.format(i['m.年份'],
                                                                    i['m.死亡人数'])
                    if i['m.死亡人数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-27-直接经济损失':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}由地质灾害导致的直接经济损失是：{1}'.format(i['m.年份'],
                                                                    i['m.直接经济损失'])
                    if i['m.直接经济损失'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-28-森林火灾次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的森林火灾次数是：{1}'.format(i['m.地区'],
                                                                    i['m.森林火灾次数'])
                    if i['m.森林火灾次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-28-一般火灾次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的一般火灾次数是：{1}'.format(i['m.地区'],
                                                                    i['m.一般火灾次数'])
                    if i['m.一般火灾次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-28-较大火灾次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的较大火灾次数是：{1}'.format(i['m.地区'],
                                                                    i['m.较大火灾次数'])
                    if i['m.较大火灾次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-28-重大火灾次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的重大火灾次数是：{1}'.format(i['m.地区'],
                                                                    i['m.重大火灾次数'])
                    if i['m.重大火灾次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-28-特别重大火灾次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的特别重大火灾次数是：{1}'.format(i['m.地区'],
                                                                    i['m.特别重大火灾次数'])
                    if i['m.特别重大火灾次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-28-火场总面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的火场总面积是：{1}'.format(i['m.地区'],
                                                                    i['m.火场总面积'])
                    if i['m.火场总面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-28-受害森林面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的受害森林面积是：{1}'.format(i['m.地区'],
                                                                    i['m.受害森林面积'])
                    if i['m.受害森林面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-28-伤亡人数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由森林火灾导致的伤亡人数是：{1}'.format(i['m.地区'],
                                                                    i['m.伤亡人数'])
                    if i['m.伤亡人数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-28-其它损失折款':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由森林火灾导致的其它损失折款是：{1}'.format(i['m.地区'],
                                                                    i['m.其它损失折款'])
                    if i['m.其它损失折款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-29-1-林业有害生物发生面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的林业有害生物发生面积是：{1}'.format(i['m.地区'],
                                                                    i['m.林业有害生物发生面积'])
                    if i['m.林业有害生物发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-1-林业有害生物防治面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的林业有害生物防治面积是：{1}'.format(i['m.地区'],
                                                                    i['m.林业有害生物防治面积'])
                    if i['m.林业有害生物防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-1-林业有害生物防治率':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的林业有害生物防治率是：{1}'.format(i['m.地区'],
                                                                    i['m.林业有害生物防治率'])
                    if i['m.林业有害生物防治率'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-1-森林病害发生面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的森林病害发生面积是：{1}'.format(i['m.地区'],
                                                                    i['m.森林病害发生面积'])
                    if i['m.森林病害发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-1-森林病害防治面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的森林病害防治面积是：{1}'.format(i['m.地区'],
                                                                    i['m.森林病害防治面积'])
                    if i['m.森林病害防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-1-森林虫害发生面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的森林虫害发生面积是：{1}'.format(i['m.地区'],
                                                                    i['m.森林虫害发生面积'])
                    if i['m.森林虫害发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-1-森林虫害防治面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的森林虫害防治面积是：{1}'.format(i['m.地区'],
                                                                    i['m.森林虫害防治面积'])
                    if i['m.森林虫害防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-1-森林鼠害发生面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的森林鼠害发生面积是：{1}'.format(i['m.地区'],
                                                                    i['m.森林鼠害发生面积'])
                    if i['m.森林鼠害发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-1-森林鼠害防治面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的森林鼠害防治面积是：{1}'.format(i['m.地区'],
                                                                    i['m.森林鼠害防治面积'])
                    if i['m.森林鼠害防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-1-有害植物发生面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的有害植物发生面积是：{1}'.format(i['m.地区'],
                                                                    i['m.有害植物发生面积'])
                    if i['m.有害植物发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-1-有害植物防治面积':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的有害植物防治面积是：{1}'.format(i['m.地区'],
                                                                    i['m.有害植物防治面积'])
                    if i['m.有害植物防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        elif question_type == '资源与环境-29-林业有害生物发生面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的林业有害生物发生面积是：{1}'.format(i['m.年份'],
                                                                    i['m.林业有害生物发生面积'])
                    if i['m.林业有害生物发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-林业有害生物防治面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的林业有害生物防治面积是：{1}'.format(i['m.年份'],
                                                                    i['m.林业有害生物防治面积'])
                    if i['m.林业有害生物防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-林业有害生物防治率':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的林业有害生物防治率是：{1}'.format(i['m.年份'],
                                                                    i['m.林业有害生物防治率'])
                    if i['m.林业有害生物防治率'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-森林病害发生面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的森林病害发生面积是：{1}'.format(i['m.年份'],
                                                                    i['m.森林病害发生面积'])
                    if i['m.森林病害发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-森林病害防治面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的森林病害防治面积是：{1}'.format(i['m.年份'],
                                                                    i['m.森林病害防治面积'])
                    if i['m.森林病害防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-森林虫害发生面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的森林虫害发生面积是：{1}'.format(i['m.年份'],
                                                                    i['m.森林虫害发生面积'])
                    if i['m.森林虫害发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-森林虫害防治面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的森林虫害防治面积是：{1}'.format(i['m.年份'],
                                                                    i['m.森林虫害防治面积'])
                    if i['m.森林虫害防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-森林鼠害发生面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的森林鼠害发生面积是：{1}'.format(i['m.年份'],
                                                                    i['m.森林鼠害发生面积'])
                    if i['m.森林鼠害发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-森林鼠害防治面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的森林鼠害防治面积是：{1}'.format(i['m.年份'],
                                                                    i['m.森林鼠害防治面积'])
                    if i['m.森林鼠害防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-有害植物发生面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的有害植物发生面积是：{1}'.format(i['m.年份'],
                                                                    i['m.有害植物发生面积'])
                    if i['m.有害植物发生面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-29-有害植物防治面积':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的有害植物防治面积是：{1}'.format(i['m.年份'],
                                                                    i['m.有害植物防治面积'])
                    if i['m.有害植物防治面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-30-突发环境事件次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的突发环境事件次数是：{1}'.format(i['m.地区'],
                                                                        i['m.突发环境事件次数'])
                    if i['m.突发环境事件次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-30-特别重大环境事件次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的特别重大环境事件次数是：{1}'.format(i['m.地区'],
                                                                        i['m.特别重大环境事件次数'])
                    if i['m.特别重大环境事件次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-30-重大环境事件次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的重大环境事件次数是：{1}'.format(i['m.地区'],
                                                                        i['m.重大环境事件次数'])
                    if i['m.重大环境事件次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-30-较大环境事件次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的较大环境事件次数是：{1}'.format(i['m.地区'],
                                                                        i['m.较大环境事件次数'])
                    if i['m.较大环境事件次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-30-一般环境事件次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的一般环境事件次数是：{1}'.format(i['m.地区'],
                                                                        i['m.一般环境事件次数'])
                    if i['m.一般环境事件次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        elif question_type == '资源与环境-31-1-地震次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的地震次数是：{1}'.format(i['m.地区'],
                                                                        i['m.地震次数'])
                    if i['m.地震次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-1-5.0-5.9级地震次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的5.0-5.9级地震次数是：{1}'.format(i['m.地区'],
                                                                        i['m.地震次数5点0_5点9级'])
                    if i['m.地震次数5点0_5点9级'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-1-6.0-6.9级地震次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的6.0-6.9级地震次数是：{1}'.format(i['m.地区'],
                                                                        i['m.地震次数6点0_6点9级'])
                    if i['m.地震次数6点0_6点9级'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-1-7.0级以上地震次数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的7.0级以上地震次数是：{1}'.format(i['m.地区'],
                                                                        i['m.地震次数7点0_7点9级'])
                    if i['m.地震次数7点0_7点9级'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-1-人员伤亡数量':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由地震导致的人员伤亡数量是：{1}'.format(i['m.地区'],
                                                                        i['m.人员伤亡数量'])
                    if i['m.人员伤亡数量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-1-死亡人数':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由地震导致的死亡人数是：{1}'.format(i['m.地区'],
                                                                        i['m.死亡人数'])
                    if i['m.死亡人数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-1-直接经济损失':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}由地震导致的直接经济损失是：{1}'.format(i['m.地区'],
                                                                        i['m.直接经济损失'])
                    if i['m.直接经济损失'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-31-地震次数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的地震次数是：{1}'.format(i['m.年份'],
                                                                        i['m.地震次数'])
                    if i['m.地震次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-5.0-5.9级地震次数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的5.0-5.9级地震次数是：{1}'.format(i['m.年份'],
                                                                        i['m.地震次数5点0_5点9级'])
                    if i['m.地震次数5点0_5点9级'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-6.0-6.9级地震次数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的6.0-6.9级地震次数是：{1}'.format(i['m.年份'],
                                                                        i['m.地震次数6点0_6点9级'])
                    if i['m.地震次数6点0_6点9级'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-7.0级以上地震次数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的7.0级以上地震次数是：{1}'.format(i['m.年份'],
                                                                        i['m.地震次数7点0_7点9级'])
                    if i['m.地震次数7点0_7点9级'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-人员伤亡数量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}由地震导致的人员伤亡数量是：{1}'.format(i['m.年份'],
                                                                        i['m.人员伤亡数量'])
                    if i['m.人员伤亡数量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-死亡人数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}由地震导致的死亡人数是：{1}'.format(i['m.年份'],
                                                                        i['m.死亡人数'])
                    if i['m.死亡人数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-31-直接经济损失':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}由地震导致的直接经济损失是：{1}'.format(i['m.年份'],
                                                                        i['m.直接经济损失'])
                    if i['m.直接经济损失'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-32-发生次数':
            l_ = []
            for i in answers:
                if i['m.灾种'] not in l_:
                    l_.append(i['m.灾种'])
                    final_answer = '{0}的发生次数是：{1}'.format(i['m.灾种'],
                                                                    i['m.发生次数'])
                    if i['m.发生次数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-32-人员死亡失踪':
            l_ = []
            for i in answers:
                if i['m.灾种'] not in l_:
                    l_.append(i['m.灾种'])
                    final_answer = '{0}导致的人员死亡失踪是：{1}'.format(i['m.灾种'],
                                                                    i['m.人员死亡失踪'])
                    if i['m.人员死亡失踪'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-32-直接经济损失':
            l_ = []
            for i in answers:
                if i['m.灾种'] not in l_:
                    l_.append(i['m.灾种'])
                    final_answer = '{0}导致的直接经济损失是：{1}'.format(i['m.灾种'],
                                                                    i['m.直接经济损失'])
                    if i['m.直接经济损失'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-33-第二类水质海域面积':
            l_ = []
            for i in answers:
                if i['m.海域'] not in l_:
                    l_.append(i['m.海域'])
                    final_answer = '{0}的第二类水质海域面积是：{1}'.format(i['m.海域'],
                                                                    i['m.第二类水质海域面积'])
                    if i['m.第二类水质海域面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-33-第三类水质海域面积':
            l_ = []
            for i in answers:
                if i['m.海域'] not in l_:
                    l_.append(i['m.海域'])
                    final_answer = '{0}的第三类水质海域面积是：{1}'.format(i['m.海域'],
                                                                    i['m.第三类水质海域面积'])
                    if i['m.第三类水质海域面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-33-第四类水质海域面积':
            l_ = []
            for i in answers:
                if i['m.海域'] not in l_:
                    l_.append(i['m.海域'])
                    final_answer = '{0}的第四类水质海域面积是：{1}'.format(i['m.海域'],
                                                                    i['m.第四类水质海域面积'])
                    if i['m.第四类水质海域面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-33-劣于第四类水质海域面积':
            l_ = []
            for i in answers:
                if i['m.海域'] not in l_:
                    l_.append(i['m.海域'])
                    final_answer = '{0}的劣于第四类水质海域面积是：{1}'.format(i['m.海域'],
                                                                    i['m.劣于第四类水质海域面积'])
                    if i['m.劣于第四类水质海域面积'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-34-城镇环境基础设施建设投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的城镇环境基础设施建设投资是：{1}'.format(i['m.地区'],
                                                                    i['m.城镇环境基础设施建设投资'])
                    if i['m.城镇环境基础设施建设投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-34-燃气建设投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的燃气建设投资是：{1}'.format(i['m.地区'],
                                                                    i['m.燃气建设投资'])
                    if i['m.燃气建设投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-34-集中供热建设投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的集中供热建设投资是：{1}'.format(i['m.地区'],
                                                                    i['m.集中供热建设投资'])
                    if i['m.集中供热建设投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-34-排水建设投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的排水建设投资是：{1}'.format(i['m.地区'],
                                                                    i['m.排水建设投资'])
                    if i['m.排水建设投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-34-园林绿化建设投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的园林绿化建设投资是：{1}'.format(i['m.地区'],
                                                                    i['m.园林绿化建设投资'])
                    if i['m.园林绿化建设投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-34-市容环境卫生建设投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的市容环境卫生建设投资是：{1}'.format(i['m.地区'],
                                                                    i['m.市容环境卫生建设投资'])
                    if i['m.市容环境卫生建设投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-35-1-工业污染治理完成投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的工业污染治理完成投资是：{1}'.format(i['m.地区'],
                                                                            i['m.工业污染治理完成投资'])
                    if i['m.工业污染治理完成投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-35-1-治理废水投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的治理废水投资是：{1}'.format(i['m.地区'],
                                                                            i['m.治理废水投资'])
                    if i['m.治理废水投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-35-1-治理废气投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的治理废气投资是：{1}'.format(i['m.地区'],
                                                                            i['m.治理废气投资'])
                    if i['m.治理废气投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-35-1-治理固体废物投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的治理固体废物投资是：{1}'.format(i['m.地区'],
                                                                            i['m.治理固体废物投资'])
                    if i['m.治理固体废物投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-35-1-治理噪声投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的治理噪声投资是：{1}'.format(i['m.地区'],
                                                                            i['m.治理噪声投资'])
                    if i['m.治理噪声投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-35-1-治理其他投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的治理其他投资是：{1}'.format(i['m.地区'],
                                                                            i['m.治理其他投资'])
                    if i['m.治理其他投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '资源与环境-35-工业污染治理完成投资':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的工业污染治理完成投资是：{1}'.format(i['m.年份'],
                                                                            i['m.工业污染治理完成投资'])
                    if i['m.工业污染治理完成投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-35-治理废水投资':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的治理废水投资是：{1}'.format(i['m.年份'],
                                                                            i['m.治理废水投资'])
                    if i['m.治理废水投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-35-治理废气投资':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的治理废气投资是：{1}'.format(i['m.年份'],
                                                                            i['m.治理废气投资'])
                    if i['m.治理废气投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-35-治理固体废物投资':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的治理固体废物投资是：{1}'.format(i['m.年份'],
                                                                            i['m.治理固体废物投资'])
                    if i['m.治理固体废物投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-35-治理噪声投资':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的治理噪声投资是：{1}'.format(i['m.年份'],
                                                                            i['m.治理噪声投资'])
                    if i['m.治理噪声投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-35-治理其他投资':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的治理其他投资是：{1}'.format(i['m.年份'],
                                                                            i['m.治理其他投资'])
                    if i['m.治理其他投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '资源与环境-36-本年完成林业草原投资总计':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的本年完成林业草原投资总计是：{1}'.format(i['m.地区'],
                                                                    i['m.本年完成林业草原投资总计'])
                    if i['m.本年完成林业草原投资总计'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-36-林业草原国家投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的林业草原国家投资是：{1}'.format(i['m.地区'],
                                                                    i['m.林业草原国家投资'])
                    if i['m.林业草原国家投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-36-林业草原生态修复治理投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的林业草原生态修复治理投资是：{1}'.format(i['m.地区'],
                                                                    i['m.林业草原生态修复治理投资'])
                    if i['m.林业草原生态修复治理投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-36-林业草原林产品加工制造投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的林业草原林产品加工制造投资是：{1}'.format(i['m.地区'],
                                                                    i['m.林业草原林产品加工制造投资'])
                    if i['m.林业草原林产品加工制造投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '资源与环境-36-林业草原林业草原服务保障和公共管理投资':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的林业草原服务保障和公共管理投资是：{1}'.format(i['m.地区'],
                                                                    i['m.林业草原林业草原服务保障和公共管理投资'])
                    if i['m.林业草原林业草原服务保障和公共管理投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-1-人均国民总收入':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均国民总收入是：{1}'.format(i['m.年份'],
                                                                        i['m.人均国民总收入'])
                    if i['m.人均国民总收入'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-人均国内生产总值':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.人均国内生产总值'])
                    if i['m.人均国内生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-国民总收入':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国民总收入是：{1}'.format(i['m.年份'],
                                                                        i['m.国民总收入'])
                    if i['m.国民总收入'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-国内生产总值':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.国内生产总值'])
                    if i['m.国内生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-第一产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第一产业国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.第一产业'])
                    if i['m.第一产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-第二产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第二产业国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.第二产业'])
                    if i['m.第二产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-第三产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第三产业国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.第三产业'])
                    if i['m.第三产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-农林牧渔业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的农林牧渔业国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.农林牧渔业'])
                    if i['m.农林牧渔业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-工业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的工业国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.工业'])
                    if i['m.工业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-建筑业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的建筑业国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.建筑业'])
                    if i['m.建筑业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-批发和零售业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的批发和零售业国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.批发和零售业'])
                    if i['m.批发和零售业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-交通运输仓储和邮政业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的交通运输仓储和邮政业国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.交通运输仓储和邮政业'])
                    if i['m.交通运输仓储和邮政业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-住宿和餐饮业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的住宿和餐饮业国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.住宿和餐饮业'])
                    if i['m.住宿和餐饮业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-金融业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的金融业国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.金融业'])
                    if i['m.金融业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-房地产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的房地产业国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.房地产业'])
                    if i['m.房地产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-1-其他':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的其他国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.其他'])
                    if i['m.其他'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-2-国内生产总值':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.国内生产总值'])
                    if i['m.国内生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-第一产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第一产业的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.第一产业'])
                    if i['m.第一产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-第二产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第二产业的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.第二产业'])
                    if i['m.第二产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-第三产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第三产业的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.第三产业'])
                    if i['m.第三产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-农林牧渔业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的农林牧渔业的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.农林牧渔业'])
                    if i['m.农林牧渔业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-工业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的工业的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.工业'])
                    if i['m.工业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-建筑业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的建筑业的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.建筑业'])
                    if i['m.建筑业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-批发和零售业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的批发和零售业的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.批发和零售业'])
                    if i['m.批发和零售业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-交通运输仓储和邮政业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的交通运输仓储和邮政业的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.交通运输仓储和邮政业'])
                    if i['m.交通运输仓储和邮政业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-住宿和餐饮业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的住宿和餐饮业的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.住宿和餐饮业'])
                    if i['m.住宿和餐饮业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-金融业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的金融业的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.金融业'])
                    if i['m.金融业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-房地产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的房地产业的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.房地产业'])
                    if i['m.房地产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-2-其他':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的其他的占比是：{1}'.format(i['m.年份'],
                                                                        i['m.其他'])
                    if i['m.其他'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-3-国内生产总值':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价国内生产总值是：{1}'.format(i['m.年份'],
                                                                        i['m.国内生产总值'])
                    if i['m.国内生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-第一产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价第一产业是：{1}'.format(i['m.年份'],
                                                                        i['m.第一产业'])
                    if i['m.第一产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-第二产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价第二产业是：{1}'.format(i['m.年份'],
                                                                        i['m.第二产业'])
                    if i['m.第二产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-第三产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价第三产业是：{1}'.format(i['m.年份'],
                                                                        i['m.第三产业'])
                    if i['m.第三产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-农林牧渔业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价农林牧渔业是：{1}'.format(i['m.年份'],
                                                                        i['m.农林牧渔业'])
                    if i['m.农林牧渔业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-工业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价工业是：{1}'.format(i['m.年份'],
                                                                        i['m.工业'])
                    if i['m.工业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-建筑业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价建筑业是：{1}'.format(i['m.年份'],
                                                                        i['m.建筑业'])
                    if i['m.建筑业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-批发和零售业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价批发和零售业是：{1}'.format(i['m.年份'],
                                                                        i['m.批发和零售业'])
                    if i['m.批发和零售业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-交通运输仓储和邮政业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价交通运输仓储和邮政业是：{1}'.format(i['m.年份'],
                                                                        i['m.交通运输仓储和邮政业'])
                    if i['m.交通运输仓储和邮政业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-住宿和餐饮业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价住宿和餐饮业是：{1}'.format(i['m.年份'],
                                                                        i['m.住宿和餐饮业'])
                    if i['m.住宿和餐饮业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-金融业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价金融业是：{1}'.format(i['m.年份'],
                                                                        i['m.金融业'])
                    if i['m.金融业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-房地产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价房地产业是：{1}'.format(i['m.年份'],
                                                                        i['m.房地产业'])
                    if i['m.房地产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-3-其他':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的不变价其他是：{1}'.format(i['m.年份'],
                                                                        i['m.其他'])
                    if i['m.其他'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-4-人均国民总收入':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均国民总收入的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.人均国民总收入'])
                    if i['m.人均国民总收入'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-人均国内生产总值':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均国内生产总值的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.人均国内生产总值'])
                    if i['m.人均国内生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-国民总收入':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国民总收入的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.国民总收入'])
                    if i['m.国民总收入'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-国内生产总值':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.国内生产总值'])
                    if i['m.国内生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-第一产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第一产业的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.第一产业'])
                    if i['m.第一产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-第二产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第二产业的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.第二产业'])
                    if i['m.第二产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-第三产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第三产业的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.第三产业'])
                    if i['m.第三产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-农林牧渔业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的农林牧渔业的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.农林牧渔业'])
                    if i['m.农林牧渔业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-工业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的工业的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.工业'])
                    if i['m.工业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-建筑业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的建筑业的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.建筑业'])
                    if i['m.建筑业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-批发和零售业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的批发和零售业的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.批发和零售业'])
                    if i['m.批发和零售业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-交通运输仓储和邮政业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的交通运输仓储和邮政业的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.交通运输仓储和邮政业'])
                    if i['m.交通运输仓储和邮政业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-住宿和餐饮业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的住宿和餐饮业的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.住宿和餐饮业'])
                    if i['m.住宿和餐饮业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-金融业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的金融业的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.金融业'])
                    if i['m.金融业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-房地产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的房地产业的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.房地产业'])
                    if i['m.房地产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-4-其他':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的其他的指数是：{1}'.format(i['m.年份'],
                                                                        i['m.其他'])
                    if i['m.其他'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-6-国内生产总值':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.国内生产总值'])
                    if i['m.国内生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-农林牧渔业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的农林牧渔业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.农林牧渔业'])
                    if i['m.农林牧渔业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-采矿业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的采矿业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.采矿业'])
                    if i['m.采矿业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-制造业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的制造业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.制造业'])
                    if i['m.制造业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-电力热力燃气及水':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的电力热力燃气及水的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.电力热力燃气及水'])
                    if i['m.电力热力燃气及水'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-建筑业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的建筑业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.建筑业'])
                    if i['m.建筑业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-批发和零售业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的批发和零售业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.批发和零售业'])
                    if i['m.批发和零售业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-交通运输仓储和邮政业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的交通运输仓储和邮政业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.交通运输仓储和邮政业'])
                    if i['m.交通运输仓储和邮政业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-住宿和餐饮业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的住宿和餐饮业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.住宿和餐饮业'])
                    if i['m.住宿和餐饮业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-信息传输软件和信息':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的信息传输软件和信息的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.信息传输软件和信息'])
                    if i['m.信息传输软件和信息'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-金融业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的金融业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.金融业'])
                    if i['m.金融业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-房地产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的房地产业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.房地产业'])
                    if i['m.房地产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-租赁和商务服务业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的租赁和商务服务业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.租赁和商务服务业'])
                    if i['m.租赁和商务服务业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-科学研究和技术服务业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的科学研究和技术服务业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.科学研究和技术服务业'])
                    if i['m.科学研究和技术服务业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-水利环境和公共设施管理业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的水利环境和公共设施管理业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.水利环境和公共设施管理业'])
                    if i['m.水利环境和公共设施管理业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-居民服务修理和其他服务业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民服务修理和其他服务业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.居民服务修理和其他服务业'])
                    if i['m.居民服务修理和其他服务业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-教育':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的教育的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.教育'])
                    if i['m.教育'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-卫生和社会工作':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的卫生和社会工作的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.卫生和社会工作'])
                    if i['m.卫生和社会工作'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-文化体育和娱乐业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的文化体育和娱乐业的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.文化体育和娱乐业'])
                    if i['m.文化体育和娱乐业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-6-公共管理社会保障':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的公共管理社会保障的增加值是：{1}'.format(i['m.年份'],
                                                                  i['m.公共管理社会保障'])
                    if i['m.公共管理社会保障'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-7-国内生产总值':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值的贡献率是：{1}'.format(i['m.年份'],
                                                                                i['m.国内生产总值'])
                    if i['m.国内生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-7-第一产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第一产业的贡献率是：{1}'.format(i['m.年份'],
                                                                                i['m.第一产业'])
                    if i['m.第一产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-7-第二产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第二产业的贡献率是：{1}'.format(i['m.年份'],
                                                                                i['m.第二产业'])
                    if i['m.第二产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-7-第三产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第三产业的贡献率是：{1}'.format(i['m.年份'],
                                                                                i['m.第三产业'])
                    if i['m.第三产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-7-工业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的工业的贡献率是：{1}'.format(i['m.年份'],
                                                                                i['m.工业'])
                    if i['m.工业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-7-批发和零售业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的批发和零售业的贡献率是：{1}'.format(i['m.年份'],
                                                                                i['m.批发和零售业'])
                    if i['m.批发和零售业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-7-金融业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的金融业的贡献率是：{1}'.format(i['m.年份'],
                                                                                i['m.金融业'])
                    if i['m.金融业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-8-国内生产总值':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值对国内生产总值增长的拉动是：{1}'.format(i['m.年份'],
                                                                                i['m.国内生产总值'])
                    if i['m.国内生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-8-第一产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第一产业对国内生产总值增长的拉动是：{1}'.format(i['m.年份'],
                                                                                i['m.第一产业'])
                    if i['m.第一产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-8-第二产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第二产业对国内生产总值增长的拉动是：{1}'.format(i['m.年份'],
                                                                                i['m.第二产业'])
                    if i['m.第二产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-8-第三产业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的第三产业对国内生产总值增长的拉动是：{1}'.format(i['m.年份'],
                                                                                i['m.第三产业'])
                    if i['m.第三产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-8-工业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的工业对国内生产总值增长的拉动是：{1}'.format(i['m.年份'],
                                                                                i['m.工业'])
                    if i['m.工业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-8-批发和零售业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的批发和零售业对国内生产总值增长的拉动是：{1}'.format(i['m.年份'],
                                                                                i['m.批发和零售业'])
                    if i['m.批发和零售业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-8-金融业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的金融业对国内生产总值增长的拉动是：{1}'.format(i['m.年份'],
                                                                                i['m.金融业'])
                    if i['m.金融业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-9-地区生产总值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的地区生产总值是：{1}'.format(i['m.地区'],
                                                                        i['m.地区生产总值'])
                    if i['m.地区生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-第一产业增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的第一产业增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.第一产业增加值'])
                    if i['m.第一产业增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-第二产业增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的第二产业增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.第二产业增加值'])
                    if i['m.第二产业增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-第三产业增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的第三产业增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.第三产业增加值'])
                    if i['m.第三产业增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-农林牧渔业增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的农林牧渔业增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.农林牧渔业增加值'])
                    if i['m.农林牧渔业增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-工业增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的工业增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.工业增加值'])
                    if i['m.工业增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-建筑业增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的建筑业增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.建筑业增加值'])
                    if i['m.建筑业增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-批发和零售业增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的批发和零售业增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.批发和零售业增加值'])
                    if i['m.批发和零售业增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-交通运输仓储和邮政业增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的交通运输仓储和邮政业增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.交通运输仓储和邮政业增加值'])
                    if i['m.交通运输仓储和邮政业增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-住宿和餐饮业增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的住宿和餐饮业增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.住宿和餐饮业增加值'])
                    if i['m.住宿和餐饮业增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-金融业增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的金融业增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.金融业增加值'])
                    if i['m.金融业增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-房地产业增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的房地产业增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.房地产业增加值'])
                    if i['m.房地产业增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-其他增加值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的其他增加值是：{1}'.format(i['m.地区'],
                                                                        i['m.其他增加值'])
                    if i['m.其他增加值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '国民经济核算-9-2-人均地区生产总值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的人均地区生产总值是：{1}'.format(i['m.地区'],
                                                                      i['m.人均地区生产总值'])
                    if i['m.人均地区生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-2-第一产业构成':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的第一产业构成的占比是：{1}'.format(i['m.地区'],
                                                                      i['m.第一产业构成'])
                    if i['m.第一产业构成'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-2-第二产业构成':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的第二产业构成的占比是：{1}'.format(i['m.地区'],
                                                                      i['m.第二产业构成'])
                    if i['m.第二产业构成'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-2-第三产业构成':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的第三产业构成的占比是：{1}'.format(i['m.地区'],
                                                                      i['m.第三产业构成'])
                    if i['m.第三产业构成'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        elif question_type == '国民经济核算-9-3-地区生产总值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的地区生产总值的指数是：{1}'.format(i['m.地区'],
                                                                          i['m.地区生产总值'])
                    if i['m.地区生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-3-第一产业':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的第一产业的指数是：{1}'.format(i['m.地区'],
                                                                          i['m.第一产业'])
                    if i['m.第一产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-3-第二产业':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的第二产业的指数是：{1}'.format(i['m.地区'],
                                                                          i['m.第二产业'])
                    if i['m.第二产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-3-第三产业':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的第三产业的指数是：{1}'.format(i['m.地区'],
                                                                          i['m.第三产业'])
                    if i['m.第三产业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-9-3-人均地区生产总值':
            l_ = []
            for i in answers:
                if i['m.地区'] not in l_:
                    l_.append(i['m.地区'])
                    final_answer = '{0}的人均地区生产总值的指数是：{1}'.format(i['m.地区'],
                                                                          i['m.人均地区生产总值'])
                    if i['m.人均地区生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '国民经济核算-10-生产总值':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的生产总值是：{1}'.format(i['m.年份'],
                                                                                    i['m.生产总值'])
                    if i['m.生产总值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-10-最终消费':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的最终消费是：{1}'.format(i['m.年份'],
                                                                                    i['m.最终消费'])
                    if i['m.最终消费'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-10-资本形成总额':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的资本形成总额是：{1}'.format(i['m.年份'],
                                                                                    i['m.资本形成总额'])
                    if i['m.资本形成总额'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-10-货物和服务净出口':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的货物和服务净出口是：{1}'.format(i['m.年份'],
                                                                                    i['m.货物和服务净出口'])
                    if i['m.货物和服务净出口'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-10-最终消费率':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的最终消费率是：{1}'.format(i['m.年份'],
                                                                                    i['m.最终消费率'])
                    if i['m.最终消费率'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-10-资本形成率':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的资本形成率是：{1}'.format(i['m.年份'],
                                                                                    i['m.资本形成率'])
                    if i['m.资本形成率'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        elif question_type == '国民经济核算-11-1-居民消费支出':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民消费支出占比是：{1}'.format(i['m.年份'],
                                                                  i['m.居民消费支出'])
                    if i['m.居民消费支出'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-11-1-政府消费支出':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的政府消费支出占比是：{1}'.format(i['m.年份'],
                                                                  i['m.政府消费支出'])
                    if i['m.政府消费支出'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-11-2-居民消费支出':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民消费支出是：{1}'.format(i['m.年份'],
                                                                        i['m.居民消费支出'])
                    if i['m.居民消费支出'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-11-2-城镇居民支出':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的城镇居民支出是：{1}'.format(i['m.年份'],
                                                                        i['m.城镇居民支出'])
                    if i['m.城镇居民支出'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-11-2-农村居民支出':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的农村居民支出是：{1}'.format(i['m.年份'],
                                                                        i['m.农村居民支出'])
                    if i['m.农村居民支出'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-11-2-政府消费支出':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的政府消费支出是：{1}'.format(i['m.年份'],
                                                                        i['m.政府消费支出'])
                    if i['m.政府消费支出'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-11-3-居民消费支出':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民消费支出占比是：{1}'.format(i['m.年份'],
                                                                  i['m.居民消费支出'])
                    if i['m.居民消费支出'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-11-3-政府消费支出':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的政府消费支出占比是：{1}'.format(i['m.年份'],
                                                                  i['m.政府消费支出'])
                    if i['m.政府消费支出'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-11-4-出口':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的出口是：{1}'.format(i['m.年份'],
                                                                        i['m.出口'])
                    if i['m.出口'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-11-4-进口':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的进口是：{1}'.format(i['m.年份'],
                                                                        i['m.进口'])
                    if i['m.进口'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '国民经济核算-11-5-固定资本形成总额':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的固定资本形成总额是：{1}'.format(i['m.年份'],
                                                            i['m.固定资本形成总额'])
                    if i['m.固定资本形成总额'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-11-5-存货变动':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的存货变动是：{1}'.format(i['m.年份'],
                                                            i['m.存货变动'])
                    if i['m.存货变动'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-11-6-固定资本形成总额':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的固定资本形成总额占比是：{1}'.format(i['m.年份'],
                                                            i['m.固定资本形成总额'])
                    if i['m.固定资本形成总额'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-11-6-存货变动':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的存货变动占比是：{1}'.format(i['m.年份'],
                                                            i['m.存货变动'])
                    if i['m.存货变动'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-12-居民实际最终消费':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民实际最终消费占比是：{1}'.format(i['m.年份'],
                                                                    i['m.居民实际最终消费'])
                    if i['m.居民实际最终消费'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-12-政府实际最终消费':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的政府实际最终消费占比是：{1}'.format(i['m.年份'],
                                                                    i['m.政府实际最终消费'])
                    if i['m.政府实际最终消费'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '国民经济核算-12-1-居民实际最终消费':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民实际最终消费是：{1}'.format(i['m.年份'],
                                                                    i['m.居民实际最终消费'])
                    if i['m.居民实际最终消费'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-12-1-政府实际最终消费':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的政府实际最终消费是：{1}'.format(i['m.年份'],
                                                                    i['m.政府实际最终消费'])
                    if i['m.政府实际最终消费'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-13-全体居民绝对数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的全体居民绝对数是：{1}'.format(i['m.年份'],
                                                                        i['m.全体居民绝对数'])
                    if i['m.全体居民绝对数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-13-城镇居民绝对数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的城镇居民绝对数是：{1}'.format(i['m.年份'],
                                                                        i['m.城镇居民绝对数'])
                    if i['m.城镇居民绝对数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-13-农村居民绝对数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的农村居民绝对数是：{1}'.format(i['m.年份'],
                                                                        i['m.农村居民绝对数'])
                    if i['m.农村居民绝对数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-13-城镇居民消费水平与农村居民消费水平的比值':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的城镇居民消费水平与农村居民消费水平的比值是：{1}'.format(i['m.年份'],
                                                                        i['m.城镇居民消费水平与农村居民消费水平的比值'])
                    if i['m.城镇居民消费水平与农村居民消费水平的比值'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-13-全体居民指数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的全体居民指数是：{1}'.format(i['m.年份'],
                                                                        i['m.全体居民指数'])
                    if i['m.全体居民指数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-13-城镇居民消费指数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的城镇居民消费指数是：{1}'.format(i['m.年份'],
                                                                        i['m.城镇居民消费指数'])
                    if i['m.城镇居民消费指数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-13-农村居民消费指数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的农村居民消费指数是：{1}'.format(i['m.年份'],
                                                                        i['m.农村居民消费指数'])
                    if i['m.农村居民消费指数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        elif question_type == '国民经济核算-14-最终消费支出贡献率':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的最终消费支出贡献率是：{1}'.format(i['m.年份'],
                                                                        i['m.最终消费支出贡献率'])
                    if i['m.最终消费支出贡献率'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-14-最终消费支出拉动':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的最终消费支出拉动是：{1}'.format(i['m.年份'],
                                                                        i['m.最终消费支出拉动'])
                    if i['m.最终消费支出拉动'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-14-资本形成总额贡献率':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的资本形成总额贡献率是：{1}'.format(i['m.年份'],
                                                                        i['m.资本形成总额贡献率'])
                    if i['m.资本形成总额贡献率'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-14-资本形成总额拉动':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的资本形成总额拉动是：{1}'.format(i['m.年份'],
                                                                        i['m.资本形成总额拉动'])
                    if i['m.资本形成总额拉动'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-14-货物和服务净出口贡献率':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的货物和服务净出口贡献率是：{1}'.format(i['m.年份'],
                                                                        i['m.货物和服务净出口贡献率'])
                    if i['m.货物和服务净出口贡献率'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-14-货物和服务净出口拉动':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的货物和服务净出口拉动是：{1}'.format(i['m.年份'],
                                                                        i['m.货物和服务净出口拉动'])
                    if i['m.货物和服务净出口拉动'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        elif question_type == '国民经济核算-16-净金融投资':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的净金融投资是：{1}'.format(i['m.交易项目'],
                                                                            i['m.净金融投资'])
                    if i['m.净金融投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-资金运用合计':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的资金运用合计是：{1}'.format(i['m.交易项目'],
                                                                            i['m.资金运用合计'])
                    if i['m.资金运用合计'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-资金来源合计':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的资金来源合计是：{1}'.format(i['m.交易项目'],
                                                                            i['m.资金来源合计'])
                    if i['m.资金来源合计'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-通货':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的通货是：{1}'.format(i['m.交易项目'],
                                                                            i['m.通货'])
                    if i['m.通货'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-存款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的存款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.存款'])
                    if i['m.存款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-活期存款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的活期存款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.活期存款'])
                    if i['m.活期存款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-定期存款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的定期存款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.定期存款'])
                    if i['m.定期存款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-财政存款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的财政存款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.财政存款'])
                    if i['m.财政存款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-外汇存款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的外汇存款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.外汇存款'])
                    if i['m.外汇存款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-其他存款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的其他存款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.其他存款'])
                    if i['m.其他存款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-证券公司客户保证金':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的证券公司客户保证金是：{1}'.format(i['m.交易项目'],
                                                                            i['m.证券公司客户保证金'])
                    if i['m.证券公司客户保证金'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-贷款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的贷款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.贷款'])
                    if i['m.贷款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-短期贷款与票据融资':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的短期贷款与票据融资是：{1}'.format(i['m.交易项目'],
                                                                            i['m.短期贷款与票据融资'])
                    if i['m.短期贷款与票据融资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-中长期贷款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的中长期贷款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.中长期贷款'])
                    if i['m.中长期贷款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-外汇贷款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的外汇贷款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.外汇贷款'])
                    if i['m.外汇贷款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-委托贷款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的委托贷款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.委托贷款'])
                    if i['m.委托贷款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-其他贷款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的其他贷款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.其他贷款'])
                    if i['m.其他贷款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-未贴现的银行承兑汇票':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的未贴现的银行承兑汇票是：{1}'.format(i['m.交易项目'],
                                                                            i['m.未贴现的银行承兑汇票'])
                    if i['m.未贴现的银行承兑汇票'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-保险准备金':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的保险准备金是：{1}'.format(i['m.交易项目'],
                                                                            i['m.保险准备金'])
                    if i['m.保险准备金'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-金融机构往来':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的金融机构往来是：{1}'.format(i['m.交易项目'],
                                                                            i['m.金融机构往来'])
                    if i['m.金融机构往来'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-存款准备金':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的存款准备金是：{1}'.format(i['m.交易项目'],
                                                                            i['m.存款准备金'])
                    if i['m.存款准备金'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-债券':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的债券是：{1}'.format(i['m.交易项目'],
                                                                            i['m.债券'])
                    if i['m.债券'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-政府债券':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的政府债券是：{1}'.format(i['m.交易项目'],
                                                                            i['m.政府债券'])
                    if i['m.政府债券'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-金融债券':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的金融债券是：{1}'.format(i['m.交易项目'],
                                                                            i['m.金融债券'])
                    if i['m.金融债券'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-中央银行债券':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的中央银行债券是：{1}'.format(i['m.交易项目'],
                                                                            i['m.中央银行债券'])
                    if i['m.中央银行债券'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-企业债券':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的企业债券是：{1}'.format(i['m.交易项目'],
                                                                            i['m.企业债券'])
                    if i['m.企业债券'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-股票':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的股票是：{1}'.format(i['m.交易项目'],
                                                                            i['m.股票'])
                    if i['m.股票'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-证券投资基金份额':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的证券投资基金份额是：{1}'.format(i['m.交易项目'],
                                                                            i['m.证券投资基金份额'])
                    if i['m.证券投资基金份额'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-库存现金':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的库存现金是：{1}'.format(i['m.交易项目'],
                                                                            i['m.库存现金'])
                    if i['m.库存现金'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-中央银行贷款':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的中央银行贷款是：{1}'.format(i['m.交易项目'],
                                                                            i['m.中央银行贷款'])
                    if i['m.中央银行贷款'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-其他':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的其他是：{1}'.format(i['m.交易项目'],
                                                                            i['m.其他'])
                    if i['m.其他'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-直接投资':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的直接投资是：{1}'.format(i['m.交易项目'],
                                                                            i['m.直接投资'])
                    if i['m.直接投资'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-其他对外债权债务':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的其他对外债权债务是：{1}'.format(i['m.交易项目'],
                                                                            i['m.其他对外债权债务'])
                    if i['m.其他对外债权债务'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-国际储备资产':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的国际储备资产是：{1}'.format(i['m.交易项目'],
                                                                            i['m.国际储备资产'])
                    if i['m.国际储备资产'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-16-国际收支错误与遗漏':
            l_ = []
            for i in answers:
                if i['m.交易项目'] not in l_:
                    l_.append(i['m.交易项目'])
                    final_answer = '{0}的国际收支错误与遗漏是：{1}'.format(i['m.交易项目'],
                                                                            i['m.国际收支错误与遗漏'])
                    if i['m.国际收支错误与遗漏'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        elif question_type == '国民经济核算-17-企业部门初次分配总收入':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的企业部门初次分配总收入是：{1}'.format(i['m.年份'],
                                                                          i['m.企业部门初次分配总收入'])
                    if i['m.企业部门初次分配总收入'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-17-企业部门占比':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的企业部门占比是：{1}'.format(i['m.年份'],
                                                                          i['m.企业部门占比'])
                    if i['m.企业部门占比'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-17-广义政府部门初次分配总收入':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的广义政府部门初次分配总收入是：{1}'.format(i['m.年份'],
                                                                          i['m.广义政府部门初次分配总收入'])
                    if i['m.广义政府部门初次分配总收入'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-17-广义政府部门占比':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的广义政府部门占比是：{1}'.format(i['m.年份'],
                                                                          i['m.广义政府部门占比'])
                    if i['m.广义政府部门占比'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-17-住户部门初次分配总收入':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的住户部门初次分配总收入是：{1}'.format(i['m.年份'],
                                                                          i['m.住户部门初次分配总收入'])
                    if i['m.住户部门初次分配总收入'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-17-住户部门占比':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的住户部门占比是：{1}'.format(i['m.年份'],
                                                                          i['m.住户部门占比'])
                    if i['m.住户部门占比'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-19-企业部门调整后可支配总收入':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的企业部门调整后可支配总收入是：{1}'.format(i['m.年份'],
                                                                    i['m.企业部门调整后可支配总收入'])
                    if i['m.企业部门调整后可支配总收入'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-19-企业部门调整后占比':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的企业部门调整后占比是：{1}'.format(i['m.年份'],
                                                                    i['m.企业部门调整后占比'])
                    if i['m.企业部门调整后占比'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-19-广义政府部门调整后可支配总收入':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的广义政府部门调整后可支配总收入是：{1}'.format(i['m.年份'],
                                                                    i['m.广义政府部门调整后可支配总收入'])
                    if i['m.广义政府部门调整后可支配总收入'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-19-广义政府部门调整后占比':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的广义政府部门调整后占比是：{1}'.format(i['m.年份'],
                                                                    i['m.广义政府部门调整后占比'])
                    if i['m.广义政府部门调整后占比'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-19-住户部门调整后可支配总收入':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的住户部门调整后可支配总收入是：{1}'.format(i['m.年份'],
                                                                    i['m.住户部门调整后可支配总收入'])
                    if i['m.住户部门调整后可支配总收入'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-19-住户部门调整后占比':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的住户部门调整后占比是：{1}'.format(i['m.年份'],
                                                                    i['m.住户部门调整后占比'])
                    if i['m.住户部门调整后占比'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '国民经济核算-22-农林牧渔产品和服务':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的农林牧渔产品和服务是：{1}'.format(i['m.投入'],
                                                                          i['m.农林牧渔产品和服务'])
                    if i['m.农林牧渔产品和服务'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-采掘产品':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的采掘产品是：{1}'.format(i['m.投入'],
                                                                          i['m.采掘产品'])
                    if i['m.采掘产品'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-食品和烟草':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的食品和烟草是：{1}'.format(i['m.投入'],
                                                                          i['m.食品和烟草'])
                    if i['m.食品和烟草'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-纺织服装鞋及皮革羽绒制品':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的纺织服装鞋及皮革羽绒制品是：{1}'.format(i['m.投入'],
                                                                          i['m.纺织服装鞋及皮革羽绒制品'])
                    if i['m.纺织服装鞋及皮革羽绒制品'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-木材加工家具造纸印刷和文教工美用品':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的木材加工家具造纸印刷和文教工美用品是：{1}'.format(i['m.投入'],
                                                                          i['m.木材加工家具造纸印刷和文教工美用品'])
                    if i['m.木材加工家具造纸印刷和文教工美用品'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-炼油炼焦和化学产品':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的炼油炼焦和化学产品是：{1}'.format(i['m.投入'],
                                                                          i['m.炼油炼焦和化学产品'])
                    if i['m.炼油炼焦和化学产品'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-非金属矿物制品':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的非金属矿物制品是：{1}'.format(i['m.投入'],
                                                                          i['m.非金属矿物制品'])
                    if i['m.非金属矿物制品'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-金属冶炼加工及制品':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的金属冶炼加工及制品是：{1}'.format(i['m.投入'],
                                                                          i['m.金属冶炼加工及制品'])
                    if i['m.金属冶炼加工及制品'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-机械设备和交通运输设备及电子电气及其他设备':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的机械设备和交通运输设备及电子电气及其他设备是：{1}'.format(i['m.投入'],
                                                                          i['m.机械设备和交通运输设备及电子电气及其他设备'])
                    if i['m.机械设备和交通运输设备及电子电气及其他设备'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-其他各类制造产品':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的其他各类制造产品是：{1}'.format(i['m.投入'],
                                                                          i['m.其他各类制造产品'])
                    if i['m.其他各类制造产品'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-电力热力燃气和水的生产和供应':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的电力热力燃气和水的生产和供应是：{1}'.format(i['m.投入'],
                                                                          i['m.电力热力燃气和水的生产和供应'])
                    if i['m.电力热力燃气和水的生产和供应'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-建筑':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的建筑是：{1}'.format(i['m.投入'],
                                                                          i['m.建筑'])
                    if i['m.建筑'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-批发零售运输仓储邮政':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的批发零售运输仓储邮政是：{1}'.format(i['m.投入'],
                                                                          i['m.批发零售运输仓储邮政'])
                    if i['m.批发零售运输仓储邮政'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-信息传输软件和信息技术服务':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的信息传输软件和信息技术服务是：{1}'.format(i['m.投入'],
                                                                          i['m.信息传输软件和信息技术服务'])
                    if i['m.信息传输软件和信息技术服务'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-金融和房地产':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的金融和房地产是：{1}'.format(i['m.投入'],
                                                                          i['m.金融和房地产'])
                    if i['m.金融和房地产'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-科学研究和技术服务':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的科学研究和技术服务是：{1}'.format(i['m.投入'],
                                                                          i['m.科学研究和技术服务'])
                    if i['m.科学研究和技术服务'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-其他服务':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的其他服务是：{1}'.format(i['m.投入'],
                                                                          i['m.其他服务'])
                    if i['m.其他服务'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '国民经济核算-22-中间投入合计':
            l_ = []
            for i in answers:
                if i['m.投入'] not in l_:
                    l_.append(i['m.投入'])
                    final_answer = '{0}的中间投入合计是：{1}'.format(i['m.投入'],
                                                                          i['m.中间投入合计'])
                    if i['m.中间投入合计'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '能源-1-一次能源生产总量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的一次能源生产总量是：{1}'.format(i['m.年份'],
                                                                          i['m.一次能源生产总量'])
                    if i['m.一次能源生产总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-1-原煤占一次能源生产总量的比重':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的原煤占一次能源生产总量的比重是：{1}'.format(i['m.年份'],
                                                                          i['m.原煤占一次能源生产总量的比重'])
                    if i['m.原煤占一次能源生产总量的比重'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-1-原油占一次能源生产总量的比重':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的原油占一次能源生产总量的比重是：{1}'.format(i['m.年份'],
                                                                          i['m.原油占一次能源生产总量的比重'])
                    if i['m.原油占一次能源生产总量的比重'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-1-天然气':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的天然气占一次能源生产总量的比重是：{1}'.format(i['m.年份'],
                                                                          i['m.天然气'])
                    if i['m.天然气'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-1-一次电力及其他能源':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的一次电力及其他能源占一次能源生产总量的比重是：{1}'.format(i['m.年份'],
                                                                          i['m.一次电力及其他能源'])
                    if i['m.一次电力及其他能源'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '能源-2-能源消费总量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的能源消费总量是：{1}'.format(i['m.年份'],
                                                                          i['m.能源消费总量'])
                    if i['m.能源消费总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-2-煤炭占能源消费总量的比重':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的煤炭占能源消费总量的比重是：{1}'.format(i['m.年份'],
                                                                          i['m.煤炭占能源消费总量的比重'])
                    if i['m.煤炭占能源消费总量的比重'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-2-石油占能源消费总量的比重':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的石油占能源消费总量的比重是：{1}'.format(i['m.年份'],
                                                                          i['m.石油占能源消费总量的比重'])
                    if i['m.石油占能源消费总量的比重'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-2-天然气占能源消费总量的比重':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的天然气占能源消费总量的比重是：{1}'.format(i['m.年份'],
                                                                          i['m.天然气占能源消费总量的比重'])
                    if i['m.天然气占能源消费总量的比重'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-2-一次电力及其他能源占能源消费总量的比重':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的一次电力及其他能源占能源消费总量的比重是：{1}'.format(i['m.年份'],
                                                                          i['m.一次电力及其他能源占能源消费总量的比重'])
                    if i['m.一次电力及其他能源占能源消费总量的比重'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '能源-3-可供消费的能源总量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的可供消费的能源总量是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.可供消费的能源总量'])
                    if i['m.可供消费的能源总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-一次能源生产总量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的一次能源生产总量是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.一次能源生产总量'])
                    if i['m.一次能源生产总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-回收量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的回收量是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.回收量'])
                    if i['m.回收量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-进口量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的进口量是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.进口量'])
                    if i['m.进口量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-出口量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的出口量是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.出口量'])
                    if i['m.出口量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-年初年末库存差额':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的年初年末库存差额是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.年初年末库存差额'])
                    if i['m.年初年末库存差额'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-能源消费总量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的能源消费总量是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.能源消费总量'])
                    if i['m.能源消费总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-渔业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的渔业是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.渔业'])
                    if i['m.渔业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-工业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的工业是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.工业'])
                    if i['m.工业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-建筑业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的建筑业是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.建筑业'])
                    if i['m.建筑业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-邮政业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的邮政业是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.邮政业'])
                    if i['m.邮政业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-住宿和餐饮业':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的住宿和餐饮业是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.住宿和餐饮业'])
                    if i['m.住宿和餐饮业'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-其他':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的其他是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.其他'])
                    if i['m.其他'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-居民生活':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民生活是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.居民生活'])
                    if i['m.居民生活'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-终端消费':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的终端消费是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.终端消费'])
                    if i['m.终端消费'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-加工转换损失量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的加工转换损失量是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.加工转换损失量'])
                    if i['m.加工转换损失量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-炼焦':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的炼焦是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.炼焦'])
                    if i['m.炼焦'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-炼油及煤制油':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的炼油及煤制油是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.炼油及煤制油'])
                    if i['m.炼油及煤制油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-损失量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的损失量是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.损失量'])
                    if i['m.损失量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-3-平衡差额':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的平衡差额是：{1}'.format(i['m.年份'],
                                                                                              i[
                                                                                                  'm.平衡差额'])
                    if i['m.平衡差额'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '能源-4-石油可供量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的石油可供量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.石油可供量'])
                    if i['m.石油可供量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-石油生产量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的石油生产量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.石油生产量'])
                    if i['m.石油生产量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-石油进口量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的石油进口量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.石油进口量'])
                    if i['m.石油进口量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-石油出口量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的石油出口量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.石油出口量'])
                    if i['m.石油出口量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-石油年初年末库存差额':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的石油年初年末库存差额是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.石油年初年末库存差额'])
                    if i['m.石油年初年末库存差额'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.石油消费量'])
                    if i['m.石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-农林牧渔业中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的农林牧渔业中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.农林牧渔业中石油消费量'])
                    if i['m.农林牧渔业中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-工业中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的工业中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.工业中石油消费量'])
                    if i['m.工业中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-建筑业中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的建筑业中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.建筑业中石油消费量'])
                    if i['m.建筑业中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-交通运输仓储和邮政业中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的交通运输仓储和邮政业中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.交通运输仓储和邮政业中石油消费量'])
                    if i['m.交通运输仓储和邮政业中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-批发和零售业住宿和餐饮业中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的批发和零售业住宿和餐饮业中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.批发和零售业住宿和餐饮业中石油消费量'])
                    if i['m.批发和零售业住宿和餐饮业中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-其他中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的其他中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.其他中石油消费量'])
                    if i['m.其他中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-居民生活中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民生活中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.居民生活中石油消费量'])
                    if i['m.居民生活中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-终端消费中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的终端消费中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.终端消费中石油消费量'])
                    if i['m.终端消费中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-中间消费中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的中间消费中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.中间消费中石油消费量'])
                    if i['m.中间消费中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-火力发电中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的火力发电中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.火力发电中石油消费量'])
                    if i['m.火力发电中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-供热中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的供热中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.供热中石油消费量'])
                    if i['m.供热中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-制气中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的制气中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.制气中石油消费量'])
                    if i['m.制气中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-炼油损失量中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的炼油损失量中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.炼油损失量中石油消费量'])
                    if i['m.炼油损失量中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-损失量中石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的损失量中石油消费量是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.损失量中石油消费量'])
                    if i['m.损失量中石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-4-石油平衡差额':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的石油平衡差额是：{1}'.format(i['m.年份'],
                                                                i[
                                                                    'm.石油平衡差额'])
                    if i['m.石油平衡差额'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        elif question_type == '能源-5-煤炭可供量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的煤炭可供量是：{1}'.format(i['m.年份'],
                                                                      i['m.煤炭可供量'])
                    if i['m.煤炭可供量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-煤炭生产量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的煤炭生产量是：{1}'.format(i['m.年份'],
                                                                      i['m.煤炭生产量'])
                    if i['m.煤炭生产量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-煤炭进口量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的煤炭进口量是：{1}'.format(i['m.年份'],
                                                                      i['m.煤炭进口量'])
                    if i['m.煤炭进口量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-煤炭出口量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的煤炭出口量是：{1}'.format(i['m.年份'],
                                                                      i['m.煤炭出口量'])
                    if i['m.煤炭出口量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-煤炭年初年末库存差额':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的煤炭年初年末库存差额是：{1}'.format(i['m.年份'],
                                                                      i['m.煤炭年初年末库存差额'])
                    if i['m.煤炭年初年末库存差额'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.煤炭消费量'])
                    if i['m.煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-农林牧渔业中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的农林牧渔业中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.农林牧渔业中煤炭消费量'])
                    if i['m.农林牧渔业中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-工业中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的工业中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.工业中煤炭消费量'])
                    if i['m.工业中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-建筑业中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的建筑业中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.建筑业中煤炭消费量'])
                    if i['m.建筑业中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-交通运输仓储和邮政业中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的交通运输仓储和邮政业中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.交通运输仓储和邮政业中煤炭消费量'])
                    if i['m.交通运输仓储和邮政业中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-批发和零售业住宿和餐饮业中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的批发和零售业住宿和餐饮业中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.批发和零售业住宿和餐饮业中煤炭消费量'])
                    if i['m.批发和零售业住宿和餐饮业中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-其他中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的其他中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.其他中煤炭消费量'])
                    if i['m.其他中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-居民生活中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民生活中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.居民生活中煤炭消费量'])
                    if i['m.居民生活中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-终端消费中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的终端消费中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.终端消费中煤炭消费量'])
                    if i['m.终端消费中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-中间消费中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的中间消费中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.中间消费中煤炭消费量'])
                    if i['m.中间消费中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-火力发电中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的火力发电中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.火力发电中煤炭消费量'])
                    if i['m.火力发电中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-供热中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的供热中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.供热中煤炭消费量'])
                    if i['m.供热中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-炼焦中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的炼焦中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.炼焦中煤炭消费量'])
                    if i['m.炼焦中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-煤制油中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的煤制油中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.煤制油中煤炭消费量'])
                    if i['m.煤制油中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-制气中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的制气中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.制气中煤炭消费量'])
                    if i['m.制气中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-洗选损耗中煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的洗选损耗中煤炭消费量是：{1}'.format(i['m.年份'],
                                                                      i['m.洗选损耗中煤炭消费量'])
                    if i['m.洗选损耗中煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-5-煤炭平衡差额':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的煤炭平衡差额是：{1}'.format(i['m.年份'],
                                                                      i['m.煤炭平衡差额'])
                    if i['m.煤炭平衡差额'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #




        elif question_type == '能源-6-可供量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的可供量是：{1}'.format(i['m.年份'],
                                                                    i['m.可供量'])
                    if i['m.可供量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-电力生产量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的电力生产量是：{1}'.format(i['m.年份'],
                                                                    i['m.电力生产量'])
                    if i['m.电力生产量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-水电生产量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的水电生产量是：{1}'.format(i['m.年份'],
                                                                    i['m.水电生产量'])
                    if i['m.水电生产量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-火电生产量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的火电生产量是：{1}'.format(i['m.年份'],
                                                                    i['m.火电生产量'])
                    if i['m.火电生产量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-核电生产量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的核电生产量是：{1}'.format(i['m.年份'],
                                                                    i['m.核电生产量'])
                    if i['m.核电生产量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-风电生产量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的风电生产量是：{1}'.format(i['m.年份'],
                                                                    i['m.风电生产量'])
                    if i['m.风电生产量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-电力进口量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的电力进口量是：{1}'.format(i['m.年份'],
                                                                    i['m.电力进口量'])
                    if i['m.电力进口量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-电力出口量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的电力出口量是：{1}'.format(i['m.年份'],
                                                                    i['m.电力出口量'])
                    if i['m.电力出口量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-电力消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的电力消费量是：{1}'.format(i['m.年份'],
                                                                    i['m.电力消费量'])
                    if i['m.电力消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-农林牧渔业中电力消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的农林牧渔业中电力消费量是：{1}'.format(i['m.年份'],
                                                                    i['m.农林牧渔业中电力消费量'])
                    if i['m.农林牧渔业中电力消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-工业中电力消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的工业中电力消费量是：{1}'.format(i['m.年份'],
                                                                    i['m.工业中电力消费量'])
                    if i['m.工业中电力消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-建筑业中电力消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的建筑业中电力消费量是：{1}'.format(i['m.年份'],
                                                                    i['m.建筑业中电力消费量'])
                    if i['m.建筑业中电力消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-交通运输仓储和邮政业中电力消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的交通运输仓储和邮政业中电力消费量是：{1}'.format(i['m.年份'],
                                                                    i['m.交通运输仓储和邮政业中电力消费量'])
                    if i['m.交通运输仓储和邮政业中电力消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-批发和零售业住宿和餐饮业中电力消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的批发和零售业住宿和餐饮业中电力消费量是：{1}'.format(i['m.年份'],
                                                                    i['m.批发和零售业住宿和餐饮业中电力消费量'])
                    if i['m.批发和零售业住宿和餐饮业中电力消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-其他中电力消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的其他中电力消费量是：{1}'.format(i['m.年份'],
                                                                    i['m.其他中电力消费量'])
                    if i['m.其他中电力消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-居民生活中电力消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民生活中电力消费量是：{1}'.format(i['m.年份'],
                                                                    i['m.居民生活中电力消费量'])
                    if i['m.居民生活中电力消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-终端消费中电力消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的终端消费中电力消费量是：{1}'.format(i['m.年份'],
                                                                    i['m.终端消费中电力消费量'])
                    if i['m.终端消费中电力消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-6-输配电损失量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的输配电损失量是：{1}'.format(i['m.年份'],
                                                                    i['m.输配电损失量'])
                    if i['m.输配电损失量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '能源-7-能源生产比上年增长':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的能源生产比上年增长是：{1}'.format(i['m.年份'],
                                                                    i['m.能源生产比上年增长'])
                    if i['m.能源生产比上年增长'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-7-电力生产比上年增长':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的电力生产比上年增长是：{1}'.format(i['m.年份'],
                                                                    i['m.电力生产比上年增长'])
                    if i['m.电力生产比上年增长'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-7-国内生产总值比上年增长':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值比上年增长是：{1}'.format(i['m.年份'],
                                                                    i['m.国内生产总值比上年增长'])
                    if i['m.国内生产总值比上年增长'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-7-能源生产弹性系数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的能源生产弹性系数是：{1}'.format(i['m.年份'],
                                                                    i['m.能源生产弹性系数'])
                    if i['m.能源生产弹性系数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-7-电力生产弹性系数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的电力生产弹性系数是：{1}'.format(i['m.年份'],
                                                                    i['m.电力生产弹性系数'])
                    if i['m.电力生产弹性系数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '能源-8-能源消费比上年增长':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的能源消费比上年增长是：{1}'.format(i['m.年份'],
                                                                        i['m.能源消费比上年增长'])
                    if i['m.能源消费比上年增长'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-8-电力消费比上年增长':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的电力消费比上年增长是：{1}'.format(i['m.年份'],
                                                                        i['m.电力消费比上年增长'])
                    if i['m.电力消费比上年增长'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-8-国内消费总值比上年增长':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内消费总值比上年增长是：{1}'.format(i['m.年份'],
                                                                        i['m.国内消费总值比上年增长'])
                    if i['m.国内消费总值比上年增长'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-8-能源消费弹性系数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的能源消费弹性系数是：{1}'.format(i['m.年份'],
                                                                        i['m.能源消费弹性系数'])
                    if i['m.能源消费弹性系数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-8-电力消费弹性系数':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的电力消费弹性系数是：{1}'.format(i['m.年份'],
                                                                        i['m.电力消费弹性系数'])
                    if i['m.电力消费弹性系数'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        elif question_type == '能源-9-能源消费总量':
            l_ = []
            for i in answers:
                if i['m.行业'] not in l_:
                    l_.append(i['m.行业'])
                    final_answer = '{0}的能源消费总量是：{1}'.format(i['m.行业'],
                                                                        i['m.能源消费总量'])
                    if i['m.能源消费总量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '能源-9-煤炭':
            l_ = []
            for i in answers:
                if i['m.行业'] not in l_:
                    l_.append(i['m.行业'])
                    final_answer = '{0}的煤炭是：{1}'.format(i['m.行业'],
                                                                        i['m.煤炭'])
                    if i['m.煤炭'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-9-焦炭':
            l_ = []
            for i in answers:
                if i['m.行业'] not in l_:
                    l_.append(i['m.行业'])
                    final_answer = '{0}的焦炭是：{1}'.format(i['m.行业'],
                                                                        i['m.焦炭'])
                    if i['m.焦炭'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-9-原油':
            l_ = []
            for i in answers:
                if i['m.行业'] not in l_:
                    l_.append(i['m.行业'])
                    final_answer = '{0}的原油是：{1}'.format(i['m.行业'],
                                                                        i['m.原油'])
                    if i['m.原油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-9-汽油':
            l_ = []
            for i in answers:
                if i['m.行业'] not in l_:
                    l_.append(i['m.行业'])
                    final_answer = '{0}的汽油是：{1}'.format(i['m.行业'],
                                                                        i['m.汽油'])
                    if i['m.汽油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-9-煤油':
            l_ = []
            for i in answers:
                if i['m.行业'] not in l_:
                    l_.append(i['m.行业'])
                    final_answer = '{0}的煤油是：{1}'.format(i['m.行业'],
                                                                        i['m.煤油'])
                    if i['m.煤油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-9-柴油':
            l_ = []
            for i in answers:
                if i['m.行业'] not in l_:
                    l_.append(i['m.行业'])
                    final_answer = '{0}的柴油是：{1}'.format(i['m.行业'],
                                                                        i['m.柴油'])
                    if i['m.柴油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-9-燃料油':
            l_ = []
            for i in answers:
                if i['m.行业'] not in l_:
                    l_.append(i['m.行业'])
                    final_answer = '{0}的燃料油是：{1}'.format(i['m.行业'],
                                                                        i['m.燃料油'])
                    if i['m.燃料油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-9-天然气':
            l_ = []
            for i in answers:
                if i['m.行业'] not in l_:
                    l_.append(i['m.行业'])
                    final_answer = '{0}的天然气是：{1}'.format(i['m.行业'],
                                                                        i['m.天然气'])
                    if i['m.天然气'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-9-电力':
            l_ = []
            for i in answers:
                if i['m.行业'] not in l_:
                    l_.append(i['m.行业'])
                    final_answer = '{0}的电力是：{1}'.format(i['m.行业'],
                                                                        i['m.电力'])
                    if i['m.电力'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '能源-10-总效率':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的总效率是：{1}'.format(i['m.年份'],
                                                                          i['m.总效率'])
                    if i['m.总效率'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-10-发电及供热':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的发电及供热是：{1}'.format(i['m.年份'],
                                                                          i['m.发电及供热'])
                    if i['m.发电及供热'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-10-炼焦':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的炼焦是：{1}'.format(i['m.年份'],
                                                                          i['m.炼焦'])
                    if i['m.炼焦'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-10-炼油及煤制油':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的炼油及煤制油是：{1}'.format(i['m.年份'],
                                                                          i['m.炼油及煤制油'])
                    if i['m.炼油及煤制油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '能源-11-合计':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的平均每天能源消费合计是：{1}'.format(i['m.年份'],
                                                                        i['m.合计'])
                    if i['m.合计'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #

        elif question_type == '能源-11-煤炭':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的平均每天煤炭消费是：{1}'.format(i['m.年份'],
                                                                        i['m.煤炭'])
                    if i['m.煤炭'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-11-焦炭':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的平均每天焦炭消费是：{1}'.format(i['m.年份'],
                                                                        i['m.焦炭'])
                    if i['m.焦炭'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-11-原油':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的平均每天原油消费是：{1}'.format(i['m.年份'],
                                                                        i['m.原油'])
                    if i['m.原油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-11-汽油':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的平均每天汽油消费是：{1}'.format(i['m.年份'],
                                                                        i['m.汽油'])
                    if i['m.汽油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-11-煤油':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的平均每天煤油消费是：{1}'.format(i['m.年份'],
                                                                        i['m.煤油'])
                    if i['m.煤油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-11-柴油':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的平均每天柴油消费是：{1}'.format(i['m.年份'],
                                                                        i['m.柴油'])
                    if i['m.柴油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-11-燃料油':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的平均每天燃料油消费是：{1}'.format(i['m.年份'],
                                                                        i['m.燃料油'])
                    if i['m.燃料油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-11-天然气':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的平均每天天然气消费是：{1}'.format(i['m.年份'],
                                                                        i['m.天然气'])
                    if i['m.天然气'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-11-电力':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的平均每天电力消费是：{1}'.format(i['m.年份'],
                                                                        i['m.电力'])
                    if i['m.电力'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        elif question_type == '能源-12-合计':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民能源消费合计是：{1}'.format(i['m.年份'],
                                                            i['m.合计'])
                    if i['m.合计'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-12-煤炭':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民煤炭消费是：{1}'.format(i['m.年份'],
                                                            i['m.煤炭'])
                    if i['m.煤炭'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-12-煤油':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民煤油消费是：{1}'.format(i['m.年份'],
                                                            i['m.煤油'])
                    if i['m.煤油'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-12-液化石油气':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民液化石油气消费是：{1}'.format(i['m.年份'],
                                                            i['m.液化石油气'])
                    if i['m.液化石油气'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-12-天然气':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民天然气消费是：{1}'.format(i['m.年份'],
                                                            i['m.天然气'])
                    if i['m.天然气'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-12-煤气':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民煤气消费是：{1}'.format(i['m.年份'],
                                                            i['m.煤气'])
                    if i['m.煤气'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-12-热力':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民热力消费是：{1}'.format(i['m.年份'],
                                                            i['m.热力'])
                    if i['m.热力'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-12-电力':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的居民电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.电力'])
                    if i['m.电力'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '能源-13-人均生活能源消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均生活能源消费量是：{1}'.format(i['m.年份'],
                                                            i['m.人均生活能源消费量'])
                    if i['m.人均生活能源消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-13-煤炭':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均煤炭消费是：{1}'.format(i['m.年份'],
                                                            i['m.煤炭'])
                    if i['m.煤炭'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-13-电力':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.电力'])
                    if i['m.电力'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-13-液化石油气':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均液化石油气消费是：{1}'.format(i['m.年份'],
                                                            i['m.液化石油气'])
                    if i['m.液化石油气'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-13-天然气':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均天然气消费是：{1}'.format(i['m.年份'],
                                                            i['m.天然气'])
                    if i['m.天然气'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-13-煤气':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的人均煤气消费是：{1}'.format(i['m.年份'],
                                                            i['m.煤气'])
                    if i['m.煤气'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        elif question_type == '能源-14-北京':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的北京电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.北京'])
                    if i['m.北京'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-天津':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的天津电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.天津'])
                    if i['m.天津'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-河北':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的河北电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.河北'])
                    if i['m.河北'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-山西':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的山西电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.山西'])
                    if i['m.山西'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-内蒙古':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的内蒙古电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.内蒙古'])
                    if i['m.内蒙古'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-辽宁':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的辽宁电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.辽宁'])
                    if i['m.辽宁'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-吉林':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的吉林电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.吉林'])
                    if i['m.吉林'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-黑龙江':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的黑龙江电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.黑龙江'])
                    if i['m.黑龙江'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-上海':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的上海电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.上海'])
                    if i['m.上海'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-江苏':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的江苏电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.江苏'])
                    if i['m.江苏'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-浙江':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的浙江电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.浙江'])
                    if i['m.浙江'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-安徽':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的安徽电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.安徽'])
                    if i['m.安徽'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-福建':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的福建电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.福建'])
                    if i['m.福建'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-江西':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的江西电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.江西'])
                    if i['m.江西'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-山东':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的山东电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.山东'])
                    if i['m.山东'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-河南':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的河南电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.河南'])
                    if i['m.河南'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-湖北':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的湖北电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.湖北'])
                    if i['m.湖北'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-湖南':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的湖南电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.湖南'])
                    if i['m.湖南'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-广东':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的广东电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.广东'])
                    if i['m.广东'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-广西':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的广西电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.广西'])
                    if i['m.广西'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-海南':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的海南电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.海南'])
                    if i['m.海南'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-重庆':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的重庆电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.重庆'])
                    if i['m.重庆'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-四川':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的四川电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.四川'])
                    if i['m.四川'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-贵州':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的贵州电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.贵州'])
                    if i['m.贵州'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-云南':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的云南电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.云南'])
                    if i['m.云南'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-西藏':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的西藏电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.西藏'])
                    if i['m.西藏'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-陕西':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的陕西电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.陕西'])
                    if i['m.陕西'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-甘肃':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的甘肃电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.甘肃'])
                    if i['m.甘肃'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-青海':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的青海电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.青海'])
                    if i['m.青海'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-宁夏':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的宁夏电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.宁夏'])
                    if i['m.宁夏'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-14-新疆':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的新疆电力消费是：{1}'.format(i['m.年份'],
                                                            i['m.新疆'])
                    if i['m.新疆'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '能源-15-发电装机容量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的发电装机容量是：{1}'.format(i['m.年份'],
                                                            i['m.发电装机容量'])
                    if i['m.发电装机容量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-15-火电':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的火发电量是：{1}'.format(i['m.年份'],
                                                            i['m.火电'])
                    if i['m.火电'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-15-水电':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的水发电量是：{1}'.format(i['m.年份'],
                                                            i['m.水电'])
                    if i['m.水电'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-15-核电':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的核发电量是：{1}'.format(i['m.年份'],
                                                            i['m.核电'])
                    if i['m.核电'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-15-风电':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的风发电量是：{1}'.format(i['m.年份'],
                                                            i['m.风电'])
                    if i['m.风电'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-15-太阳能发电':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的太阳能发电量是：{1}'.format(i['m.年份'],
                                                            i['m.太阳能发电'])
                    if i['m.太阳能发电'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-15-其他':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的其他是：{1}'.format(i['m.年份'],
                                                            i['m.其他'])
                    if i['m.其他'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #


        elif question_type == '能源-16-国内生产总值能源消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值能源消费量是：{1}'.format(i['m.年份'],
                                                            i['m.国内生产总值能源消费量'])
                    if i['m.国内生产总值能源消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-16-国内生产总值煤炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值煤炭消费量是：{1}'.format(i['m.年份'],
                                                            i['m.国内生产总值煤炭消费量'])
                    if i['m.国内生产总值煤炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-16-国内生产总值焦炭消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值焦炭消费量是：{1}'.format(i['m.年份'],
                                                            i['m.国内生产总值焦炭消费量'])
                    if i['m.国内生产总值焦炭消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-16-国内生产总值石油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值石油消费量是：{1}'.format(i['m.年份'],
                                                            i['m.国内生产总值石油消费量'])
                    if i['m.国内生产总值石油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-16-国内生产总值原油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值原油消费量是：{1}'.format(i['m.年份'],
                                                            i['m.国内生产总值原油消费量'])
                    if i['m.国内生产总值原油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-16-国内生产总值燃料油消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值燃料油消费量是：{1}'.format(i['m.年份'],
                                                            i['m.国内生产总值燃料油消费量'])
                    if i['m.国内生产总值燃料油消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #
        elif question_type == '能源-16-国内生产总值电力消费量':
            l_ = []
            for i in answers:
                if i['m.年份'] not in l_:
                    l_.append(i['m.年份'])
                    final_answer = '{0}的国内生产总值电力消费量是：{1}'.format(i['m.年份'],
                                                            i['m.国内生产总值电力消费量'])
                    if i['m.国内生产总值电力消费量'] == '':
                        print(no_data)
                    else:
                        if final_answer not in lfy_answers:
                           lfy_answers.append(final_answer)
                           #



        Global.lfy_answers=lfy_answers
        return final_answer








        



if __name__ == '__main__':
    searcher = AnswerSearcher()