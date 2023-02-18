import os
import ahocorasick
import Global
class QuestionClassifier:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        cur_dir='./data/1-资源与环境'
        cur_dir2='./data/2-国民经济核算'
        cur_dir3='./data/3-能源'
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
        self.buguosheng_path_2_3 = os.path.join(cur_dir2, 'C03-03不变价国内生产总值.txt')
        self.guoshengzhi_path_2_4 = os.path.join(cur_dir2, 'C03-04国内生产总值指数.txt')
        self.fenzeng_path_2_6 = os.path.join(cur_dir2, 'C03-06分行业增加值.txt')
        self.yegong_path_2_7 = os.path.join(cur_dir2, 'C03-07三次产业和主要行业贡献率.txt')
        self.yela_path_2_8 = os.path.join(cur_dir2, 'C03-08.三次产业和主要行业对国内生产总值增长的拉动xls.txt')
        self.shengzong_path_2_9 = os.path.join(cur_dir2, 'C03-09生产总值.txt')
        self.shengzong_path_2_9_2 = os.path.join(cur_dir2, 'C03-09（2）生产总值占比.txt')
        self.shengzong_path_2_9_3 = os.path.join(cur_dir2, 'C03-09（3）生产总值指数.txt')
        self.zhizong_path_2_10 = os.path.join(cur_dir2, 'C03-10支出法国内生产总值.txt')
        self.juzhi_path_2_11_1 = os.path.join(cur_dir2, 'C03-11居民消费支出占比.txt')
        self.zuizhi_path_2_11_2 = os.path.join(cur_dir2, 'C03-11最终消费支出.txt')
        self.zuizhi_path_2_11_3 = os.path.join(cur_dir2, 'C03-11最终消费支出占比.txt')
        self.jinchu_path_2_11_4 = os.path.join(cur_dir2, 'C03-11货物与服务净出口.txt')
        self.zizong_path_2_11_5 = os.path.join(cur_dir2, 'C03-11资本形成总额.txt')
        self.zizong_path_2_11_6 = os.path.join(cur_dir2, 'C03-11资本形成总额占比.txt')
        self.shixiao_path_2_12 = os.path.join(cur_dir2, 'C03-12实际最终消费构成.txt')
        self.shixiao_path_2_12_1 = os.path.join(cur_dir2, 'C03-12（1）实际最终消费.txt')
        self.shengxiao_path_2_13 = os.path.join(cur_dir2, 'C03-13生活消费水平.txt')
        self.gongla_path_2_14 = os.path.join(cur_dir2, 'C03-14三大需求对国内生产总值增长的贡献率和拉动.txt')
        self.ziliu_path_2_16 = os.path.join(cur_dir2, 'C03-16资金流量表 (金融交易，2020年).txt')
        self.shoubi_path_2_17 = os.path.join(cur_dir2, 'C03-17企业、广义政府与住户部门初次分配总收入及比重.txt')
        self.tiaoshoubi_path_2_19 = os.path.join(cur_dir2, 'C03-19企业、广义政府与住户部门调整后可支配总收入及比重.txt')
        self.touchan_path_2_22 = os.path.join(cur_dir2, 'C03-22 2020年投入产出基本流量表(最终使用部分.txt')

        #  第三大类——能源
        self.yizong_path_3_1 = os.path.join(cur_dir3, 'C09-01一次能源生产总量及构成.txt')
        self.nengzong_path_3_2 = os.path.join(cur_dir3, 'C09-02能源消费总量及构成.txt')
        self.zongneng_path_3_3 = os.path.join(cur_dir3, 'C09-03综合能源平衡表.txt')
        self.shiping_path_3_4 = os.path.join(cur_dir3, 'C09-04石油平衡表.txt')
        self.meiping_path_3_5 = os.path.join(cur_dir3, 'C09-05煤炭平衡表.txt')
        self.dianping_path_3_6 = os.path.join(cur_dir3, 'C09-06电力平衡表.txt')
        self.nengsheng_path_3_7 = os.path.join(cur_dir3, 'C09-07能源生产弹性系数.txt')
        self.nengxiao_path_3_8 = os.path.join(cur_dir3, 'C09-08.能源消费弹性系数.txt')
        self.hangneng_path_3_9 = os.path.join(cur_dir3, 'C09-09按行业分能源消费量 (2020年).txt')
        self.nengjia_path_3_10 = os.path.join(cur_dir3, 'C09-10能源加工转换效率.txt')
        self.pingneng_path_3_11 = os.path.join(cur_dir3, 'C09-11平均每天能源消费量.txt')
        self.juneng_path_3_12 = os.path.join(cur_dir3, 'C09-12居民生活能源消费量.txt')
        self.rensheng_path_3_13 = os.path.join(cur_dir3, 'C09-13人均生活能源消费量.txt')
        self.fendian_path_3_14 = os.path.join(cur_dir3, 'C09-14分地区电力能源消费量.txt')
        self.fazhuang_path_3_15 = os.path.join(cur_dir3, 'C09-15发电装机容量.txt')
        self.guoneng_path_3_16 = os.path.join(cur_dir3, 'C09-16万元国内生产总值能源消费量.txt')

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
        self.buguosheng_wds_2_3 = [i.strip() for i in open(self.buguosheng_path_2_3, encoding="utf-8") if i.strip()]
        self.guoshengzhi_wds_2_4 = [i.strip() for i in open(self.guoshengzhi_path_2_4, encoding="utf-8") if i.strip()]
        self.fenzeng_wds_2_6 = [i.strip() for i in open(self.fenzeng_path_2_6, encoding="utf-8") if i.strip()]
        self.yegong_wds_2_7 = [i.strip() for i in open(self.yegong_path_2_7, encoding="utf-8") if i.strip()]
        self.yela_wds_2_8 = [i.strip() for i in open(self.yela_path_2_8, encoding="utf-8") if i.strip()]
        self.shengzong_wds_2_9 = [i.strip() for i in open(self.shengzong_path_2_9, encoding="utf-8") if i.strip()]
        self.shengzong_wds_2_9_2 = [i.strip() for i in open(self.shengzong_path_2_9_2, encoding="utf-8") if i.strip()]
        self.shengzong_wds_2_9_3 = [i.strip() for i in open(self.shengzong_path_2_9_3, encoding="utf-8") if i.strip()]
        self.zhizong_wds_2_10 = [i.strip() for i in open(self.zhizong_path_2_10, encoding="utf-8") if i.strip()]
        self.juzhi_wds_2_11_1 = [i.strip() for i in open(self.juzhi_path_2_11_1, encoding="utf-8") if i.strip()]
        self.zuizhi_wds_2_11_2 = [i.strip() for i in open(self.zuizhi_path_2_11_2, encoding="utf-8") if i.strip()]
        self.zuizhi_wds_2_11_3 = [i.strip() for i in open(self.zuizhi_path_2_11_3, encoding="utf-8") if i.strip()]
        self.jinchu_wds_2_11_4 = [i.strip() for i in open(self.jinchu_path_2_11_4, encoding="utf-8") if i.strip()]
        self.zizong_wds_2_11_5 = [i.strip() for i in open(self.zizong_path_2_11_5, encoding="utf-8") if i.strip()]
        self.zizong_wds_2_11_6 = [i.strip() for i in open(self.zizong_path_2_11_6, encoding="utf-8") if i.strip()]
        self.shixiao_wds_2_12 = [i.strip() for i in open(self.shixiao_path_2_12, encoding="utf-8") if i.strip()]
        self.shixiao_wds_2_12_1 = [i.strip() for i in open(self.shixiao_path_2_12_1, encoding="utf-8") if i.strip()]
        self.shengxiao_wds_2_13 = [i.strip() for i in open(self.shengxiao_path_2_13, encoding="utf-8") if i.strip()]
        self.gongla_wds_2_14 = [i.strip() for i in open(self.gongla_path_2_14, encoding="utf-8") if i.strip()]
        self.ziliu_wds_2_16 = [i.strip() for i in open(self.ziliu_path_2_16, encoding="utf-8") if i.strip()]
        self.shoubi_wds_2_17 = [i.strip() for i in open(self.shoubi_path_2_17, encoding="utf-8") if i.strip()]
        self.tiaoshoubi_wds_2_19 = [i.strip() for i in open(self.tiaoshoubi_path_2_19, encoding="utf-8") if i.strip()]
        self.touchan_wds_2_22 = [i.strip() for i in open(self.touchan_path_2_22, encoding="utf-8") if i.strip()]

        self.yizong_wds_3_1 = [i.strip() for i in open(self.yizong_path_3_1, encoding="utf-8") if i.strip()]
        self.nengzong_wds_3_2 = [i.strip() for i in open(self.nengzong_path_3_2, encoding="utf-8") if i.strip()]
        self.zongneng_wds_3_3 = [i.strip() for i in open(self.zongneng_path_3_3, encoding="utf-8") if i.strip()]
        self.shiping_wds_3_4 = [i.strip() for i in open(self.shiping_path_3_4, encoding="utf-8") if i.strip()]
        self.meiping_wds_3_5 = [i.strip() for i in open(self.meiping_path_3_5, encoding="utf-8") if i.strip()]
        self.dianping_wds_3_6 = [i.strip() for i in open(self.dianping_path_3_6, encoding="utf-8") if i.strip()]
        self.nengsheng_wds_3_7 = [i.strip() for i in open(self.nengsheng_path_3_7, encoding="utf-8") if i.strip()]
        self.nengxiao_wds_3_8 = [i.strip() for i in open(self.nengxiao_path_3_8, encoding="utf-8") if i.strip()]
        self.hangneng_wds_3_9 = [i.strip() for i in open(self.hangneng_path_3_9, encoding="utf-8") if i.strip()]
        self.nengjia_wds_3_10 = [i.strip() for i in open(self.nengjia_path_3_10, encoding="utf-8") if i.strip()]
        self.pingneng_wds_3_11 = [i.strip() for i in open(self.pingneng_path_3_11, encoding="utf-8") if i.strip()]
        self.juneng_wds_3_12 = [i.strip() for i in open(self.juneng_path_3_12, encoding="utf-8") if i.strip()]
        self.rensheng_wds_3_13 = [i.strip() for i in open(self.rensheng_path_3_13, encoding="utf-8") if i.strip()]
        self.fendian_wds_3_14 = [i.strip() for i in open(self.fendian_path_3_14, encoding="utf-8") if i.strip()]
        self.fazhuang_wds_3_15 = [i.strip() for i in open(self.fazhuang_path_3_15, encoding="utf-8") if i.strip()]
        self.guoneng_wds_3_16 = [i.strip() for i in open(self.guoneng_path_3_16, encoding="utf-8") if i.strip()]


        self.region_words = set(
            self.tudi_wds_1_1+self.heliu_wds_1_2+self.liuyu_wds_1_3 +self.kuangchan_wds_1_4+self.chengwen_wds_1_5+self.chengshi_wds_1_6+self.chengjiang_wds_1_7
            +self.chengri_wds_1_8+self.dishui_wds_1_9+self.nianshui_wds_1_9+self.digong_wds_1_10+self.niangong_wds_1_10+self.difei_wds_1_11
            +self.chengfei_wds_1_12+self.difei_wds_1_13+self.chengfei_wds_1_14+self.digu_wds_1_15+self.chenggu_wds_1_16+self.chengkong_wds_1_17
            +self.dila_wds_1_18+self.chengzao_wds_1_19+self.digeng_wds_1_20+self.diyong_wds_1_21+self.disen_wds_1_22+self.dizao_wds_1_23_1
            +self.nianzao_wds_1_23+self.dicao_wds_1_24+self.dizi_wds_1_25+self.dizi_wds_1_26+self.dizhi_wds_1_27_1+self.nianzhi_wds_1_27+self.disen_wds_1_28
            +self.disheng_wds_1_29_1+self.niansheng_wds_1_29+self.ditu_wds_1_30+self.dizheng_wds_1_31_1+self.nianzheng_wds_1_31+self.haizai_wds_1_32
            +self.haizhi_wds_1_33+self.diji_wds_1_34+self.diwu_wds_1_35_1+self.nianwu_wds_1_35+self.lintou_wds_1_36+self.guosheng_wds_2_1+self.guoshenggou_wds_2_2
            +self.buguosheng_wds_2_3+self.guoshengzhi_wds_2_4+self.fenzeng_wds_2_6+self.yegong_wds_2_7+self.yela_wds_2_8+self.shengzong_wds_2_9+self.shengzong_wds_2_9_2
            +self.shengzong_wds_2_9_3+self.zhizong_wds_2_10+self.juzhi_wds_2_11_1+self.zuizhi_wds_2_11_2+self.zuizhi_wds_2_11_3+self.jinchu_wds_2_11_4+self.zizong_wds_2_11_5
            +self.zizong_wds_2_11_6+self.shixiao_wds_2_12+self.shixiao_wds_2_12_1+self.shengxiao_wds_2_13+self.gongla_wds_2_14+self.ziliu_wds_2_16+self.shoubi_wds_2_17
            +self.tiaoshoubi_wds_2_19+self.touchan_wds_2_22+self.yizong_wds_3_1+self.nengzong_wds_3_2+self.zongneng_wds_3_3+self.shiping_wds_3_4+self.meiping_wds_3_5
            +self.dianping_wds_3_6+self.nengsheng_wds_3_7+self.nengxiao_wds_3_8+self.hangneng_wds_3_9+self.nengjia_wds_3_10+self.pingneng_wds_3_11+self.juneng_wds_3_12
            +self.rensheng_wds_3_13+self.fendian_wds_3_14+self.fazhuang_wds_3_15+self.guoneng_wds_3_16
        )

        # Global.shiti_list=self.region_words


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
        self.q1_qwds_1_5 = ['2021年的1月温度']
        self.q2_qwds_1_5 = ['2021年的2月温度']
        self.q3_qwds_1_5 = ['2021年的3月温度']
        self.q4_qwds_1_5 = ['2021年的4月温度']
        self.q5_qwds_1_5 = ['2021年的5月温度']
        self.q6_qwds_1_5 = ['2021年的6月温度']
        self.q7_qwds_1_5 = ['2021年的7月温度']
        self.q8_qwds_1_5 = ['2021年的8月温度']
        self.q9_qwds_1_5 = ['2021年的9月温度']
        self.q10_qwds_1_5 = ['2021年的10月温度']
        self.q11_qwds_1_5 = ['2021年的11月温度']
        self.q12_qwds_1_5 = ['2021年的12月温度']
        self.q13_qwds_1_5 = ['2021年的年平均温度']
        # 6-城市湿度
        self.q1_qwds_1_6 = ['2021年的1月湿度']
        self.q2_qwds_1_6 = ['2021年的2月湿度']
        self.q3_qwds_1_6 = ['2021年的3月湿度']
        self.q4_qwds_1_6 = ['2021年的4月湿度']
        self.q5_qwds_1_6 = ['2021年的5月湿度']
        self.q6_qwds_1_6 = ['2021年的6月湿度']
        self.q7_qwds_1_6 = ['2021年的7月湿度']
        self.q8_qwds_1_6 = ['2021年的8月湿度']
        self.q9_qwds_1_6 = ['2021年的9月湿度']
        self.q10_qwds_1_6 = ['2021年的10月湿度']
        self.q11_qwds_1_6 = ['2021年的11月湿度']
        self.q12_qwds_1_6 = ['2021年的12月湿度']
        self.q13_qwds_1_6 = ['2021年的年平均湿度']
        # 7-城市降水量

        self.q1_qwds_1_7 = ['2021年的1月降水量']
        self.q2_qwds_1_7 = ['2021年的2月降水量']
        self.q3_qwds_1_7 = ['2021年的3月降水量']
        self.q4_qwds_1_7 = ['2021年的4月降水量']
        self.q5_qwds_1_7 = ['2021年的5月降水量']
        self.q6_qwds_1_7 = ['2021年的6月降水量']
        self.q7_qwds_1_7 = ['2021年的7月降水量']
        self.q8_qwds_1_7 = ['2021年的8月降水量']
        self.q9_qwds_1_7 = ['2021年的9月降水量']
        self.q10_qwds_1_7 = ['2021年的10月降水量']
        self.q11_qwds_1_7 = ['2021年的11月降水量']
        self.q12_qwds_1_7 = ['2021年的12月降水量']
        self.q13_qwds_1_7 = ['2021年的全年降水量']

        # 8-城市日照时间数
        self.q1_qwds_1_8 = ['2021年的1月日照时数']
        self.q2_qwds_1_8 = ['2021年的2月日照时数']
        self.q3_qwds_1_8 = ['2021年的3月日照时数']
        self.q4_qwds_1_8 = ['2021年的4月日照时数']
        self.q5_qwds_1_8 = ['2021年的5月日照时数']
        self.q6_qwds_1_8 = ['2021年的6月日照时数']
        self.q7_qwds_1_8 = ['2021年的7月日照时数']
        self.q8_qwds_1_8 = ['2021年的8月日照时数']
        self.q9_qwds_1_8 = ['2021年的9月日照时数']
        self.q10_qwds_1_8 = ['2021年的10月日照时数']
        self.q11_qwds_1_8 = ['2021年的11月日照时数']
        self.q12_qwds_1_8 = ['2021年的12月日照时数']
        self.q13_qwds_1_8 = ['2021年的全年日照时数']
        # 9-1-不同地区水资源总量
        self.q1_qwds_1_9 = ['水资源总量']
        self.q2_qwds_1_9 = ['地表水资源量']
        self.q3_qwds_1_9 = ['地下水资源量']
        self.q4_qwds_1_9 = ['地表水与地下水资源重复量']
        self.q5_qwds_1_9 = ['人均水资源量']

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
        self.q2_qwds_1_18 = ['垃圾无害化处理厂数']
        self.q3_qwds_1_18 = ['卫生填埋厂数']
        self.q4_qwds_1_18 = ['垃圾焚烧厂数']
        self.q5_qwds_1_18 = ['其他厂数']
        self.q6_qwds_1_18 = ['垃圾无害化处理能力']
        self.q7_qwds_1_18 = ['卫生填埋处理能力']
        self.q8_qwds_1_18 = ['垃圾焚烧处理能力']
        self.q9_qwds_1_18 = ['其他处理能力']
        self.q10_qwds_1_18 = ['垃圾无害化处理量']
        self.q11_qwds_1_18 = ['卫生填埋处理量']
        self.q12_qwds_1_18 = ['垃圾焚烧处理量']
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
        self.q1_qwds_1_21 = ['耕地面积']
        self.q2_qwds_1_21 = ['园地面积']
        self.q3_qwds_1_21 = ['林地面积']
        self.q4_qwds_1_21 = ['草地面积']
        self.q5_qwds_1_21 = ['湿地面积']
        self.q6_qwds_1_21 = ['城镇村及工矿用地面积']
        self.q7_qwds_1_21 = ['交通运输用地面积']
        self.q8_qwds_1_21 = ['水域及水利设施用地面积']

        # 22-不同地区森林资源情况
        self.q1_qwds_1_22 = ['林业用地面积']
        self.q2_qwds_1_22 = ['森林面积']
        self.q3_qwds_1_22 = ['人工林面积']
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
        self.q1_qwds_1_26 = ['农作物受灾面积']
        self.q2_qwds_1_26 = ['农作物绝收面积']
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
        self.q2_qwds_1_27_1 = ['地质灾害导致的滑坡次数']
        self.q3_qwds_1_27_1 = ['地质灾害导致的崩塌次数']
        self.q4_qwds_1_27_1 = ['地质灾害导致的泥石流次数']
        self.q5_qwds_1_27_1 = ['地质灾害导致的地面塌陷次数']
        self.q6_qwds_1_27_1 = ['地质灾害导致的人员伤亡数量']
        self.q7_qwds_1_27_1 = ['地质灾害导致的死亡人数']
        self.q8_qwds_1_27_1 = ['地质灾害导致的直接经济损失']

        # 27-不同年份地质灾害情况
        self.q1_qwds_1_27 = ['发生地质灾害数量']
        self.q2_qwds_1_27 = ['地质灾害导致的滑坡次数']
        self.q3_qwds_1_27 = ['地质灾害导致的崩塌次数']
        self.q4_qwds_1_27 = ['地质灾害导致的泥石流次数']
        self.q5_qwds_1_27 = ['地质灾害导致的地面塌陷次数']
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
        self.q8_qwds_1_28 = ['森林火灾导致的伤亡人数']
        self.q9_qwds_1_28 = ['森林火灾导致的其它损失折款']

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
        self.q2_qwds_1_32 = ['导致的人员死亡失踪']
        self.q3_qwds_1_32 = ['导致的直接经济损失']

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
        self.q5_qwds_1_36 = ['林业草原服务保障和公共管理投资']

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

        # C03-03不变价国内生产总值
        self.q1_qwds_2_3 = ['不变价国内生产总值']
        self.q2_qwds_2_3 = ['不变价第一产业']
        self.q3_qwds_2_3 = ['不变价第二产业']
        self.q4_qwds_2_3 = ['不变价第三产业']
        self.q5_qwds_2_3 = ['不变价农林牧渔业']
        self.q6_qwds_2_3 = ['不变价工业']
        self.q7_qwds_2_3 = ['不变价建筑业']
        self.q8_qwds_2_3 = ['不变价批发和零售业']
        self.q9_qwds_2_3 = ['不变价交通运输仓储和邮政业']
        self.q10_qwds_2_3 = ['不变价住宿和餐饮业']
        self.q11_qwds_2_3 = ['不变价金融业']
        self.q12_qwds_2_3 = ['不变价房地产业']
        self.q13_qwds_2_3 = ['不变价其他']

        # C03-04国内生产总值指数
        self.q1_qwds_2_4 = ['国民总收入的指数']
        self.q2_qwds_2_4 = ['国内生产总值的指数']
        self.q3_qwds_2_4 = ['第一产业的指数']
        self.q4_qwds_2_4 = ['第二产业的指数']
        self.q5_qwds_2_4 = ['第三产业的指数']
        self.q6_qwds_2_4 = ['农林牧渔业的指数']
        self.q7_qwds_2_4 = ['工业的指数']
        self.q8_qwds_2_4 = ['建筑业的指数']
        self.q9_qwds_2_4 = ['批发和零售业的指数']
        self.q10_qwds_2_4 = ['交通运输仓储和邮政业的指数']
        self.q11_qwds_2_4 = ['住宿和餐饮业的指数']
        self.q12_qwds_2_4 = ['金融业的指数']
        self.q13_qwds_2_4 = ['房地产业的指数']
        self.q14_qwds_2_4 = ['其他的指数']
        self.q15_qwds_2_4 = ['人均国民总收入的指数']
        self.q16_qwds_2_4 = ['人均国内生产总值的指数']

        # C03-06分行业增加值
        self.q1_qwds_2_6 = ['国内生产总值的增加值']
        self.q2_qwds_2_6 = ['农林牧渔业的增加值']
        self.q3_qwds_2_6 = ['采矿业的增加值']
        self.q4_qwds_2_6 = ['制造业的增加值']
        self.q5_qwds_2_6 = ['电力热力燃气及水的增加值']
        self.q6_qwds_2_6 = ['建筑业的增加值']
        self.q7_qwds_2_6 = ['批发和零售业的增加值']
        self.q8_qwds_2_6 = ['交通运输仓储和邮政业的增加值']
        self.q9_qwds_2_6 = ['住宿和餐饮业的增加值']
        self.q10_qwds_2_6 = ['信息传输软件和信息的增加值']
        self.q11_qwds_2_6 = ['金融业的增加值']
        self.q12_qwds_2_6 = ['房地产业的增加值']
        self.q13_qwds_2_6 = ['租赁和商务服务业的增加值']
        self.q14_qwds_2_6 = ['科学研究和技术服务业的增加值']
        self.q15_qwds_2_6 = ['水利环境和公共设施管理业的增加值']
        self.q16_qwds_2_6 = ['居民服务修理和其他服务业的增加值']
        self.q17_qwds_2_6 = ['教育的增加值']
        self.q18_qwds_2_6 = ['卫生和社会工作的增加值']
        self.q19_qwds_2_6 = ['文化体育和娱乐业的增加值']
        self.q20_qwds_2_6 = ['公共管理社会保障的增加值']

        # C03-07三次产业和主要行业贡献率
        self.q1_qwds_2_7 = ['国内生产总值的贡献率']
        self.q2_qwds_2_7 = ['第一产业的贡献率']
        self.q3_qwds_2_7 = ['第二产业的贡献率']
        self.q4_qwds_2_7 = ['第三产业的贡献率']
        self.q5_qwds_2_7 = ['工业的贡献率']
        self.q6_qwds_2_7 = ['批发和零售业的贡献率']
        self.q7_qwds_2_7 = ['金融业的贡献率']

        # C03-08.三次产业和主要行业对国内生产总值增长的拉动xls
        self.q1_qwds_2_8 = ['国内生产总值对国内生产总值增长的拉动']
        self.q2_qwds_2_8 = ['第一产业对国内生产总值增长的拉动']
        self.q3_qwds_2_8 = ['第二产业对国内生产总值增长的拉动']
        self.q4_qwds_2_8 = ['第三产业对国内生产总值增长的拉动']
        self.q5_qwds_2_8 = ['工业对国内生产总值增长的拉动']
        self.q6_qwds_2_8 = ['批发和零售业对国内生产总值增长的拉动']
        self.q7_qwds_2_8 = ['金融业对国内生产总值增长的拉动']

        # C03-09生产总值
        self.q1_qwds_2_9 = ['地区生产总值']
        self.q2_qwds_2_9 = ['第一产业增加值']
        self.q3_qwds_2_9 = ['第二产业增加值']
        self.q4_qwds_2_9 = ['第三产业增加值']
        self.q5_qwds_2_9 = ['农林牧渔业增加值']
        self.q6_qwds_2_9 = ['工业增加值']
        self.q7_qwds_2_9 = ['建筑业增加值']
        self.q8_qwds_2_9 = ['批发和零售业增加值']
        self.q9_qwds_2_9 = ['交通运输仓储和邮政业增加值']
        self.q10_qwds_2_9 = ['住宿和餐饮业增加值']
        self.q11_qwds_2_9 = ['金融业增加值']
        self.q12_qwds_2_9 = ['房地产业增加值']
        self.q13_qwds_2_9 = ['其他增加值']

        # C03-09（2）生产总值占比
        self.q1_qwds_2_9_2 = ['人均地区生产总值']
        self.q2_qwds_2_9_2 = ['第一产业构成占比']
        self.q3_qwds_2_9_2 = ['第二产业构成占比']
        self.q4_qwds_2_9_2 = ['第三产业构成占比']

        # C03-09（3）生产总值指数
        self.q1_qwds_2_9_3 = ['地区生产总值指数']
        self.q2_qwds_2_9_3 = ['第一产业指数']
        self.q3_qwds_2_9_3 = ['第二产业指数']
        self.q4_qwds_2_9_3 = ['第三产业指数']
        self.q5_qwds_2_9_3 = ['人均地区生产总值指数']

        # C03-10支出法国内生产总值
        self.q1_qwds_2_10 = ['生产总值']
        self.q2_qwds_2_10 = ['最终消费']
        self.q3_qwds_2_10 = ['资本形成总额']
        self.q4_qwds_2_10 = ['货物和服务净出口']
        self.q5_qwds_2_10 = ['最终消费率']
        self.q6_qwds_2_10 = ['资本形成率']

        # C03-11居民消费支出占比
        self.q1_qwds_2_11_1 = ['居民消费中居民消费支出占比']
        self.q2_qwds_2_11_1 = ['居民消费中政府消费支出占比']

        # C03-11最终消费支出
        self.q1_qwds_2_11_2 = ['居民消费支出']
        self.q2_qwds_2_11_2 = ['城镇居民支出']
        self.q3_qwds_2_11_2 = ['农村居民支出']
        self.q4_qwds_2_11_2 = ['政府消费支出']

        # C03-11最终消费支出占比
        self.q1_qwds_2_11_3 = ['最终消费中居民消费支出占比']
        self.q2_qwds_2_11_3 = ['最终消费中政府消费支出占比']

        # C03-11货物与服务净出口
        self.q1_qwds_2_11_4 = ['出口']
        self.q2_qwds_2_11_4 = ['进口']

        # C03-11资本形成总额
        self.q1_qwds_2_11_5 = ['固定资本形成总额']
        self.q2_qwds_2_11_5 = ['存货变动']

        # C03-11资本形成总额占比
        self.q1_qwds_2_11_6 = ['固定资本形成总额占比']
        self.q2_qwds_2_11_6 = ['存货变动占比']

        # C03-12实际最终消费构成
        self.q1_qwds_2_12 = ['居民实际最终消费占比']
        self.q2_qwds_2_12 = ['政府实际最终消费占比']

        # C03-12（1）实际最终消费
        self.q1_qwds_2_12_1 = ['居民实际最终消费']
        self.q2_qwds_2_12_1 = ['政府实际最终消费']

        # C03-13生活消费水平
        self.q1_qwds_2_13 = ['全体居民绝对数']
        self.q2_qwds_2_13 = ['城镇居民绝对数']
        self.q3_qwds_2_13 = ['农村居民绝对数']
        self.q4_qwds_2_13 = ['城镇居民消费水平与农村居民消费水平的比值']
        self.q5_qwds_2_13 = ['全体居民指数']
        self.q6_qwds_2_13 = ['城镇居民消费指数']
        self.q7_qwds_2_13 = ['农村居民消费指数']

        # C03-14三大需求对国内生产总值增长的贡献率和拉动
        self.q1_qwds_2_14 = ['最终消费支出贡献率']
        self.q2_qwds_2_14 = ['最终消费支出拉动']
        self.q3_qwds_2_14 = ['资本形成总额贡献率']
        self.q4_qwds_2_14 = ['资本形成总额拉动']
        self.q5_qwds_2_14 = ['货物和服务净出口贡献率']
        self.q6_qwds_2_14 = ['货物和服务净出口拉动']

        # C03-16资金流量表 (金融交易，2020年)
        self.q1_qwds_2_16 = ['净金融投资']
        self.q2_qwds_2_16 = ['资金运用合计']
        self.q3_qwds_2_16 = ['资金来源合计']
        self.q4_qwds_2_16 = ['通货']
        self.q5_qwds_2_16 = ['存款']
        self.q6_qwds_2_16 = ['活期存款']
        self.q7_qwds_2_16 = ['定期存款']
        self.q8_qwds_2_16 = ['财政存款']
        self.q9_qwds_2_16 = ['外汇存款']
        self.q10_qwds_2_16 = ['其他存款']
        self.q11_qwds_2_16 = ['证券公司客户保证金']
        self.q12_qwds_2_16 = ['贷款']
        self.q13_qwds_2_16 = ['短期贷款与票据融资']
        self.q14_qwds_2_16 = ['中长期贷款']
        self.q15_qwds_2_16 = ['外汇贷款']
        self.q16_qwds_2_16 = ['委托贷款']
        self.q17_qwds_2_16 = ['其他贷款']
        self.q18_qwds_2_16 = ['未贴现的银行承兑汇票']
        self.q19_qwds_2_16 = ['保险准备金']
        self.q20_qwds_2_16 = ['金融机构往来']
        self.q21_qwds_2_16 = ['存款准备金']
        self.q22_qwds_2_16 = ['债券']
        self.q23_qwds_2_16 = ['政府债券']
        self.q24_qwds_2_16 = ['金融债券']
        self.q25_qwds_2_16 = ['中央银行债券']
        self.q26_qwds_2_16 = ['企业债券']
        self.q27_qwds_2_16 = ['股票']
        self.q28_qwds_2_16 = ['证券投资基金份额']
        self.q29_qwds_2_16 = ['库存现金']
        self.q30_qwds_2_16 = ['中央银行贷款']
        self.q31_qwds_2_16 = ['其他']
        self.q32_qwds_2_16 = ['直接投资']
        self.q33_qwds_2_16 = ['其他对外债权债务']
        self.q34_qwds_2_16 = ['国际储备资产']
        self.q35_qwds_2_16 = ['国际收支错误与遗漏']

        # C03-17企业、广义政府与住户部门初次分配总收入及比重
        self.q1_qwds_2_17 = ['企业部门初次分配总收入']
        self.q2_qwds_2_17 = ['企业部门占比']
        self.q3_qwds_2_17 = ['广义政府部门初次分配总收入']
        self.q4_qwds_2_17 = ['广义政府部门占比']
        self.q5_qwds_2_17 = ['住户部门初次分配总收入']
        self.q6_qwds_2_17 = ['住户部门占比']

        # C03-19企业、广义政府与住户部门调整后可支配总收入及比重
        self.q1_qwds_2_19 = ['企业部门调整后可支配总收入']
        self.q2_qwds_2_19 = ['企业部门调整后占比']
        self.q3_qwds_2_19 = ['广义政府部门调整后可支配总收入']
        self.q4_qwds_2_19 = ['广义政府部门调整后占比']
        self.q5_qwds_2_19 = ['住户部门调整后可支配总收入']
        self.q6_qwds_2_19 = ['住户部门调整后占比']

        # C03-22 2020年投入产出基本流量表(最终使用部分
        self.q1_qwds_2_22 = ['农林牧渔产品和服务']
        self.q2_qwds_2_22 = ['采掘产品']
        self.q3_qwds_2_22 = ['食品和烟草']
        self.q4_qwds_2_22 = ['纺织服装鞋及皮革羽绒制品']
        self.q5_qwds_2_22 = ['木材加工家具造纸印刷和文教工美用品']
        self.q6_qwds_2_22 = ['炼油炼焦和化学产品']
        self.q7_qwds_2_22 = ['非金属矿物制品']
        self.q8_qwds_2_22 = ['金属冶炼加工及制品']
        self.q9_qwds_2_22 = ['机械设备和交通运输设备及电子电气及其他设备']
        self.q10_qwds_2_22 = ['其他各类制造产品']
        self.q11_qwds_2_22 = ['电力热力燃气和水的生产和供应']
        self.q12_qwds_2_22 = ['建筑']
        self.q13_qwds_2_22 = ['批发零售运输仓储邮政']
        self.q14_qwds_2_22 = ['信息传输软件和信息技术服务']
        self.q15_qwds_2_22 = ['金融和房地产']
        self.q16_qwds_2_22 = ['科学研究和技术服务']
        self.q17_qwds_2_22 = ['其他服务']
        self.q18_qwds_2_22 = ['中间投入合计']

        #  第三大类——能源
        #C09-01一次能源生产总量及构成
        self.q1_qwds_3_1 = ['一次能源生产总量']
        self.q2_qwds_3_1 = ['原煤占一次能源生产总量的比重']
        self.q3_qwds_3_1 = ['原油占一次能源生产总量的比重']
        self.q4_qwds_3_1 = ['天然气占一次能源生产总量的比重']
        self.q5_qwds_3_1 = ['一次电力及其他能源占一次能源生产总量的比重']

        # C09-02能源消费总量及构成
        self.q1_qwds_3_2 = ['能源消费总量']
        self.q2_qwds_3_2 = ['煤炭占能源消费总量的比重']
        self.q3_qwds_3_2 = ['石油占能源消费总量的比重']
        self.q4_qwds_3_2 = ['天然气占能源消费总量的比重']
        self.q5_qwds_3_2 = ['一次电力及其他能源占能源消费总量的比重']

        # C09-03综合能源平衡表
        self.q1_qwds_3_3 = ['可供消费的能源总量']
        self.q2_qwds_3_3 = ['一次能源生产总量']
        self.q3_qwds_3_3 = ['回收量']
        self.q4_qwds_3_3 = ['进口量']
        self.q5_qwds_3_3 = ['出口量']
        self.q6_qwds_3_3 = ['年初年末库存差额']
        self.q7_qwds_3_3 = ['能源消费总量']
        self.q8_qwds_3_3 = ['渔业']
        self.q9_qwds_3_3 = ['工业']
        self.q10_qwds_3_3 = ['建筑业']
        self.q11_qwds_3_3 = ['邮政业']
        self.q12_qwds_3_3 = ['住宿和餐饮业']
        self.q13_qwds_3_3 = ['其他']
        self.q14_qwds_3_3 = ['居民生活']
        self.q15_qwds_3_3 = ['终端消费']
        self.q16_qwds_3_3 = ['加工转换损失量']
        self.q17_qwds_3_3 = ['炼焦']
        self.q18_qwds_3_3 = ['炼油及煤制油']
        self.q19_qwds_3_3 = ['损失量']
        self.q20_qwds_3_3 = ['平衡差额']

        # C09-04石油平衡表
        self.q1_qwds_3_4 = ['石油可供量']
        self.q2_qwds_3_4 = ['石油生产量']
        self.q3_qwds_3_4 = ['石油进口量']
        self.q4_qwds_3_4 = ['石油出口量']
        self.q5_qwds_3_4 = ['石油年初年末库存差额']
        self.q6_qwds_3_4 = ['石油消费量']
        self.q7_qwds_3_4 = ['农林牧渔业中石油消费量']
        self.q8_qwds_3_4 = ['工业中石油消费量']
        self.q9_qwds_3_4 = ['建筑业中石油消费量']
        self.q10_qwds_3_4 = ['交通运输仓储和邮政业中石油消费量']
        self.q11_qwds_3_4 = ['批发和零售业住宿和餐饮业中石油消费量']
        self.q12_qwds_3_4 = ['其他中石油消费量']
        self.q13_qwds_3_4 = ['居民生活中石油消费量']
        self.q14_qwds_3_4 = ['终端消费中石油消费量']
        self.q15_qwds_3_4 = ['中间消费中石油消费量']
        self.q16_qwds_3_4 = ['火力发电中石油消费量']
        self.q17_qwds_3_4 = ['供热中石油消费量']
        self.q18_qwds_3_4 = ['制气中石油消费量']
        self.q19_qwds_3_4 = ['炼油损失量中石油消费量']
        self.q20_qwds_3_4 = ['损失量中石油消费量']
        self.q21_qwds_3_4 = ['石油平衡差额']

        # C09-05煤炭平衡表
        self.q1_qwds_3_5 = ['煤炭可供量']
        self.q2_qwds_3_5 = ['煤炭生产量']
        self.q3_qwds_3_5 = ['煤炭进口量']
        self.q4_qwds_3_5 = ['煤炭出口量']
        self.q5_qwds_3_5 = ['煤炭年初年末库存差额']
        self.q6_qwds_3_5 = ['煤炭消费量']
        self.q7_qwds_3_5 = ['农林牧渔业中煤炭消费量']
        self.q8_qwds_3_5 = ['工业中煤炭消费量']
        self.q9_qwds_3_5 = ['建筑业中煤炭消费量']
        self.q10_qwds_3_5 = ['交通运输仓储和邮政业中煤炭消费量']
        self.q11_qwds_3_5 = ['批发和零售业住宿和餐饮业中煤炭消费量']
        self.q12_qwds_3_5 = ['其他中煤炭消费量']
        self.q13_qwds_3_5 = ['居民生活中煤炭消费量']
        self.q14_qwds_3_5 = ['终端消费中煤炭消费量']
        self.q15_qwds_3_5 = ['中间消费中煤炭消费量']
        self.q16_qwds_3_5 = ['火力发电中煤炭消费量']
        self.q17_qwds_3_5 = ['供热中煤炭消费量']
        self.q18_qwds_3_5 = ['炼焦中煤炭消费量']
        self.q19_qwds_3_5 = ['煤制油中煤炭消费量']
        self.q20_qwds_3_5 = ['制气中煤炭消费量']
        self.q21_qwds_3_5 = ['洗选损耗中煤炭消费量']
        self.q22_qwds_3_5 = ['煤炭平衡差额']

        # C09-06电力平衡表
        self.q1_qwds_3_6 = ['可供量']
        self.q2_qwds_3_6 = ['电力生产量']
        self.q3_qwds_3_6 = ['水电生产量']
        self.q4_qwds_3_6 = ['火电生产量']
        self.q5_qwds_3_6 = ['核电生产量']
        self.q6_qwds_3_6 = ['风电生产量']
        self.q7_qwds_3_6 = ['电力进口量']
        self.q8_qwds_3_6 = ['电力出口量']
        self.q9_qwds_3_6 = ['电力消费量']
        self.q10_qwds_3_6 = ['农林牧渔业中电力消费量']
        self.q11_qwds_3_6 = ['工业中电力消费量']
        self.q12_qwds_3_6 = ['建筑业中电力消费量']
        self.q13_qwds_3_6 = ['交通运输仓储和邮政业中电力消费量']
        self.q14_qwds_3_6 = ['批发和零售业住宿和餐饮业中电力消费量']
        self.q15_qwds_3_6 = ['其他中电力消费量']
        self.q16_qwds_3_6 = ['居民生活中电力消费量']
        self.q17_qwds_3_6 = ['终端消费中电力消费量']
        self.q18_qwds_3_6 = ['输配电损失量']

        # C09-07能源生产弹性系数
        self.q1_qwds_3_7 = ['能源生产比上年增长']
        self.q2_qwds_3_7 = ['电力生产比上年增长']
        self.q3_qwds_3_7 = ['国内生产总值比上年增长']
        self.q4_qwds_3_7 = ['能源生产弹性系数']
        self.q5_qwds_3_7 = ['电力生产弹性系数']

        # C09-08.能源消费弹性系数
        self.q1_qwds_3_8 = ['能源消费比上年增长']
        self.q2_qwds_3_8 = ['电力消费比上年增长']
        self.q3_qwds_3_8 = ['国内消费总值比上年增长']
        self.q4_qwds_3_8 = ['能源消费弹性系数']
        self.q5_qwds_3_8 = ['电力消费弹性系数']


        # C09-09按行业分能源消费量 (2020年)
        self.q1_qwds_3_9 = ['能源消费总量']
        self.q2_qwds_3_9 = ['煤炭']
        self.q3_qwds_3_9 = ['焦炭']
        self.q4_qwds_3_9 = ['原油']
        self.q5_qwds_3_9 = ['汽油']
        self.q6_qwds_3_9 = ['煤油']
        self.q7_qwds_3_9 = ['柴油']
        self.q8_qwds_3_9 = ['燃料油']
        self.q9_qwds_3_9 = ['天然气']
        self.q10_qwds_3_9 = ['电力']

        # C09-10能源加工转换效率
        self.q1_qwds_3_10 = ['总效率']
        self.q2_qwds_3_10 = ['发电及供热']
        self.q3_qwds_3_10 = ['炼焦']
        self.q4_qwds_3_10 = ['炼油及煤制油']

        # C09-11平均每天能源消费量
        self.q1_qwds_3_11 = ['平均每天能源消费合计']
        self.q2_qwds_3_11 = ['平均每天煤炭消费']
        self.q3_qwds_3_11 = ['平均每天焦炭消费']
        self.q4_qwds_3_11 = ['平均每天原油消费']
        self.q5_qwds_3_11 = ['平均每天燃料油消费']
        self.q6_qwds_3_11 = ['平均每天汽油消费']
        self.q7_qwds_3_11 = ['平均每天煤油消费']
        self.q8_qwds_3_11 = ['平均每天柴油消费']
        self.q9_qwds_3_11 = ['平均每天天然气消费']
        self.q10_qwds_3_11 = ['平均每天电力消费']

        # C09-12居民生活能源消费量
        self.q1_qwds_3_12 = ['居民能源消费合计']
        self.q2_qwds_3_12 = ['居民煤炭消费']
        self.q3_qwds_3_12 = ['居民煤油消费']
        self.q4_qwds_3_12 = ['居民液化石油气消费']
        self.q5_qwds_3_12 = ['居民天然气消费']
        self.q6_qwds_3_12 = ['居民煤气消费']
        self.q7_qwds_3_12 = ['居民热力消费']
        self.q8_qwds_3_12 = ['居民电力消费']

        # C09-13人均生活能源消费量
        self.q1_qwds_3_13 = ['人均生活能源消费量']
        self.q2_qwds_3_13 = ['人均煤炭消费']
        self.q3_qwds_3_13 = ['人均电力消费']
        self.q4_qwds_3_13 = ['人均液化石油气消费']
        self.q5_qwds_3_13 = ['人均天然气消费']
        self.q6_qwds_3_13 = ['人均煤气消费']


        # C09-14分地区电力能源消费量
        self.q1_qwds_3_14 = ['北京电力消费']
        self.q2_qwds_3_14 = ['天津电力消费']
        self.q3_qwds_3_14 = ['河北电力消费']
        self.q4_qwds_3_14 = ['山西电力消费']
        self.q5_qwds_3_14 = ['内蒙古电力消费']
        self.q6_qwds_3_14 = ['辽宁电力消费']
        self.q7_qwds_3_14 = ['吉林电力消费']
        self.q8_qwds_3_14 = ['黑龙江电力消费']
        self.q9_qwds_3_14 = ['上海电力消费']
        self.q10_qwds_3_14 = ['江苏电力消费']
        self.q11_qwds_3_14 = ['浙江电力消费']
        self.q12_qwds_3_14 = ['安徽电力消费']
        self.q13_qwds_3_14 = ['福建电力消费']
        self.q14_qwds_3_14 = ['江西电力消费']
        self.q15_qwds_3_14 = ['山东电力消费']
        self.q16_qwds_3_14 = ['河南电力消费']
        self.q17_qwds_3_14 = ['湖北电力消费']
        self.q18_qwds_3_14 = ['湖南电力消费']
        self.q19_qwds_3_14 = ['广东电力消费']
        self.q20_qwds_3_14 = ['广西电力消费']
        self.q21_qwds_3_14 = ['海南电力消费']
        self.q22_qwds_3_14 = ['重庆电力消费']
        self.q23_qwds_3_14 = ['四川电力消费']
        self.q24_qwds_3_14 = ['贵州电力消费']
        self.q25_qwds_3_14 = ['云南电力消费']
        self.q26_qwds_3_14 = ['西藏电力消费']
        self.q27_qwds_3_14 = ['陕西电力消费']
        self.q28_qwds_3_14 = ['甘肃电力消费']
        self.q29_qwds_3_14 = ['青海电力消费']
        self.q30_qwds_3_14 = ['宁夏电力消费']
        self.q31_qwds_3_14 = ['新疆电力消费']

        # C09-15发电装机容量
        self.q1_qwds_3_15 = ['发电装机容量']
        self.q2_qwds_3_15 = ['火发电量']
        self.q3_qwds_3_15 = ['水发电量']
        self.q4_qwds_3_15 = ['核发电量']
        self.q5_qwds_3_15 = ['风发电量']
        self.q6_qwds_3_15 = ['太阳能发电量']
        self.q7_qwds_3_15 = ['其他']

        # C09-16万元国内生产总值能源消费量
        self.q1_qwds_3_16 = ['国内生产总值能源消费量']
        self.q2_qwds_3_16 = ['国内生产总值煤炭消费量']
        self.q3_qwds_3_16 = ['国内生产总值焦炭消费量']
        self.q4_qwds_3_16 = ['国内生产总值石油消费量']
        self.q5_qwds_3_16 = ['国内生产总值原油消费量']
        self.q6_qwds_3_16 = ['国内生产总值燃料油消费量']
        self.q7_qwds_3_16 = ['国内生产总值电力消费量']

        print('model init finished ......')
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
        if self.check_words(self.q2_qwds_1_20, question) and ('20-不同地区耕地面积情况' in types):
            question_type = '资源与环境-20-2014耕地面积'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_20, question) and ('20-不同地区耕地面积情况' in types):
            question_type = '资源与环境-20-2015耕地面积'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_20, question) and ('20-不同地区耕地面积情况' in types):
            question_type = '资源与环境-20-2016耕地面积'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_20, question) and ('20-不同地区耕地面积情况' in types):
            question_type = '资源与环境-20-2017耕地面积'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_20, question) and ('20-不同地区耕地面积情况' in types):
            question_type = '资源与环境-20-2019耕地面积'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_1, question) and ('1-土地面积' in types):
            question_type = '资源与环境-1-面积'
            question_types.append(question_type)
        if self.check_words(self.q1_qwds_1_2, question) and ('2-河流面积' in types):
            question_type = '资源与环境-2-流域面积'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_2, question) and ('2-河流面积' in types):
            question_type = '资源与环境-2-河长'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_2, question) and ('2-河流面积' in types):
            question_type = '资源与环境-2-年径流量'
            question_types.append(question_type)
        if self.check_words(self.q1_qwds_1_3, question) and ('3-流域面积' in types):
            question_type = '资源与环境-3-流域面积'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_3, question) and ('3-流域面积' in types):
            question_type = '资源与环境-3-面积占比'
            question_types.append(question_type)
        if self.check_words(self.q1_qwds_1_4, question) and ('4-矿产产量' in types):
            question_type = '资源与环境-4-2020年产量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_4, question) and ('4-矿产产量' in types):
            question_type = '资源与环境-4-2021年产量'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-11月温度'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-12月温度'
            question_types.append(question_type)
        if self.check_words(self.q1_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-1月温度'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-2月温度'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-3月温度'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-4月温度'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-5月温度'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-6月温度'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-7月温度'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-8月温度'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-9月温度'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-10月温度'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_1_5, question) and ('5-城市温度' in types):
            question_type = '资源与环境-5-年平均温度'
            question_types.append(question_type)


        if self.check_words(self.q11_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-11月湿度'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-12月湿度'
            question_types.append(question_type)
        if self.check_words(self.q1_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-1月湿度'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-2月湿度'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-3月湿度'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-4月湿度'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-5月湿度'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-6月湿度'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-7月湿度'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-8月湿度'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-9月湿度'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-10月湿度'
            question_types.append(question_type)

        if self.check_words(self.q13_qwds_1_6, question) and ('6-城市湿度' in types):
            question_type = '资源与环境-6-年平均湿度'
            question_types.append(question_type)


        if self.check_words(self.q11_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-11月降水量'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-12月降水量'
            question_types.append(question_type)
        if self.check_words(self.q1_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-1月降水量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-2月降水量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-3月降水量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-4月降水量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-5月降水量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-6月降水量'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-7月降水量'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-8月降水量'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-9月降水量'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-10月降水量'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_1_7, question) and ('7-城市降水量' in types):
            question_type = '资源与环境-7-全年降水量'
            question_types.append(question_type)

        if self.check_words(self.q11_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-11月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-12月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q1_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-1月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-2月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-3月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-4月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-5月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-6月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-7月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-8月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-9月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-10月日照时数'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_1_8, question) and ('8-城市日照时间数' in types):
            question_type = '资源与环境-8-全年日照时数'
            question_types.append(question_type)

        if self.check_words(self.q1_qwds_1_9, question) and ('9-1-不同地区水资源总量' in types):
            question_type = '资源与环境-9-水资源总量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_9, question) and ('9-1-不同地区水资源总量' in types):
            question_type = '资源与环境-9-地表水资源量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_9, question) and ('9-1-不同地区水资源总量' in types):
            question_type = '资源与环境-9-地下水资源量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_9, question) and ('9-1-不同地区水资源总量' in types):
            question_type = '资源与环境-9-地表水与地下水资源重复量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_9, question) and ('9-1-不同地区水资源总量' in types):
            question_type = '资源与环境-9-人均水资源量'
            question_types.append(question_type)

        if self.check_words(self.q1_qwds_1_9_1, question) and ('9-不同年份水资源总量' in types):
            question_type = '资源与环境-9-1-水资源总量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_9_1, question) and ('9-不同年份水资源总量' in types):
            question_type = '资源与环境-9-1-地表水资源量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_9_1, question) and ('9-不同年份水资源总量' in types):
            question_type = '资源与环境-9-1-地下水资源量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_9_1, question) and ('9-不同年份水资源总量' in types):
            question_type = '资源与环境-9-1-地表水与地下水资源重复量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_9_1, question) and ('9-不同年份水资源总量' in types):
            question_type = '资源与环境-9-1-人均水资源量'
            question_types.append(question_type)

        if self.check_words(self.q1_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-供水总量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-地表水供水量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-地下水供水量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-其他供水量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-用水总量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-农业用水量'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-工业用水量'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-生活用水量'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-人工生态环境补水用水量'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_1_10_1, question) and ('10-1-不同地区供水总量' in types):
            question_type = '资源与环境-10-1-人均用水量'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-供水总量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-地表水供水量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-地下水供水量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-其他供水量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-用水总量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-农业用水量'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-工业用水量'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-生活用水量'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-人工生态环境补水用水量'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_1_10, question) and ('10-不同年份供水总量' in types):
            question_type = '资源与环境-10-人均用水量'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中化学需氧量排放量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中氨氮排放量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总氮排放量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总磷排放量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中石油类排放量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中挥发酚排放量'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总铅排放量'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总汞排放量'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总镉排放量'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中六价铬排放量'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总铬排放量'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_1_11, question) and ('11-不用地区废水污染物含量' in types):
            question_type = '资源与环境-11-废水中总砷排放量'
            question_types.append(question_type)

        if self.check_words(self.q1_qwds_1_12, question) and ('12-不同城市废水污染物含量' in types):
            question_type = '资源与环境-12-城市废水中工业化学需氧量排放量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_12, question) and ('12-不同城市废水污染物含量' in types):
            question_type = '资源与环境-12-城市废水中工业氨氮排放量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_12, question) and ('12-不同城市废水污染物含量' in types):
            question_type = '资源与环境-12-城市废水中生活化学需氧量排放量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_12, question) and ('12-不同城市废水污染物含量' in types):
            question_type = '资源与环境-12-城市废水中生活氨氮排放量'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-工业二氧化硫排放量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-工业氮氧化物排放量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-工业颗粒物排放量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-生活及其他二氧化硫排放量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-生活及其他氮氧化物排放量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_14, question) and ('14-不同城市废气污染物含量' in types):
            question_type = '资源与环境-14-生活及其他颗粒物排放量'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_13, question) and ('13-不同地区废气污染物含量' in types):
            question_type = '资源与环境-13-二氧化硫排放量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_13, question) and ('13-不同地区废气污染物含量' in types):
            question_type = '资源与环境-13-氮氧化物排放量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_13, question) and ('13-不同地区废气污染物含量' in types):
            question_type = '资源与环境-13-颗粒物排放量'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-一般工业固体废物产生量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-一般工业固体废物综合利用量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-一般工业固体废物处置量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-一般工业固体废物贮存量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-一般工业固体废物倾倒丢弃量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-危险废物产生量'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-危险废物利用处置量'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_15, question) and ('15-不同地区固体废物处理情况' in types):
            question_type = '资源与环境-15-危险废物本年末贮存量'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_1_16, question) and ('16-不同城市固体废物处理情况' in types):
            question_type = '资源与环境-16-一般工业固体废物产生量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_16, question) and ('16-不同城市固体废物处理情况' in types):
            question_type = '资源与环境-16-一般工业固体废物综合利用量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_16, question) and ('16-不同城市固体废物处理情况' in types):
            question_type = '资源与环境-16-一般工业固体废物处置量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_16, question) and ('16-不同城市固体废物处理情况' in types):
            question_type = '资源与环境-16-一般工业固体废物贮存量'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-二氧化硫年平均浓度'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-二氧化氮年平均浓度'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-可吸入颗粒物年平均浓度'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-一氧化碳日均值第95百分位浓度'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-臭氧日最大8小时第90百分位浓度'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-细颗粒物年平均浓度'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_17, question) and ('17-不同城市空气污染物含量' in types):
            question_type = '资源与环境-17-空气质量优良天数比例'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-生活垃圾清运量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-无害化处理厂数'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-卫生填埋厂数'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-焚烧厂数'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-其他厂数'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-无害化处理能力'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-卫生填埋处理能力'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-焚烧处理能力'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-其他处理能力'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-无害化处理量'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-卫生填埋处理量'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-焚烧处理量'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-其他处理量'
            question_types.append(question_type)
        if self.check_words(self.q14_qwds_1_18, question) and ('18-不同地区垃圾处理情况' in types):
            question_type = '资源与环境-18-生活垃圾无害化处理率'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_19, question) and ('19-不同城市噪声污染情况' in types):
            question_type = '资源与环境-19-道路交通噪声等效声级'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_19, question) and ('19-不同城市噪声污染情况' in types):
            question_type = '资源与环境-19-区域环境噪声等效声级'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-耕地'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-园地'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-林地'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-草地'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-湿地'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-城镇村及工矿用地'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-交通运输用地'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_21, question) and ('21-不同地区用地情况' in types):
            question_type = '资源与环境-21-水域及水利设施用地'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-林业用地面积'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-森林面积'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-人工林'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-森林覆盖率'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-活立木总蓄积量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_22, question) and ('22-不同地区森林资源情况' in types):
            question_type = '资源与环境-22-森林蓄积量'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-造林总面积'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-人工造林面积'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-飞播造林面积'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-封山育林面积'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-退化林修复面积'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_23_1, question) and ('23-1-不同地区造林面积' in types):
            question_type = '资源与环境-23-1-人工更新面积'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-造林总面积'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-人工造林面积'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-飞播造林面积'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-封山育林面积'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-退化林修复面积'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_23, question) and ('23-不同年份造林面积' in types):
            question_type = '资源与环境-23-人工更新面积'
            question_types.append(question_type)

        if self.check_words(self.q1_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-种草面积'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原改良面积'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原鼠害发生面积'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原鼠害防治面积'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原虫害发生面积'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原虫害防治面积'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_24, question) and ('24-不同地区草原建设情况' in types):
            question_type = '资源与环境-24-草原火灾受害面积'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_1_25, question) and ('25-不同地区自然保护情况' in types):
            question_type = '资源与环境-25-国家级自然保护区个数'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_25, question) and ('25-不同地区自然保护情况' in types):
            question_type = '资源与环境-25-国家级自然保护区面积'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-农作物受灾面积合计'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-农作物绝收面积合计'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-旱灾受灾面积'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-旱灾绝收面积'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-洪涝地质灾害和台风受灾面积'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-洪涝地质灾害和台风绝收面积'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-风雹灾害受灾面积'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-风雹灾害绝收面积'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-低温冷冻和雪灾受灾面积'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-低温冷冻和雪灾绝收面积'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-受灾人口'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-死亡人口'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_1_26, question) and ('26-不同地区自然灾害情况' in types):
            question_type = '资源与环境-26-直接经济损失'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-发生地质灾害数量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-滑坡次数'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-崩塌次数'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-泥石流次数'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-地面塌陷次数'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-人员伤亡数量'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-死亡人数'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_27_1, question) and ('27-1-不同地区地质灾害情况' in types):
            question_type = '资源与环境-27-1-直接经济损失'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-发生地质灾害数量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-滑坡次数'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-崩塌次数'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-泥石流次数'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-地面塌陷次数'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-人员伤亡数量'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-死亡人数'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_27, question) and ('27-不同年份地质灾害情况' in types):
            question_type = '资源与环境-27-直接经济损失'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-森林火灾次数'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-一般火灾次数'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-较大火灾次数'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-重大火灾次数'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-特别重大火灾次数'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-火场总面积'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-受害森林面积'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-伤亡人数'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_28, question) and ('28-不同地区森林火灾情况' in types):
            question_type = '资源与环境-28-其它损失折款'
            question_types.append(question_type)

        if self.check_words(self.q1_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-林业有害生物发生面积'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-林业有害生物防治面积'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-林业有害生物防治率'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林病害发生面积'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林病害防治面积'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林虫害发生面积'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林虫害防治面积'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林鼠害发生面积'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-森林鼠害防治面积'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-有害植物发生面积'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_1_29_1, question) and ('29-1-不同地区生物灾害情况' in types):
            question_type = '资源与环境-29-1-有害植物防治面积'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-林业有害生物发生面积'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-林业有害生物防治面积'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-林业有害生物防治率'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林病害发生面积'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林病害防治面积'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林虫害发生面积'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林虫害防治面积'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林鼠害发生面积'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-森林鼠害防治面积'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-有害植物发生面积'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_1_29, question) and ('29-不同年份生物灾害情况' in types):
            question_type = '资源与环境-29-有害植物防治面积'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_30, question) and ('30-不同地区突发环境事件次数' in types):
            question_type = '资源与环境-30-突发环境事件次数'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_30, question) and ('30-不同地区突发环境事件次数' in types):
            question_type = '资源与环境-30-特别重大环境事件次数'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_30, question) and ('30-不同地区突发环境事件次数' in types):
            question_type = '资源与环境-30-重大环境事件次数'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_30, question) and ('30-不同地区突发环境事件次数' in types):
            question_type = '资源与环境-30-较大环境事件次数'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_30, question) and ('30-不同地区突发环境事件次数' in types):
            question_type = '资源与环境-30-一般环境事件次数'
            question_types.append(question_type)



        if self.check_words(self.q2_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-5.0-5.9级地震次数'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-6.0-6.9级地震次数'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-7.0级以上地震次数'
            question_types.append(question_type)
        if self.check_words(self.q1_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-地震次数'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-人员伤亡数量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-死亡人数'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_31_1, question) and ('31-1-不同地区地震情况' in types):
            question_type = '资源与环境-31-1-直接经济损失'
            question_types.append(question_type)




        if self.check_words(self.q2_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-5.0-5.9级地震次数'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-6.0-6.9级地震次数'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-7.0级以上地震次数'
            question_types.append(question_type)
        if self.check_words(self.q1_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-地震次数'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-人员伤亡数量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-死亡人数'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_1_31, question) and ('31-不同年份地震情况' in types):
            question_type = '资源与环境-31-直接经济损失'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_32, question) and ('32-海洋灾害情况' in types):
            question_type = '资源与环境-32-发生次数'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_32, question) and ('32-海洋灾害情况' in types):
            question_type = '资源与环境-32-人员死亡失踪'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_32, question) and ('32-海洋灾害情况' in types):
            question_type = '资源与环境-32-直接经济损失'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_33, question) and ('33-海域不同水质面积' in types):
            question_type = '资源与环境-33-第二类水质海域面积'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_33, question) and ('33-海域不同水质面积' in types):
            question_type = '资源与环境-33-第三类水质海域面积'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_33, question) and ('33-海域不同水质面积' in types):
            question_type = '资源与环境-33-劣于第四类水质海域面积'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_33, question) and ('33-海域不同水质面积' in types):
            question_type = '资源与环境-33-第四类水质海域面积'
            question_types.append(question_type)

        if self.check_words(self.q1_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-城镇环境基础设施建设投资'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-燃气建设投资'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-集中供热建设投资'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-排水建设投资'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-园林绿化建设投资'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_34, question) and ('34-不同地区基础建设投资' in types):
            question_type = '资源与环境-34-市容环境卫生建设投资'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-工业污染治理完成投资'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-治理废水投资'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-治理废气投资'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-治理固体废物投资'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-治理噪声投资'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_35_1, question) and ('35-1-不同地区污染治理情况' in types):
            question_type = '资源与环境-35-1-治理其他投资'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-工业污染治理完成投资'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-治理废水投资'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-治理废气投资'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-治理固体废物投资'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-治理噪声投资'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_1_35, question) and ('35-不同年份污染治理情况' in types):
            question_type = '资源与环境-35-治理其他投资'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_1_36, question) and ('36-林业草原投资完成情况' in types):
            question_type = '资源与环境-36-本年完成林业草原投资总计'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_1_36, question) and ('36-林业草原投资完成情况' in types):
            question_type = '资源与环境-36-林业草原国家投资'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_1_36, question) and ('36-林业草原投资完成情况' in types):
            question_type = '资源与环境-36-林业草原生态修复治理投资'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_1_36, question) and ('36-林业草原投资完成情况' in types):
            question_type = '资源与环境-36-林业草原林产品加工制造投资'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_1_36, question) and ('36-林业草原投资完成情况' in types):
            question_type = '资源与环境-36-林业草原林业草原服务保障和公共管理投资'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-国内生产总值'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-第一产业'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-第二产业'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-第三产业'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-农林牧渔业'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-工业'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-建筑业'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-批发和零售业'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-交通运输仓储和邮政业'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-住宿和餐饮业'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-金融业'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-房地产业'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_2_2, question) and ('C03-02国内生产总值构成' in types):
            question_type = '国民经济核算-2-其他'
            question_types.append(question_type)

        if self.check_words(self.q15_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-人均国民总收入'
            question_types.append(question_type)
        if self.check_words(self.q16_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-人均国内生产总值'
            question_types.append(question_type)
        if self.check_words(self.q1_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-国民总收入'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-国内生产总值'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-第一产业'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-第二产业'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-第三产业'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-农林牧渔业'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-工业'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-建筑业'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-批发和零售业'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-交通运输仓储和邮政业'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-住宿和餐饮业'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-金融业'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-房地产业'
            question_types.append(question_type)
        if self.check_words(self.q14_qwds_2_1, question) and ('C03-01国民生产总值' in types):
            question_type = '国民经济核算-1-其他'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-国内生产总值'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-第一产业'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-第二产业'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-第三产业'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-农林牧渔业'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-工业'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-建筑业'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-批发和零售业'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-交通运输仓储和邮政业'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-住宿和餐饮业'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-金融业'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-房地产业'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_2_3, question) and ('C03-03不变价国内生产总值' in types):
            question_type = '国民经济核算-3-其他'
            question_types.append(question_type)


        if self.check_words(self.q15_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-人均国民总收入'
            question_types.append(question_type)
        if self.check_words(self.q16_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-人均国内生产总值'
            question_types.append(question_type)
        if self.check_words(self.q1_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-国民总收入'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-国内生产总值'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-第一产业'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-第二产业'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-第三产业'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-农林牧渔业'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-工业'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-建筑业'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-批发和零售业'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-交通运输仓储和邮政业'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-住宿和餐饮业'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-金融业'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-房地产业'
            question_types.append(question_type)
        if self.check_words(self.q14_qwds_2_4, question) and ('C03-04国内生产总值指数' in types):
            question_type = '国民经济核算-4-其他'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-国内生产总值'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-农林牧渔业'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-采矿业'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-制造业'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-电力热力燃气及水'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-建筑业'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-批发和零售业'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-交通运输仓储和邮政业'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-住宿和餐饮业'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-信息传输软件和信息'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-金融业'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-房地产业'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-租赁和商务服务业'
            question_types.append(question_type)
        if self.check_words(self.q14_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-科学研究和技术服务业'
            question_types.append(question_type)
        if self.check_words(self.q15_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-水利环境和公共设施管理业'
            question_types.append(question_type)
        if self.check_words(self.q16_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-居民服务修理和其他服务业'
            question_types.append(question_type)
        if self.check_words(self.q17_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-教育'
            question_types.append(question_type)
        if self.check_words(self.q18_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-卫生和社会工作'
            question_types.append(question_type)
        if self.check_words(self.q19_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-文化体育和娱乐业'
            question_types.append(question_type)
        if self.check_words(self.q20_qwds_2_6, question) and ('C03-06分行业增加值' in types):
            question_type = '国民经济核算-6-公共管理社会保障'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_7, question) and ('C03-07三次产业和主要行业贡献率' in types):
            question_type = '国民经济核算-7-国内生产总值'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_7, question) and ('C03-07三次产业和主要行业贡献率' in types):
            question_type = '国民经济核算-7-第一产业'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_7, question) and ('C03-07三次产业和主要行业贡献率' in types):
            question_type = '国民经济核算-7-第二产业'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_7, question) and ('C03-07三次产业和主要行业贡献率' in types):
            question_type = '国民经济核算-7-第三产业'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_7, question) and ('C03-07三次产业和主要行业贡献率' in types):
            question_type = '国民经济核算-7-工业'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_7, question) and ('C03-07三次产业和主要行业贡献率' in types):
            question_type = '国民经济核算-7-批发和零售业'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_2_7, question) and ('C03-07三次产业和主要行业贡献率' in types):
            question_type = '国民经济核算-7-金融业'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_8, question) and ('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls' in types):
            question_type = '国民经济核算-8-国内生产总值'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_8, question) and ('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls' in types):
            question_type = '国民经济核算-8-第一产业'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_8, question) and ('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls' in types):
            question_type = '国民经济核算-8-第二产业'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_8, question) and ('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls' in types):
            question_type = '国民经济核算-8-第三产业'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_8, question) and ('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls' in types):
            question_type = '国民经济核算-8-工业'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_8, question) and ('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls' in types):
            question_type = '国民经济核算-8-批发和零售业'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_2_8, question) and ('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls' in types):
            question_type = '国民经济核算-8-金融业'
            question_types.append(question_type)

        if self.check_words(self.q1_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-地区生产总值'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-第一产业增加值'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-第二产业增加值'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-第三产业增加值'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-农林牧渔业增加值'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-工业增加值'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-建筑业增加值'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-批发和零售业增加值'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-交通运输仓储和邮政业增加值'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-住宿和餐饮业增加值'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-金融业增加值'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-房地产业增加值'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_2_9, question) and ('C03-09生产总值' in types):
            question_type = '国民经济核算-9-其他增加值'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_9_2, question) and ('C03-09（2）生产总值占比' in types):
            question_type = '国民经济核算-9-2-人均地区生产总值'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_9_2, question) and ('C03-09（2）生产总值占比' in types):
            question_type = '国民经济核算-9-2-第一产业构成'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_9_2, question) and ('C03-09（2）生产总值占比' in types):
            question_type = '国民经济核算-9-2-第二产业构成'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_9_2, question) and ('C03-09（2）生产总值占比' in types):
            question_type = '国民经济核算-9-2-第三产业构成'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_9_3, question) and ('C03-09（3）生产总值指数' in types):
            question_type = '国民经济核算-9-3-地区生产总值'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_9_3, question) and ('C03-09（3）生产总值指数' in types):
            question_type = '国民经济核算-9-3-第一产业'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_9_3, question) and ('C03-09（3）生产总值指数' in types):
            question_type = '国民经济核算-9-3-第二产业'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_9_3, question) and ('C03-09（3）生产总值指数' in types):
            question_type = '国民经济核算-9-3-第三产业'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_9_3, question) and ('C03-09（3）生产总值指数' in types):
            question_type = '国民经济核算-9-3-人均地区生产总值'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_10, question) and ('C03-10支出法国内生产总值' in types):
            question_type = '国民经济核算-10-生产总值'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_10, question) and ('C03-10支出法国内生产总值' in types):
            question_type = '国民经济核算-10-最终消费'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_10, question) and ('C03-10支出法国内生产总值' in types):
            question_type = '国民经济核算-10-资本形成总额'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_10, question) and ('C03-10支出法国内生产总值' in types):
            question_type = '国民经济核算-10-货物和服务净出口'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_10, question) and ('C03-10支出法国内生产总值' in types):
            question_type = '国民经济核算-10-最终消费率'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_10, question) and ('C03-10支出法国内生产总值' in types):
            question_type = '国民经济核算-10-资本形成率'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_2_11_1, question) and ('C03-11居民消费支出占比' in types):
            question_type = '国民经济核算-11-1-居民消费支出'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_11_1, question) and ('C03-11居民消费支出占比' in types):
            question_type = '国民经济核算-11-1-政府消费支出'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_11_2, question) and ('C03-11最终消费支出' in types):
            question_type = '国民经济核算-11-2-居民消费支出'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_11_2, question) and ('C03-11最终消费支出' in types):
            question_type = '国民经济核算-11-2-城镇居民支出'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_11_2, question) and ('C03-11最终消费支出' in types):
            question_type = '国民经济核算-11-2-农村居民支出'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_11_2, question) and ('C03-11最终消费支出' in types):
            question_type = '国民经济核算-11-2-政府消费支出'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_11_3, question) and ('C03-11最终消费支出占比' in types):
            question_type = '国民经济核算-11-3-居民消费支出'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_11_3, question) and ('C03-11最终消费支出占比' in types):
            question_type = '国民经济核算-11-3-政府消费支出'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_11_4, question) and ('C03-11货物与服务净出口' in types):
            question_type = '国民经济核算-11-4-出口'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_11_4, question) and ('C03-11货物与服务净出口' in types):
            question_type = '国民经济核算-11-4-进口'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_11_5, question) and ('C03-11资本形成总额' in types):
            question_type = '国民经济核算-11-5-固定资本形成总额'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_11_5, question) and ('C03-11资本形成总额' in types):
            question_type = '国民经济核算-11-5-存货变动'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_11_6, question) and ('C03-11资本形成总额占比' in types):
            question_type = '国民经济核算-11-6-固定资本形成总额'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_11_6, question) and ('C03-11资本形成总额占比' in types):
            question_type = '国民经济核算-11-6-存货变动'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_12, question) and ('C03-12实际最终消费构成' in types):
            question_type = '国民经济核算-12-居民实际最终消费'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_12, question) and ('C03-12实际最终消费构成' in types):
            question_type = '国民经济核算-12-政府实际最终消费'
            question_types.append(question_type)

        if self.check_words(self.q1_qwds_2_12_1, question) and ('C03-12（1）实际最终消费' in types):
            question_type = '国民经济核算-12-1-居民实际最终消费'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_12_1, question) and ('C03-12（1）实际最终消费' in types):
            question_type = '国民经济核算-12-1-政府实际最终消费'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_13, question) and ('C03-13生活消费水平' in types):
            question_type = '国民经济核算-13-全体居民绝对数'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_13, question) and ('C03-13生活消费水平' in types):
            question_type = '国民经济核算-13-城镇居民绝对数'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_13, question) and ('C03-13生活消费水平' in types):
            question_type = '国民经济核算-13-农村居民绝对数'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_13, question) and ('C03-13生活消费水平' in types):
            question_type = '国民经济核算-13-城镇居民消费水平与农村居民消费水平的比值'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_13, question) and ('C03-13生活消费水平' in types):
            question_type = '国民经济核算-13-全体居民指数'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_13, question) and ('C03-13生活消费水平' in types):
            question_type = '国民经济核算-13-城镇居民消费指数'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_2_13, question) and ('C03-13生活消费水平' in types):
            question_type = '国民经济核算-13-农村居民消费指数'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_14, question) and ('C03-14三大需求对国内生产总值增长的贡献率和拉动' in types):
            question_type = '国民经济核算-14-最终消费支出贡献率'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_14, question) and ('C03-14三大需求对国内生产总值增长的贡献率和拉动' in types):
            question_type = '国民经济核算-14-最终消费支出拉动'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_14, question) and ('C03-14三大需求对国内生产总值增长的贡献率和拉动' in types):
            question_type = '国民经济核算-14-资本形成总额贡献率'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_14, question) and ('C03-14三大需求对国内生产总值增长的贡献率和拉动' in types):
            question_type = '国民经济核算-14-资本形成总额拉动'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_14, question) and ('C03-14三大需求对国内生产总值增长的贡献率和拉动' in types):
            question_type = '国民经济核算-14-货物和服务净出口贡献率'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_14, question) and ('C03-14三大需求对国内生产总值增长的贡献率和拉动' in types):
            question_type = '国民经济核算-14-货物和服务净出口拉动'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-净金融投资'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-资金运用合计'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-资金来源合计'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-通货'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-存款'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-活期存款'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-定期存款'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-财政存款'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-外汇存款'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-其他存款'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-证券公司客户保证金'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-贷款'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-短期贷款与票据融资'
            question_types.append(question_type)
        if self.check_words(self.q14_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-中长期贷款'
            question_types.append(question_type)
        if self.check_words(self.q15_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-外汇贷款'
            question_types.append(question_type)
        if self.check_words(self.q16_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-委托贷款'
            question_types.append(question_type)
        if self.check_words(self.q17_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-其他贷款'
            question_types.append(question_type)
        if self.check_words(self.q18_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-未贴现的银行承兑汇票'
            question_types.append(question_type)
        if self.check_words(self.q19_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-保险准备金'
            question_types.append(question_type)
        if self.check_words(self.q20_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-金融机构往来'
            question_types.append(question_type)
        if self.check_words(self.q21_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-存款准备金'
            question_types.append(question_type)
        if self.check_words(self.q22_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-债券'
            question_types.append(question_type)
        if self.check_words(self.q23_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-政府债券'
            question_types.append(question_type)
        if self.check_words(self.q24_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-金融债券'
            question_types.append(question_type)
        if self.check_words(self.q25_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-中央银行债券'
            question_types.append(question_type)
        if self.check_words(self.q26_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-企业债券'
            question_types.append(question_type)
        if self.check_words(self.q27_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-股票'
            question_types.append(question_type)
        if self.check_words(self.q28_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-证券投资基金份额'
            question_types.append(question_type)
        if self.check_words(self.q29_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-库存现金'
            question_types.append(question_type)
        if self.check_words(self.q30_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-中央银行贷款'
            question_types.append(question_type)
        if self.check_words(self.q31_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-其他'
            question_types.append(question_type)
        if self.check_words(self.q32_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-直接投资'
            question_types.append(question_type)
        if self.check_words(self.q33_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-其他对外债权债务'
            question_types.append(question_type)
        if self.check_words(self.q34_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-国际储备资产'
            question_types.append(question_type)
        if self.check_words(self.q35_qwds_2_16, question) and ('C03-16资金流量表 (金融交易，2020年)' in types):
            question_type = '国民经济核算-16-国际收支错误与遗漏'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_17, question) and ('C03-17企业、广义政府与住户部门初次分配总收入及比重' in types):
            question_type = '国民经济核算-17-企业部门初次分配总收入'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_17, question) and ('C03-17企业、广义政府与住户部门初次分配总收入及比重' in types):
            question_type = '国民经济核算-17-企业部门占比'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_17, question) and ('C03-17企业、广义政府与住户部门初次分配总收入及比重' in types):
            question_type = '国民经济核算-17-广义政府部门初次分配总收入'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_17, question) and ('C03-17企业、广义政府与住户部门初次分配总收入及比重' in types):
            question_type = '国民经济核算-17-广义政府部门占比'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_17, question) and ('C03-17企业、广义政府与住户部门初次分配总收入及比重' in types):
            question_type = '国民经济核算-17-住户部门初次分配总收入'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_17, question) and ('C03-17企业、广义政府与住户部门初次分配总收入及比重' in types):
            question_type = '国民经济核算-17-住户部门占比'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_2_19, question) and ('C03-19企业、广义政府与住户部门调整后可支配总收入及比重' in types):
            question_type = '国民经济核算-19-企业部门调整后可支配总收入'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_19, question) and ('C03-19企业、广义政府与住户部门调整后可支配总收入及比重' in types):
            question_type = '国民经济核算-19-企业部门调整后占比'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_19, question) and ('C03-19企业、广义政府与住户部门调整后可支配总收入及比重' in types):
            question_type = '国民经济核算-19-广义政府部门调整后可支配总收入'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_19, question) and ('C03-19企业、广义政府与住户部门调整后可支配总收入及比重' in types):
            question_type = '国民经济核算-19-广义政府部门调整后占比'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_19, question) and ('C03-19企业、广义政府与住户部门调整后可支配总收入及比重' in types):
            question_type = '国民经济核算-19-住户部门调整后可支配总收入'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_19, question) and ('C03-19企业、广义政府与住户部门调整后可支配总收入及比重' in types):
            question_type = '国民经济核算-19-住户部门调整后占比'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-农林牧渔产品和服务'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-采掘产品'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-食品和烟草'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-纺织服装鞋及皮革羽绒制品'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-木材加工家具造纸印刷和文教工美用品'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-炼油炼焦和化学产品'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-非金属矿物制品'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-金属冶炼加工及制品'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-机械设备和交通运输设备及电子电气及其他设备'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-其他各类制造产品'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-电力热力燃气和水的生产和供应'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-建筑'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-批发零售运输仓储邮政'
            question_types.append(question_type)
        if self.check_words(self.q14_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-信息传输软件和信息技术服务'
            question_types.append(question_type)
        if self.check_words(self.q15_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-金融和房地产'
            question_types.append(question_type)
        if self.check_words(self.q16_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-科学研究和技术服务'
            question_types.append(question_type)
        if self.check_words(self.q17_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-其他服务'
            question_types.append(question_type)
        if self.check_words(self.q18_qwds_2_22, question) and ('C03-22 2020年投入产出基本流量表(最终使用部分' in types):
            question_type = '国民经济核算-22-中间投入合计'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_3_1, question) and ('C09-01一次能源生产总量及构成' in types):
            question_type = '能源-1-一次能源生产总量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_1, question) and ('C09-01一次能源生产总量及构成' in types):
            question_type = '能源-1-原煤占一次能源生产总量的比重'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_1, question) and ('C09-01一次能源生产总量及构成' in types):
            question_type = '能源-1-原油占一次能源生产总量的比重'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_1, question) and ('C09-01一次能源生产总量及构成' in types):
            question_type = '能源-1-天然气'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_1, question) and ('C09-01一次能源生产总量及构成' in types):
            question_type = '能源-1-一次电力及其他能源'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_3_2, question) and ('C09-02能源消费总量及构成' in types):
            question_type = '能源-2-能源消费总量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_2, question) and ('C09-02能源消费总量及构成' in types):
            question_type = '能源-2-煤炭占能源消费总量的比重'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_2, question) and ('C09-02能源消费总量及构成' in types):
            question_type = '能源-2-石油占能源消费总量的比重'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_2, question) and ('C09-02能源消费总量及构成' in types):
            question_type = '能源-2-天然气占能源消费总量的比重'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_2, question) and ('C09-02能源消费总量及构成' in types):
            question_type = '能源-2-一次电力及其他能源占能源消费总量的比重'
            question_types.append(question_type)

        if self.check_words(self.q1_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-可供消费的能源总量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-一次能源生产总量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-回收量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-进口量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-出口量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-年初年末库存差额'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-能源消费总量'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-渔业'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-工业'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-建筑业'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-邮政业'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-住宿和餐饮业'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-其他'
            question_types.append(question_type)
        if self.check_words(self.q14_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-居民生活'
            question_types.append(question_type)
        if self.check_words(self.q15_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-终端消费'
            question_types.append(question_type)
        if self.check_words(self.q16_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-加工转换损失量'
            question_types.append(question_type)
        if self.check_words(self.q17_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-炼焦'
            question_types.append(question_type)
        if self.check_words(self.q18_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-炼油及煤制油'
            question_types.append(question_type)
        if self.check_words(self.q19_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-损失量'
            question_types.append(question_type)
        if self.check_words(self.q20_qwds_3_3, question) and ('C09-03综合能源平衡表' in types):
            question_type = '能源-3-平衡差额'
            question_types.append(question_type)




        if self.check_words(self.q1_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-石油可供量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-石油生产量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-石油进口量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-石油出口量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-石油年初年末库存差额'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-农林牧渔业中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-工业中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-建筑业中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-交通运输仓储和邮政业中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-批发和零售业住宿和餐饮业中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-其他中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-居民生活中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q14_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-终端消费中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q15_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-中间消费中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q16_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-火力发电中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q17_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-供热中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q18_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-制气中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q19_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-炼油损失量中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q20_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-损失量中石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q21_qwds_3_4, question) and ('C09-04石油平衡表' in types):
            question_type = '能源-4-石油平衡差额'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-煤炭可供量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-煤炭生产量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-煤炭进口量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-煤炭出口量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-煤炭年初年末库存差额'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-农林牧渔业中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-工业中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-建筑业中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-交通运输仓储和邮政业中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-批发和零售业住宿和餐饮业中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-其他中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-居民生活中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q14_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-终端消费中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q15_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-中间消费中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q16_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-火力发电中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q17_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-供热中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q18_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-炼焦中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q19_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-煤制油中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q20_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-制气中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q21_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-洗选损耗中煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q22_qwds_3_5, question) and ('C09-05煤炭平衡表' in types):
            question_type = '能源-5-煤炭平衡差额'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-可供量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-电力生产量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-水电生产量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-火电生产量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-核电生产量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-风电生产量'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-电力进口量'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-电力出口量'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-电力消费量'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-农林牧渔业中电力消费量'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-工业中电力消费量'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-建筑业中电力消费量'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-交通运输仓储和邮政业中电力消费量'
            question_types.append(question_type)
        if self.check_words(self.q14_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-批发和零售业住宿和餐饮业中电力消费量'
            question_types.append(question_type)
        if self.check_words(self.q15_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-其他中电力消费量'
            question_types.append(question_type)
        if self.check_words(self.q16_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-居民生活中电力消费量'
            question_types.append(question_type)
        if self.check_words(self.q17_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-终端消费中电力消费量'
            question_types.append(question_type)
        if self.check_words(self.q18_qwds_3_6, question) and ('C09-06电力平衡表' in types):
            question_type = '能源-6-输配电损失量'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_3_7, question) and ('C09-07能源生产弹性系数' in types):
            question_type = '能源-7-能源生产比上年增长'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_7, question) and ('C09-07能源生产弹性系数' in types):
            question_type = '能源-7-电力生产比上年增长'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_7, question) and ('C09-07能源生产弹性系数' in types):
            question_type = '能源-7-国内生产总值比上年增长'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_7, question) and ('C09-07能源生产弹性系数' in types):
            question_type = '能源-7-能源生产弹性系数'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_7, question) and ('C09-07能源生产弹性系数' in types):
            question_type = '能源-7-电力生产弹性系数'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_3_8, question) and ('C09-08.能源消费弹性系数' in types):
            question_type = '能源-8-能源消费比上年增长'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_8, question) and ('C09-08.能源消费弹性系数' in types):
            question_type = '能源-8-电力消费比上年增长'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_8, question) and ('C09-08.能源消费弹性系数' in types):
            question_type = '能源-8-国内消费总值比上年增长'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_8, question) and ('C09-08.能源消费弹性系数' in types):
            question_type = '能源-8-能源消费弹性系数'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_8, question) and ('C09-08.能源消费弹性系数' in types):
            question_type = '能源-8-电力消费弹性系数'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_3_9, question) and ('C09-09按行业分能源消费量 (2020年)' in types):
            question_type = '能源-9-能源消费总量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_9, question) and ('C09-09按行业分能源消费量 (2020年)' in types):
            question_type = '能源-9-煤炭'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_9, question) and ('C09-09按行业分能源消费量 (2020年)' in types):
            question_type = '能源-9-焦炭'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_9, question) and ('C09-09按行业分能源消费量 (2020年)' in types):
            question_type = '能源-9-原油'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_9, question) and ('C09-09按行业分能源消费量 (2020年)' in types):
            question_type = '能源-9-汽油'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_3_9, question) and ('C09-09按行业分能源消费量 (2020年)' in types):
            question_type = '能源-9-煤油'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_3_9, question) and ('C09-09按行业分能源消费量 (2020年)' in types):
            question_type = '能源-9-柴油'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_3_9, question) and ('C09-09按行业分能源消费量 (2020年)' in types):
            question_type = '能源-9-燃料油'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_3_9, question) and ('C09-09按行业分能源消费量 (2020年)' in types):
            question_type = '能源-9-天然气'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_3_9, question) and ('C09-09按行业分能源消费量 (2020年)' in types):
            question_type = '能源-9-电力'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_3_10, question) and ('C09-10能源加工转换效率' in types):
            question_type = '能源-10-总效率'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_10, question) and ('C09-10能源加工转换效率' in types):
            question_type = '能源-10-发电及供热'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_10, question) and ('C09-10能源加工转换效率' in types):
            question_type = '能源-10-炼焦'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_10, question) and ('C09-10能源加工转换效率' in types):
            question_type = '能源-10-炼油及煤制油'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_3_11, question) and ('C09-11平均每天能源消费量' in types):
            question_type = '能源-11-合计'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_11, question) and ('C09-11平均每天能源消费量' in types):
            question_type = '能源-11-煤炭'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_11, question) and ('C09-11平均每天能源消费量' in types):
            question_type = '能源-11-焦炭'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_11, question) and ('C09-11平均每天能源消费量' in types):
            question_type = '能源-11-原油'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_3_11, question) and ('C09-11平均每天能源消费量' in types):
            question_type = '能源-11-汽油'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_3_11, question) and ('C09-11平均每天能源消费量' in types):
            question_type = '能源-11-煤油'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_3_11, question) and ('C09-11平均每天能源消费量' in types):
            question_type = '能源-11-柴油'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_11, question) and ('C09-11平均每天能源消费量' in types):
            question_type = '能源-11-燃料油'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_3_11, question) and ('C09-11平均每天能源消费量' in types):
            question_type = '能源-11-天然气'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_3_11, question) and ('C09-11平均每天能源消费量' in types):
            question_type = '能源-11-电力'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_3_12, question) and ('C09-12居民生活能源消费量' in types):
            question_type = '能源-12-合计'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_12, question) and ('C09-12居民生活能源消费量' in types):
            question_type = '能源-12-煤炭'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_12, question) and ('C09-12居民生活能源消费量' in types):
            question_type = '能源-12-煤油'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_12, question) and ('C09-12居民生活能源消费量' in types):
            question_type = '能源-12-液化石油气'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_12, question) and ('C09-12居民生活能源消费量' in types):
            question_type = '能源-12-天然气'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_3_12, question) and ('C09-12居民生活能源消费量' in types):
            question_type = '能源-12-煤气'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_3_12, question) and ('C09-12居民生活能源消费量' in types):
            question_type = '能源-12-热力'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_3_12, question) and ('C09-12居民生活能源消费量' in types):
            question_type = '能源-12-电力'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_3_13, question) and ('C09-13人均生活能源消费量' in types):
            question_type = '能源-13-人均生活能源消费量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_13, question) and ('C09-13人均生活能源消费量' in types):
            question_type = '能源-13-煤炭'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_13, question) and ('C09-13人均生活能源消费量' in types):
            question_type = '能源-13-电力'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_13, question) and ('C09-13人均生活能源消费量' in types):
            question_type = '能源-13-液化石油气'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_13, question) and ('C09-13人均生活能源消费量' in types):
            question_type = '能源-13-天然气'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_3_13, question) and ('C09-13人均生活能源消费量' in types):
            question_type = '能源-13-煤气'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-北京'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-天津'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-河北'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-山西'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-内蒙古'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-辽宁'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-吉林'
            question_types.append(question_type)
        if self.check_words(self.q8_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-黑龙江'
            question_types.append(question_type)
        if self.check_words(self.q9_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-上海'
            question_types.append(question_type)
        if self.check_words(self.q10_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-江苏'
            question_types.append(question_type)
        if self.check_words(self.q11_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-浙江'
            question_types.append(question_type)
        if self.check_words(self.q12_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-安徽'
            question_types.append(question_type)
        if self.check_words(self.q13_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-福建'
            question_types.append(question_type)
        if self.check_words(self.q14_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-江西'
            question_types.append(question_type)
        if self.check_words(self.q15_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-山东'
            question_types.append(question_type)
        if self.check_words(self.q16_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-河南'
            question_types.append(question_type)
        if self.check_words(self.q17_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-湖北'
            question_types.append(question_type)
        if self.check_words(self.q18_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-湖南'
            question_types.append(question_type)
        if self.check_words(self.q19_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-广东'
            question_types.append(question_type)
        if self.check_words(self.q20_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-广西'
            question_types.append(question_type)
        if self.check_words(self.q21_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-海南'
            question_types.append(question_type)
        if self.check_words(self.q22_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-重庆'
            question_types.append(question_type)
        if self.check_words(self.q23_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-四川'
            question_types.append(question_type)
        if self.check_words(self.q24_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-贵州'
            question_types.append(question_type)
        if self.check_words(self.q25_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-云南'
            question_types.append(question_type)
        if self.check_words(self.q26_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-西藏'
            question_types.append(question_type)
        if self.check_words(self.q27_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-陕西'
            question_types.append(question_type)
        if self.check_words(self.q28_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-甘肃'
            question_types.append(question_type)
        if self.check_words(self.q29_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-青海'
            question_types.append(question_type)
        if self.check_words(self.q30_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-宁夏'
            question_types.append(question_type)
        if self.check_words(self.q31_qwds_3_14, question) and ('C09-14分地区电力能源消费量' in types):
            question_type = '能源-14-新疆'
            question_types.append(question_type)


        if self.check_words(self.q1_qwds_3_15, question) and ('C09-15发电装机容量' in types):
            question_type = '能源-15-发电装机容量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_15, question) and ('C09-15发电装机容量' in types):
            question_type = '能源-15-火电'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_15, question) and ('C09-15发电装机容量' in types):
            question_type = '能源-15-水电'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_15, question) and ('C09-15发电装机容量' in types):
            question_type = '能源-15-核电'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_15, question) and ('C09-15发电装机容量' in types):
            question_type = '能源-15-风电'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_3_15, question) and ('C09-15发电装机容量' in types):
            question_type = '能源-15-太阳能发电'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_3_15, question) and ('C09-15发电装机容量' in types):
            question_type = '能源-15-其他'
            question_types.append(question_type)



        if self.check_words(self.q1_qwds_3_16, question) and ('C09-16万元国内生产总值能源消费量' in types):
            question_type = '能源-16-国内生产总值能源消费量'
            question_types.append(question_type)
        if self.check_words(self.q2_qwds_3_16, question) and ('C09-16万元国内生产总值能源消费量' in types):
            question_type = '能源-16-国内生产总值煤炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q3_qwds_3_16, question) and ('C09-16万元国内生产总值能源消费量' in types):
            question_type = '能源-16-国内生产总值焦炭消费量'
            question_types.append(question_type)
        if self.check_words(self.q4_qwds_3_16, question) and ('C09-16万元国内生产总值能源消费量' in types):
            question_type = '能源-16-国内生产总值石油消费量'
            question_types.append(question_type)
        if self.check_words(self.q5_qwds_3_16, question) and ('C09-16万元国内生产总值能源消费量' in types):
            question_type = '能源-16-国内生产总值原油消费量'
            question_types.append(question_type)
        if self.check_words(self.q6_qwds_3_16, question) and ('C09-16万元国内生产总值能源消费量' in types):
            question_type = '能源-16-国内生产总值燃料油消费量'
            question_types.append(question_type)
        if self.check_words(self.q7_qwds_3_16, question) and ('C09-16万元国内生产总值能源消费量' in types):
            question_type = '能源-16-国内生产总值电力消费量'
            question_types.append(question_type)

        # 将多个分类结果进行合并处理，组装成一个字典
        if len(question_types)==0:
            data['question_types']={}
        else:
            data['question_types'] = question_types
        # print("data:",data)
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
            if wd in self.buguosheng_wds_2_3:
                wd_dict[wd].append('C03-03不变价国内生产总值')
            if wd in self.guoshengzhi_wds_2_4:
                wd_dict[wd].append('C03-04国内生产总值指数')
            if wd in self.fenzeng_wds_2_6:
                wd_dict[wd].append('C03-06分行业增加值')
            if wd in self.yegong_wds_2_7:
                wd_dict[wd].append('C03-07三次产业和主要行业贡献率')
            if wd in self.yela_wds_2_8:
                wd_dict[wd].append('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls')
            if wd in self.shengzong_wds_2_9:
                wd_dict[wd].append('C03-09生产总值')
            if wd in self.shengzong_wds_2_9_2:
                wd_dict[wd].append('C03-09（2）生产总值占比')
            if wd in self.shengzong_wds_2_9_3:
                wd_dict[wd].append('C03-09（3）生产总值指数')
            if wd in self.zhizong_wds_2_10:
                wd_dict[wd].append('C03-10支出法国内生产总值')
            if wd in self.juzhi_wds_2_11_1:
                wd_dict[wd].append('C03-11居民消费支出占比')
            if wd in self.zuizhi_wds_2_11_2:
                wd_dict[wd].append('C03-11最终消费支出')
            if wd in self.zuizhi_wds_2_11_3:
                wd_dict[wd].append('C03-11最终消费支出占比')
            if wd in self.jinchu_wds_2_11_4:
                wd_dict[wd].append('C03-11货物与服务净出口')
            if wd in self.zizong_wds_2_11_5:
                wd_dict[wd].append('C03-11资本形成总额')
            if wd in self.zizong_wds_2_11_6:
                wd_dict[wd].append('C03-11资本形成总额占比')
            if wd in self.shixiao_wds_2_12:
                wd_dict[wd].append('C03-12实际最终消费构成')
            if wd in self.shixiao_wds_2_12_1:
                wd_dict[wd].append('C03-12（1）实际最终消费')
            if wd in self.shengxiao_wds_2_13:
                wd_dict[wd].append('C03-13生活消费水平')
            if wd in self.gongla_wds_2_14:
                wd_dict[wd].append('C03-14三大需求对国内生产总值增长的贡献率和拉动')
            if wd in self.ziliu_wds_2_16:
                wd_dict[wd].append('C03-16资金流量表 (金融交易，2020年)')
            if wd in self.shoubi_wds_2_17:
                wd_dict[wd].append('C03-17企业、广义政府与住户部门初次分配总收入及比重')
            if wd in self.tiaoshoubi_wds_2_19:
                wd_dict[wd].append('C03-19企业、广义政府与住户部门调整后可支配总收入及比重')
            if wd in self.touchan_wds_2_22:
                wd_dict[wd].append('C03-22 2020年投入产出基本流量表(最终使用部分')
            if wd in self.yizong_wds_3_1:
                wd_dict[wd].append('C09-01一次能源生产总量及构成')
            if wd in self.nengzong_wds_3_2:
                wd_dict[wd].append('C09-02能源消费总量及构成')
            if wd in self.zongneng_wds_3_3:
                wd_dict[wd].append('C09-03综合能源平衡表')
            if wd in self.shiping_wds_3_4:
                wd_dict[wd].append('C09-04石油平衡表')
            if wd in self.meiping_wds_3_5:
                wd_dict[wd].append('C09-05煤炭平衡表')
            if wd in self.dianping_wds_3_6:
                wd_dict[wd].append('C09-06电力平衡表')
            if wd in self.nengsheng_wds_3_7:
                wd_dict[wd].append('C09-07能源生产弹性系数')
            if wd in self.nengxiao_wds_3_8:
                wd_dict[wd].append('C09-08.能源消费弹性系数')
            if wd in self.hangneng_wds_3_9:
                wd_dict[wd].append('C09-09按行业分能源消费量 (2020年)')
            if wd in self.nengjia_wds_3_10:
                wd_dict[wd].append('C09-10能源加工转换效率')
            if wd in self.pingneng_wds_3_11:
                wd_dict[wd].append('C09-11平均每天能源消费量')
            if wd in self.juneng_wds_3_12:
                wd_dict[wd].append('C09-12居民生活能源消费量')
            if wd in self.rensheng_wds_3_13:
                wd_dict[wd].append('C09-13人均生活能源消费量')
            if wd in self.fendian_wds_3_14:
                wd_dict[wd].append('C09-14分地区电力能源消费量')
            if wd in self.fazhuang_wds_3_15:
                wd_dict[wd].append('C09-15发电装机容量')
            if wd in self.guoneng_wds_3_16:
                wd_dict[wd].append('C09-16万元国内生产总值能源消费量')



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