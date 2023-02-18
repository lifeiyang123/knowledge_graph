# import os
# while 1:
#     a=int(input('请输入一个数字：'))
#     b=int(input('请输入一个数字: '))
#     print(a+b)
#     os.system('pause')
# a=['beijing','shanghai','tianjin']
# print(a[1])
# if __name__ == '__main__':
    # handler = ChatBotGraph()
    # t=0
hanzi = ['全国', '北京', '北京', '天津', '天津', '河北', '河北', '山西', '山西', '内蒙古', '内蒙古', '辽宁', '辽宁',
         '吉林', '吉林', '黑龙江', '黑龙江', '上海', '上海', '江苏', '江苏', '浙江', '浙江', '安徽', '安徽', '福建',
         '福建', '江西', '江西', '山东', '山东', '河南', '河南', '湖北', '湖北', '湖南', '湖南', '广东', '广东', '广西',
         '广西', '海南', '海南',
         '重庆', '重庆', '四川', '四川', '贵州', '贵州', '云南', '云南', '西藏', '西藏', '陕西', '陕西', '甘肃', '甘肃',
         '青海', '青海', '宁夏', '宁夏', '新疆', '新疆', '石家庄',
         '太原', '呼和浩特', '沈阳', '长春', '哈尔滨', '南京', '杭州', '合肥', '福州', '南昌', '济南', '郑州', '武汉',
         '长沙', '广州', '南宁', '海口', '成都', '贵阳', '昆明', '拉萨',
         '西安', '兰州', '西宁', '银川', '乌鲁木齐']
    # pingying=['beijing','tianjin','hebei','shanxi','neimenggu','liaoning','jilin','heilongjiang','shanghai','jiangsu','zhejiang','anhui','fujian','jiangxi','shandong','henan','hubei','hunan','guangdong','guangxi','hainan',
    #        'chongqin','sichuang','guizhou','yunnan','xizang','shanxi','gansu','qinghai','ningxia','xinjiang']
    # print(hanzi[0])
    #测试-start
    # problems=["十面埋伏和功夫的评分","十面埋伏和功夫的上映时间","十面埋伏和功夫的风格","十面埋伏和功夫的简介","十面埋伏和功夫的演员","李连杰和成龙的简介",
    #          "成龙和李连杰和周星驰合作的电影","成龙和李连杰和周星驰总共演了多少的电影","成龙和李连杰合作的电影","周星驰和李连杰的生日是？","我女朋友是谁？"]
    # for id,problem in enumerate(problems):
    #     print("第{0}个问题是{1}：".format(id,problem))
    #     handler.chat_main(problem)
    #     print("\n")
    # print("测试结束")
    # 测试-end
    # while 1:
    #     question = input('咨询:')
    #     for i in pingying:
    #         if i in question:
    #             question = question.replace(i, hanzi[t])
    #             break
    #         t=t+1
    #     print(question)
        # handler.chat_main(question)
    # def cut(s: str):
    #     results = []
    #     num = 0
    #     # x + 1 表示子字符串长度
    #     for x in range(len(s)):
    #         # i 表示偏移量
    #         for i in range(len(s) - x):
    #             results.append(s[i:i + x + 1])
    #     return results
    # def cut2(s: str):
    #     results = []
    #     num = 0
    #
    #     # x + 1 表示子字符串长度
    #     for x in range(len(s)):
    #         # i 表示偏移量
    #         for i in range(len(s) - x):
    #             if x == 0:
    #                 results.append(s[i:i + x + 1])
    #             elif x < 2:
    #                 for j in range(len(s) - x - i):
    #                     results.append(s[i] + s[j + x + i])
    #             else:
    #                 for j in range(len(s) - x - i):
    #                     results.append(s[i:i + x] + s[j + x + i])
    #     # 判断子字符串中能被n整除的个数
    #     # for y in results:
    #     #     if int(y) % int(n) == 0:
    #     #         num = num + 1
    #
    #     return results
    # a=input('请输入:')
    # b=cut2(a)
    # b.reverse()
    # print(b)

