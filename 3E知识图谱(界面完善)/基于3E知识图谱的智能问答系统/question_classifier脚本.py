import os
import ahocorasick

class QuestionClassifier:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        cur_dir='D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/1-资源与环境'
        cur_dir2='D:/知识图谱智能问答/NLP_process-main1/NLP_process-main/基于3E知识图谱的智能问答系统/data/2-国民经济核算'
        #　特征词路径
        #  第一大类——资源与环境
        self.tudi_path_1_1 = os.path.join(cur_dir, '1-土地面积.txt')
        self.heliu_path_1_2= os.path.join(cur_dir,'2-河流面积.txt')
        self.liuyu_path_1_3= os.path.join(cur_dir,'3-流域面积.txt')
        self.kuangchan_path_1_4=os.path.join(cur_dir,'4-矿产产量.txt')
        self.chengwen_path_1_5 = os.path.join(cur_dir, '5-城市温度.txt')
        self.chengshi_path_1_6 = os.path.join(cur_dir, '6-城市湿度.txt')
        self.chengjiang_path_1_7 = os.path.join(cur_dir, '7-城市降水量.txt')
        self.chengri_path_1_8 = os.path.join(cur_dir, '8-城市日照时间数.txt')
        self.dishui_path_1_9 = os.path.join(cur_dir, '9-1-不同地区水资源总量.txt')
        self.nianshui_path_1_9 = os.path.join(cur_dir, '9-不同年份水资源总量.txt')
        self.digong_path_1_10_1 = os.path.join(cur_dir, '10-1-不同地区供水总量.txt')
        self.niangong_path_1_10 = os.path.join(cur_dir, '10-不同年份供水总量.txt')
        self.difei_path_1_11 = os.path.join(cur_dir, '11-不用地区废水污染物含量.txt')
        self.chengfei_path_1_12 = os.path.join(cur_dir, '12-不同城市废水污染物含量.txt')
        self.difei_path_1_13 = os.path.join(cur_dir, '13-不同地区废气污染物含量.txt')
        self.chengfei_path_1_14 = os.path.join(cur_dir, '14-不同城市废气污染物含量.txt')
        self.digu_path_1_15 = os.path.join(cur_dir, '15-不同地区固体废物处理情况.txt')
        self.chenggu_path_1_16 = os.path.join(cur_dir, '16-不同城市固体废物处理情况.txt')
        self.chengkong_path_1_17 = os.path.join(cur_dir, '17-不同城市空气污染物含量.txt')
        self.dila_path_1_18 = os.path.join(cur_dir, '18-不同地区垃圾处理情况.txt')
        self.chengzao_path_1_19 = os.path.join(cur_dir, '19-不同城市噪声污染情况.txt')
        self.digeng_path_1_20 = os.path.join(cur_dir, '20-不同地区耕地面积情况.txt')
        self.diyong_path_1_21 = os.path.join(cur_dir, '21-不同地区用地情况.txt')
        self.disen_path_1_22 = os.path.join(cur_dir, '22-不同地区森林资源情况.txt')
        self.dizao_path_1_23_1 = os.path.join(cur_dir, '23-1-不同地区造林面积.txt')
        self.nianzao_path_1_23 = os.path.join(cur_dir, '23-不同年份造林面积.txt')
        self.dicao_path_1_24 = os.path.join(cur_dir, '24-不同地区草原建设情况.txt')
        self.dizi_path_1_25 = os.path.join(cur_dir, '25-不同地区自然保护情况.txt')
        self.dizi_path_1_26 = os.path.join(cur_dir, '26-不同地区自然灾害情况.txt')
        self.dizhi_path_1_27_1 = os.path.join(cur_dir, '27-1-不同地区地质灾害情况.txt')
        self.nianzhi_path_1_27 = os.path.join(cur_dir, '27-不同年份地质灾害情况.txt')
        self.disen_path_1_28 = os.path.join(cur_dir, '28-不同地区森林火灾情况.txt')
        self.disheng_path_1_29_1 = os.path.join(cur_dir, '29-1-不同地区生物灾害情况.txt')
        self.niansheng_path_1_29 = os.path.join(cur_dir, '29-不同年份生物灾害情况.txt')
        self.ditu_path_1_30 = os.path.join(cur_dir, '30-不同地区突发环境事件次数.txt')
        self.dizheng_path_1_31_1 = os.path.join(cur_dir, '31-1-不同地区地震情况.txt')
        self.nianzheng_path_1_31 = os.path.join(cur_dir, '31-不同年份地震情况.txt')
        self.haizai_path_1_32 = os.path.join(cur_dir, '32-海洋灾害情况.txt')
        self.haizhi_path_1_33 = os.path.join(cur_dir, '33-海域不同水质面积.txt')
        self.diji_path_1_34 = os.path.join(cur_dir, '34-不同地区基础建设投资.txt')
        self.diwu_path_1_35_1 = os.path.join(cur_dir, '35-1-不同地区污染治理情况.txt')
        self.nianwu_path_1_35 = os.path.join(cur_dir, '35-不同年份污染治理情况.txt')
        self.lintou_path_1_36 = os.path.join(cur_dir, '36-林业草原投资完成情况.txt')

        #  第二大类——国民经济核算
        self.guosheng_path_2_1 = os.path.join(cur_dir2, 'C03-01国民生产总值.txt')
        self.guoshenggou_path_2_2 = os.path.join(cur_dir2, 'C03-02国内生产总值构成.txt')

        # 加载特征词
        self.tudi_wds_1_1= [i.strip() for i in open(self.tudi_path_1_1,encoding="utf-8") if i.strip()]#encoding="utf-8"
        self.heliu_wds_1_2 = [i.strip() for i in open(self.heliu_path_1_2, encoding="utf-8") if i.strip()]
        self.liuyu_wds_1_3 = [i.strip() for i in open(self.liuyu_path_1_3, encoding="utf-8") if i.strip()]
        self.kuangchan_wds_1_4 = [i.strip() for i in open(self.kuangchan_path_1_4, encoding="utf-8") if i.strip()]
        self.chengwen_wds_1_5 = [i.strip() for i in open(self.chengwen_path_1_5, encoding="utf-8") if i.strip()]
        self.chengshi_wds_1_6 = [i.strip() for i in open(self.chengshi_path_1_6, encoding="utf-8") if i.strip()]
        self.chengjiang_wds_1_7 = [i.strip() for i in open(self.chengjiang_path_1_7, encoding="utf-8") if i.strip()]
        self.chengri_wds_1_8 = [i.strip() for i in open(self.chengri_path_1_8, encoding="utf-8") if i.strip()]
        self.dishui_wds_1_9 = [i.strip() for i in open(self.dishui_path_1_9, encoding="utf-8") if i.strip()]
        self.nianshui_wds_1_9 = [i.strip() for i in open(self.nianshui_path_1_9, encoding="utf-8") if i.strip()]
        self.digong_wds_1_10 = [i.strip() for i in open(self.digong_path_1_10_1, encoding="utf-8") if i.strip()]
        self.niangong_wds_1_10 = [i.strip() for i in open(self.niangong_path_1_10, encoding="utf-8") if i.strip()]
        self.difei_wds_1_11 = [i.strip() for i in open(self.difei_path_1_11, encoding="utf-8") if i.strip()]
        self.chengfei_wds_1_12 = [i.strip() for i in open(self.chengfei_path_1_12, encoding="utf-8") if i.strip()]
        self.difei_wds_1_13 = [i.strip() for i in open(self.difei_path_1_13, encoding="utf-8") if i.strip()]
        self.chengfei_wds_1_14 = [i.strip() for i in open(self.chengfei_path_1_14, encoding="utf-8") if i.strip()]
        self.digu_wds_1_15 = [i.strip() for i in open(self.digu_path_1_15, encoding="utf-8") if i.strip()]
        self.chenggu_wds_1_16 = [i.strip() for i in open(self.chenggu_path_1_16, encoding="utf-8") if i.strip()]
        self.chengkong_wds_1_17 = [i.strip() for i in open(self.chengkong_path_1_17, encoding="utf-8") if i.strip()]
        self.dila_wds_1_18 = [i.strip() for i in open(self.dila_path_1_18, encoding="utf-8") if i.strip()]
        self.chengzao_wds_1_19 = [i.strip() for i in open(self.chengzao_path_1_19, encoding="utf-8") if i.strip()]
        self.digeng_wds_1_20 = [i.strip() for i in open(self.digeng_path_1_20, encoding="utf-8") if i.strip()]
        self.diyong_wds_1_21 = [i.strip() for i in open(self.diyong_path_1_21, encoding="utf-8") if i.strip()]
        self.disen_wds_1_22 = [i.strip() for i in open(self.disen_path_1_22, encoding="utf-8") if i.strip()]
        self.dizao_wds_1_23_1 = [i.strip() for i in open(self.dizao_path_1_23_1, encoding="utf-8") if i.strip()]
        self.nianzao_wds_1_23 = [i.strip() for i in open(self.nianzao_path_1_23, encoding="utf-8") if i.strip()]
        self.dicao_wds_1_24 = [i.strip() for i in open(self.dicao_path_1_24, encoding="utf-8") if i.strip()]
        self.dizi_wds_1_25 = [i.strip() for i in open(self.dizi_path_1_25, encoding="utf-8") if i.strip()]
        self.dizi_wds_1_26 = [i.strip() for i in open(self.dizi_path_1_26, encoding="utf-8") if i.strip()]
        self.dizhi_wds_1_27_1 = [i.strip() for i in open(self.dizhi_path_1_27_1, encoding="utf-8") if i.strip()]
        self.nianzhi_wds_1_27 = [i.strip() for i in open(self.nianzhi_path_1_27, encoding="utf-8") if i.strip()]
        self.disen_wds_1_28 = [i.strip() for i in open(self.disen_path_1_28, encoding="utf-8") if i.strip()]
        self.disheng_wds_1_29_1 = [i.strip() for i in open(self.disheng_path_1_29_1, encoding="utf-8") if i.strip()]
        self.niansheng_wds_1_29 = [i.strip() for i in open(self.niansheng_path_1_29, encoding="utf-8") if i.strip()]
        self.ditu_wds_1_30 = [i.strip() for i in open(self.ditu_path_1_30, encoding="utf-8") if i.strip()]
        self.dizheng_wds_1_31_1 = [i.strip() for i in open(self.dizheng_path_1_31_1, encoding="utf-8") if i.strip()]
        self.nianzheng_wds_1_31 = [i.strip() for i in open(self.nianzheng_path_1_31, encoding="utf-8") if i.strip()]
        self.haizai_wds_1_32 = [i.strip() for i in open(self.haizai_path_1_32, encoding="utf-8") if i.strip()]
        self.haizhi_wds_1_33 = [i.strip() for i in open(self.haizhi_path_1_33, encoding="utf-8") if i.strip()]
        self.diji_wds_1_34 = [i.strip() for i in open(self.diji_path_1_34, encoding="utf-8") if i.strip()]
        self.diwu_wds_1_35_1 = [i.strip() for i in open(self.diwu_path_1_35_1, encoding="utf-8") if i.strip()]
        self.nianwu_wds_1_35 = [i.strip() for i in open(self.nianwu_path_1_35, encoding="utf-8") if i.strip()]
        self.lintou_wds_1_36 = [i.strip() for i in open(self.lintou_path_1_36, encoding="utf-8") if i.strip()]

        self.guosheng_wds_2_1 = [i.strip() for i in open(self.guosheng_path_2_1, encoding="utf-8") if i.strip()]
        self.guoshenggou_wds_2_2 = [i.strip() for i in open(self.guoshenggou_path_2_2, encoding="utf-8") if i.strip()]
        self.region_words = set(
            self.tudi_wds_1_1+self.heliu_wds_1_2+self.liuyu_wds_1_3 +self.kuangchan_wds_1_4+self.chengwen_wds_1_5+self.chengshi_wds_1_6+self.chengjiang_wds_1_7
            +self.chengri_wds_1_8+self.dishui_wds_1_9+self.nianshui_wds_1_9+self.digong_wds_1_10+self.niangong_wds_1_10+self.difei_wds_1_11
            +self.chengfei_wds_1_12+self.difei_wds_1_13+self.chengfei_wds_1_14+self.digu_wds_1_15+self.chenggu_wds_1_16+self.chengkong_wds_1_17
            +self.dila_wds_1_18+self.chengzao_wds_1_19+self.digeng_wds_1_20+self.diyong_wds_1_21+self.disen_wds_1_22+self.dizao_wds_1_23_1
            +self.nianzao_wds_1_23+self.dicao_wds_1_24+self.dizi_wds_1_25+self.dizi_wds_1_26+self.dizhi_wds_1_27_1+self.nianzhi_wds_1_27+self.disen_wds_1_28
            +self.disheng_wds_1_29_1+self.niansheng_wds_1_29+self.ditu_wds_1_30+self.dizheng_wds_1_31_1+self.nianzheng_wds_1_31+self.haizai_wds_1_32
            +self.haizhi_wds_1_33+self.diji_wds_1_34+self.diwu_wds_1_35_1+self.nianwu_wds_1_35+self.lintou_wds_1_36+self.guosheng_wds_2_1+self.guoshenggou_wds_2_2
        )

        # 构造领域actree
        self.region_tree = self.build_actree(list(self.region_words))
        # 构建词典
        self.wdtype_dict = self.build_wdtype_dict()

        #  第一大类——资源与环境
        # 1-土地面积
        self.q1_qwds_1_1 = ['面积']
        # 2-河流面积
        self.q1_qwds_1_2 = ['流域面积']
        self.q2_qwds_1_2 = ['河长']
        self.q3_qwds_1_2 =['年径流量']
        # 3-流域面积
        self.q1_qwds_1_3 = ['流域面积']
        self.q2_qwds_1_3 = ['面积占比']
        # 4-矿产产量
        self.q1_qwds_1_4 = ['2020年产量']
        self.q2_qwds_1_4 = ['2021年产量']
        # 5-城市温度
        self.q1_qwds_1_5 = ['1月温度']
        self.q2_qwds_1_5 = ['2月温度']
        self.q3_qwds_1_5 = ['3月温度']
        self.q4_qwds_1_5 = ['4月温度']
        self.q5_qwds_1_5 = ['5月温度']
        self.q6_qwds_1_5 = ['6月温度']
        self.q7_qwds_1_5 = ['7月温度']
        self.q8_qwds_1_5 = ['8月温度']
        self.q9_qwds_1_5 = ['9月温度']
        self.q10_qwds_1_5 = ['10月温度']
        self.q11_qwds_1_5 = ['11月温度']
        self.q12_qwds_1_5 = ['12月温度']
        self.q13_qwds_1_5 = ['年平均温度']
        # 6-城市湿度
        self.q1_qwds_1_6 = ['1月湿度']
        self.q2_qwds_1_6 = ['2月湿度']
        self.q3_qwds_1_6 = ['3月湿度']
        self.q4_qwds_1_6 = ['4月湿度']
        self.q5_qwds_1_6 = ['5月湿度']
        self.q6_qwds_1_6 = ['6月湿度']
        self.q7_qwds_1_6 = ['7月湿度']
        self.q8_qwds_1_6 = ['8月湿度']
        self.q9_qwds_1_6 = ['9月湿度']
        self.q10_qwds_1_6 = ['10月湿度']
        self.q11_qwds_1_6 = ['11月湿度']
        self.q12_qwds_1_6 = ['12月湿度']
        self.q13_qwds_1_6 = ['年平均湿度']
        # 7-城市降水量

        self.q1_qwds_1_7 = ['1月降水量']
        self.q2_qwds_1_7 = ['2月降水量']
        self.q3_qwds_1_7 = ['3月降水量']
        self.q4_qwds_1_7 = ['4月降水量']
        self.q5_qwds_1_7 = ['5月降水量']
        self.q6_qwds_1_7 = ['6月降水量']
        self.q7_qwds_1_7 = ['7月降水量']
        self.q8_qwds_1_7 = ['8月降水量']
        self.q9_qwds_1_7 = ['9月降水量']
        self.q10_qwds_1_7 = ['10月降水量']
        self.q11_qwds_1_7 = ['11月降水量']
        self.q12_qwds_1_7 = ['12月降水量']
        self.q13_qwds_1_7 = ['全年降水量']

        # 8-城市日照时间数
        self.q1_qwds_1_8 = ['1月日照时数']
        self.q2_qwds_1_8 = ['2月日照时数']
        self.q3_qwds_1_8 = ['3月日照时数']
        self.q4_qwds_1_8 = ['4月日照时数']
        self.q5_qwds_1_8 = ['5月日照时数']
        self.q6_qwds_1_8 = ['6月日照时数']
        self.q7_qwds_1_8 = ['7月日照时数']
        self.q8_qwds_1_8 = ['8月日照时数']
        self.q9_qwds_1_8 = ['9月日照时数']
        self.q10_qwds_1_8 = ['10月日照时数']
        self.q11_qwds_1_8 = ['11月日照时数']
        self.q12_qwds_1_8 = ['12月日照时数']
        self.q13_qwds_1_8 = ['全年日照时数']
        # 9-1-不同地区水资源总量
        self.q1_qwds_1_9 = ['水资源总量']
        self.q2_qwds_1_9 = ['地表水资源量']
        self.q3_qwds_1_9 = ['地下水资源量']
        self.q4_qwds_1_9 = ['地表水与地下水资源重复量']
        self.q5_qwds_1_9 = ['人均水资源量']
        print('model init finished ......')
        # 9-不同年份水资源总量
        self.q1_qwds_1_9_1 = ['水资源总量']
        self.q2_qwds_1_9_1 = ['地表水资源量']
        self.q3_qwds_1_9_1 = ['地下水资源量']
        self.q4_qwds_1_9_1 = ['地表水与地下水资源重复量']
        self.q5_qwds_1_9_1 = ['人均水资源量']

        # 10-1-不同地区供水总量
        self.q1_qwds_1_10_1 = ['供水总量']
        self.q2_qwds_1_10_1 = ['地表水供水量']
        self.q3_qwds_1_10_1 = ['地下水供水量']
        self.q4_qwds_1_10_1 = ['其他供水量']
        self.q5_qwds_1_10_1 = ['用水总量']
        self.q6_qwds_1_10_1 = ['农业用水量']
        self.q7_qwds_1_10_1 = ['工业用水量']
        self.q8_qwds_1_10_1 = ['生活用水量']
        self.q9_qwds_1_10_1 = ['人工生态环境补水用水量']
        self.q10_qwds_1_10_1 = ['人均用水量']

        # 10-不同年份供水总量
        self.q1_qwds_1_10 = ['供水总量']
        self.q2_qwds_1_10 = ['地表水供水量']
        self.q3_qwds_1_10 = ['地下水供水量']
        self.q4_qwds_1_10 = ['其他供水量']
        self.q5_qwds_1_10 = ['用水总量']
        self.q6_qwds_1_10 = ['农业用水量']
        self.q7_qwds_1_10 = ['工业用水量']
        self.q8_qwds_1_10 = ['生活用水量']
        self.q9_qwds_1_10 = ['人工生态环境补水用水量']
        self.q10_qwds_1_10 = ['人均用水量']

        # 11-不用地区废水污染物含量
        self.q1_qwds_1_11 = ['废水中化学需氧量排放量']
        self.q2_qwds_1_11 = ['废水中氨氮排放量']
        self.q3_qwds_1_11 = ['废水中总氮排放量']
        self.q4_qwds_1_11 = ['废水中总磷排放量']
        self.q5_qwds_1_11 = ['废水中石油类排放量']
        self.q6_qwds_1_11 = ['废水中挥发酚排放量']
        self.q7_qwds_1_11 = ['废水中总铅排放量']
        self.q8_qwds_1_11 = ['废水中总汞排放量']
        self.q9_qwds_1_11 = ['废水中总镉排放量']
        self.q10_qwds_1_11 = ['废水中六价铬排放量']
        self.q11_qwds_1_11 = ['废水中总铬排放量']
        self.q12_qwds_1_11 = ['废水中总砷排放量']

        # 12-不同城市废水污染物含量
        self.q1_qwds_1_12 = ['城市废水中工业化学需氧量排放量']
        self.q2_qwds_1_12 = ['城市废水中工业氨氮排放量']
        self.q3_qwds_1_12 = ['城市废水中生活化学需氧量排放量']
        self.q4_qwds_1_12 = ['城市废水中生活氨氮排放量']

        # 13-不同地区废气污染物含量
        self.q1_qwds_1_13 = ['二氧化硫排放量']
        self.q2_qwds_1_13 = ['氮氧化物排放量']
        self.q3_qwds_1_13 = ['颗粒物排放量']

        # 14-不同城市废气污染物含量
        self.q1_qwds_1_14 = ['工业二氧化硫排放量']
        self.q2_qwds_1_14 = ['工业氮氧化物排放量']
        self.q3_qwds_1_14 = ['工业颗粒物排放量']
        self.q4_qwds_1_14 = ['生活及其他二氧化硫排放量']
        self.q5_qwds_1_14 = ['生活及其他氮氧化物排放量']
        self.q6_qwds_1_14 = ['生活及其他颗粒物排放量']

        # 15-不同地区固体废物处理情况
        self.q1_qwds_1_15 = ['一般工业固体废物产生量']
        self.q2_qwds_1_15 = ['一般工业固体废物综合利用量']
        self.q3_qwds_1_15 = ['一般工业固体废物处置量']
        self.q4_qwds_1_15 = ['一般工业固体废物贮存量']
        self.q5_qwds_1_15 = ['一般工业固体废物倾倒丢弃量']
        self.q6_qwds_1_15 = ['危险废物产生量']
        self.q7_qwds_1_15 = ['危险废物利用处置量']
        self.q8_qwds_1_15 = ['危险废物本年末贮存量']

        # 16-不同城市固体废物处理情况
        self.q1_qwds_1_16 = ['一般工业固体废物产生量']
        self.q2_qwds_1_16 = ['一般工业固体废物综合利用量']
        self.q3_qwds_1_16 = ['一般工业固体废物处置量']
        self.q4_qwds_1_16 = ['一般工业固体废物贮存量']

        # 17-不同城市空气污染物含量
        self.q1_qwds_1_17 = ['二氧化硫年平均浓度']
        self.q2_qwds_1_17 = ['二氧化氮年平均浓度']
        self.q3_qwds_1_17 = ['可吸入颗粒物年平均浓度']
        self.q4_qwds_1_17 = ['一氧化碳日均值第95百分位浓度']
        self.q5_qwds_1_17 = ['臭氧日最大8小时第90百分位浓度']
        self.q6_qwds_1_17 = ['细颗粒物年平均浓度']
        self.q7_qwds_1_17 = ['空气质量优良天数比例']

        # 18-不同地区垃圾处理情况
        self.q1_qwds_1_18 = ['生活垃圾清运量']
        self.q2_qwds_1_18 = ['无害化处理厂数']
        self.q3_qwds_1_18 = ['卫生填埋厂数']
        self.q4_qwds_1_18 = ['焚烧厂数']
        self.q5_qwds_1_18 = ['其他厂数']
        self.q6_qwds_1_18 = ['无害化处理能力']
        self.q7_qwds_1_18 = ['卫生填埋处理能力']
        self.q8_qwds_1_18 = ['焚烧处理能力']
        self.q9_qwds_1_18 = ['其他处理能力']
        self.q10_qwds_1_18 = ['无害化处理量']
        self.q11_qwds_1_18 = ['卫生填埋处理量']
        self.q12_qwds_1_18 = ['焚烧处理量']
        self.q13_qwds_1_18 = ['其他处理量']
        self.q14_qwds_1_18 = ['生活垃圾无害化处理率']

        # 19-不同城市噪声污染情况
        self.q1_qwds_1_19 = ['道路交通噪声等效声级']
        self.q2_qwds_1_19 = ['区域环境噪声等效声级']

        # 20-不同地区耕地面积情况
        self.q1_qwds_1_20 = ['2013年的耕地面积']
        self.q2_qwds_1_20 = ['2014年的耕地面积']
        self.q3_qwds_1_20 = ['2015年的耕地面积']
        self.q4_qwds_1_20 = ['2016年的耕地面积']
        self.q5_qwds_1_20 = ['2017年的耕地面积']
        self.q6_qwds_1_20 = ['2019年的耕地面积']

        # 21-不同地区用地情况
        self.q1_qwds_1_21 = ['耕地']
        self.q2_qwds_1_21 = ['园地']
        self.q3_qwds_1_21 = ['林地']
        self.q4_qwds_1_21 = ['草地']
        self.q5_qwds_1_21 = ['湿地']
        self.q6_qwds_1_21 = ['城镇村及工矿用地']
        self.q7_qwds_1_21 = ['交通运输用地']
        self.q8_qwds_1_21 = ['水域及水利设施用地']

        # 22-不同地区森林资源情况
        self.q1_qwds_1_22 = ['林业用地面积']
        self.q2_qwds_1_22 = ['森林面积']
        self.q3_qwds_1_22 = ['人工林']
        self.q4_qwds_1_22 = ['森林覆盖率']
        self.q5_qwds_1_22 = ['活立木总蓄积量']
        self.q6_qwds_1_22 = ['森林蓄积量']

        # 23-1-不同地区造林面积
        self.q1_qwds_1_23_1 = ['造林总面积']
        self.q2_qwds_1_23_1 = ['人工造林面积']
        self.q3_qwds_1_23_1 = ['飞播造林面积']
        self.q4_qwds_1_23_1 = ['封山育林面积']
        self.q5_qwds_1_23_1 = ['退化林修复面积']
        self.q6_qwds_1_23_1 = ['人工更新面积']

        # 23-不同年份造林面积
        self.q1_qwds_1_23 = ['造林总面积']
        self.q2_qwds_1_23 = ['人工造林面积']
        self.q3_qwds_1_23 = ['飞播造林面积']
        self.q4_qwds_1_23 = ['封山育林面积']
        self.q5_qwds_1_23 = ['退化林修复面积']
        self.q6_qwds_1_23 = ['人工更新面积']

        # 24-不同地区草原建设情况
        self.q1_qwds_1_24 = ['种草面积']
        self.q2_qwds_1_24 = ['草原改良面积']
        self.q3_qwds_1_24 = ['草原鼠害发生面积']
        self.q4_qwds_1_24 = ['草原鼠害防治面积']
        self.q5_qwds_1_24 = ['草原虫害发生面积']
        self.q6_qwds_1_24 = ['草原虫害防治面积']
        self.q7_qwds_1_24 = ['草原火灾受害面积']

        # 25-不同地区自然保护情况
        self.q1_qwds_1_25 = ['国家级自然保护区个数']
        self.q2_qwds_1_25 = ['国家级自然保护区面积']

        # 26-不同地区自然灾害情况
        self.q1_qwds_1_26 = ['农作物受灾面积合计']
        self.q2_qwds_1_26 = ['农作物绝收面积合计']
        self.q3_qwds_1_26 = ['旱灾受灾面积']
        self.q4_qwds_1_26 = ['旱灾绝收面积']
        self.q5_qwds_1_26 = ['洪涝地质灾害和台风受灾面积']
        self.q6_qwds_1_26 = ['洪涝地质灾害和台风绝收面积']
        self.q7_qwds_1_26 = ['风雹灾害受灾面积']
        self.q8_qwds_1_26 = ['风雹灾害绝收面积']
        self.q9_qwds_1_26 = ['低温冷冻和雪灾受灾面积']
        self.q10_qwds_1_26 = ['低温冷冻和雪灾绝收面积']
        self.q11_qwds_1_26 = ['受灾人口']
        self.q12_qwds_1_26 = ['死亡人口']
        self.q13_qwds_1_26 = ['自然灾害导致的直接经济损失']

        # 27-1-不同地区地质灾害情况
        self.q1_qwds_1_27_1 = ['发生地质灾害数量']
        self.q2_qwds_1_27_1 = ['滑坡次数']
        self.q3_qwds_1_27_1 = ['崩塌次数']
        self.q4_qwds_1_27_1 = ['泥石流次数']
        self.q5_qwds_1_27_1 = ['地面塌陷次数']
        self.q6_qwds_1_27_1 = ['地质灾害导致的人员伤亡数量']
        self.q7_qwds_1_27_1 = ['地质灾害导致的死亡人数']
        self.q8_qwds_1_27_1 = ['地质灾害导致的直接经济损失']

        # 27-不同年份地质灾害情况
        self.q1_qwds_1_27 = ['发生地质灾害数量']
        self.q2_qwds_1_27 = ['滑坡次数']
        self.q3_qwds_1_27 = ['崩塌次数']
        self.q4_qwds_1_27 = ['泥石流次数']
        self.q5_qwds_1_27 = ['地面塌陷次数']
        self.q6_qwds_1_27 = ['地质灾害导致的人员伤亡数量']
        self.q7_qwds_1_27 = ['地质灾害导致的死亡人数']
        self.q8_qwds_1_27 = ['地质灾害导致的直接经济损失']

        # 28-不同地区森林火灾情况
        self.q1_qwds_1_28 = ['森林火灾次数']
        self.q2_qwds_1_28 = ['一般火灾次数']
        self.q3_qwds_1_28 = ['较大火灾次数']
        self.q4_qwds_1_28 = ['重大火灾次数']
        self.q5_qwds_1_28 = ['特别重大火灾次数']
        self.q6_qwds_1_28 = ['火场总面积']
        self.q7_qwds_1_28 = ['受害森林面积']
        self.q8_qwds_1_28 = ['伤亡人数']
        self.q9_qwds_1_28 = ['其它损失折款']

        # 29-1-不同地区生物灾害情况
        self.q1_qwds_1_29_1 = ['林业有害生物发生面积']
        self.q2_qwds_1_29_1 = ['林业有害生物防治面积']
        self.q3_qwds_1_29_1 = ['林业有害生物防治率']
        self.q4_qwds_1_29_1 = ['森林病害发生面积']
        self.q5_qwds_1_29_1 = ['森林病害防治面积']
        self.q6_qwds_1_29_1 = ['森林虫害发生面积']
        self.q7_qwds_1_29_1 = ['森林虫害防治面积']
        self.q8_qwds_1_29_1 = ['森林鼠害发生面积']
        self.q9_qwds_1_29_1 = ['森林鼠害防治面积']
        self.q10_qwds_1_29_1 = ['有害植物发生面积']
        self.q11_qwds_1_29_1 = ['有害植物防治面积']

        # 29-不同年份生物灾害情况
        self.q1_qwds_1_29 = ['林业有害生物发生面积']
        self.q2_qwds_1_29 = ['林业有害生物防治面积']
        self.q3_qwds_1_29 = ['林业有害生物防治率']
        self.q4_qwds_1_29 = ['森林病害发生面积']
        self.q5_qwds_1_29 = ['森林病害防治面积']
        self.q6_qwds_1_29 = ['森林虫害发生面积']
        self.q7_qwds_1_29 = ['森林虫害防治面积']
        self.q8_qwds_1_29 = ['森林鼠害发生面积']
        self.q9_qwds_1_29 = ['森林鼠害防治面积']
        self.q10_qwds_1_29 = ['有害植物发生面积']
        self.q11_qwds_1_29 = ['有害植物防治面积']

        # 30-不同地区突发环境事件次数
        self.q1_qwds_1_30 = ['突发环境事件次数']
        self.q2_qwds_1_30 = ['特别重大环境事件次数']
        self.q3_qwds_1_30 = ['重大环境事件次数']
        self.q4_qwds_1_30 = ['较大环境事件次数']
        self.q5_qwds_1_30 = ['一般环境事件次数']

        #31-1-不同地区地震情况
        self.q1_qwds_1_31_1 = ['地震次数']
        self.q2_qwds_1_31_1 = ['5.0-5.9级地震次数']
        self.q3_qwds_1_31_1 = ['6.0-6.9级地震次数']
        self.q4_qwds_1_31_1 = ['7.0级以上地震次数']
        self.q5_qwds_1_31_1 = ['地震导致的人员伤亡数量']
        self.q6_qwds_1_31_1 = ['地震导致的死亡人数']
        self.q7_qwds_1_31_1 = ['地震导致的直接经济损失']
        # 31-不同年份地震情况
        self.q1_qwds_1_31 = ['地震次数']
        self.q2_qwds_1_31 = ['5.0-5.9级地震次数']
        self.q3_qwds_1_31 = ['6.0-6.9级地震次数']
        self.q4_qwds_1_31 = ['7.0级以上地震次数']
        self.q5_qwds_1_31 = ['地震导致的人员伤亡数量']
        self.q6_qwds_1_31 = ['地震导致的死亡人数']
        self.q7_qwds_1_31 = ['地震导致的直接经济损失']

        # 32-海洋灾害情况
        self.q1_qwds_1_32 = ['发生次数']
        self.q2_qwds_1_32 = ['人员死亡失踪']
        self.q3_qwds_1_32 = ['直接经济损失']

        # 33-海域不同水质面积
        self.q1_qwds_1_33 = ['第二类水质海域面积']
        self.q2_qwds_1_33 = ['第三类水质海域面积']
        self.q3_qwds_1_33 = ['第四类水质海域面积']
        self.q4_qwds_1_33 = ['劣于第四类水质海域面积']

        # 34-不同地区基础建设投资
        self.q1_qwds_1_34 = ['城镇环境基础设施建设投资']
        self.q2_qwds_1_34 = ['燃气建设投资']
        self.q3_qwds_1_34 = ['集中供热建设投资']
        self.q4_qwds_1_34 = ['排水建设投资']
        self.q5_qwds_1_34 = ['园林绿化建设投资']
        self.q6_qwds_1_34 = ['市容环境卫生建设投资']

        # 35-1-不同地区污染治理情况
        self.q1_qwds_1_35_1 = ['工业污染治理完成投资']
        self.q2_qwds_1_35_1 = ['治理废水投资']
        self.q3_qwds_1_35_1 = ['治理废气投资']
        self.q4_qwds_1_35_1 = ['治理固体废物投资']
        self.q5_qwds_1_35_1 = ['治理噪声投资']
        self.q6_qwds_1_35_1 = ['治理其他投资']

        # 35-不同年份污染治理情况
        self.q1_qwds_1_35 = ['工业污染治理完成投资']
        self.q2_qwds_1_35 = ['治理废水投资']
        self.q3_qwds_1_35 = ['治理废气投资']
        self.q4_qwds_1_35 = ['治理固体废物投资']
        self.q5_qwds_1_35 = ['治理噪声投资']
        self.q6_qwds_1_35 = ['治理其他投资']

        # 36-林业草原投资完成情况
        self.q1_qwds_1_36 = ['本年完成林业草原投资总计']
        self.q2_qwds_1_36 = ['林业草原国家投资']
        self.q3_qwds_1_36 = ['林业草原生态修复治理投资']
        self.q4_qwds_1_36 = ['林业草原林产品加工制造投资']
        self.q5_qwds_1_36 = ['林业草原林业草原服务保障和公共管理投资']

        #  第二大类——国民经济核算
        # C03-01国民生产总值
        self.q1_qwds_2_1 = ['国民总收入']
        self.q2_qwds_2_1 = ['国内生产总值']
        self.q3_qwds_2_1 = ['第一产业']
        self.q4_qwds_2_1 = ['第二产业']
        self.q5_qwds_2_1 = ['第三产业']
        self.q6_qwds_2_1 = ['农林牧渔业']
        self.q7_qwds_2_1 = ['工业']
        self.q8_qwds_2_1 = ['建筑业']
        self.q9_qwds_2_1 = ['批发和零售业']
        self.q10_qwds_2_1 = ['交通运输仓储和邮政业']
        self.q11_qwds_2_1 = ['住宿和餐饮业']
        self.q12_qwds_2_1 = ['金融业']
        self.q13_qwds_2_1 = ['房地产业']
        self.q14_qwds_2_1 = ['其他']
        self.q15_qwds_2_1 = ['人均国民总收入']
        self.q16_qwds_2_1 = ['人均国内生产总值']

        # C03-02国内生产总值构成
        self.q1_qwds_2_2 = ['国内生产总值的占比']
        self.q2_qwds_2_2 = ['第一产业的占比']
        self.q3_qwds_2_2 = ['第二产业的占比']
        self.q4_qwds_2_2 = ['第三产业的占比']
        self.q5_qwds_2_2 = ['农林牧渔业的占比']
        self.q6_qwds_2_2 = ['工业的占比']
        self.q7_qwds_2_2 = ['建筑业的占比']
        self.q8_qwds_2_2 = ['批发和零售业的占比']
        self.q9_qwds_2_2 = ['交通运输仓储和邮政业的占比']
        self.q10_qwds_2_2 = ['住宿和餐饮业的占比']
        self.q11_qwds_2_2 = ['金融业的占比']
        self.q12_qwds_2_2 = ['房地产业的占比']
        self.q13_qwds_2_2 = ['其他的占比']

        return

    '''分类主函数'''
    def classify(self, question):
        data = {}
        medical_dict = self.check_medical(question)
        if not medical_dict:
            return {}
        data['args'] = medical_dict
        #收集问句当中所涉及到的实体类型
        types = []
        for type_ in medical_dict.values():
            types += type_
        question_type = 'others'

        question_types = []

        #  第一大类——资源与环境
        if self.check_words(self.q1_qwds_1_20, question) and ('20-不同地区耕地面积情况' in types):
            question_type = '资源与环境-20-2013耕地面积'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_20, question) and ('20-不同地区耕地面积情况' in types):
            question_type = '资源与环境-20-2014耕地面积'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_20, question) and ('20-不同地区耕地面积情况' in types):
            question_type = '资源与环境-20-2015耕地面积'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_20, question) and ('20-不同地区耕地面积情况' in types):
            question_type = '资源与环境-20-2016耕地面积'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_20, question) and ('20-不同地区耕地面积情况' in types):
            question_type = '资源与环境-20-2017耕地面积'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_20, question) and ('20-不同地区耕地面积情况' in types):
            question_type = '资源与环境-20-2019耕地面积'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_1, question) and ('1-土地面积' in types):
            question_type = '资源与环境-1-面积'
            question_types.append(question_type)
        elif self.check_words(self.q1_qwds_1_2, question) and ('2-河流面积' in types):
            question_type = '资源与环境-2-流域面积'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_2, question) and ('2-河流面积' in types):
            question_type = '资源与环境-2-河长'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_2, question) and ('2-河流面积' in types):
            question_type = '资源与环境-2-年径流量'
            question_types.append(question_type)
        elif self.check_words(self.q1_qwds_1_3, question) and ('3-流域面积' in types):
            question_type = '资源与环境-3-流域面积'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_3, question) and ('3-流域面积' in types):
            question_type = '资源与环境-3-面积占比'
            question_types.append(question_type)
        elif self.check_words(self.q1_qwds_1_4, question) and ('4-矿产产量' in types):
            question_type = '资源与环境-4-2020年产量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_4, question) and ('4-矿产产量' in types):
            question_type = '资源与环境-4-2021年产量'
            question_types.append(question_type)
        elif self.check_words(self.q11_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-11月温度'
            question_types.append(question_type)
        elif self.check_words(self.q12_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-12月温度'
            question_types.append(question_type)
        elif self.check_words(self.q1_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-1月温度'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-2月温度'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-3月温度'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-4月温度'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-5月温度'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-6月温度'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-7月温度'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-8月温度'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-9月温度'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-10月温度'
            question_types.append(question_type)
        elif self.check_words(self.q13_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-年平均温度'
            question_types.append(question_type)


        elif self.check_words(self.q11_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-11月湿度'
            question_types.append(question_type)
        elif self.check_words(self.q12_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-12月湿度'
            question_types.append(question_type)
        elif self.check_words(self.q1_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-1月湿度'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-2月湿度'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-3月湿度'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-4月湿度'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-5月湿度'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-6月湿度'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-7月湿度'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-8月湿度'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-9月湿度'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-10月湿度'
            question_types.append(question_type)

        elif self.check_words(self.q13_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-年平均湿度'
            question_types.append(question_type)


        elif self.check_words(self.q11_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-11月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q12_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-12月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q1_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-1月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-2月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-3月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-4月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-5月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-6月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-7月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-8月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-9月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-10月降水量'
            question_types.append(question_type)
        elif self.check_words(self.q13_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-全年降水量'
            question_types.append(question_type)

        elif self.check_words(self.q11_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-11月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q12_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-12月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q1_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-1月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-2月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-3月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-4月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-5月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-6月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-7月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-8月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-9月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-10月日照时数'
            question_types.append(question_type)
        elif self.check_words(self.q13_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-全年日照时数'
            question_types.append(question_type)

        elif self.check_words(self.q1_qwds_1_9, question) and ('9-1-不同地区水资源总量' in types):
            question_type = '资源与环境-9-水资源总量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_9, question) and ('9-1-不同地区水资源总量' in types):
            question_type = '资源与环境-9-地表水资源量'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_9, question) and ('9-1-不同地区水资源总量' in types):
            question_type = '资源与环境-9-地下水资源量'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_9, question) and ('9-1-不同地区水资源总量' in types):
            question_type = '资源与环境-9-地表水与地下水资源重复量'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_9, question) and ('9-1-不同地区水资源总量' in types):
            question_type = '资源与环境-9-人均水资源量'
            question_types.append(question_type)

        elif self.check_words(self.q1_qwds_1_9_1, question) and ('9-不同年份水资源总量' in types):
            question_type = '资源与环境-9-1-水资源总量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_9_1, question) and ('9-不同年份水资源总量' in types):
            question_type = '资源与环境-9-1-地表水资源量'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_9_1, question) and ('9-不同年份水资源总量' in types):
            question_type = '资源与环境-9-1-地下水资源量'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_9_1, question) and ('9-不同年份水资源总量' in types):
            question_type = '资源与环境-9-1-地表水与地下水资源重复量'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_9_1, question) and ('9-不同年份水资源总量' in types):
            question_type = '资源与环境-9-1-人均水资源量'
            question_types.append(question_type)

        elif self.check_words(self.q1_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-供水总量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-地表水供水量'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-地下水供水量'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-其他供水量'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-用水总量'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-农业用水量'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-工业用水量'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-生活用水量'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-人工生态环境补水用水量'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-人均用水量'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-供水总量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-地表水供水量'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-地下水供水量'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-其他供水量'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-用水总量'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-农业用水量'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-工业用水量'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-生活用水量'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-人工生态环境补水用水量'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-人均用水量'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中化学需氧量排放量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中氨氮排放量'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总氮排放量'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总磷排放量'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中石油类排放量'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中挥发酚排放量'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总铅排放量'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总汞排放量'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总镉排放量'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中六价铬排放量'
            question_types.append(question_type)
        elif self.check_words(self.q11_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总铬排放量'
            question_types.append(question_type)
        elif self.check_words(self.q12_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总砷排放量'
            question_types.append(question_type)

        elif self.check_words(self.q1_qwds_1_12, question) and ('12-不同城市废水污染物含量' in types):
            question_type = '资源与环境-12-城市废水中工业化学需氧量排放量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_12, question) and ('12-不同城市废水污染物含量' in types):
            question_type = '资源与环境-12-城市废水中工业氨氮排放量'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_12, question) and ('12-不同城市废水污染物含量' in types):
            question_type = '资源与环境-12-城市废水中生活化学需氧量排放量'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_12, question) and ('12-不同城市废水污染物含量' in types):
            question_type = '资源与环境-12-城市废水中生活氨氮排放量'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-工业二氧化硫排放量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-工业氮氧化物排放量'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-工业颗粒物排放量'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-生活及其他二氧化硫排放量'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-生活及其他氮氧化物排放量'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-生活及其他颗粒物排放量'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_13, question) and ('13-不同地区废气污染物含量' in types):
            question_type = '资源与环境-13-二氧化硫排放量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_13, question) and ('13-不同地区废气污染物含量' in types):
            question_type = '资源与环境-13-氮氧化物排放量'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_13, question) and ('13-不同地区废气污染物含量' in types):
            question_type = '资源与环境-13-颗粒物排放量'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-一般工业固体废物产生量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-一般工业固体废物综合利用量'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-一般工业固体废物处置量'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-一般工业固体废物贮存量'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-一般工业固体废物倾倒丢弃量'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-危险废物产生量'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-危险废物利用处置量'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-危险废物本年末贮存量'
            question_types.append(question_type)



        elif self.check_words(self.q1_qwds_1_16, question) and ('16-不同城市固体废物处理情况' in types):
            question_type = '资源与环境-16-一般工业固体废物产生量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_16, question) and ('16-不同城市固体废物处理情况' in types):
            question_type = '资源与环境-16-一般工业固体废物综合利用量'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_16, question) and ('16-不同城市固体废物处理情况' in types):
            question_type = '资源与环境-16-一般工业固体废物处置量'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_16, question) and ('16-不同城市固体废物处理情况' in types):
            question_type = '资源与环境-16-一般工业固体废物贮存量'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-二氧化硫年平均浓度'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-二氧化氮年平均浓度'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-可吸入颗粒物年平均浓度'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-一氧化碳日均值第95百分位浓度'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-臭氧日最大8小时第90百分位浓度'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-细颗粒物年平均浓度'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-空气质量优良天数比例'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-生活垃圾清运量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-无害化处理厂数'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-卫生填埋厂数'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-焚烧厂数'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-其他厂数'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-无害化处理能力'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-卫生填埋处理能力'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-焚烧处理能力'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-其他处理能力'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-无害化处理量'
            question_types.append(question_type)
        elif self.check_words(self.q11_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-卫生填埋处理量'
            question_types.append(question_type)
        elif self.check_words(self.q12_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-焚烧处理量'
            question_types.append(question_type)
        elif self.check_words(self.q13_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-其他处理量'
            question_types.append(question_type)
        elif self.check_words(self.q14_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-生活垃圾无害化处理率'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_19, question) and ('19-不同城市噪声污染情况' in types):
            question_type = '资源与环境-19-道路交通噪声等效声级'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_19, question) and ('19-不同城市噪声污染情况' in types):
            question_type = '资源与环境-19-区域环境噪声等效声级'
            question_types.append(question_type)



        elif self.check_words(self.q1_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-耕地'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-园地'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-林地'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-草地'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-湿地'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-城镇村及工矿用地'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-交通运输用地'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-水域及水利设施用地'
            question_types.append(question_type)



        elif self.check_words(self.q1_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-林业用地面积'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-森林面积'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-人工林'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-森林覆盖率'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-活立木总蓄积量'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-森林蓄积量'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-造林总面积'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-人工造林面积'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-飞播造林面积'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-封山育林面积'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-退化林修复面积'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-人工更新面积'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-造林总面积'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-人工造林面积'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-飞播造林面积'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-封山育林面积'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-退化林修复面积'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-人工更新面积'
            question_types.append(question_type)

        elif self.check_words(self.q1_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-种草面积'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原改良面积'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原鼠害发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原鼠害防治面积'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原虫害发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原虫害防治面积'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原火灾受害面积'
            question_types.append(question_type)



        elif self.check_words(self.q1_qwds_1_25, question) and ('25-不同地区自然保护情况' in types):
            question_type = '资源与环境-25-国家级自然保护区个数'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_25, question) and ('25-不同地区自然保护情况' in types):
            question_type = '资源与环境-25-国家级自然保护区面积'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-农作物受灾面积合计'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-农作物绝收面积合计'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-旱灾受灾面积'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-旱灾绝收面积'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-洪涝地质灾害和台风受灾面积'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-洪涝地质灾害和台风绝收面积'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-风雹灾害受灾面积'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-风雹灾害绝收面积'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-低温冷冻和雪灾受灾面积'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-低温冷冻和雪灾绝收面积'
            question_types.append(question_type)
        elif self.check_words(self.q11_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-受灾人口'
            question_types.append(question_type)
        elif self.check_words(self.q12_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-死亡人口'
            question_types.append(question_type)
        elif self.check_words(self.q13_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-直接经济损失'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-发生地质灾害数量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-滑坡次数'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-崩塌次数'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-泥石流次数'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-地面塌陷次数'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-人员伤亡数量'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-死亡人数'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-直接经济损失'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-发生地质灾害数量'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-滑坡次数'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-崩塌次数'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-泥石流次数'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-地面塌陷次数'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-人员伤亡数量'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-死亡人数'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-直接经济损失'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-森林火灾次数'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-一般火灾次数'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-较大火灾次数'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-重大火灾次数'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-特别重大火灾次数'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-火场总面积'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-受害森林面积'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-伤亡人数'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-其它损失折款'
            question_types.append(question_type)

        elif self.check_words(self.q1_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-林业有害生物发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-林业有害生物防治面积'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-林业有害生物防治率'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林病害发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林病害防治面积'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林虫害发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林虫害防治面积'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林鼠害发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林鼠害防治面积'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-有害植物发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q11_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-有害植物防治面积'
            question_types.append(question_type)



        elif self.check_words(self.q1_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-林业有害生物发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-林业有害生物防治面积'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-林业有害生物防治率'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林病害发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林病害防治面积'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林虫害发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林虫害防治面积'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林鼠害发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林鼠害防治面积'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-有害植物发生面积'
            question_types.append(question_type)
        elif self.check_words(self.q11_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-有害植物防治面积'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_30, question) and ('30-不同地区突发环境事件次数' in types):
            question_type = '资源与环境-30-突发环境事件次数'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_30, question) and ('30-不同地区突发环境事件次数' in types):
            question_type = '资源与环境-30-特别重大环境事件次数'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_30, question) and ('30-不同地区突发环境事件次数' in types):
            question_type = '资源与环境-30-重大环境事件次数'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_30, question) and ('30-不同地区突发环境事件次数' in types):
            question_type = '资源与环境-30-较大环境事件次数'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_30, question) and ('30-不同地区突发环境事件次数' in types):
            question_type = '资源与环境-30-一般环境事件次数'
            question_types.append(question_type)



        elif self.check_words(self.q2_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-5.0-5.9级地震次数'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-6.0-6.9级地震次数'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-7.0级以上地震次数'
            question_types.append(question_type)
        elif self.check_words(self.q1_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-地震次数'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-人员伤亡数量'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-死亡人数'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-直接经济损失'
            question_types.append(question_type)




        elif self.check_words(self.q2_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-5.0-5.9级地震次数'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-6.0-6.9级地震次数'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-7.0级以上地震次数'
            question_types.append(question_type)
        elif self.check_words(self.q1_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-地震次数'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-人员伤亡数量'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-死亡人数'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-直接经济损失'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_32, question) and ('32-海洋灾害情况' in types):
            question_type = '资源与环境-32-发生次数'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_32, question) and ('32-海洋灾害情况' in types):
            question_type = '资源与环境-32-人员死亡失踪'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_32, question) and ('32-海洋灾害情况' in types):
            question_type = '资源与环境-32-直接经济损失'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_33, question) and ('33-海域不同水质面积' in types):
            question_type = '资源与环境-33-第二类水质海域面积'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_33, question) and ('33-海域不同水质面积' in types):
            question_type = '资源与环境-33-第三类水质海域面积'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_33, question) and ('33-海域不同水质面积' in types):
            question_type = '资源与环境-33-劣于第四类水质海域面积'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_33, question) and ('33-海域不同水质面积' in types):
            question_type = '资源与环境-33-第四类水质海域面积'
            question_types.append(question_type)

        elif self.check_words(self.q1_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-城镇环境基础设施建设投资'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-燃气建设投资'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-集中供热建设投资'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-排水建设投资'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-园林绿化建设投资'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-市容环境卫生建设投资'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-工业污染治理完成投资'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-治理废水投资'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-治理废气投资'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-治理固体废物投资'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-治理噪声投资'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-治理其他投资'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-工业污染治理完成投资'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-治理废水投资'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-治理废气投资'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-治理固体废物投资'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-治理噪声投资'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-治理其他投资'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_1_36, question) and ('36-林业草原投资完成情况' in types):
            question_type = '资源与环境-36-本年完成林业草原投资总计'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_1_36, question) and ('36-林业草原投资完成情况' in types):
            question_type = '资源与环境-36-林业草原国家投资'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_1_36, question) and ('36-林业草原投资完成情况' in types):
            question_type = '资源与环境-36-林业草原生态修复治理投资'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_1_36, question) and ('36-林业草原投资完成情况' in types):
            question_type = '资源与环境-36-林业草原林产品加工制造投资'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_1_36, question) and ('36-林业草原投资完成情况' in types):
            question_type = '资源与环境-36-林业草原林业草原服务保障和公共管理投资'
            question_types.append(question_type)


        elif self.check_words(self.q1_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-国内生产总值'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-第一产业'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-第二产业'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-第三产业'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-农林牧渔业'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-工业'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-建筑业'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-批发和零售业'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-交通运输仓储和邮政业'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-住宿和餐饮业'
            question_types.append(question_type)
        elif self.check_words(self.q11_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-金融业'
            question_types.append(question_type)
        elif self.check_words(self.q12_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-房地产业'
            question_types.append(question_type)
        elif self.check_words(self.q13_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-其他'
            question_types.append(question_type)

        elif self.check_words(self.q15_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-人均国民总收入'
            question_types.append(question_type)
        elif self.check_words(self.q16_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-人均国内生产总值'
            question_types.append(question_type)
        elif self.check_words(self.q1_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-国民总收入'
            question_types.append(question_type)
        elif self.check_words(self.q2_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-国内生产总值'
            question_types.append(question_type)
        elif self.check_words(self.q3_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-第一产业'
            question_types.append(question_type)
        elif self.check_words(self.q4_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-第二产业'
            question_types.append(question_type)
        elif self.check_words(self.q5_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-第三产业'
            question_types.append(question_type)
        elif self.check_words(self.q6_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-农林牧渔业'
            question_types.append(question_type)
        elif self.check_words(self.q7_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-工业'
            question_types.append(question_type)
        elif self.check_words(self.q8_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-建筑业'
            question_types.append(question_type)
        elif self.check_words(self.q9_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-批发和零售业'
            question_types.append(question_type)
        elif self.check_words(self.q10_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-交通运输仓储和邮政业'
            question_types.append(question_type)
        elif self.check_words(self.q11_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-住宿和餐饮业'
            question_types.append(question_type)
        elif self.check_words(self.q12_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-金融业'
            question_types.append(question_type)
        elif self.check_words(self.q13_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-房地产业'
            question_types.append(question_type)
        elif self.check_words(self.q14_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-其他'
            question_types.append(question_type)






        # 将多个分类结果进行合并处理，组装成一个字典
        if len(question_types)==0:
            data['question_types']={}
        else:
            data['question_types'] = question_types
        print("data:",data)
        return data

    '''构造词对应的类型'''
    def build_wdtype_dict(self):
        wd_dict = dict()
        for wd in self.region_words:
            wd_dict[wd] = []
            if wd in self.tudi_wds_1_1:
                wd_dict[wd].append('1-土地面积')
            if wd in self.heliu_wds_1_2:
                wd_dict[wd].append('2-河流面积')
            if wd in self.liuyu_wds_1_3:
                wd_dict[wd].append('3-流域面积')
            if wd in self.kuangchan_wds_1_4:
                wd_dict[wd].append('4-矿产产量')
            if wd in self.chengwen_wds_1_5:
                wd_dict[wd].append('5-城市温度')
            if wd in self.chengshi_wds_1_6:
                wd_dict[wd].append('6-城市湿度')
            if wd in self.chengjiang_wds_1_7:
                wd_dict[wd].append('7-城市降水量')
            if wd in self.chengri_wds_1_8:
                wd_dict[wd].append('8-城市日照时间数')
            if wd in self.dishui_wds_1_9:
                wd_dict[wd].append('9-1-不同地区水资源总量')
            if wd in self.nianshui_wds_1_9:
                wd_dict[wd].append('9-不同年份水资源总量')
            if wd in self.digong_wds_1_10:
                wd_dict[wd].append('10-1-不同地区供水总量')
            if wd in self.niangong_wds_1_10:
                wd_dict[wd].append('10-不同年份供水总量')
            if wd in self.difei_wds_1_11:
                wd_dict[wd].append('11-不用地区废水污染物含量')
            if wd in self.chengfei_wds_1_12:
                wd_dict[wd].append('12-不同城市废水污染物含量')
            if wd in self.difei_wds_1_13:
                wd_dict[wd].append('13-不同地区废气污染物含量')
            if wd in self.chengfei_wds_1_14:
                wd_dict[wd].append('14-不同城市废气污染物含量')
            if wd in self.digu_wds_1_15:
                wd_dict[wd].append('15-不同地区固体废物处理情况')
            if wd in self.chenggu_wds_1_16:
                wd_dict[wd].append('16-不同城市固体废物处理情况')
            if wd in self.chengkong_wds_1_17:
                wd_dict[wd].append('17-不同城市空气污染物含量')
            if wd in self.dila_wds_1_18:
                wd_dict[wd].append('18-不同地区垃圾处理情况')
            if wd in self.chengzao_wds_1_19:
                wd_dict[wd].append('19-不同城市噪声污染情况')
            if wd in self.digeng_wds_1_20:
                wd_dict[wd].append('20-不同地区耕地面积情况')
            if wd in self.diyong_wds_1_21:
                wd_dict[wd].append('21-不同地区用地情况')
            if wd in self.disen_wds_1_22:
                wd_dict[wd].append('22-不同地区森林资源情况')
            if wd in self.dizao_wds_1_23_1:
                wd_dict[wd].append('23-1-不同地区造林面积')
            if wd in self.nianzao_wds_1_23:
                wd_dict[wd].append('23-不同年份造林面积')
            if wd in self.dicao_wds_1_24:
                wd_dict[wd].append('24-不同地区草原建设情况')
            if wd in self.dizi_wds_1_25:
                wd_dict[wd].append('25-不同地区自然保护情况')
            if wd in self.dizi_wds_1_26:
                wd_dict[wd].append('26-不同地区自然灾害情况')
            if wd in self.dizhi_wds_1_27_1:
                wd_dict[wd].append('27-1-不同地区地质灾害情况')
            if wd in self.nianzhi_wds_1_27:
                wd_dict[wd].append('27-不同年份地质灾害情况')
            if wd in self.disen_wds_1_28:
                wd_dict[wd].append('28-不同地区森林火灾情况')
            if wd in self.disheng_wds_1_29_1:
                wd_dict[wd].append('29-1-不同地区生物灾害情况')
            if wd in self.niansheng_wds_1_29:
                wd_dict[wd].append('29-不同年份生物灾害情况')
            if wd in self.ditu_wds_1_30:
                wd_dict[wd].append('30-不同地区突发环境事件次数')
            if wd in self.dizheng_wds_1_31_1:
                wd_dict[wd].append('31-1-不同地区地震情况')
            if wd in self.nianzheng_wds_1_31:
                wd_dict[wd].append('31-不同年份地震情况')
            if wd in self.haizai_wds_1_32:
                wd_dict[wd].append('32-海洋灾害情况')
            if wd in self.haizhi_wds_1_33:
                wd_dict[wd].append('33-海域不同水质面积')
            if wd in self.diji_wds_1_34:
                wd_dict[wd].append('34-不同地区基础建设投资')
            if wd in self.diwu_wds_1_35_1:
                wd_dict[wd].append('35-1-不同地区污染治理情况')
            if wd in self.nianwu_wds_1_35:
                wd_dict[wd].append('35-不同年份污染治理情况')
            if wd in self.lintou_wds_1_36:
                wd_dict[wd].append('36-林业草原投资完成情况')
            if wd in self.guosheng_wds_2_1:
                wd_dict[wd].append('C03-01国民生产总值')
            if wd in self.guoshenggou_wds_2_2:
                wd_dict[wd].append('C03-02国内生产总值构成')
        return wd_dict

    '''构造actree，加速过滤'''
    def build_actree(self, wordlist):
        actree = ahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    '''问句过滤'''
    def check_medical(self, question):
        region_wds = []
        for i in self.region_tree.iter(question):
            wd = i[1][1]
            region_wds.append(wd)
        stop_wds = []
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        final_dict = {i:self.wdtype_dict.get(i) for i in final_wds}

        return final_dict

    '''基于特征词进行分类'''
    def check_words(self, wds, sent):
        for wd in wds:
            if wd in sent:
                return True
        return False


if __name__ == '__main__':
    handler = QuestionClassifier()
    while 1:
        question = input('input an question:')
        data = handler.classify(question)
        print(data)