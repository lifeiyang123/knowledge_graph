class QuestionPaser:

    '''构建实体节点'''
    def build_entitydict(self, args):
        entity_dict = {}
        for arg, types in args.items():
            for type in types:
                if type not in entity_dict:
                    entity_dict[type] = [arg]
                else:
                    entity_dict[type].append(arg)

        return entity_dict

    '''解析主函数'''
    def parser_main(self, res_classify):
        #提取出实体
        args = res_classify['args']
        entity_dict = self.build_entitydict(args)
        # print(entity_dict)
        #提取出查询类型
        question_types = res_classify['question_types']
        sqls = []
        for question_type in question_types:
            sql_ = {}
            sql_['question_type'] = question_type
            sql = []
            if question_type == '资源与环境-1-面积':
                sql = self.sql_transfer(question_type, entity_dict.get('1-土地面积'))

            elif question_type == '资源与环境-2-流域面积':
                sql = self.sql_transfer(question_type, entity_dict.get('2-河流面积'))
            elif question_type == '资源与环境-2-河长':
                sql = self.sql_transfer(question_type, entity_dict.get('2-河流面积'))
            elif question_type == '资源与环境-2-年径流量':
                sql = self.sql_transfer(question_type, entity_dict.get('2-河流面积'))

            elif question_type == '资源与环境-3-流域面积':
                sql = self.sql_transfer(question_type, entity_dict.get('3-流域面积'))
            elif question_type == '资源与环境-3-面积占比':
                sql = self.sql_transfer(question_type, entity_dict.get('3-流域面积'))

            elif question_type == '资源与环境-4-2020年产量':
                sql = self.sql_transfer(question_type, entity_dict.get('4-矿产产量'))
            elif question_type == '资源与环境-4-2021年产量':
                sql = self.sql_transfer(question_type, entity_dict.get('4-矿产产量'))

            elif question_type == '资源与环境-5-1月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-2月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-3月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-4月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-5月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-6月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-7月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-8月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-9月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-10月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-11月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-12月温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))
            elif question_type == '资源与环境-5-年平均温度':
                sql = self.sql_transfer(question_type, entity_dict.get('5-城市温度'))

            elif question_type == '资源与环境-6-1月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-2月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-3月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-4月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-5月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-6月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-7月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-8月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-9月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-10月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-11月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-12月湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))
            elif question_type == '资源与环境-6-年平均湿度':
                sql = self.sql_transfer(question_type, entity_dict.get('6-城市湿度'))

            elif question_type == '资源与环境-7-1月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-2月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-3月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-4月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-5月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-6月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-7月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-8月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-9月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-10月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-11月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-12月降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))
            elif question_type == '资源与环境-7-全年降水量':
                sql = self.sql_transfer(question_type, entity_dict.get('7-城市降水量'))


            elif question_type == '资源与环境-8-1月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-2月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-3月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-4月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-5月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-6月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-7月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-8月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-9月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-10月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-11月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-12月日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))
            elif question_type == '资源与环境-8-全年日照时数':
                sql = self.sql_transfer(question_type, entity_dict.get('8-城市日照时间数'))

            elif question_type == '资源与环境-9-水资源总量':
                sql = self.sql_transfer(question_type, entity_dict.get('9-1-不同地区水资源总量'))
            elif question_type == '资源与环境-9-地表水资源量':
                sql = self.sql_transfer(question_type, entity_dict.get('9-1-不同地区水资源总量'))
            elif question_type == '资源与环境-9-地下水资源量':
                sql = self.sql_transfer(question_type, entity_dict.get('9-1-不同地区水资源总量'))
            elif question_type == '资源与环境-9-地表水与地下水资源重复量':
                sql = self.sql_transfer(question_type, entity_dict.get('9-1-不同地区水资源总量'))
            elif question_type == '资源与环境-9-人均水资源量':
                sql = self.sql_transfer(question_type, entity_dict.get('9-1-不同地区水资源总量'))

            elif question_type == '资源与环境-9-1-水资源总量':
                sql = self.sql_transfer(question_type, entity_dict.get('9-不同年份水资源总量'))
            elif question_type == '资源与环境-9-1-地表水资源量':
                sql = self.sql_transfer(question_type, entity_dict.get('9-不同年份水资源总量'))
            elif question_type == '资源与环境-9-1-地下水资源量':
                sql = self.sql_transfer(question_type, entity_dict.get('9-不同年份水资源总量'))
            elif question_type == '资源与环境-9-1-地表水与地下水资源重复量':
                sql = self.sql_transfer(question_type, entity_dict.get('9-不同年份水资源总量'))
            elif question_type == '资源与环境-9-1-人均水资源量':
                sql = self.sql_transfer(question_type, entity_dict.get('9-不同年份水资源总量'))


            elif question_type == '资源与环境-10-1-供水总量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-1-不同地区供水总量'))
            elif question_type == '资源与环境-10-1-地表水供水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-1-不同地区供水总量'))
            elif question_type == '资源与环境-10-1-地下水供水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-1-不同地区供水总量'))
            elif question_type == '资源与环境-10-1-其他供水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-1-不同地区供水总量'))
            elif question_type == '资源与环境-10-1-用水总量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-1-不同地区供水总量'))
            elif question_type == '资源与环境-10-1-农业用水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-1-不同地区供水总量'))
            elif question_type == '资源与环境-10-1-工业用水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-1-不同地区供水总量'))
            elif question_type == '资源与环境-10-1-生活用水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-1-不同地区供水总量'))
            elif question_type == '资源与环境-10-1-人工生态环境补水用水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-1-不同地区供水总量'))
            elif question_type == '资源与环境-10-1-人均用水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-1-不同地区供水总量'))


            elif question_type == '资源与环境-10-供水总量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-不同年份供水总量'))
            elif question_type == '资源与环境-10-地表水供水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-不同年份供水总量'))
            elif question_type == '资源与环境-10-地下水供水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-不同年份供水总量'))
            elif question_type == '资源与环境-10-其他供水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-不同年份供水总量'))
            elif question_type == '资源与环境-10-用水总量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-不同年份供水总量'))
            elif question_type == '资源与环境-10-农业用水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-不同年份供水总量'))
            elif question_type == '资源与环境-10-工业用水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-不同年份供水总量'))
            elif question_type == '资源与环境-10-生活用水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-不同年份供水总量'))
            elif question_type == '资源与环境-10-人工生态环境补水用水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-不同年份供水总量'))
            elif question_type == '资源与环境-10-人均用水量':
                sql = self.sql_transfer(question_type, entity_dict.get('10-不同年份供水总量'))


            elif question_type == '资源与环境-11-废水中化学需氧量排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))
            elif question_type == '资源与环境-11-废水中氨氮排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))
            elif question_type == '资源与环境-11-废水中总氮排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))
            elif question_type == '资源与环境-11-废水中总磷排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))
            elif question_type == '资源与环境-11-废水中石油类排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))
            elif question_type == '资源与环境-11-废水中挥发酚排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))
            elif question_type == '资源与环境-11-废水中总铅排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))
            elif question_type == '资源与环境-11-废水中总汞排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))
            elif question_type == '资源与环境-11-废水中总镉排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))
            elif question_type == '资源与环境-11-废水中六价铬排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))
            elif question_type == '资源与环境-11-废水中总铬排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))
            elif question_type == '资源与环境-11-废水中总砷排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('11-不用地区废水污染物含量'))

            elif question_type == '资源与环境-12-城市废水中工业化学需氧量排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('12-不同城市废水污染物含量'))
            elif question_type == '资源与环境-12-城市废水中工业氨氮排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('12-不同城市废水污染物含量'))
            elif question_type == '资源与环境-12-城市废水中生活化学需氧量排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('12-不同城市废水污染物含量'))
            elif question_type == '资源与环境-12-城市废水中生活氨氮排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('12-不同城市废水污染物含量'))


            elif question_type == '资源与环境-13-二氧化硫排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('13-不同地区废气污染物含量'))
            elif question_type == '资源与环境-13-氮氧化物排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('13-不同地区废气污染物含量'))
            elif question_type == '资源与环境-13-颗粒物排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('13-不同地区废气污染物含量'))

            elif question_type == '资源与环境-14-工业二氧化硫排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('14-不同城市废气污染物含量'))
            elif question_type == '资源与环境-14-工业氮氧化物排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('14-不同城市废气污染物含量'))
            elif question_type == '资源与环境-14-工业颗粒物排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('14-不同城市废气污染物含量'))
            elif question_type == '资源与环境-14-生活及其他二氧化硫排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('14-不同城市废气污染物含量'))
            elif question_type == '资源与环境-14-生活及其他氮氧化物排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('14-不同城市废气污染物含量'))
            elif question_type == '资源与环境-14-生活及其他颗粒物排放量':
                sql = self.sql_transfer(question_type, entity_dict.get('14-不同城市废气污染物含量'))


            elif question_type == '资源与环境-15-一般工业固体废物产生量':
                sql = self.sql_transfer(question_type, entity_dict.get('15-不同地区固体废物处理情况'))
            elif question_type == '资源与环境-15-一般工业固体废物综合利用量':
                sql = self.sql_transfer(question_type, entity_dict.get('15-不同地区固体废物处理情况'))
            elif question_type == '资源与环境-15-一般工业固体废物处置量':
                sql = self.sql_transfer(question_type, entity_dict.get('15-不同地区固体废物处理情况'))
            elif question_type == '资源与环境-15-一般工业固体废物贮存量':
                sql = self.sql_transfer(question_type, entity_dict.get('15-不同地区固体废物处理情况'))
            elif question_type == '资源与环境-15-一般工业固体废物倾倒丢弃量':
                sql = self.sql_transfer(question_type, entity_dict.get('15-不同地区固体废物处理情况'))
            elif question_type == '资源与环境-15-危险废物产生量':
                sql = self.sql_transfer(question_type, entity_dict.get('15-不同地区固体废物处理情况'))
            elif question_type == '资源与环境-15-危险废物利用处置量':
                sql = self.sql_transfer(question_type, entity_dict.get('15-不同地区固体废物处理情况'))
            elif question_type == '资源与环境-15-危险废物本年末贮存量':
                sql = self.sql_transfer(question_type, entity_dict.get('15-不同地区固体废物处理情况'))


            elif question_type == '资源与环境-16-一般工业固体废物产生量':
                sql = self.sql_transfer(question_type, entity_dict.get('16-不同城市固体废物处理情况'))
            elif question_type == '资源与环境-16-一般工业固体废物综合利用量':
                sql = self.sql_transfer(question_type, entity_dict.get('16-不同城市固体废物处理情况'))
            elif question_type == '资源与环境-16-一般工业固体废物处置量':
                sql = self.sql_transfer(question_type, entity_dict.get('16-不同城市固体废物处理情况'))
            elif question_type == '资源与环境-16-一般工业固体废物贮存量':
                sql = self.sql_transfer(question_type, entity_dict.get('16-不同城市固体废物处理情况'))



            elif question_type == '资源与环境-17-二氧化硫年平均浓度':
                sql = self.sql_transfer(question_type, entity_dict.get('17-不同城市空气污染物含量'))
            elif question_type == '资源与环境-17-二氧化氮年平均浓度':
                sql = self.sql_transfer(question_type, entity_dict.get('17-不同城市空气污染物含量'))
            elif question_type == '资源与环境-17-可吸入颗粒物年平均浓度':
                sql = self.sql_transfer(question_type, entity_dict.get('17-不同城市空气污染物含量'))
            elif question_type == '资源与环境-17-一氧化碳日均值第95百分位浓度':
                sql = self.sql_transfer(question_type, entity_dict.get('17-不同城市空气污染物含量'))
            elif question_type == '资源与环境-17-臭氧日最大8小时第90百分位浓度':
                sql = self.sql_transfer(question_type, entity_dict.get('17-不同城市空气污染物含量'))
            elif question_type == '资源与环境-17-细颗粒物年平均浓度':
                sql = self.sql_transfer(question_type, entity_dict.get('17-不同城市空气污染物含量'))
            elif question_type == '资源与环境-17-空气质量优良天数比例':
                sql = self.sql_transfer(question_type, entity_dict.get('17-不同城市空气污染物含量'))


            elif question_type == '资源与环境-18-生活垃圾清运量':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-无害化处理厂数':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-卫生填埋厂数':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-焚烧厂数':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-其他厂数':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-无害化处理能力':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-卫生填埋处理能力':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-焚烧处理能力':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-其他处理能力':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-无害化处理量':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-卫生填埋处理量':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-焚烧处理量':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-其他处理量':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))
            elif question_type == '资源与环境-18-生活垃圾无害化处理率':
                sql = self.sql_transfer(question_type, entity_dict.get('18-不同地区垃圾处理情况'))

            elif question_type == '资源与环境-19-道路交通噪声等效声级':
                sql = self.sql_transfer(question_type, entity_dict.get('19-不同城市噪声污染情况'))
            elif question_type == '资源与环境-19-区域环境噪声等效声级':
                sql = self.sql_transfer(question_type, entity_dict.get('19-不同城市噪声污染情况'))

            elif question_type == '资源与环境-20-2013耕地面积':
                sql = self.sql_transfer(question_type, entity_dict.get('20-不同地区耕地面积情况'))
            elif question_type == '资源与环境-20-2014耕地面积':
                sql = self.sql_transfer(question_type, entity_dict.get('20-不同地区耕地面积情况'))
            elif question_type == '资源与环境-20-2015耕地面积':
                sql = self.sql_transfer(question_type, entity_dict.get('20-不同地区耕地面积情况'))
            elif question_type == '资源与环境-20-2016耕地面积':
                sql = self.sql_transfer(question_type, entity_dict.get('20-不同地区耕地面积情况'))
            elif question_type == '资源与环境-20-2017耕地面积':
                sql = self.sql_transfer(question_type, entity_dict.get('20-不同地区耕地面积情况'))
            elif question_type == '资源与环境-20-2019耕地面积':
                sql = self.sql_transfer(question_type, entity_dict.get('20-不同地区耕地面积情况'))


            elif question_type == '资源与环境-21-耕地':
                sql = self.sql_transfer(question_type, entity_dict.get('21-不同地区用地情况'))
            elif question_type == '资源与环境-21-园地':
                sql = self.sql_transfer(question_type, entity_dict.get('21-不同地区用地情况'))
            elif question_type == '资源与环境-21-林地':
                sql = self.sql_transfer(question_type, entity_dict.get('21-不同地区用地情况'))
            elif question_type == '资源与环境-21-草地':
                sql = self.sql_transfer(question_type, entity_dict.get('21-不同地区用地情况'))
            elif question_type == '资源与环境-21-湿地':
                sql = self.sql_transfer(question_type, entity_dict.get('21-不同地区用地情况'))
            elif question_type == '资源与环境-21-城镇村及工矿用地':
                sql = self.sql_transfer(question_type, entity_dict.get('21-不同地区用地情况'))
            elif question_type == '资源与环境-21-交通运输用地':
                sql = self.sql_transfer(question_type, entity_dict.get('21-不同地区用地情况'))
            elif question_type == '资源与环境-21-水域及水利设施用地':
                sql = self.sql_transfer(question_type, entity_dict.get('21-不同地区用地情况'))


            elif question_type == '资源与环境-22-林业用地面积':
                sql = self.sql_transfer(question_type, entity_dict.get('22-不同地区森林资源情况'))
            elif question_type == '资源与环境-22-森林面积':
                sql = self.sql_transfer(question_type, entity_dict.get('22-不同地区森林资源情况'))
            elif question_type == '资源与环境-22-人工林':
                sql = self.sql_transfer(question_type, entity_dict.get('22-不同地区森林资源情况'))
            elif question_type == '资源与环境-22-森林覆盖率':
                sql = self.sql_transfer(question_type, entity_dict.get('22-不同地区森林资源情况'))
            elif question_type == '资源与环境-22-活立木总蓄积量':
                sql = self.sql_transfer(question_type, entity_dict.get('22-不同地区森林资源情况'))
            elif question_type == '资源与环境-22-森林蓄积量':
                sql = self.sql_transfer(question_type, entity_dict.get('22-不同地区森林资源情况'))


            elif question_type == '资源与环境-23-1-造林总面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-1-不同地区造林面积'))
            elif question_type == '资源与环境-23-1-人工造林面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-1-不同地区造林面积'))
            elif question_type == '资源与环境-23-1-飞播造林面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-1-不同地区造林面积'))
            elif question_type == '资源与环境-23-1-封山育林面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-1-不同地区造林面积'))
            elif question_type == '资源与环境-23-1-退化林修复面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-1-不同地区造林面积'))
            elif question_type == '资源与环境-23-1-人工更新面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-1-不同地区造林面积'))


            elif question_type == '资源与环境-23-造林总面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-不同年份造林面积'))
            elif question_type == '资源与环境-23-人工造林面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-不同年份造林面积'))
            elif question_type == '资源与环境-23-飞播造林面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-不同年份造林面积'))
            elif question_type == '资源与环境-23-封山育林面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-不同年份造林面积'))
            elif question_type == '资源与环境-23-退化林修复面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-不同年份造林面积'))
            elif question_type == '资源与环境-23-人工更新面积':
                sql = self.sql_transfer(question_type, entity_dict.get('23-不同年份造林面积'))



            elif question_type == '资源与环境-24-种草面积':
                sql = self.sql_transfer(question_type, entity_dict.get('24-不同地区草原建设情况'))
            elif question_type == '资源与环境-24-草原改良面积':
                sql = self.sql_transfer(question_type, entity_dict.get('24-不同地区草原建设情况'))
            elif question_type == '资源与环境-24-草原鼠害发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('24-不同地区草原建设情况'))
            elif question_type == '资源与环境-24-草原鼠害防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('24-不同地区草原建设情况'))
            elif question_type == '资源与环境-24-草原虫害发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('24-不同地区草原建设情况'))
            elif question_type == '资源与环境-24-草原虫害防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('24-不同地区草原建设情况'))
            elif question_type == '资源与环境-24-草原火灾受害面积':
                sql = self.sql_transfer(question_type, entity_dict.get('24-不同地区草原建设情况'))


            elif question_type == '资源与环境-25-国家级自然保护区个数':
                sql = self.sql_transfer(question_type, entity_dict.get('25-不同地区自然保护情况'))
            elif question_type == '资源与环境-25-国家级自然保护区面积':
                sql = self.sql_transfer(question_type, entity_dict.get('25-不同地区自然保护情况'))



            elif question_type == '资源与环境-26-农作物受灾面积合计':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-农作物绝收面积合计':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-旱灾受灾面积':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-旱灾绝收面积':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-洪涝地质灾害和台风受灾面积':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-洪涝地质灾害和台风绝收面积':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-风雹灾害受灾面积':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-风雹灾害绝收面积':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-低温冷冻和雪灾受灾面积':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-低温冷冻和雪灾绝收面积':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-受灾人口':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-死亡人口':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))
            elif question_type == '资源与环境-26-直接经济损失':
                sql = self.sql_transfer(question_type, entity_dict.get('26-不同地区自然灾害情况'))


            elif question_type == '资源与环境-27-1-发生地质灾害数量':
                sql = self.sql_transfer(question_type, entity_dict.get('27-1-不同地区地质灾害情况'))
            elif question_type == '资源与环境-27-1-滑坡次数':
                sql = self.sql_transfer(question_type, entity_dict.get('27-1-不同地区地质灾害情况'))
            elif question_type == '资源与环境-27-1-崩塌次数':
                sql = self.sql_transfer(question_type, entity_dict.get('27-1-不同地区地质灾害情况'))
            elif question_type == '资源与环境-27-1-泥石流次数':
                sql = self.sql_transfer(question_type, entity_dict.get('27-1-不同地区地质灾害情况'))
            elif question_type == '资源与环境-27-1-地面塌陷次数':
                sql = self.sql_transfer(question_type, entity_dict.get('27-1-不同地区地质灾害情况'))
            elif question_type == '资源与环境-27-1-人员伤亡数量':
                sql = self.sql_transfer(question_type, entity_dict.get('27-1-不同地区地质灾害情况'))
            elif question_type == '资源与环境-27-1-死亡人数':
                sql = self.sql_transfer(question_type, entity_dict.get('27-1-不同地区地质灾害情况'))
            elif question_type == '资源与环境-27-1-直接经济损失':
                sql = self.sql_transfer(question_type, entity_dict.get('27-1-不同地区地质灾害情况'))


            elif question_type == '资源与环境-27-发生地质灾害数量':
                sql = self.sql_transfer(question_type, entity_dict.get('27-不同年份地质灾害情况'))
            elif question_type == '资源与环境-27-滑坡次数':
                sql = self.sql_transfer(question_type, entity_dict.get('27-不同年份地质灾害情况'))
            elif question_type == '资源与环境-27-崩塌次数':
                sql = self.sql_transfer(question_type, entity_dict.get('27-不同年份地质灾害情况'))
            elif question_type == '资源与环境-27-泥石流次数':
                sql = self.sql_transfer(question_type, entity_dict.get('27-不同年份地质灾害情况'))
            elif question_type == '资源与环境-27-地面塌陷次数':
                sql = self.sql_transfer(question_type, entity_dict.get('27-不同年份地质灾害情况'))
            elif question_type == '资源与环境-27-人员伤亡数量':
                sql = self.sql_transfer(question_type, entity_dict.get('27-不同年份地质灾害情况'))
            elif question_type == '资源与环境-27-死亡人数':
                sql = self.sql_transfer(question_type, entity_dict.get('27-不同年份地质灾害情况'))
            elif question_type == '资源与环境-27-直接经济损失':
                sql = self.sql_transfer(question_type, entity_dict.get('27-不同年份地质灾害情况'))


            elif question_type == '资源与环境-28-森林火灾次数':
                sql = self.sql_transfer(question_type, entity_dict.get('28-不同地区森林火灾情况'))
            elif question_type == '资源与环境-28-一般火灾次数':
                sql = self.sql_transfer(question_type, entity_dict.get('28-不同地区森林火灾情况'))
            elif question_type == '资源与环境-28-较大火灾次数':
                sql = self.sql_transfer(question_type, entity_dict.get('28-不同地区森林火灾情况'))
            elif question_type == '资源与环境-28-重大火灾次数':
                sql = self.sql_transfer(question_type, entity_dict.get('28-不同地区森林火灾情况'))
            elif question_type == '资源与环境-28-特别重大火灾次数':
                sql = self.sql_transfer(question_type, entity_dict.get('28-不同地区森林火灾情况'))
            elif question_type == '资源与环境-28-火场总面积':
                sql = self.sql_transfer(question_type, entity_dict.get('28-不同地区森林火灾情况'))
            elif question_type == '资源与环境-28-受害森林面积':
                sql = self.sql_transfer(question_type, entity_dict.get('28-不同地区森林火灾情况'))
            elif question_type == '资源与环境-28-伤亡人数':
                sql = self.sql_transfer(question_type, entity_dict.get('28-不同地区森林火灾情况'))
            elif question_type == '资源与环境-28-其它损失折款':
                sql = self.sql_transfer(question_type, entity_dict.get('28-不同地区森林火灾情况'))


            elif question_type == '资源与环境-29-1-林业有害生物发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-1-不同地区生物灾害情况'))
            elif question_type == '资源与环境-29-1-林业有害生物防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-1-不同地区生物灾害情况'))
            elif question_type == '资源与环境-29-1-林业有害生物防治率':
                sql = self.sql_transfer(question_type, entity_dict.get('29-1-不同地区生物灾害情况'))
            elif question_type == '资源与环境-29-1-森林病害发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-1-不同地区生物灾害情况'))
            elif question_type == '资源与环境-29-1-森林病害防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-1-不同地区生物灾害情况'))
            elif question_type == '资源与环境-29-1-森林虫害发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-1-不同地区生物灾害情况'))
            elif question_type == '资源与环境-29-1-森林虫害防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-1-不同地区生物灾害情况'))
            elif question_type == '资源与环境-29-1-森林鼠害发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-1-不同地区生物灾害情况'))
            elif question_type == '资源与环境-29-1-森林鼠害防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-1-不同地区生物灾害情况'))
            elif question_type == '资源与环境-29-1-有害植物发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-1-不同地区生物灾害情况'))
            elif question_type == '资源与环境-29-1-有害植物防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-1-不同地区生物灾害情况'))

            elif question_type == '资源与环境-29-林业有害生物发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-不同年份生物灾害情况'))
            elif question_type == '资源与环境-29-林业有害生物防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-不同年份生物灾害情况'))
            elif question_type == '资源与环境-29-林业有害生物防治率':
                sql = self.sql_transfer(question_type, entity_dict.get('29-不同年份生物灾害情况'))
            elif question_type == '资源与环境-29-森林病害发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-不同年份生物灾害情况'))
            elif question_type == '资源与环境-29-森林病害防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-不同年份生物灾害情况'))
            elif question_type == '资源与环境-29-森林虫害发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-不同年份生物灾害情况'))
            elif question_type == '资源与环境-29-森林虫害防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-不同年份生物灾害情况'))
            elif question_type == '资源与环境-29-森林鼠害发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-不同年份生物灾害情况'))
            elif question_type == '资源与环境-29-森林鼠害防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-不同年份生物灾害情况'))
            elif question_type == '资源与环境-29-有害植物发生面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-不同年份生物灾害情况'))
            elif question_type == '资源与环境-29-有害植物防治面积':
                sql = self.sql_transfer(question_type, entity_dict.get('29-不同年份生物灾害情况'))

            elif question_type == '资源与环境-30-突发环境事件次数':
                sql = self.sql_transfer(question_type, entity_dict.get('30-不同地区突发环境事件次数'))
            elif question_type == '资源与环境-30-特别重大环境事件次数':
                sql = self.sql_transfer(question_type, entity_dict.get('30-不同地区突发环境事件次数'))
            elif question_type == '资源与环境-30-重大环境事件次数':
                sql = self.sql_transfer(question_type, entity_dict.get('30-不同地区突发环境事件次数'))
            elif question_type == '资源与环境-30-较大环境事件次数':
                sql = self.sql_transfer(question_type, entity_dict.get('30-不同地区突发环境事件次数'))
            elif question_type == '资源与环境-30-一般环境事件次数':
                sql = self.sql_transfer(question_type, entity_dict.get('30-不同地区突发环境事件次数'))

            elif question_type == '资源与环境-31-1-地震次数':
                sql = self.sql_transfer(question_type, entity_dict.get('31-1-不同地区地震情况'))
            elif question_type == '资源与环境-31-1-5.0-5.9级地震次数':
                sql = self.sql_transfer(question_type, entity_dict.get('31-1-不同地区地震情况'))
            elif question_type == '资源与环境-31-1-6.0-6.9级地震次数':
                sql = self.sql_transfer(question_type, entity_dict.get('31-1-不同地区地震情况'))
            elif question_type == '资源与环境-31-1-7.0级以上地震次数':
                sql = self.sql_transfer(question_type, entity_dict.get('31-1-不同地区地震情况'))
            elif question_type == '资源与环境-31-1-人员伤亡数量':
                sql = self.sql_transfer(question_type, entity_dict.get('31-1-不同地区地震情况'))
            elif question_type == '资源与环境-31-1-死亡人数':
                sql = self.sql_transfer(question_type, entity_dict.get('31-1-不同地区地震情况'))
            elif question_type == '资源与环境-31-1-直接经济损失':
                sql = self.sql_transfer(question_type, entity_dict.get('31-1-不同地区地震情况'))


            elif question_type == '资源与环境-31-地震次数':
                sql = self.sql_transfer(question_type, entity_dict.get('31-不同年份地震情况'))
            elif question_type == '资源与环境-31-5.0-5.9级地震次数':
                sql = self.sql_transfer(question_type, entity_dict.get('31-不同年份地震情况'))
            elif question_type == '资源与环境-31-6.0-6.9级地震次数':
                sql = self.sql_transfer(question_type, entity_dict.get('31-不同年份地震情况'))
            elif question_type == '资源与环境-31-7.0级以上地震次数':
                sql = self.sql_transfer(question_type, entity_dict.get('31-不同年份地震情况'))
            elif question_type == '资源与环境-31-人员伤亡数量':
                sql = self.sql_transfer(question_type, entity_dict.get('31-不同年份地震情况'))
            elif question_type == '资源与环境-31-死亡人数':
                sql = self.sql_transfer(question_type, entity_dict.get('31-不同年份地震情况'))
            elif question_type == '资源与环境-31-直接经济损失':
                sql = self.sql_transfer(question_type, entity_dict.get('31-不同年份地震情况'))


            elif question_type == '资源与环境-32-发生次数':
                sql = self.sql_transfer(question_type, entity_dict.get('32-海洋灾害情况'))
            elif question_type == '资源与环境-32-人员死亡失踪':
                sql = self.sql_transfer(question_type, entity_dict.get('32-海洋灾害情况'))
            elif question_type == '资源与环境-32-直接经济损失':
                sql = self.sql_transfer(question_type, entity_dict.get('32-海洋灾害情况'))

            elif question_type == '资源与环境-33-第二类水质海域面积':
                sql = self.sql_transfer(question_type, entity_dict.get('33-海域不同水质面积'))
            elif question_type == '资源与环境-33-第三类水质海域面积':
                sql = self.sql_transfer(question_type, entity_dict.get('33-海域不同水质面积'))
            elif question_type == '资源与环境-33-第四类水质海域面积':
                sql = self.sql_transfer(question_type, entity_dict.get('33-海域不同水质面积'))
            elif question_type == '资源与环境-33-劣于第四类水质海域面积':
                sql = self.sql_transfer(question_type, entity_dict.get('33-海域不同水质面积'))


            elif question_type == '资源与环境-34-城镇环境基础设施建设投资':
                sql = self.sql_transfer(question_type, entity_dict.get('34-不同地区基础建设投资'))
            elif question_type == '资源与环境-34-燃气建设投资':
                sql = self.sql_transfer(question_type, entity_dict.get('34-不同地区基础建设投资'))
            elif question_type == '资源与环境-34-集中供热建设投资':
                sql = self.sql_transfer(question_type, entity_dict.get('34-不同地区基础建设投资'))
            elif question_type == '资源与环境-34-排水建设投资':
                sql = self.sql_transfer(question_type, entity_dict.get('34-不同地区基础建设投资'))
            elif question_type == '资源与环境-34-园林绿化建设投资':
                sql = self.sql_transfer(question_type, entity_dict.get('34-不同地区基础建设投资'))
            elif question_type == '资源与环境-34-市容环境卫生建设投资':
                sql = self.sql_transfer(question_type, entity_dict.get('34-不同地区基础建设投资'))


            elif question_type == '资源与环境-35-1-工业污染治理完成投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-1-不同地区污染治理情况'))
            elif question_type == '资源与环境-35-1-治理废水投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-1-不同地区污染治理情况'))
            elif question_type == '资源与环境-35-1-治理废气投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-1-不同地区污染治理情况'))
            elif question_type == '资源与环境-35-1-治理固体废物投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-1-不同地区污染治理情况'))
            elif question_type == '资源与环境-35-1-治理噪声投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-1-不同地区污染治理情况'))
            elif question_type == '资源与环境-35-1-治理其他投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-1-不同地区污染治理情况'))


            elif question_type == '资源与环境-35-工业污染治理完成投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-不同年份污染治理情况'))
            elif question_type == '资源与环境-35-治理废水投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-不同年份污染治理情况'))
            elif question_type == '资源与环境-35-治理废气投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-不同年份污染治理情况'))
            elif question_type == '资源与环境-35-治理固体废物投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-不同年份污染治理情况'))
            elif question_type == '资源与环境-35-治理噪声投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-不同年份污染治理情况'))
            elif question_type == '资源与环境-35-治理其他投资':
                sql = self.sql_transfer(question_type, entity_dict.get('35-不同年份污染治理情况'))


            elif question_type == '资源与环境-36-本年完成林业草原投资总计':
                sql = self.sql_transfer(question_type, entity_dict.get('36-林业草原投资完成情况'))
            elif question_type == '资源与环境-36-林业草原国家投资':
                sql = self.sql_transfer(question_type, entity_dict.get('36-林业草原投资完成情况'))
            elif question_type == '资源与环境-36-林业草原生态修复治理投资':
                sql = self.sql_transfer(question_type, entity_dict.get('36-林业草原投资完成情况'))
            elif question_type == '资源与环境-36-林业草原林产品加工制造投资':
                sql = self.sql_transfer(question_type, entity_dict.get('36-林业草原投资完成情况'))
            elif question_type == '资源与环境-36-林业草原林业草原服务保障和公共管理投资':
                sql = self.sql_transfer(question_type, entity_dict.get('36-林业草原投资完成情况'))

            elif question_type == '国民经济核算-1-人均国民总收入':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-人均国内生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-国民总收入':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-国内生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-第一产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-第二产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-第三产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-农林牧渔业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-工业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-建筑业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-批发和零售业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-交通运输仓储和邮政业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-住宿和餐饮业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-金融业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-房地产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))
            elif question_type == '国民经济核算-1-其他':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-01国民生产总值'))


            elif question_type == '国民经济核算-2-国内生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-第一产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-第二产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-第三产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-农林牧渔业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-工业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-建筑业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-批发和零售业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-交通运输仓储和邮政业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-住宿和餐饮业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-金融业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-房地产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))
            elif question_type == '国民经济核算-2-其他':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-02国内生产总值构成'))


            elif question_type == '国民经济核算-3-国内生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-第一产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-第二产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-第三产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-农林牧渔业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-工业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-建筑业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-批发和零售业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-交通运输仓储和邮政业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-住宿和餐饮业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-金融业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-房地产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))
            elif question_type == '国民经济核算-3-其他':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-03不变价国内生产总值'))


            elif question_type == '国民经济核算-4-人均国民总收入':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-人均国内生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-国民总收入':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-国内生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-第一产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-第二产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-第三产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-农林牧渔业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-工业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-建筑业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-批发和零售业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-交通运输仓储和邮政业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-住宿和餐饮业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-金融业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-房地产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))
            elif question_type == '国民经济核算-4-其他':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-04国内生产总值指数'))


            elif question_type == '国民经济核算-6-国内生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-农林牧渔业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-采矿业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-制造业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-电力热力燃气及水':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-建筑业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-批发和零售业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-交通运输仓储和邮政业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-住宿和餐饮业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-信息传输软件和信息':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-金融业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-房地产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-租赁和商务服务业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-科学研究和技术服务业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-水利环境和公共设施管理业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-居民服务修理和其他服务业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-教育':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-卫生和社会工作':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-文化体育和娱乐业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))
            elif question_type == '国民经济核算-6-公共管理社会保障':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-06分行业增加值'))


            elif question_type == '国民经济核算-7-国内生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-07三次产业和主要行业贡献率'))
            elif question_type == '国民经济核算-7-第一产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-07三次产业和主要行业贡献率'))
            elif question_type == '国民经济核算-7-第二产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-07三次产业和主要行业贡献率'))
            elif question_type == '国民经济核算-7-第三产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-07三次产业和主要行业贡献率'))
            elif question_type == '国民经济核算-7-工业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-07三次产业和主要行业贡献率'))
            elif question_type == '国民经济核算-7-批发和零售业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-07三次产业和主要行业贡献率'))
            elif question_type == '国民经济核算-7-金融业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-07三次产业和主要行业贡献率'))


            elif question_type == '国民经济核算-8-国内生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls'))
            elif question_type == '国民经济核算-8-第一产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls'))
            elif question_type == '国民经济核算-8-第二产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls'))
            elif question_type == '国民经济核算-8-第三产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls'))
            elif question_type == '国民经济核算-8-工业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls'))
            elif question_type == '国民经济核算-8-批发和零售业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls'))
            elif question_type == '国民经济核算-8-金融业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-08.三次产业和主要行业对国内生产总值增长的拉动xls'))

            elif question_type == '国民经济核算-9-地区生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-第一产业增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-第二产业增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-第三产业增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-农林牧渔业增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-工业增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-建筑业增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-批发和零售业增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-交通运输仓储和邮政业增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-住宿和餐饮业增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-金融业增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-房地产业增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))
            elif question_type == '国民经济核算-9-其他增加值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09生产总值'))


            elif question_type == '国民经济核算-9-2-人均地区生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09（2）生产总值占比'))
            elif question_type == '国民经济核算-9-2-第一产业构成':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09（2）生产总值占比'))
            elif question_type == '国民经济核算-9-2-第二产业构成':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09（2）生产总值占比'))
            elif question_type == '国民经济核算-9-2-第三产业构成':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09（2）生产总值占比'))


            elif question_type == '国民经济核算-9-3-地区生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09（3）生产总值指数'))
            elif question_type == '国民经济核算-9-3-第一产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09（3）生产总值指数'))
            elif question_type == '国民经济核算-9-3-第二产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09（3）生产总值指数'))
            elif question_type == '国民经济核算-9-3-第三产业':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09（3）生产总值指数'))
            elif question_type == '国民经济核算-9-3-人均地区生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-09（3）生产总值指数'))


            elif question_type == '国民经济核算-10-生产总值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-10支出法国内生产总值'))
            elif question_type == '国民经济核算-10-最终消费':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-10支出法国内生产总值'))
            elif question_type == '国民经济核算-10-资本形成总额':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-10支出法国内生产总值'))
            elif question_type == '国民经济核算-10-货物和服务净出口':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-10支出法国内生产总值'))
            elif question_type == '国民经济核算-10-最终消费率':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-10支出法国内生产总值'))
            elif question_type == '国民经济核算-10-资本形成率':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-10支出法国内生产总值'))


            elif question_type == '国民经济核算-11-1-居民消费支出':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11居民消费支出占比'))
            elif question_type == '国民经济核算-11-1-政府消费支出':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11居民消费支出占比'))


            elif question_type == '国民经济核算-11-2-居民消费支出':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11最终消费支出'))
            elif question_type == '国民经济核算-11-2-城镇居民支出':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11最终消费支出'))
            elif question_type == '国民经济核算-11-2-农村居民支出':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11最终消费支出'))
            elif question_type == '国民经济核算-11-2-政府消费支出':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11最终消费支出'))


            elif question_type == '国民经济核算-11-3-居民消费支出':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11最终消费支出占比'))
            elif question_type == '国民经济核算-11-3-政府消费支出':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11最终消费支出占比'))

            elif question_type == '国民经济核算-11-4-出口':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11货物与服务净出口'))
            elif question_type == '国民经济核算-11-4-进口':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11货物与服务净出口'))

            elif question_type == '国民经济核算-11-5-固定资本形成总额':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11资本形成总额'))
            elif question_type == '国民经济核算-11-5-存货变动':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11资本形成总额'))

            elif question_type == '国民经济核算-11-6-固定资本形成总额':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11资本形成总额占比'))
            elif question_type == '国民经济核算-11-6-存货变动':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-11资本形成总额占比'))


            elif question_type == '国民经济核算-12-居民实际最终消费':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-12实际最终消费构成'))
            elif question_type == '国民经济核算-12-政府实际最终消费':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-12实际最终消费构成'))


            elif question_type == '国民经济核算-12-1-居民实际最终消费':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-12（1）实际最终消费'))
            elif question_type == '国民经济核算-12-1-政府实际最终消费':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-12（1）实际最终消费'))


            elif question_type == '国民经济核算-13-全体居民绝对数':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-13生活消费水平'))
            elif question_type == '国民经济核算-13-城镇居民绝对数':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-13生活消费水平'))
            elif question_type == '国民经济核算-13-农村居民绝对数':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-13生活消费水平'))
            elif question_type == '国民经济核算-13-城镇居民消费水平与农村居民消费水平的比值':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-13生活消费水平'))
            elif question_type == '国民经济核算-13-全体居民指数':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-13生活消费水平'))
            elif question_type == '国民经济核算-13-城镇居民消费指数':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-13生活消费水平'))
            elif question_type == '国民经济核算-13-农村居民消费指数':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-13生活消费水平'))


            elif question_type == '国民经济核算-14-最终消费支出贡献率':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-14三大需求对国内生产总值增长的贡献率和拉动'))
            elif question_type == '国民经济核算-14-最终消费支出拉动':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-14三大需求对国内生产总值增长的贡献率和拉动'))
            elif question_type == '国民经济核算-14-资本形成总额贡献率':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-14三大需求对国内生产总值增长的贡献率和拉动'))
            elif question_type == '国民经济核算-14-资本形成总额拉动':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-14三大需求对国内生产总值增长的贡献率和拉动'))
            elif question_type == '国民经济核算-14-货物和服务净出口贡献率':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-14三大需求对国内生产总值增长的贡献率和拉动'))
            elif question_type == '国民经济核算-14-货物和服务净出口拉动':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-14三大需求对国内生产总值增长的贡献率和拉动'))


            elif question_type == '国民经济核算-16-净金融投资':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-资金运用合计':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-资金来源合计':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-通货':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-存款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-活期存款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-定期存款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-财政存款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-外汇存款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-其他存款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-证券公司客户保证金':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-贷款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-短期贷款与票据融资':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-中长期贷款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-外汇贷款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-委托贷款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-其他贷款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-未贴现的银行承兑汇票':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-保险准备金':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-金融机构往来':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-存款准备金':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-债券':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-政府债券':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-金融债券':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-中央银行债券':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-企业债券':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-股票':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-证券投资基金份额':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-库存现金':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-中央银行贷款':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-其他':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-直接投资':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-其他对外债权债务':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-国际储备资产':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))
            elif question_type == '国民经济核算-16-国际收支错误与遗漏':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-16资金流量表 (金融交易，2020年)'))


            elif question_type == '国民经济核算-17-企业部门初次分配总收入':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-17企业、广义政府与住户部门初次分配总收入及比重'))
            elif question_type == '国民经济核算-17-企业部门占比':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-17企业、广义政府与住户部门初次分配总收入及比重'))
            elif question_type == '国民经济核算-17-广义政府部门初次分配总收入':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-17企业、广义政府与住户部门初次分配总收入及比重'))
            elif question_type == '国民经济核算-17-广义政府部门占比':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-17企业、广义政府与住户部门初次分配总收入及比重'))
            elif question_type == '国民经济核算-17-住户部门初次分配总收入':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-17企业、广义政府与住户部门初次分配总收入及比重'))
            elif question_type == '国民经济核算-17-住户部门占比':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-17企业、广义政府与住户部门初次分配总收入及比重'))


            elif question_type == '国民经济核算-19-企业部门调整后可支配总收入':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-19企业、广义政府与住户部门调整后可支配总收入及比重'))
            elif question_type == '国民经济核算-19-企业部门调整后占比':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-19企业、广义政府与住户部门调整后可支配总收入及比重'))
            elif question_type == '国民经济核算-19-广义政府部门调整后可支配总收入':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-19企业、广义政府与住户部门调整后可支配总收入及比重'))
            elif question_type == '国民经济核算-19-广义政府部门调整后占比':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-19企业、广义政府与住户部门调整后可支配总收入及比重'))
            elif question_type == '国民经济核算-19-住户部门调整后可支配总收入':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-19企业、广义政府与住户部门调整后可支配总收入及比重'))
            elif question_type == '国民经济核算-19-住户部门调整后占比':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-19企业、广义政府与住户部门调整后可支配总收入及比重'))




            elif question_type == '国民经济核算-22-农林牧渔产品和服务':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-采掘产品':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-食品和烟草':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-纺织服装鞋及皮革羽绒制品':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-木材加工家具造纸印刷和文教工美用品':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-炼油炼焦和化学产品':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-非金属矿物制品':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-金属冶炼加工及制品':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-机械设备和交通运输设备及电子电气及其他设备':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-其他各类制造产品':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-电力热力燃气和水的生产和供应':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-建筑':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-批发零售运输仓储邮政':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-信息传输软件和信息技术服务':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-金融和房地产':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-科学研究和技术服务':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-其他服务':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))
            elif question_type == '国民经济核算-22-中间投入合计':
                sql = self.sql_transfer(question_type, entity_dict.get('C03-22 2020年投入产出基本流量表(最终使用部分'))



            elif question_type == '能源-1-一次能源生产总量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-01一次能源生产总量及构成'))
            elif question_type == '能源-1-原煤占一次能源生产总量的比重':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-01一次能源生产总量及构成'))
            elif question_type == '能源-1-原油占一次能源生产总量的比重':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-01一次能源生产总量及构成'))
            elif question_type == '能源-1-天然气':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-01一次能源生产总量及构成'))
            elif question_type == '能源-1-一次电力及其他能源':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-01一次能源生产总量及构成'))



            elif question_type == '能源-2-能源消费总量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-02能源消费总量及构成'))
            elif question_type == '能源-2-煤炭占能源消费总量的比重':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-02能源消费总量及构成'))
            elif question_type == '能源-2-石油占能源消费总量的比重':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-02能源消费总量及构成'))
            elif question_type == '能源-2-天然气占能源消费总量的比重':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-02能源消费总量及构成'))
            elif question_type == '能源-2-一次电力及其他能源占能源消费总量的比重':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-02能源消费总量及构成'))



            elif question_type == '能源-3-可供消费的能源总量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-一次能源生产总量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-回收量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-进口量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-出口量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-年初年末库存差额':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-能源消费总量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-渔业':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-工业':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-建筑业':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-邮政业':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-住宿和餐饮业':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-其他':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-居民生活':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-终端消费':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-加工转换损失量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-炼焦':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-炼油及煤制油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-损失量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))
            elif question_type == '能源-3-平衡差额':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-03综合能源平衡表'))


            elif question_type == '能源-4-石油可供量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-石油生产量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-石油进口量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-石油出口量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-石油年初年末库存差额':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-农林牧渔业中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-工业中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-建筑业中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-交通运输仓储和邮政业中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-批发和零售业住宿和餐饮业中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-其他中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-居民生活中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-终端消费中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-中间消费中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-火力发电中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-供热中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-制气中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-炼油损失量中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-损失量中石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))
            elif question_type == '能源-4-石油平衡差额':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-04石油平衡表'))



            elif question_type == '能源-5-煤炭可供量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-煤炭生产量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-煤炭进口量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-煤炭出口量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-煤炭年初年末库存差额':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-农林牧渔业中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-工业中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-建筑业中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-交通运输仓储和邮政业中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-批发和零售业住宿和餐饮业中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-其他中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-居民生活中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-终端消费中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-中间消费中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-火力发电中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-供热中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-炼焦中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-煤制油中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-制气中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-洗选损耗中煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))
            elif question_type == '能源-5-煤炭平衡差额':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-05煤炭平衡表'))



            elif question_type == '能源-6-可供量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-电力生产量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-水电生产量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-火电生产量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-核电生产量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-风电生产量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-电力进口量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-电力出口量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-电力消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-农林牧渔业中电力消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-工业中电力消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-建筑业中电力消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-交通运输仓储和邮政业中电力消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-批发和零售业住宿和餐饮业中电力消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-其他中电力消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-居民生活中电力消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-终端消费中电力消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))
            elif question_type == '能源-6-输配电损失量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-06电力平衡表'))


            elif question_type == '能源-7-能源生产比上年增长':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-07能源生产弹性系数'))
            elif question_type == '能源-7-电力生产比上年增长':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-07能源生产弹性系数'))
            elif question_type == '能源-7-国内生产总值比上年增长':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-07能源生产弹性系数'))
            elif question_type == '能源-7-能源生产弹性系数':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-07能源生产弹性系数'))
            elif question_type == '能源-7-电力生产弹性系数':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-07能源生产弹性系数'))


            elif question_type == '能源-8-能源消费比上年增长':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-08.能源消费弹性系数'))
            elif question_type == '能源-8-电力消费比上年增长':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-08.能源消费弹性系数'))
            elif question_type == '能源-8-国内消费总值比上年增长':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-08.能源消费弹性系数'))
            elif question_type == '能源-8-能源消费弹性系数':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-08.能源消费弹性系数'))
            elif question_type == '能源-8-电力消费弹性系数':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-08.能源消费弹性系数'))


            elif question_type == '能源-9-能源消费总量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-09按行业分能源消费量 (2020年)'))
            elif question_type == '能源-9-煤炭':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-09按行业分能源消费量 (2020年)'))
            elif question_type == '能源-9-焦炭':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-09按行业分能源消费量 (2020年)'))
            elif question_type == '能源-9-原油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-09按行业分能源消费量 (2020年)'))
            elif question_type == '能源-9-汽油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-09按行业分能源消费量 (2020年)'))
            elif question_type == '能源-9-煤油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-09按行业分能源消费量 (2020年)'))
            elif question_type == '能源-9-柴油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-09按行业分能源消费量 (2020年)'))
            elif question_type == '能源-9-燃料油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-09按行业分能源消费量 (2020年)'))
            elif question_type == '能源-9-天然气':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-09按行业分能源消费量 (2020年)'))
            elif question_type == '能源-9-电力':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-09按行业分能源消费量 (2020年)'))



            elif question_type == '能源-10-总效率':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-10能源加工转换效率'))
            elif question_type == '能源-10-发电及供热':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-10能源加工转换效率'))
            elif question_type == '能源-10-炼焦':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-10能源加工转换效率'))
            elif question_type == '能源-10-炼油及煤制油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-10能源加工转换效率'))


            elif question_type == '能源-11-合计':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-11平均每天能源消费量'))
            elif question_type == '能源-11-煤炭':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-11平均每天能源消费量'))
            elif question_type == '能源-11-焦炭':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-11平均每天能源消费量'))
            elif question_type == '能源-11-原油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-11平均每天能源消费量'))
            elif question_type == '能源-11-汽油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-11平均每天能源消费量'))
            elif question_type == '能源-11-煤油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-11平均每天能源消费量'))
            elif question_type == '能源-11-柴油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-11平均每天能源消费量'))
            elif question_type == '能源-11-燃料油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-11平均每天能源消费量'))
            elif question_type == '能源-11-天然气':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-11平均每天能源消费量'))
            elif question_type == '能源-11-电力':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-11平均每天能源消费量'))



            elif question_type == '能源-12-合计':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-12居民生活能源消费量'))
            elif question_type == '能源-12-煤炭':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-12居民生活能源消费量'))
            elif question_type == '能源-12-煤油':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-12居民生活能源消费量'))
            elif question_type == '能源-12-液化石油气':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-12居民生活能源消费量'))
            elif question_type == '能源-12-天然气':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-12居民生活能源消费量'))
            elif question_type == '能源-12-煤气':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-12居民生活能源消费量'))
            elif question_type == '能源-12-热力':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-12居民生活能源消费量'))
            elif question_type == '能源-12-电力':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-12居民生活能源消费量'))


            elif question_type == '能源-13-人均生活能源消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-13人均生活能源消费量'))
            elif question_type == '能源-13-煤炭':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-13人均生活能源消费量'))
            elif question_type == '能源-13-电力':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-13人均生活能源消费量'))
            elif question_type == '能源-13-液化石油气':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-13人均生活能源消费量'))
            elif question_type == '能源-13-天然气':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-13人均生活能源消费量'))
            elif question_type == '能源-13-煤气':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-13人均生活能源消费量'))


            elif question_type == '能源-14-北京':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-天津':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-河北':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-山西':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-内蒙古':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-辽宁':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-吉林':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-黑龙江':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-上海':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-江苏':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-浙江':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-安徽':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-福建':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-江西':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-山东':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-河南':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-湖北':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-湖南':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-广东':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-广西':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-海南':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-重庆':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-四川':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-贵州':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-云南':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-西藏':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-陕西':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-甘肃':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-青海':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-宁夏':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))
            elif question_type == '能源-14-新疆':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-14分地区电力能源消费量'))


            elif question_type == '能源-15-发电装机容量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-15发电装机容量'))
            elif question_type == '能源-15-火电':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-15发电装机容量'))
            elif question_type == '能源-15-水电':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-15发电装机容量'))
            elif question_type == '能源-15-核电':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-15发电装机容量'))
            elif question_type == '能源-15-风电':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-15发电装机容量'))
            elif question_type == '能源-15-太阳能发电':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-15发电装机容量'))
            elif question_type == '能源-15-其他':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-15发电装机容量'))


            elif question_type == '能源-16-国内生产总值能源消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-16万元国内生产总值能源消费量'))
            elif question_type == '能源-16-国内生产总值煤炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-16万元国内生产总值能源消费量'))
            elif question_type == '能源-16-国内生产总值焦炭消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-16万元国内生产总值能源消费量'))
            elif question_type == '能源-16-国内生产总值石油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-16万元国内生产总值能源消费量'))
            elif question_type == '能源-16-国内生产总值原油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-16万元国内生产总值能源消费量'))
            elif question_type == '能源-16-国内生产总值燃料油消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-16万元国内生产总值能源消费量'))
            elif question_type == '能源-16-国内生产总值电力消费量':
                sql = self.sql_transfer(question_type, entity_dict.get('C09-16万元国内生产总值能源消费量'))

            if sql:
                sql_['sql'] = sql

                sqls.append(sql_)

        return sqls

    '''针对不同的问题，分开进行处理'''
    def sql_transfer(self, question_type, entities):
        if not entities:
            return []

        # 查询语句
        sql = []
        # 查询性别
        if question_type == '资源与环境-1-面积':
            sql = ["match (m:土地面积) where m.土地类型='{0}' return m.面积,m.土地类型".format(i) for i in entities]
        elif question_type == '资源与环境-2-流域面积':
            sql = ["match (m:河流面积) where m.河流名称='{0}' return m.流域面积,m.河流名称".format(i) for i in entities]
        elif question_type == '资源与环境-2-河长':
            sql = ["match (m:河流面积) where m.河流名称='{0}' return m.河长,m.河流名称".format(i) for i in entities]
        elif question_type == '资源与环境-2-年径流量':
            sql = ["match (m:河流面积) where m.河流名称='{0}' return m.年径流量,m.河流名称".format(i) for i in entities]
        elif question_type == '资源与环境-3-流域面积':
            sql = ["match (m:流域面积) where m.流域名称='{0}' return m.流域面积,m.流域名称".format(i) for i in entities]
        elif question_type == '资源与环境-3-面积占比':
            sql = ["match (m:流域面积) where m.流域名称='{0}' return m.占外流河和内陆河流域面积合计,m.流域名称".format(i) for i in entities]
        elif question_type == '资源与环境-4-2020年产量':
            sql = ["match (m:矿产产量) where m.矿产名称='{0}' return m.年产量2020年,m.矿产名称".format(i) for i in entities]
        elif question_type == '资源与环境-4-2021年产量':
            sql = ["match (m:矿产产量) where m.矿产名称='{0}' return m.年产量2021年,m.矿产名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-1月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度1月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-2月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度2月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-3月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度3月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-4月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度4月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-5月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度5月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-6月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度6月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-7月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度7月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-8月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度8月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-9月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度9月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-10月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度10月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-11月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度11月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-12月温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.温度12月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-5-年平均温度':
            sql = ["match (m:城市温度) where m.城市名称='{0}' return m.年平均温度,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-1月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度1月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-2月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度2月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-3月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度3月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-4月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度4月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-5月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度5月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-6月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度6月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-7月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度7月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-8月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度8月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-9月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度9月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-10月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度10月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-11月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度11月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-12月湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.湿度12月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-6-年平均湿度':
            sql = ["match (m:城市湿度) where m.城市名称='{0}' return m.年平均湿度,m.城市名称".format(i) for i in entities]

        elif question_type == '资源与环境-7-1月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量1月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-2月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量2月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-3月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量3月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-4月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量4月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-5月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量5月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-6月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量6月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-7月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量7月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-8月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量8月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-9月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量9月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-10月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量10月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-11月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量11月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-12月降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.降水量12月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-7-全年降水量':
            sql = ["match (m:城市降水量) where m.城市名称='{0}' return m.全年降水量,m.城市名称".format(i) for i in entities]

        elif question_type == '资源与环境-8-1月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数1月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-2月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数2月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-3月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数3月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-4月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数4月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-5月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数5月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-6月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数6月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-7月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数7月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-8月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数8月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-9月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数9月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-10月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数10月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-11月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数11月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-12月日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.日照时数12月,m.城市名称".format(i) for i in entities]
        elif question_type == '资源与环境-8-全年日照时数':
            sql = ["match (m:城市日照时间数) where m.城市名称='{0}' return m.全年日照时数,m.城市名称".format(i) for i in entities]

        elif question_type == '资源与环境-9-水资源总量':
            sql = ["match (m:不同地区水资源总量) where m.地区='{0}' return m.水资源总量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-9-地表水资源量':
            sql = ["match (m:不同地区水资源总量) where m.地区='{0}' return m.地表水资源量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-9-地下水资源量':
            sql = ["match (m:不同地区水资源总量) where m.地区='{0}' return m.地下水资源量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-9-地表水与地下水资源重复量':
            sql = ["match (m:不同地区水资源总量) where m.地区='{0}' return m.地表水与地下水资源重复量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-9-人均水资源量':
            sql = ["match (m:不同地区水资源总量) where m.地区='{0}' return m.人均水资源量,m.地区".format(i) for i in entities]

        elif question_type == '资源与环境-9-1-水资源总量':
            sql = ["match (m:不同年份水资源总量) where m.年份='{0}' return m.水资源总量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-9-1-地表水资源量':
            sql = ["match (m:不同年份水资源总量) where m.年份='{0}' return m.地表水资源量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-9-1-地下水资源量':
            sql = ["match (m:不同年份水资源总量) where m.年份='{0}' return m.地下水资源量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-9-1-地表水与地下水资源重复量':
            sql = ["match (m:不同年份水资源总量) where m.年份='{0}' return m.地表水与地下水资源重复量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-9-1-人均水资源量':
            sql = ["match (m:不同年份水资源总量) where m.年份='{0}' return m.人均水资源量,m.年份".format(i) for i in entities]


        elif question_type == '资源与环境-10-1-供水总量':
            sql = ["match (m:不同地区供水总量) where m.地区='{0}' return m.供水总量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-10-1-地表水供水量':
            sql = ["match (m:不同地区供水总量) where m.地区='{0}' return m.地表水供水量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-10-1-地下水供水量':
            sql = ["match (m:不同地区供水总量) where m.地区='{0}' return m.地下水供水量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-10-1-其他供水量':
            sql = ["match (m:不同地区供水总量) where m.地区='{0}' return m.其他供水量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-10-1-用水总量':
            sql = ["match (m:不同地区供水总量) where m.地区='{0}' return m.用水总量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-10-1-农业用水量':
            sql = ["match (m:不同地区供水总量) where m.地区='{0}' return m.农业用水量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-10-1-工业用水量':
            sql = ["match (m:不同地区供水总量) where m.地区='{0}' return m.工业用水量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-10-1-生活用水量':
            sql = ["match (m:不同地区供水总量) where m.地区='{0}' return m.生活用水量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-10-1-人工生态环境补水用水量':
            sql = ["match (m:不同地区供水总量) where m.地区='{0}' return m.人工生态环境补水用水量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-10-1-人均用水量':
            sql = ["match (m:不同地区供水总量) where m.地区='{0}' return m.人均用水量,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-10-供水总量':
            sql = ["match (m:不同年份供水总量) where m.年份='{0}' return m.供水总量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-10-地表水供水量':
            sql = ["match (m:不同年份供水总量) where m.年份='{0}' return m.地表水供水量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-10-地下水供水量':
            sql = ["match (m:不同年份供水总量) where m.年份='{0}' return m.地下水供水量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-10-其他供水量':
            sql = ["match (m:不同年份供水总量) where m.年份='{0}' return m.其他供水量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-10-用水总量':
            sql = ["match (m:不同年份供水总量) where m.年份='{0}' return m.用水总量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-10-农业用水量':
            sql = ["match (m:不同年份供水总量) where m.年份='{0}' return m.农业用水量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-10-工业用水量':
            sql = ["match (m:不同年份供水总量) where m.年份='{0}' return m.工业用水量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-10-生活用水量':
            sql = ["match (m:不同年份供水总量) where m.年份='{0}' return m.生活用水量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-10-人工生态环境补水用水量':
            sql = ["match (m:不同年份供水总量) where m.年份='{0}' return m.人工生态环境补水用水量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-10-人均用水量':
            sql = ["match (m:不同年份供水总量) where m.年份='{0}' return m.人均用水量,m.年份".format(i) for i in entities]

        elif question_type == '资源与环境-11-废水中化学需氧量排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中化学需氧量排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-11-废水中氨氮排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中氨氮排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-11-废水中总氮排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中总氮排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-11-废水中总磷排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中总磷排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-11-废水中石油类排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中石油类排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-11-废水中挥发酚排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中挥发酚排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-11-废水中总铅排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中总铅排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-11-废水中总汞排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中总汞排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-11-废水中总镉排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中总镉排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-11-废水中六价铬排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中六价铬排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-11-废水中总铬排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中总铬排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-11-废水中总砷排放量':
            sql = ["match (m:不用地区废水污染物含量11) where m.地区='{0}' return m.废水中总砷排放量,m.地区".format(i) for i in entities]

        elif question_type == '资源与环境-12-城市废水中工业化学需氧量排放量':
            sql = ["match (m:不同城市废水污染物含量12) where m.城市='{0}' return m.城市废水中工业化学需氧量排放量,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-12-城市废水中工业氨氮排放量':
            sql = ["match (m:不同城市废水污染物含量12) where m.城市='{0}' return m.城市废水中工业氨氮排放量,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-12-城市废水中生活化学需氧量排放量':
            sql = ["match (m:不同城市废水污染物含量12) where m.城市='{0}' return m.城市废水中生活化学需氧量排放量,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-12-城市废水中生活氨氮排放量':
            sql = ["match (m:不同城市废水污染物含量12) where m.城市='{0}' return m.城市废水中生活氨氮排放量,m.城市".format(i) for i in entities]



        elif question_type == '资源与环境-13-二氧化硫排放量':
            sql = ["match (m:不同地区废气污染物含量13) where m.地区='{0}' return m.二氧化硫排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-13-氮氧化物排放量':
            sql = ["match (m:不同地区废气污染物含量13) where m.地区='{0}' return m.氮氧化物排放量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-13-颗粒物排放量':
            sql = ["match (m:不同地区废气污染物含量13) where m.地区='{0}' return m.颗粒物排放量,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-14-工业二氧化硫排放量':
            sql = ["match (m:不同城市废气污染物含量14) where m.城市='{0}' return m.工业二氧化硫排放量,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-14-工业氮氧化物排放量':
            sql = ["match (m:不同城市废气污染物含量14) where m.城市='{0}' return m.工业氮氧化物排放量,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-14-工业颗粒物排放量':
            sql = ["match (m:不同城市废气污染物含量14) where m.城市='{0}' return m.工业颗粒物排放量,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-14-生活及其他二氧化硫排放量':
            sql = ["match (m:不同城市废气污染物含量14) where m.城市='{0}' return m.生活及其他二氧化硫排放量,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-14-生活及其他氮氧化物排放量':
            sql = ["match (m:不同城市废气污染物含量14) where m.城市='{0}' return m.生活及其他氮氧化物排放量,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-14-生活及其他颗粒物排放量':
            sql = ["match (m:不同城市废气污染物含量14) where m.城市='{0}' return m.生活及其他颗粒物排放量,m.城市".format(i) for i in entities]


        elif question_type == '资源与环境-15-一般工业固体废物产生量':
            sql = ["match (m:不同地区固体废物处理情况15) where m.地区='{0}' return m.一般工业固体废物产生量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-15-一般工业固体废物综合利用量':
            sql = ["match (m:不同地区固体废物处理情况15) where m.地区='{0}' return m.一般工业固体废物综合利用量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-15-一般工业固体废物处置量':
            sql = ["match (m:不同地区固体废物处理情况15) where m.地区='{0}' return m.一般工业固体废物处置量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-15-一般工业固体废物贮存量':
            sql = ["match (m:不同地区固体废物处理情况15) where m.地区='{0}' return m.一般工业固体废物贮存量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-15-一般工业固体废物倾倒丢弃量':
            sql = ["match (m:不同地区固体废物处理情况15) where m.地区='{0}' return m.一般工业固体废物倾倒丢弃量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-15-危险废物产生量':
            sql = ["match (m:不同地区固体废物处理情况15) where m.地区='{0}' return m.危险废物产生量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-15-危险废物利用处置量':
            sql = ["match (m:不同地区固体废物处理情况15) where m.地区='{0}' return m.危险废物利用处置量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-15-危险废物本年末贮存量':
            sql = ["match (m:不同地区固体废物处理情况15) where m.地区='{0}' return m.危险废物本年末贮存量,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-16-一般工业固体废物产生量':
            sql = ["match (m:不同城市固体废物处理情况16) where m.城市='{0}' return m.一般工业固体废物产生量,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-16-一般工业固体废物综合利用量':
            sql = ["match (m:不同城市固体废物处理情况16) where m.城市='{0}' return m.一般工业固体废物综合利用量,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-16-一般工业固体废物处置量':
            sql = ["match (m:不同城市固体废物处理情况16) where m.城市='{0}' return m.一般工业固体废物处置量,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-16-一般工业固体废物贮存量':
            sql = ["match (m:不同城市固体废物处理情况16) where m.城市='{0}' return m.一般工业固体废物贮存量,m.城市".format(i) for i in entities]


        elif question_type == '资源与环境-17-二氧化硫年平均浓度':
            sql = ["match (m:不同城市空气污染物含量17) where m.城市='{0}' return m.二氧化硫年平均浓度,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-17-二氧化氮年平均浓度':
            sql = ["match (m:不同城市空气污染物含量17) where m.城市='{0}' return m.二氧化氮年平均浓度,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-17-可吸入颗粒物年平均浓度':
            sql = ["match (m:不同城市空气污染物含量17) where m.城市='{0}' return m.可吸入颗粒物年平均浓度,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-17-一氧化碳日均值第95百分位浓度':
            sql = ["match (m:不同城市空气污染物含量17) where m.城市='{0}' return m.一氧化碳日均值第95百分位浓度,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-17-臭氧日最大8小时第90百分位浓度':
            sql = ["match (m:不同城市空气污染物含量17) where m.城市='{0}' return m.臭氧日最大8小时第90百分位浓度,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-17-细颗粒物年平均浓度':
            sql = ["match (m:不同城市空气污染物含量17) where m.城市='{0}' return m.细颗粒物年平均浓度,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-17-空气质量优良天数比例':
            sql = ["match (m:不同城市空气污染物含量17) where m.城市='{0}' return m.空气质量优良天数比例,m.城市".format(i) for i in entities]


        elif question_type == '资源与环境-18-生活垃圾清运量':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.生活垃圾清运量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-无害化处理厂数':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.无害化处理厂数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-卫生填埋厂数':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.卫生填埋厂数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-焚烧厂数':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.焚烧厂数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-其他厂数':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.其他厂数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-无害化处理能力':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.无害化处理能力,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-卫生填埋处理能力':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.卫生填埋处理能力,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-焚烧处理能力':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.焚烧处理能力,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-其他处理能力':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.其他处理能力,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-无害化处理量':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.无害化处理量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-卫生填埋处理量':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.卫生填埋处理量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-焚烧处理量':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.焚烧处理量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-其他处理量':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.其他处理量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-18-生活垃圾无害化处理率':
            sql = ["match (m:不同地区垃圾处理情况18) where m.地区='{0}' return m.生活垃圾无害化处理率,m.地区".format(i) for i in entities]



        elif question_type == '资源与环境-19-道路交通噪声等效声级':
            sql = ["match (m:不同城市噪声污染情况19) where m.城市='{0}' return m.道路交通噪声等效声级,m.城市".format(i) for i in entities]
        elif question_type == '资源与环境-19-区域环境噪声等效声级':
            sql = ["match (m:不同城市噪声污染情况19) where m.城市='{0}' return m.区域环境噪声等效声级,m.城市".format(i) for i in entities]



        elif question_type == '资源与环境-20-2013耕地面积':
            sql = ["match (m:不同地区耕地面积情况20) where m.地区='{0}' return m.耕地面积2013,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-20-2014耕地面积':
            sql = ["match (m:不同地区耕地面积情况20) where m.地区='{0}' return m.耕地面积2014,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-20-2015耕地面积':
            sql = ["match (m:不同地区耕地面积情况20) where m.地区='{0}' return m.耕地面积2015,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-20-2016耕地面积':
            sql = ["match (m:不同地区耕地面积情况20) where m.地区='{0}' return m.耕地面积2016,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-20-2017耕地面积':
            sql = ["match (m:不同地区耕地面积情况20) where m.地区='{0}' return m.耕地面积2017,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-20-2019耕地面积':
            sql = ["match (m:不同地区耕地面积情况20) where m.地区='{0}' return m.耕地面积2019,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-21-耕地':
            sql = ["match (m:不同地区用地情况21) where m.地区='{0}' return m.耕地,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-21-园地':
            sql = ["match (m:不同地区用地情况21) where m.地区='{0}' return m.园地,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-21-林地':
            sql = ["match (m:不同地区用地情况21) where m.地区='{0}' return m.林地,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-21-草地':
            sql = ["match (m:不同地区用地情况21) where m.地区='{0}' return m.草地,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-21-湿地':
            sql = ["match (m:不同地区用地情况21) where m.地区='{0}' return m.湿地,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-21-城镇村及工矿用地':
            sql = ["match (m:不同地区用地情况21) where m.地区='{0}' return m.城镇村及工矿用地,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-21-交通运输用地':
            sql = ["match (m:不同地区用地情况21) where m.地区='{0}' return m.交通运输用地,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-21-水域及水利设施用地':
            sql = ["match (m:不同地区用地情况21) where m.地区='{0}' return m.水域及水利设施用地,m.地区".format(i) for i in entities]



        elif question_type == '资源与环境-22-林业用地面积':
            sql = ["match (m:不同地区森林资源情况22) where m.地区='{0}' return m.林业用地面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-22-森林面积':
            sql = ["match (m:不同地区森林资源情况22) where m.地区='{0}' return m.森林面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-22-人工林':
            sql = ["match (m:不同地区森林资源情况22) where m.地区='{0}' return m.人工林,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-22-森林覆盖率':
            sql = ["match (m:不同地区森林资源情况22) where m.地区='{0}' return m.森林覆盖率,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-22-活立木总蓄积量':
            sql = ["match (m:不同地区森林资源情况22) where m.地区='{0}' return m.活立木总蓄积量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-22-森林蓄积量':
            sql = ["match (m:不同地区森林资源情况22) where m.地区='{0}' return m.森林蓄积量,m.地区".format(i) for i in entities]



        elif question_type == '资源与环境-23-1-造林总面积':
            sql = ["match (m:不同地区造林面积23_1) where m.地区='{0}' return m.造林总面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-23-1-人工造林面积':
            sql = ["match (m:不同地区造林面积23_1) where m.地区='{0}' return m.人工造林面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-23-1-飞播造林面积':
            sql = ["match (m:不同地区造林面积23_1) where m.地区='{0}' return m.飞播造林面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-23-1-封山育林面积':
            sql = ["match (m:不同地区造林面积23_1) where m.地区='{0}' return m.封山育林面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-23-1-退化林修复面积':
            sql = ["match (m:不同地区造林面积23_1) where m.地区='{0}' return m.退化林修复面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-23-1-人工更新面积':
            sql = ["match (m:不同地区造林面积23_1) where m.地区='{0}' return m.人工更新面积,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-23-造林总面积':
            sql = ["match (m:不同年份造林面积23) where m.年份='{0}' return m.造林总面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-23-人工造林面积':
            sql = ["match (m:不同年份造林面积23) where m.年份='{0}' return m.人工造林面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-23-飞播造林面积':
            sql = ["match (m:不同年份造林面积23) where m.年份='{0}' return m.飞播造林面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-23-封山育林面积':
            sql = ["match (m:不同年份造林面积23) where m.年份='{0}' return m.封山育林面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-23-退化林修复面积':
            sql = ["match (m:不同年份造林面积23) where m.年份='{0}' return m.退化林修复面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-23-人工更新面积':
            sql = ["match (m:不同年份造林面积23) where m.年份='{0}' return m.人工更新面积,m.年份".format(i) for i in entities]


        elif question_type == '资源与环境-24-种草面积':
            sql = ["match (m:不同地区草原建设情况24) where m.地区='{0}' return m.种草面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-24-草原改良面积':
            sql = ["match (m:不同地区草原建设情况24) where m.地区='{0}' return m.草原改良面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-24-草原鼠害发生面积':
            sql = ["match (m:不同地区草原建设情况24) where m.地区='{0}' return m.草原鼠害发生面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-24-草原鼠害防治面积':
            sql = ["match (m:不同地区草原建设情况24) where m.地区='{0}' return m.草原鼠害防治面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-24-草原虫害发生面积':
            sql = ["match (m:不同地区草原建设情况24) where m.地区='{0}' return m.草原虫害发生面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-24-草原虫害防治面积':
            sql = ["match (m:不同地区草原建设情况24) where m.地区='{0}' return m.草原虫害防治面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-24-草原火灾受害面积':
            sql = ["match (m:不同地区草原建设情况24) where m.地区='{0}' return m.草原火灾受害面积,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-25-国家级自然保护区个数':
            sql = ["match (m:不同地区自然保护情况25) where m.地区='{0}' return m.国家级自然保护区个数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-25-国家级自然保护区面积':
            sql = ["match (m:不同地区自然保护情况25) where m.地区='{0}' return m.国家级自然保护区面积,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-26-农作物受灾面积合计':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.农作物受灾面积合计,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-农作物绝收面积合计':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.农作物绝收面积合计,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-旱灾受灾面积':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.旱灾受灾面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-旱灾绝收面积':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.旱灾绝收面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-洪涝地质灾害和台风受灾面积':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.洪涝地质灾害和台风受灾面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-洪涝地质灾害和台风绝收面积':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.洪涝地质灾害和台风绝收面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-风雹灾害受灾面积':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.风雹灾害受灾面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-风雹灾害绝收面积':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.风雹灾害绝收面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-低温冷冻和雪灾受灾面积':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.低温冷冻和雪灾受灾面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-低温冷冻和雪灾绝收面积':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.低温冷冻和雪灾绝收面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-受灾人口':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.受灾人口,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-死亡人口':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.死亡人口,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-26-直接经济损失':
            sql = ["match (m:不同地区自然灾害情况26) where m.地区='{0}' return m.直接经济损失,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-27-1-发生地质灾害数量':
            sql = ["match (m:不同地区地质灾害情况27_1) where m.地区='{0}' return m.发生地质灾害数量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-27-1-滑坡次数':
            sql = ["match (m:不同地区地质灾害情况27_1) where m.地区='{0}' return m.滑坡次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-27-1-崩塌次数':
            sql = ["match (m:不同地区地质灾害情况27_1) where m.地区='{0}' return m.崩塌次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-27-1-泥石流次数':
            sql = ["match (m:不同地区地质灾害情况27_1) where m.地区='{0}' return m.泥石流次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-27-1-地面塌陷次数':
            sql = ["match (m:不同地区地质灾害情况27_1) where m.地区='{0}' return m.地面塌陷次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-27-1-人员伤亡数量':
            sql = ["match (m:不同地区地质灾害情况27_1) where m.地区='{0}' return m.人员伤亡数量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-27-1-死亡人数':
            sql = ["match (m:不同地区地质灾害情况27_1) where m.地区='{0}' return m.死亡人数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-27-1-直接经济损失':
            sql = ["match (m:不同地区地质灾害情况27_1) where m.地区='{0}' return m.直接经济损失,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-27-发生地质灾害数量':
            sql = ["match (m:不同年份地质灾害情况27) where m.年份='{0}' return m.发生地质灾害数量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-27-滑坡次数':
            sql = ["match (m:不同年份地质灾害情况27) where m.年份='{0}' return m.滑坡次数,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-27-崩塌次数':
            sql = ["match (m:不同年份地质灾害情况27) where m.年份='{0}' return m.崩塌次数,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-27-泥石流次数':
            sql = ["match (m:不同年份地质灾害情况27) where m.年份='{0}' return m.泥石流次数,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-27-地面塌陷次数':
            sql = ["match (m:不同年份地质灾害情况27) where m.年份='{0}' return m.地面塌陷次数,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-27-人员伤亡数量':
            sql = ["match (m:不同年份地质灾害情况27) where m.年份='{0}' return m.人员伤亡数量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-27-死亡人数':
            sql = ["match (m:不同年份地质灾害情况27) where m.年份='{0}' return m.死亡人数,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-27-直接经济损失':
            sql = ["match (m:不同年份地质灾害情况27) where m.年份='{0}' return m.直接经济损失,m.年份".format(i) for i in entities]


        elif question_type == '资源与环境-28-森林火灾次数':
            sql = ["match (m:不同地区森林火灾情况28) where m.地区='{0}' return m.森林火灾次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-28-一般火灾次数':
            sql = ["match (m:不同地区森林火灾情况28) where m.地区='{0}' return m.一般火灾次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-28-较大火灾次数':
            sql = ["match (m:不同地区森林火灾情况28) where m.地区='{0}' return m.较大火灾次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-28-重大火灾次数':
            sql = ["match (m:不同地区森林火灾情况28) where m.地区='{0}' return m.重大火灾次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-28-特别重大火灾次数':
            sql = ["match (m:不同地区森林火灾情况28) where m.地区='{0}' return m.特别重大火灾次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-28-火场总面积':
            sql = ["match (m:不同地区森林火灾情况28) where m.地区='{0}' return m.火场总面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-28-受害森林面积':
            sql = ["match (m:不同地区森林火灾情况28) where m.地区='{0}' return m.受害森林面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-28-伤亡人数':
            sql = ["match (m:不同地区森林火灾情况28) where m.地区='{0}' return m.伤亡人数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-28-其它损失折款':
            sql = ["match (m:不同地区森林火灾情况28) where m.地区='{0}' return m.其它损失折款,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-29-1-林业有害生物发生面积':
            sql = ["match (m:不同地区生物灾害情况29_1) where m.地区='{0}' return m.林业有害生物发生面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-29-1-林业有害生物防治面积':
            sql = ["match (m:不同地区生物灾害情况29_1) where m.地区='{0}' return m.林业有害生物防治面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-29-1-林业有害生物防治率':
            sql = ["match (m:不同地区生物灾害情况29_1) where m.地区='{0}' return m.林业有害生物防治率,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-29-1-森林病害发生面积':
            sql = ["match (m:不同地区生物灾害情况29_1) where m.地区='{0}' return m.森林病害发生面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-29-1-森林病害防治面积':
            sql = ["match (m:不同地区生物灾害情况29_1) where m.地区='{0}' return m.森林病害防治面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-29-1-森林虫害发生面积':
            sql = ["match (m:不同地区生物灾害情况29_1) where m.地区='{0}' return m.森林虫害发生面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-29-1-森林虫害防治面积':
            sql = ["match (m:不同地区生物灾害情况29_1) where m.地区='{0}' return m.森林虫害防治面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-29-1-森林鼠害发生面积':
            sql = ["match (m:不同地区生物灾害情况29_1) where m.地区='{0}' return m.森林鼠害发生面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-29-1-森林鼠害防治面积':
            sql = ["match (m:不同地区生物灾害情况29_1) where m.地区='{0}' return m.森林鼠害防治面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-29-1-有害植物发生面积':
            sql = ["match (m:不同地区生物灾害情况29_1) where m.地区='{0}' return m.有害植物发生面积,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-29-1-有害植物防治面积':
            sql = ["match (m:不同地区生物灾害情况29_1) where m.地区='{0}' return m.有害植物防治面积,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-29-林业有害生物发生面积':
            sql = ["match (m:不同年份生物灾害情况29) where m.年份='{0}' return m.林业有害生物发生面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-29-林业有害生物防治面积':
            sql = ["match (m:不同年份生物灾害情况29) where m.年份='{0}' return m.林业有害生物防治面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-29-林业有害生物防治率':
            sql = ["match (m:不同年份生物灾害情况29) where m.年份='{0}' return m.林业有害生物防治率,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-29-森林病害发生面积':
            sql = ["match (m:不同年份生物灾害情况29) where m.年份='{0}' return m.森林病害发生面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-29-森林病害防治面积':
            sql = ["match (m:不同年份生物灾害情况29) where m.年份='{0}' return m.森林病害防治面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-29-森林虫害发生面积':
            sql = ["match (m:不同年份生物灾害情况29) where m.年份='{0}' return m.森林虫害发生面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-29-森林虫害防治面积':
            sql = ["match (m:不同年份生物灾害情况29) where m.年份='{0}' return m.森林虫害防治面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-29-森林鼠害发生面积':
            sql = ["match (m:不同年份生物灾害情况29) where m.年份='{0}' return m.森林鼠害发生面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-29-森林鼠害防治面积':
            sql = ["match (m:不同年份生物灾害情况29) where m.年份='{0}' return m.森林鼠害防治面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-29-有害植物发生面积':
            sql = ["match (m:不同年份生物灾害情况29) where m.年份='{0}' return m.有害植物发生面积,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-29-有害植物防治面积':
            sql = ["match (m:不同年份生物灾害情况29 where m.年份='{0}' return m.有害植物防治面积,m.年份".format(i) for i in entities]


        elif question_type == '资源与环境-30-突发环境事件次数':
            sql = ["match (m:不同地区突发环境事件次数30) where m.地区='{0}' return m.突发环境事件次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-30-特别重大环境事件次数':
            sql = ["match (m:不同地区突发环境事件次数30) where m.地区='{0}' return m.特别重大环境事件次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-30-重大环境事件次数':
            sql = ["match (m:不同地区突发环境事件次数30) where m.地区='{0}' return m.重大环境事件次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-30-较大环境事件次数':
            sql = ["match (m:不同地区突发环境事件次数30) where m.地区='{0}' return m.较大环境事件次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-30-一般环境事件次数':
            sql = ["match (m:不同地区突发环境事件次数30) where m.地区='{0}' return m.一般环境事件次数,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-31-1-地震次数':
            sql = ["match (m:不同地区地震情况31_1) where m.地区='{0}' return m.地震次数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-31-1-5.0-5.9级地震次数':
            sql = ["match (m:不同地区地震情况31_1) where m.地区='{0}' return m.地震次数5点0_5点9级,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-31-1-6.0-6.9级地震次数':
            sql = ["match (m:不同地区地震情况31_1) where m.地区='{0}' return m.地震次数6点0_6点9级,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-31-1-7.0级以上地震次数':
            sql = ["match (m:不同地区地震情况31_1) where m.地区='{0}' return m.地震次数7点0_7点9级,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-31-1-人员伤亡数量':
            sql = ["match (m:不同地区地震情况31_1) where m.地区='{0}' return m.人员伤亡数量,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-31-1-死亡人数':
            sql = ["match (m:不同地区地震情况31_1) where m.地区='{0}' return m.死亡人数,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-31-1-直接经济损失':
            sql = ["match (m:不同地区地震情况31_1) where m.地区='{0}' return m.直接经济损失,m.地区".format(i) for i in entities]



        elif question_type == '资源与环境-31-地震次数':
            sql = ["match (m:不同年份地震情况31) where m.年份='{0}' return m.地震次数,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-31-5.0-5.9级地震次数':
            sql = ["match (m:不同年份地震情况31) where m.年份='{0}' return m.地震次数5点0_5点9级,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-31-6.0-6.9级地震次数':
            sql = ["match (m:不同年份地震情况31) where m.年份='{0}' return m.地震次数6点0_6点9级,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-31-7.0级以上地震次数':
            sql = ["match (m:不同年份地震情况31) where m.年份='{0}' return m.地震次数7点0_7点9级,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-31-人员伤亡数量':
            sql = ["match (m:不同年份地震情况31) where m.年份='{0}' return m.人员伤亡数量,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-31-死亡人数':
            sql = ["match (m:不同年份地震情况31) where m.年份='{0}' return m.死亡人数,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-31-直接经济损失':
            sql = ["match (m:不同年份地震情况31) where m.年份='{0}' return m.直接经济损失,m.年份".format(i) for i in entities]


        elif question_type == '资源与环境-32-发生次数':
            sql = ["match (m:海洋灾害情况32) where m.灾种='{0}' return m.发生次数,m.灾种".format(i) for i in entities]
        elif question_type == '资源与环境-32-人员死亡失踪':
            sql = ["match (m:海洋灾害情况32) where m.灾种='{0}' return m.人员死亡失踪,m.灾种".format(i) for i in entities]
        elif question_type == '资源与环境-32-直接经济损失':
            sql = ["match (m:海洋灾害情况32) where m.灾种='{0}' return m.直接经济损失,m.灾种".format(i) for i in entities]

        elif question_type == '资源与环境-33-第二类水质海域面积':
            sql = ["match (m:海域不同水质面积33) where m.海域='{0}' return m.第二类水质海域面积,m.海域".format(i) for i in entities]
        elif question_type == '资源与环境-33-第三类水质海域面积':
            sql = ["match (m:海域不同水质面积33) where m.海域='{0}' return m.第三类水质海域面积,m.海域".format(i) for i in entities]
        elif question_type == '资源与环境-33-第四类水质海域面积':
            sql = ["match (m:海域不同水质面积33) where m.海域='{0}' return m.第四类水质海域面积,m.海域".format(i) for i in entities]
        elif question_type == '资源与环境-33-劣于第四类水质海域面积':
            sql = ["match (m:海域不同水质面积33) where m.海域='{0}' return m.劣于第四类水质海域面积,m.海域".format(i) for i in entities]


        elif question_type == '资源与环境-34-城镇环境基础设施建设投资':
            sql = ["match (m:不同地区基础建设投资34) where m.地区='{0}' return m.城镇环境基础设施建设投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-34-燃气建设投资':
            sql = ["match (m:不同地区基础建设投资34) where m.地区='{0}' return m.燃气建设投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-34-集中供热建设投资':
            sql = ["match (m:不同地区基础建设投资34) where m.地区='{0}' return m.集中供热建设投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-34-排水建设投资':
            sql = ["match (m:不同地区基础建设投资34) where m.地区='{0}' return m.排水建设投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-34-园林绿化建设投资':
            sql = ["match (m:不同地区基础建设投资34) where m.地区='{0}' return m.园林绿化建设投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-34-市容环境卫生建设投资':
            sql = ["match (m:不同地区基础建设投资34) where m.地区='{0}' return m.市容环境卫生建设投资,m.地区".format(i) for i in entities]



        elif question_type == '资源与环境-35-1-工业污染治理完成投资':
            sql = ["match (m:不同地区污染治理情况35_1) where m.地区='{0}' return m.工业污染治理完成投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-35-1-治理废水投资':
            sql = ["match (m:不同地区污染治理情况35_1) where m.地区='{0}' return m.治理废水投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-35-1-治理废气投资':
            sql = ["match (m:不同地区污染治理情况35_1) where m.地区='{0}' return m.治理废气投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-35-1-治理固体废物投资':
            sql = ["match (m:不同地区污染治理情况35_1) where m.地区='{0}' return m.治理固体废物投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-35-1-治理噪声投资':
            sql = ["match (m:不同地区污染治理情况35_1) where m.地区='{0}' return m.治理噪声投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-35-1-治理其他投资':
            sql = ["match (m:不同地区污染治理情况35_1) where m.地区='{0}' return m.治理其他投资,m.地区".format(i) for i in entities]


        elif question_type == '资源与环境-35-工业污染治理完成投资':
            sql = ["match (m:不同年份污染治理情况35) where m.年份='{0}' return m.工业污染治理完成投资,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-35-治理废水投资':
            sql = ["match (m:不同年份污染治理情况35) where m.年份='{0}' return m.治理废水投资,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-35-治理废气投资':
            sql = ["match (m:不同年份污染治理情况35) where m.年份='{0}' return m.治理废气投资,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-35-治理固体废物投资':
            sql = ["match (m:不同年份污染治理情况35) where m.年份='{0}' return m.治理固体废物投资,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-35-治理噪声投资':
            sql = ["match (m:不同年份污染治理情况35) where m.年份='{0}' return m.治理噪声投资,m.年份".format(i) for i in entities]
        elif question_type == '资源与环境-35-治理其他投资':
            sql = ["match (m:不同年份污染治理情况35) where m.年份='{0}' return m.治理其他投资,m.年份".format(i) for i in entities]


        elif question_type == '资源与环境-36-本年完成林业草原投资总计':
            sql = ["match (m:林业草原投资完成情况36) where m.地区='{0}' return m.本年完成林业草原投资总计,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-36-林业草原国家投资':
            sql = ["match (m:林业草原投资完成情况36) where m.地区='{0}' return m.林业草原国家投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-36-林业草原生态修复治理投资':
            sql = ["match (m:林业草原投资完成情况36) where m.地区='{0}' return m.林业草原生态修复治理投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-36-林业草原林产品加工制造投资':
            sql = ["match (m:林业草原投资完成情况36) where m.地区='{0}' return m.林业草原林产品加工制造投资,m.地区".format(i) for i in entities]
        elif question_type == '资源与环境-36-林业草原林业草原服务保障和公共管理投资':
            sql = ["match (m:林业草原投资完成情况36) where m.地区='{0}' return m.林业草原林业草原服务保障和公共管理投资,m.地区".format(i) for i in entities]

        elif question_type == '国民经济核算-1-人均国民总收入':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.人均国民总收入,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-人均国内生产总值':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.人均国内生产总值,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-国民总收入':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.国民总收入,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-国内生产总值':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.国内生产总值,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-第一产业':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.第一产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-第二产业':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.第二产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-第三产业':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.第三产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-农林牧渔业':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.农林牧渔业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-工业':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.工业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-建筑业':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.建筑业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-批发和零售业':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.批发和零售业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-交通运输仓储和邮政业':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.交通运输仓储和邮政业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-住宿和餐饮业':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.住宿和餐饮业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-金融业':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.金融业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-房地产业':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.房地产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-1-其他':
            sql = ["match (m:国民生产总值2_1) where m.年份='{0}' return m.其他,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-2-国内生产总值':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.国内生产总值,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-第一产业':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.第一产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-第二产业':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.第二产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-第三产业':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.第三产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-农林牧渔业':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.农林牧渔业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-工业':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.工业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-建筑业':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.建筑业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-批发和零售业':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.批发和零售业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-交通运输仓储和邮政业':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.交通运输仓储和邮政业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-住宿和餐饮业':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.住宿和餐饮业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-金融业':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.金融业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-房地产业':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.房地产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-2-其他':
            sql = ["match (m:国内生产总值构成2_2) where m.年份='{0}' return m.其他,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-3-国内生产总值':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.国内生产总值,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-第一产业':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.第一产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-第二产业':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.第二产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-第三产业':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.第三产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-农林牧渔业':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.农林牧渔业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-工业':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.工业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-建筑业':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.建筑业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-批发和零售业':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.批发和零售业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-交通运输仓储和邮政业':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.交通运输仓储和邮政业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-住宿和餐饮业':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.住宿和餐饮业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-金融业':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.金融业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-房地产业':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.房地产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-3-其他':
            sql = ["match (m:不变价国内生产总值2_3) where m.年份='{0}' return m.其他,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-4-人均国民总收入':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.人均国民总收入,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-人均国内生产总值':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.人均国内生产总值,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-国民总收入':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.国民总收入,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-国内生产总值':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.国内生产总值,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-第一产业':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.第一产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-第二产业':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.第二产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-第三产业':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.第三产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-农林牧渔业':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.农林牧渔业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-工业':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.工业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-建筑业':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.建筑业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-批发和零售业':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.批发和零售业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-交通运输仓储和邮政业':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.交通运输仓储和邮政业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-住宿和餐饮业':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.住宿和餐饮业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-金融业':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.金融业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-房地产业':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.房地产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-4-其他':
            sql = ["match (m:国内生产总值指数2_4) where m.年份='{0}' return m.其他,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-6-国内生产总值':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.国内生产总值,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-农林牧渔业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.农林牧渔业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-采矿业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.采矿业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-制造业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.制造业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-电力热力燃气及水':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.电力热力燃气及水,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-建筑业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.建筑业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-批发和零售业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.批发和零售业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-交通运输仓储和邮政业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.交通运输仓储和邮政业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-住宿和餐饮业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.住宿和餐饮业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-信息传输软件和信息':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.信息传输软件和信息,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-金融业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.金融业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-房地产业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.房地产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-租赁和商务服务业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.租赁和商务服务业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-科学研究和技术服务业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.科学研究和技术服务业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-水利环境和公共设施管理业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.水利环境和公共设施管理业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-居民服务修理和其他服务业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.居民服务修理和其他服务业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-教育':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.教育,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-卫生和社会工作':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.卫生和社会工作,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-文化体育和娱乐业':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.文化体育和娱乐业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-6-公共管理社会保障':
            sql = ["match (m:分行业增加值2_6) where m.年份='{0}' return m.公共管理社会保障,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-7-国内生产总值':
            sql = ["match (m:三次产业和主要行业贡献率2_7) where m.年份='{0}' return m.国内生产总值,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-7-第一产业':
            sql = ["match (m:三次产业和主要行业贡献率2_7) where m.年份='{0}' return m.第一产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-7-第二产业':
            sql = ["match (m:三次产业和主要行业贡献率2_7) where m.年份='{0}' return m.第二产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-7-第三产业':
            sql = ["match (m:三次产业和主要行业贡献率2_7) where m.年份='{0}' return m.第三产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-7-工业':
            sql = ["match (m:三次产业和主要行业贡献率2_7) where m.年份='{0}' return m.工业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-7-批发和零售业':
            sql = ["match (m:三次产业和主要行业贡献率2_7) where m.年份='{0}' return m.批发和零售业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-7-金融业':
            sql = ["match (m:三次产业和主要行业贡献率2_7) where m.年份='{0}' return m.金融业,m.年份".format(i) for i in entities]

        elif question_type == '国民经济核算-8-国内生产总值':
            sql = ["match (m:三次产业和主要行业对国内生产总值增长的拉动xls2_8) where m.年份='{0}' return m.国内生产总值,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-8-第一产业':
            sql = ["match (m:三次产业和主要行业对国内生产总值增长的拉动xls2_8) where m.年份='{0}' return m.第一产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-8-第二产业':
            sql = ["match (m:三次产业和主要行业对国内生产总值增长的拉动xls2_8) where m.年份='{0}' return m.第二产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-8-第三产业':
            sql = ["match (m:三次产业和主要行业对国内生产总值增长的拉动xls2_8) where m.年份='{0}' return m.第三产业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-8-工业':
            sql = ["match (m:三次产业和主要行业对国内生产总值增长的拉动xls2_8) where m.年份='{0}' return m.工业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-8-批发和零售业':
            sql = ["match (m:三次产业和主要行业对国内生产总值增长的拉动xls2_8) where m.年份='{0}' return m.批发和零售业,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-8-金融业':
            sql = ["match (m:三次产业和主要行业对国内生产总值增长的拉动xls2_8) where m.年份='{0}' return m.金融业,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-9-地区生产总值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.地区生产总值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-第一产业增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.第一产业增加值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-第二产业增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.第二产业增加值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-第三产业增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.第三产业增加值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-农林牧渔业增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.农林牧渔业增加值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-工业增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.工业增加值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-建筑业增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.建筑业增加值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-批发和零售业增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.批发和零售业增加值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-交通运输仓储和邮政业增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.交通运输仓储和邮政业增加值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-住宿和餐饮业增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.住宿和餐饮业增加值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-金融业增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.金融业增加值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-房地产业增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.房地产业增加值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-其他增加值':
            sql = ["match (m:生产总值2_9) where m.地区='{0}' return m.其他增加值,m.地区".format(i) for i in entities]


        elif question_type == '国民经济核算-9-2-人均地区生产总值':
            sql = ["match (m:生产总值占比2_9_2) where m.地区='{0}' return m.人均地区生产总值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-2-第一产业构成':
            sql = ["match (m:生产总值占比2_9_2) where m.地区='{0}' return m.第一产业构成,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-2-第二产业构成':
            sql = ["match (m:生产总值占比2_9_2) where m.地区='{0}' return m.第二产业构成,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-2-第三产业构成':
            sql = ["match (m:生产总值占比2_9_2) where m.地区='{0}' return m.第三产业构成,m.地区".format(i) for i in entities]



        elif question_type == '国民经济核算-9-3-地区生产总值':
            sql = ["match (m:生产总值指数2_9_3) where m.地区='{0}' return m.地区生产总值,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-3-第一产业':
            sql = ["match (m:生产总值指数2_9_3) where m.地区='{0}' return m.第一产业,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-3-第二产业':
            sql = ["match (m:生产总值指数2_9_3) where m.地区='{0}' return m.第二产业,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-3-第三产业':
            sql = ["match (m:生产总值指数2_9_3) where m.地区='{0}' return m.第三产业,m.地区".format(i) for i in entities]
        elif question_type == '国民经济核算-9-3-人均地区生产总值':
            sql = ["match (m:生产总值指数2_9_3) where m.地区='{0}' return m.人均地区生产总值,m.地区".format(i) for i in entities]


        elif question_type == '国民经济核算-10-生产总值':
            sql = ["match (m:支出法国内生产总值2_10) where m.年份='{0}' return m.生产总值,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-10-最终消费':
            sql = ["match (m:支出法国内生产总值2_10) where m.年份='{0}' return m.最终消费,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-10-资本形成总额':
            sql = ["match (m:支出法国内生产总值2_10) where m.年份='{0}' return m.资本形成总额,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-10-货物和服务净出口':
            sql = ["match (m:支出法国内生产总值2_10) where m.年份='{0}' return m.货物和服务净出口,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-10-最终消费率':
            sql = ["match (m:支出法国内生产总值2_10) where m.年份='{0}' return m.最终消费率,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-10-资本形成率':
            sql = ["match (m:支出法国内生产总值2_10) where m.年份='{0}' return m.资本形成率,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-11-1-居民消费支出':
            sql = ["match (m:居民消费支出占比2_11_1) where m.年份='{0}' return m.居民消费支出,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-11-1-政府消费支出':
            sql = ["match (m:居民消费支出占比2_11_1) where m.年份='{0}' return m.政府消费支出,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-11-2-居民消费支出':
            sql = ["match (m:最终消费支出2_11_2) where m.年份='{0}' return m.居民消费支出,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-11-2-城镇居民支出':
            sql = ["match (m:最终消费支出2_11_2) where m.年份='{0}' return m.城镇居民支出,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-11-2-农村居民支出':
            sql = ["match (m:最终消费支出2_11_2) where m.年份='{0}' return m.农村居民支出,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-11-2-政府消费支出':
            sql = ["match (m:最终消费支出2_11_2) where m.年份='{0}' return m.政府消费支出,m.年份".format(i) for i in entities]



        elif question_type == '国民经济核算-11-3-居民消费支出':
            sql = ["match (m:最终消费支出占比2_11_3) where m.年份='{0}' return m.居民消费支出,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-11-3-政府消费支出':
            sql = ["match (m:最终消费支出占比2_11_3) where m.年份='{0}' return m.政府消费支出,m.年份".format(i) for i in entities]

        elif question_type == '国民经济核算-11-4-出口':
            sql = ["match (m:货物与服务净出口2_11_4) where m.年份='{0}' return m.出口,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-11-4-进口':
            sql = ["match (m:货物与服务净出口2_11_4) where m.年份='{0}' return m.进口,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-11-5-固定资本形成总额':
            sql = ["match (m:资本形成总额2_11_5) where m.年份='{0}' return m.固定资本形成总额,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-11-5-存货变动':
            sql = ["match (m:资本形成总额2_11_5) where m.年份='{0}' return m.存货变动,m.年份".format(i) for i in entities]

        elif question_type == '国民经济核算-11-6-固定资本形成总额':
            sql = ["match (m:资本形成总额占比2_11_6) where m.年份='{0}' return m.固定资本形成总额,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-11-6-存货变动':
            sql = ["match (m:资本形成总额占比2_11_6) where m.年份='{0}' return m.存货变动,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-12-居民实际最终消费':
            sql = ["match (m:实际最终消费构成2_12) where m.年份='{0}' return m.居民实际最终消费,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-12-政府实际最终消费':
            sql = ["match (m:实际最终消费构成2_12) where m.年份='{0}' return m.政府实际最终消费,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-12-1-居民实际最终消费':
            sql = ["match (m:实际最终消费2_12_1) where m.年份='{0}' return m.居民实际最终消费,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-12-1-政府实际最终消费':
            sql = ["match (m:实际最终消费2_12_1) where m.年份='{0}' return m.政府实际最终消费,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-13-全体居民绝对数':
            sql = ["match (m:生活消费水平2_13) where m.年份='{0}' return m.全体居民绝对数,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-13-城镇居民绝对数':
            sql = ["match (m:生活消费水平2_13) where m.年份='{0}' return m.城镇居民绝对数,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-13-农村居民绝对数':
            sql = ["match (m:生活消费水平2_13) where m.年份='{0}' return m.农村居民绝对数,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-13-城镇居民消费水平与农村居民消费水平的比值':
            sql = ["match (m:生活消费水平2_13) where m.年份='{0}' return m.城镇居民消费水平与农村居民消费水平的比值,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-13-全体居民指数':
            sql = ["match (m:生活消费水平2_13) where m.年份='{0}' return m.全体居民指数,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-13-城镇居民消费指数':
            sql = ["match (m:生活消费水平2_13) where m.年份='{0}' return m.城镇居民消费指数,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-13-农村居民消费指数':
            sql = ["match (m:生活消费水平2_13) where m.年份='{0}' return m.农村居民消费指数,m.年份".format(i) for i in entities]



        elif question_type == '国民经济核算-14-最终消费支出贡献率':
            sql = ["match (m:三大需求对国内生产总值增长的贡献率和拉动2_14) where m.年份='{0}' return m.最终消费支出贡献率,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-14-最终消费支出拉动':
            sql = ["match (m:三大需求对国内生产总值增长的贡献率和拉动2_14) where m.年份='{0}' return m.最终消费支出拉动,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-14-资本形成总额贡献率':
            sql = ["match (m:三大需求对国内生产总值增长的贡献率和拉动2_14) where m.年份='{0}' return m.资本形成总额贡献率,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-14-资本形成总额拉动':
            sql = ["match (m:三大需求对国内生产总值增长的贡献率和拉动2_14) where m.年份='{0}' return m.资本形成总额拉动,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-14-货物和服务净出口贡献率':
            sql = ["match (m:三大需求对国内生产总值增长的贡献率和拉动2_14) where m.年份='{0}' return m.货物和服务净出口贡献率,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-14-货物和服务净出口拉动':
            sql = ["match (m:三大需求对国内生产总值增长的贡献率和拉动2_14) where m.年份='{0}' return m.货物和服务净出口拉动,m.年份".format(i) for i in entities]




        elif question_type == '国民经济核算-16-净金融投资':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.净金融投资,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-资金运用合计':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.资金运用合计,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-资金来源合计':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.资金来源合计,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-通货':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.通货,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-存款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.存款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-活期存款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.活期存款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-定期存款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.定期存款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-财政存款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.财政存款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-外汇存款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.外汇存款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-其他存款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.其他存款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-证券公司客户保证金':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.证券公司客户保证金,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-贷款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.贷款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-短期贷款与票据融资':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.短期贷款与票据融资,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-中长期贷款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.中长期贷款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-外汇贷款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.外汇贷款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-委托贷款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.委托贷款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-其他贷款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.其他贷款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-未贴现的银行承兑汇票':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.未贴现的银行承兑汇票,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-保险准备金':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.保险准备金,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-金融机构往来':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.金融机构往来,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-存款准备金':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.存款准备金,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-债券':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.债券,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-政府债券':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.政府债券,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-金融债券':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.金融债券,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-中央银行债券':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.中央银行债券,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-企业债券':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.企业债券,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-股票':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.股票,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-证券投资基金份额':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.证券投资基金份额,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-库存现金':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.库存现金,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-中央银行贷款':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.中央银行贷款,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-其他':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.其他,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-直接投资':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.直接投资,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-其他对外债权债务':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.其他对外债权债务,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-国际储备资产':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.国际储备资产,m.交易项目".format(i) for i in entities]
        elif question_type == '国民经济核算-16-国际收支错误与遗漏':
            sql = ["match (m:资金流量表_金融交易_2020年_2_16) where m.交易项目='{0}' return m.国际收支错误与遗漏,m.交易项目".format(i) for i in entities]

        elif question_type == '国民经济核算-17-企业部门初次分配总收入':
            sql = ["match (m:企业广义政府与住户部门初次分配总收入及比重_2_17) where m.年份='{0}' return m.企业部门初次分配总收入,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-17-企业部门占比':
            sql = ["match (m:企业广义政府与住户部门初次分配总收入及比重_2_17) where m.年份='{0}' return m.企业部门占比,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-17-广义政府部门初次分配总收入':
            sql = ["match (m:企业广义政府与住户部门初次分配总收入及比重_2_17) where m.年份='{0}' return m.广义政府部门初次分配总收入,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-17-广义政府部门占比':
            sql = ["match (m:企业广义政府与住户部门初次分配总收入及比重_2_17) where m.年份='{0}' return m.广义政府部门占比,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-17-住户部门初次分配总收入':
            sql = ["match (m:企业广义政府与住户部门初次分配总收入及比重_2_17) where m.年份='{0}' return m.住户部门初次分配总收入,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-17-住户部门占比':
            sql = ["match (m:企业广义政府与住户部门初次分配总收入及比重_2_17) where m.年份='{0}' return m.住户部门占比,m.年份".format(i) for i in entities]


        elif question_type == '国民经济核算-19-企业部门调整后可支配总收入':
            sql = ["match (m:企业广义政府与住户部门调整后可支配总收入及比重_2_19) where m.年份='{0}' return m.企业部门调整后可支配总收入,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-19-企业部门调整后占比':
            sql = ["match (m:企业广义政府与住户部门调整后可支配总收入及比重_2_19) where m.年份='{0}' return m.企业部门调整后占比,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-19-广义政府部门调整后可支配总收入':
            sql = ["match (m:企业广义政府与住户部门调整后可支配总收入及比重_2_19) where m.年份='{0}' return m.广义政府部门调整后可支配总收入,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-19-广义政府部门调整后占比':
            sql = ["match (m:企业广义政府与住户部门调整后可支配总收入及比重_2_19) where m.年份='{0}' return m.广义政府部门调整后占比,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-19-住户部门调整后可支配总收入':
            sql = ["match (m:企业广义政府与住户部门调整后可支配总收入及比重_2_19) where m.年份='{0}' return m.住户部门调整后可支配总收入,m.年份".format(i) for i in entities]
        elif question_type == '国民经济核算-19-住户部门调整后占比':
            sql = ["match (m:企业广义政府与住户部门调整后可支配总收入及比重_2_19) where m.年份='{0}' return m.住户部门调整后占比,m.年份".format(i) for i in entities]



        elif question_type == '国民经济核算-22-农林牧渔产品和服务':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.农林牧渔产品和服务,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-采掘产品':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.采掘产品,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-食品和烟草':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.食品和烟草,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-纺织服装鞋及皮革羽绒制品':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.纺织服装鞋及皮革羽绒制品,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-木材加工家具造纸印刷和文教工美用品':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.木材加工家具造纸印刷和文教工美用品,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-炼油炼焦和化学产品':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.炼油炼焦和化学产品,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-非金属矿物制品':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.非金属矿物制品,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-金属冶炼加工及制品':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.金属冶炼加工及制品,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-机械设备和交通运输设备及电子电气及其他设备':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.机械设备和交通运输设备及电子电气及其他设备,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-其他各类制造产品':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.其他各类制造产品,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-电力热力燃气和水的生产和供应':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.电力热力燃气和水的生产和供应,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-建筑':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.建筑,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-批发零售运输仓储邮政':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.批发零售运输仓储邮政,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-信息传输软件和信息技术服务':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.信息传输软件和信息技术服务,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-金融和房地产':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.金融和房地产,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-科学研究和技术服务':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.科学研究和技术服务,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-其他服务':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.其他服务,m.投入".format(i) for i in entities]
        elif question_type == '国民经济核算-22-中间投入合计':
            sql = ["match (m:投入产出基本流量表2020年_2_22) where m.投入='{0}' return m.中间投入合计,m.投入".format(i) for i in entities]



        elif question_type == '能源-1-一次能源生产总量':
            sql = ["match (m:一次能源生产总量及构成3_1) where m.年份='{0}' return m.一次能源生产总量,m.年份".format(i) for i in entities]
        elif question_type == '能源-1-原煤占一次能源生产总量的比重':
            sql = ["match (m:一次能源生产总量及构成3_1) where m.年份='{0}' return m.原煤占一次能源生产总量的比重,m.年份".format(i) for i in entities]
        elif question_type == '能源-1-原油占一次能源生产总量的比重':
            sql = ["match (m:一次能源生产总量及构成3_1) where m.年份='{0}' return m.原油占一次能源生产总量的比重,m.年份".format(i) for i in entities]
        elif question_type == '能源-1-天然气':
            sql = ["match (m:一次能源生产总量及构成3_1) where m.年份='{0}' return m.天然气,m.年份".format(i) for i in entities]
        elif question_type == '能源-1-一次电力及其他能源':
            sql = ["match (m:一次能源生产总量及构成3_1) where m.年份='{0}' return m.一次电力及其他能源,m.年份".format(i) for i in entities]


        elif question_type == '能源-2-能源消费总量':
            sql = ["match (m:能源消费总量及构成3_2) where m.年份='{0}' return m.能源消费总量,m.年份".format(i) for i in entities]
        elif question_type == '能源-2-煤炭占能源消费总量的比重':
            sql = ["match (m:能源消费总量及构成3_2) where m.年份='{0}' return m.煤炭占能源消费总量的比重,m.年份".format(i) for i in entities]
        elif question_type == '能源-2-石油占能源消费总量的比重':
            sql = ["match (m:能源消费总量及构成3_2) where m.年份='{0}' return m.石油占能源消费总量的比重,m.年份".format(i) for i in entities]
        elif question_type == '能源-2-天然气占能源消费总量的比重':
            sql = ["match (m:能源消费总量及构成3_2) where m.年份='{0}' return m.天然气占能源消费总量的比重,m.年份".format(i) for i in entities]
        elif question_type == '能源-2-一次电力及其他能源占能源消费总量的比重':
            sql = ["match (m:能源消费总量及构成3_2) where m.年份='{0}' return m.一次电力及其他能源占能源消费总量的比重,m.年份".format(i) for i in entities]



        elif question_type == '能源-3-可供消费的能源总量':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.可供消费的能源总量,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-一次能源生产总量':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.一次能源生产总量,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-回收量':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.回收量,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-进口量':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.进口量,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-出口量':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.出口量,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-年初年末库存差额':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.年初年末库存差额,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-能源消费总量':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.能源消费总量,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-渔业':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.渔业,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-工业':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.工业,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-建筑业':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.建筑业,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-邮政业':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.邮政业,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-住宿和餐饮业':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.住宿和餐饮业,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-其他':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.其他,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-居民生活':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.居民生活,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-终端消费':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.终端消费,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-加工转换损失量':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.加工转换损失量,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-炼焦':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.炼焦,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-炼油及煤制油':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.炼油及煤制油,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-损失量':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.损失量,m.年份".format(i) for i in entities]
        elif question_type == '能源-3-平衡差额':
            sql = ["match (m:综合能源平衡表3_3) where m.年份='{0}' return m.平衡差额,m.年份".format(i) for i in entities]



        elif question_type == '能源-4-石油可供量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.石油可供量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-石油生产量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.石油生产量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-石油进口量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.石油进口量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-石油出口量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.石油出口量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-石油年初年末库存差额':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.石油年初年末库存差额,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-农林牧渔业中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.农林牧渔业中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-工业中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.工业中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-建筑业中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.建筑业中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-交通运输仓储和邮政业中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.交通运输仓储和邮政业中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-批发和零售业住宿和餐饮业中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.批发和零售业住宿和餐饮业中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-其他中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.其他中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-居民生活中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.居民生活中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-终端消费中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.终端消费中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-中间消费中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.中间消费中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-火力发电中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.火力发电中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-供热中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.供热中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-制气中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.制气中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-炼油损失量中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.炼油损失量中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-损失量中石油消费量':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.损失量中石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-4-石油平衡差额':
            sql = ["match (m:石油平衡表3_4) where m.年份='{0}' return m.石油平衡差额,m.年份".format(i) for i in entities]



        elif question_type == '能源-5-煤炭可供量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.煤炭可供量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-煤炭生产量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.煤炭生产量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-煤炭进口量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.煤炭进口量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-煤炭出口量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.煤炭出口量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-煤炭年初年末库存差额':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.煤炭年初年末库存差额,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-农林牧渔业中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.农林牧渔业中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-工业中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.工业中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-建筑业中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.建筑业中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-交通运输仓储和邮政业中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.交通运输仓储和邮政业中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-批发和零售业住宿和餐饮业中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.批发和零售业住宿和餐饮业中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-其他中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.其他中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-居民生活中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.居民生活中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-终端消费中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.终端消费中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-中间消费中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.中间消费中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-火力发电中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.火力发电中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-供热中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.供热中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-炼焦中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.炼焦中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-煤制油中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.煤制油中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-制气中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.制气中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-洗选损耗中煤炭消费量':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.洗选损耗中煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-5-煤炭平衡差额':
            sql = ["match (m:煤炭平衡表3_5) where m.年份='{0}' return m.煤炭平衡差额,m.年份".format(i) for i in entities]




        elif question_type == '能源-6-可供量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.可供量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-电力生产量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.电力生产量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-水电生产量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.水电生产量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-火电生产量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.火电生产量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-核电生产量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.核电生产量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-风电生产量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.风电生产量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-电力进口量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.电力进口量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-电力出口量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.电力出口量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-电力消费量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.电力消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-农林牧渔业中电力消费量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.农林牧渔业中电力消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-工业中电力消费量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.工业中电力消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-建筑业中电力消费量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.建筑业中电力消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-交通运输仓储和邮政业中电力消费量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.交通运输仓储和邮政业中电力消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-批发和零售业住宿和餐饮业中电力消费量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.批发和零售业住宿和餐饮业中电力消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-其他中电力消费量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.其他中电力消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-居民生活中电力消费量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.居民生活中电力消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-终端消费中电力消费量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.终端消费中电力消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-6-输配电损失量':
            sql = ["match (m:电力平衡表3_6) where m.年份='{0}' return m.输配电损失量,m.年份".format(i) for i in entities]


        elif question_type == '能源-7-能源生产比上年增长':
            sql = ["match (m:能源生产弹性系数3_7) where m.年份='{0}' return m.能源生产比上年增长,m.年份".format(i) for i in entities]
        elif question_type == '能源-7-电力生产比上年增长':
            sql = ["match (m:能源生产弹性系数3_7) where m.年份='{0}' return m.电力生产比上年增长,m.年份".format(i) for i in entities]
        elif question_type == '能源-7-国内生产总值比上年增长':
            sql = ["match (m:能源生产弹性系数3_7) where m.年份='{0}' return m.国内生产总值比上年增长,m.年份".format(i) for i in entities]
        elif question_type == '能源-7-能源生产弹性系数':
            sql = ["match (m:能源生产弹性系数3_7) where m.年份='{0}' return m.能源生产弹性系数,m.年份".format(i) for i in entities]
        elif question_type == '能源-7-电力生产弹性系数':
            sql = ["match (m:能源生产弹性系数3_7) where m.年份='{0}' return m.电力生产弹性系数,m.年份".format(i) for i in entities]



        elif question_type == '能源-8-能源消费比上年增长':
            sql = ["match (m:能源消费弹性系数3_8) where m.年份='{0}' return m.能源消费比上年增长,m.年份".format(i) for i in entities]
        elif question_type == '能源-8-电力消费比上年增长':
            sql = ["match (m:能源消费弹性系数3_8) where m.年份='{0}' return m.电力消费比上年增长,m.年份".format(i) for i in entities]
        elif question_type == '能源-8-国内消费总值比上年增长':
            sql = ["match (m:能源消费弹性系数3_8) where m.年份='{0}' return m.国内消费总值比上年增长,m.年份".format(i) for i in entities]
        elif question_type == '能源-8-能源消费弹性系数':
            sql = ["match (m:能源消费弹性系数3_8) where m.年份='{0}' return m.能源消费弹性系数,m.年份".format(i) for i in entities]
        elif question_type == '能源-8-电力消费弹性系数':
            sql = ["match (m:能源消费弹性系数3_8) where m.年份='{0}' return m.电力消费弹性系数,m.年份".format(i) for i in entities]


        elif question_type == '能源-9-能源消费总量':
            sql = ["match (m:按行业分能源消费量_2020年_3_9) where m.行业='{0}' return m.能源消费总量,m.行业".format(i) for i in entities]
        elif question_type == '能源-9-煤炭':
            sql = ["match (m:按行业分能源消费量_2020年_3_9) where m.行业='{0}' return m.煤炭,m.行业".format(i) for i in entities]
        elif question_type == '能源-9-焦炭':
            sql = ["match (m:按行业分能源消费量_2020年_3_9) where m.行业='{0}' return m.焦炭,m.行业".format(i) for i in entities]
        elif question_type == '能源-9-原油':
            sql = ["match (m:按行业分能源消费量_2020年_3_9) where m.行业='{0}' return m.原油,m.行业".format(i) for i in entities]
        elif question_type == '能源-9-汽油':
            sql = ["match (m:按行业分能源消费量_2020年_3_9) where m.行业='{0}' return m.汽油,m.行业".format(i) for i in entities]
        elif question_type == '能源-9-煤油':
            sql = ["match (m:按行业分能源消费量_2020年_3_9) where m.行业='{0}' return m.煤油,m.行业".format(i) for i in entities]
        elif question_type == '能源-9-柴油':
            sql = ["match (m:按行业分能源消费量_2020年_3_9) where m.行业='{0}' return m.柴油,m.行业".format(i) for i in entities]
        elif question_type == '能源-9-燃料油':
            sql = ["match (m:按行业分能源消费量_2020年_3_9) where m.行业='{0}' return m.燃料油,m.行业".format(i) for i in entities]
        elif question_type == '能源-9-天然气':
            sql = ["match (m:按行业分能源消费量_2020年_3_9) where m.行业='{0}' return m.天然气,m.行业".format(i) for i in entities]
        elif question_type == '能源-9-电力':
            sql = ["match (m:按行业分能源消费量_2020年_3_9) where m.行业='{0}' return m.电力,m.行业".format(i) for i in entities]


        elif question_type == '能源-10-总效率':
            sql = ["match (m:能源加工转换效率3_10) where m.年份='{0}' return m.总效率,m.年份".format(i) for i in entities]
        elif question_type == '能源-10-发电及供热':
            sql = ["match (m:能源加工转换效率3_10) where m.年份='{0}' return m.发电及供热,m.年份".format(i) for i in entities]
        elif question_type == '能源-10-炼焦':
            sql = ["match (m:能源加工转换效率3_10) where m.年份='{0}' return m.炼焦,m.年份".format(i) for i in entities]
        elif question_type == '能源-10-炼油及煤制油':
            sql = ["match (m:能源加工转换效率3_10) where m.年份='{0}' return m.炼油及煤制油,m.年份".format(i) for i in entities]


        elif question_type == '能源-11-合计':
            sql = ["match (m:平均每天能源消费量3_11) where m.年份='{0}' return m.合计,m.年份".format(i) for i in entities]
        elif question_type == '能源-11-煤炭':
            sql = ["match (m:平均每天能源消费量3_11) where m.年份='{0}' return m.煤炭,m.年份".format(i) for i in entities]
        elif question_type == '能源-11-焦炭':
            sql = ["match (m:平均每天能源消费量3_11) where m.年份='{0}' return m.焦炭,m.年份".format(i) for i in entities]
        elif question_type == '能源-11-原油':
            sql = ["match (m:平均每天能源消费量3_11) where m.年份='{0}' return m.原油,m.年份".format(i) for i in entities]
        elif question_type == '能源-11-汽油':
            sql = ["match (m:平均每天能源消费量3_11) where m.年份='{0}' return m.汽油,m.年份".format(i) for i in entities]
        elif question_type == '能源-11-煤油':
            sql = ["match (m:平均每天能源消费量3_11) where m.年份='{0}' return m.煤油,m.年份".format(i) for i in entities]
        elif question_type == '能源-11-柴油':
            sql = ["match (m:平均每天能源消费量3_11) where m.年份='{0}' return m.柴油,m.年份".format(i) for i in entities]
        elif question_type == '能源-11-燃料油':
            sql = ["match (m:平均每天能源消费量3_11) where m.年份='{0}' return m.燃料油,m.年份".format(i) for i in entities]
        elif question_type == '能源-11-天然气':
            sql = ["match (m:平均每天能源消费量3_11) where m.年份='{0}' return m.天然气,m.年份".format(i) for i in entities]
        elif question_type == '能源-11-电力':
            sql = ["match (m:平均每天能源消费量3_11) where m.年份='{0}' return m.电力,m.年份".format(i) for i in entities]



        elif question_type == '能源-12-合计':
            sql = ["match (m:居民生活能源消费量3_12) where m.年份='{0}' return m.合计,m.年份".format(i) for i in entities]
        elif question_type == '能源-12-煤炭':
            sql = ["match (m:居民生活能源消费量3_12) where m.年份='{0}' return m.煤炭,m.年份".format(i) for i in entities]
        elif question_type == '能源-12-煤油':
            sql = ["match (m:居民生活能源消费量3_12) where m.年份='{0}' return m.煤油,m.年份".format(i) for i in entities]
        elif question_type == '能源-12-液化石油气':
            sql = ["match (m:居民生活能源消费量3_12) where m.年份='{0}' return m.液化石油气,m.年份".format(i) for i in entities]
        elif question_type == '能源-12-天然气':
            sql = ["match (m:居民生活能源消费量3_12) where m.年份='{0}' return m.天然气,m.年份".format(i) for i in entities]
        elif question_type == '能源-12-煤气':
            sql = ["match (m:居民生活能源消费量3_12) where m.年份='{0}' return m.煤气,m.年份".format(i) for i in entities]
        elif question_type == '能源-12-热力':
            sql = ["match (m:居民生活能源消费量3_12) where m.年份='{0}' return m.热力,m.年份".format(i) for i in entities]
        elif question_type == '能源-12-电力':
            sql = ["match (m:居民生活能源消费量3_12) where m.年份='{0}' return m.电力,m.年份".format(i) for i in entities]


        elif question_type == '能源-13-人均生活能源消费量':
            sql = ["match (m:人均生活能源消费量3_13) where m.年份='{0}' return m.人均生活能源消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-13-煤炭':
            sql = ["match (m:人均生活能源消费量3_13) where m.年份='{0}' return m.煤炭,m.年份".format(i) for i in entities]
        elif question_type == '能源-13-电力':
            sql = ["match (m:人均生活能源消费量3_13) where m.年份='{0}' return m.电力,m.年份".format(i) for i in entities]
        elif question_type == '能源-13-液化石油气':
            sql = ["match (m:人均生活能源消费量3_13) where m.年份='{0}' return m.液化石油气,m.年份".format(i) for i in entities]
        elif question_type == '能源-13-天然气':
            sql = ["match (m:人均生活能源消费量3_13) where m.年份='{0}' return m.天然气,m.年份".format(i) for i in entities]
        elif question_type == '能源-13-煤气':
            sql = ["match (m:人均生活能源消费量3_13) where m.年份='{0}' return m.煤气,m.年份".format(i) for i in entities]



        elif question_type == '能源-14-北京':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.北京,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-天津':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.天津,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-河北':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.河北,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-山西':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.山西,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-内蒙古':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.内蒙古,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-辽宁':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.辽宁,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-吉林':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.吉林,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-黑龙江':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.黑龙江,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-上海':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.上海,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-江苏':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.江苏,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-浙江':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.浙江,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-安徽':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.安徽,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-福建':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.福建,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-江西':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.江西,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-山东':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.山东,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-河南':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.河南,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-湖北':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.湖北,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-湖南':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.湖南,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-广东':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.广东,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-广西':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.广西,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-海南':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.海南,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-重庆':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.重庆,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-四川':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.四川,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-贵州':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.贵州,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-云南':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.云南,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-西藏':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.西藏,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-陕西':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.陕西,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-甘肃':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.甘肃,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-青海':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.青海,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-宁夏':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.宁夏,m.年份".format(i) for i in entities]
        elif question_type == '能源-14-新疆':
            sql = ["match (m:分地区电力能源消费量3_14) where m.年份='{0}' return m.新疆,m.年份".format(i) for i in entities]


        elif question_type == '能源-15-发电装机容量':
            sql = ["match (m:发电装机容量3_15) where m.年份='{0}' return m.发电装机容量,m.年份".format(i) for i in entities]
        elif question_type == '能源-15-火电':
            sql = ["match (m:发电装机容量3_15) where m.年份='{0}' return m.火电,m.年份".format(i) for i in entities]
        elif question_type == '能源-15-水电':
            sql = ["match (m:发电装机容量3_15) where m.年份='{0}' return m.水电,m.年份".format(i) for i in entities]
        elif question_type == '能源-15-核电':
            sql = ["match (m:发电装机容量3_15) where m.年份='{0}' return m.核电,m.年份".format(i) for i in entities]
        elif question_type == '能源-15-风电':
            sql = ["match (m:发电装机容量3_15) where m.年份='{0}' return m.风电,m.年份".format(i) for i in entities]
        elif question_type == '能源-15-太阳能发电':
            sql = ["match (m:发电装机容量3_15) where m.年份='{0}' return m.太阳能发电,m.年份".format(i) for i in entities]
        elif question_type == '能源-15-其他':
            sql = ["match (m:发电装机容量3_15) where m.年份='{0}' return m.其他,m.年份".format(i) for i in entities]


        elif question_type == '能源-16-国内生产总值能源消费量':
            sql = ["match (m:国内生产总值能源消费量3_16) where m.年份='{0}' return m.国内生产总值能源消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-16-国内生产总值煤炭消费量':
            sql = ["match (m:国内生产总值能源消费量3_16) where m.年份='{0}' return m.国内生产总值煤炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-16-国内生产总值焦炭消费量':
            sql = ["match (m:国内生产总值能源消费量3_16) where m.年份='{0}' return m.国内生产总值焦炭消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-16-国内生产总值石油消费量':
            sql = ["match (m:国内生产总值能源消费量3_16) where m.年份='{0}' return m.国内生产总值石油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-16-国内生产总值原油消费量':
            sql = ["match (m:国内生产总值能源消费量3_16) where m.年份='{0}' return m.国内生产总值原油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-16-国内生产总值燃料油消费量':
            sql = ["match (m:国内生产总值能源消费量3_16) where m.年份='{0}' return m.国内生产总值燃料油消费量,m.年份".format(i) for i in entities]
        elif question_type == '能源-16-国内生产总值电力消费量':
            sql = ["match (m:国内生产总值能源消费量3_16) where m.年份='{0}' return m.国内生产总值电力消费量,m.年份".format(i) for i in entities]

        # # 查询年级
        # elif question_type == 'nianji':
        #     #sql = ["MATCH (m:Disease) where m.name = '{0}' return m.name, m.prevent".format(i) for i in entities]
        #     sql=["match(m:个人信息) where m.姓名='{0}' return m.年级,m.姓名".format(i) for i in entities]
        # # 专业
        # elif question_type == 'zhuanye':
        #     sql = ["match(m:个人信息) where m.姓名='{0}' return m.专业,m.姓名".format(i) for i in entities]
        #
        # # 生日
        # elif question_type == 'shengri':
        #     sql = ["match(m:个人信息) where m.姓名='{0}' return m.生日,m.姓名".format(i) for i in entities]
        #
        # # 爱好
        # elif question_type == 'aihao':
        #     sql = ["match(n:个人信息)-[r:`爱好是`]->(m:爱好类型) where n.姓名=\"{0}\" return n.姓名,m.name".format(i) for i in entities]


        # print(sql)
        return sql



if __name__ == '__main__':
    handler = QuestionPaser()
