# -*- coding: utf-8 -*-
import scrapy
from 发改委.NDRC.items import NdrcItem
from 发改委.NDRC.date import *
from 发改委.NDRC.utility import *
from scrapy_splash import SplashRequest
global count
count = 0


class GeneralSpider(scrapy.Spider):
    name = "NDRC_general"
    allowed_domains = ['ndrc.gov.cn']
    start_urls = [
        'http://www.ndrc.gov.cn/xwzx/xwfb/',  # 新闻发布中心-新闻发布
        """
        'http://www.ndrc.gov.cn/xwzx/wszb/',  # 新闻发布中心-网上直播
        'http://www.ndrc.gov.cn/fzgggz/fzgh/zhdt/',  # 发展改革工作-发展规划-综合情况
        'http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/gjjh/',  # 发展改革工作-发展规划-规划文本-国家总体规划
        'http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/ztgngh/',  # 发展改革工作-发展规划-规划文本-主体功能区规划
        'http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/gjjgh/',  # 发展改革工作-发展规划-规划文本-国家级专项规划
        'http://www.ndrc.gov.cn/fzgggz/fzgh/ghwb/dfztgh/',  # 发展改革工作-发展规划-规划文本-地方总体规划
        'http://www.ndrc.gov.cn/fzgggz/fzgh/zcfg/',  # 发展改革工作-发展规划-政策法规
        'http://www.ndrc.gov.cn/fzgggz/hgjj/',  # 发展改革工作-宏观经济
        'http://www.ndrc.gov.cn/fzgggz/jjyx/zhdt/',  # 发展改革工作>经济运行>综合情况
        'http://www.ndrc.gov.cn/fzgggz/jjyx/gjyx/',  # 发展改革工作>经济运行>宏观经济运行
        'http://www.ndrc.gov.cn/fzgggz/jjyx/mtzhgl/',  # 发展改革工作>经济运行>煤电油气运
        'http://www.ndrc.gov.cn/fzgggz/jjyx/xdwl/',  # 发展改革工作>经济运行>现代物流
        'http://www.ndrc.gov.cn/fzgggz/jjyx/yjxt/',  # 发展改革工作>经济运行>应急管理
        'http://www.ndrc.gov.cn/fzgggz/tzgg/zhdt/',  # 发展改革工作>体制改革>综合情况
        'http://www.ndrc.gov.cn/fzgggz/tzgg/ggkx/',  # 发展改革工作>体制改革>改革快讯
        'http://www.ndrc.gov.cn/fzgggz/gdzctz/tzgz/',  # 发展改革工作>固定资产投资>投资工作
        'http://www.ndrc.gov.cn/fzgggz/gdzctz/tzfg/',  # 发展改革工作>固定资产投资>投资法规
        'http://www.ndrc.gov.cn/fzgggz/wzly/zhdt/',  # 发展改革工作>外资利用>综合情况
        'http://www.ndrc.gov.cn/fzgggz/wzly/jwtz/jwtzgk/',  # 发展改革工作>外资利用>境外投资>发展情况
        'http://www.ndrc.gov.cn/fzgggz/wzly/jwtz/jwtzzl/',  # 发展改革工作>外资利用>境外投资>国别资料
        'http://www.ndrc.gov.cn/fzgggz/wzly/wstz/wstzgk/',  # 发展改革工作>外资利用>外商投资>外商投资情况
        'http://www.ndrc.gov.cn/fzgggz/wzly/wstz/wstzqk/',  # 发展改革工作>外资利用>外商投资>开发区情况
        'http://www.ndrc.gov.cn/fzgggz/wzly/wzgl/',  # 发展改革工作>外资利用>外债管理
        'http://www.ndrc.gov.cn/fzgggz/wzly/zcfg/',  # 发展改革工作>外资利用>政策法规
        'http://www.ndrc.gov.cn/fzgggz/dqjj/zhdt/',  # 发展改革工作>地区经济>综合情况  未完成！！！
        'http://www.ndrc.gov.cn/fzgggz/dqjj/qygh/',  # 发展改革工作>地区经济>区域规划和区域政策
        'http://www.ndrc.gov.cn/fzgggz/dqjj/fpkf/',  # 发展改革工作>地区经济>扶贫开发
        'http://www.ndrc.gov.cn/fzgggz/dqjj/dkzy/',  # 发展改革工作>地区经济>对口支援
        'http://www.ndrc.gov.cn/fzgggz/ncjj/zhdt/',  # 发展改革工作>农村经济>综合情况
        'http://www.ndrc.gov.cn/fzgggz/ncjj/nczc/',  # 发展改革工作>农村经济>农村政策
        'http://www.ndrc.gov.cn/fzgggz/ncjj/njxx/',  # 发展改革工作>农村经济>农经信息
        'http://www.ndrc.gov.cn/fzgggz/nyjt/zhdt/',  # 发展改革工作>基础产业>综合情况
        'http://www.ndrc.gov.cn/fzgggz/nyjt/fzgh/',  # 发展改革工作>基础产业>政策规划
        'http://www.ndrc.gov.cn/fzgggz/nyjt/zdxm/',  # 发展改革工作>基础产业>重大工程
        'http://www.ndrc.gov.cn/fzgggz/gyfz/gyfz/',  # 发展改革工作>产业发展>工业发展
        'http://www.ndrc.gov.cn/fzgggz/gyfz/fwyfz/',  # 发展改革工作>产业发展>服务业发展
        'http://gjss.ndrc.gov.cn/gjsgz/',  # 高技术产业司>高技术工作
        'http://gjss.ndrc.gov.cn/gzdtx/',  # 高技术产业司>发展动态
        'http://gjss.ndrc.gov.cn/ghzc/',  # 高技术产业司>政策发布
        'http://www.ndrc.gov.cn/fzgggz/hjbh/hjzhdt/',  # 发展改革工作>环境与资源>综合情况
        'http://www.ndrc.gov.cn/fzgggz/hjbh/hjjsjyxsh/',  # 发展改革工作>环境与资源>生态文明建设
        'http://www.ndrc.gov.cn/fzgggz/hjbh/jnjs/',  # 发展改革工作>环境与资源>节能节水
        'http://www.ndrc.gov.cn/fzgggz/hjbh/huanjing/',  # 发展改革工作>环境与资源>环境保护
        'http://hzs.ndrc.gov.cn/newfzxhjj/zcfg/',  # 发展改革工作>环境与资源>发展循环经济>政策法规
        'http://hzs.ndrc.gov.cn/newfzxhjj/xfxd/',  # 发展改革工作>环境与资源>发展循环经济>示范试点
        'http://hzs.ndrc.gov.cn/newfzxhjj/dtxx/',  # 发展改革工作>环境与资源>发展循环经济>动态信息
        'http://shs.ndrc.gov.cn/gzdt/',  # 社会发展司>社会发展工作
        'http://shs.ndrc.gov.cn/shfzdt/',  # 社会发展司>社会发展动态
        'http://shs.ndrc.gov.cn/zcyj/',  # 社会发展司>社会发展规划、政策与研究
        'http://www.ndrc.gov.cn/fzgggz/jyysr/jqyw/',  # 发展改革工作>就业与收入>近期要闻
        'http://www.ndrc.gov.cn/fzgggz/jyysr/zhdt/',  # 发展改革工作>就业与收入>工作动态
        'http://www.ndrc.gov.cn/fzgggz/jyysr/dfjy/',  # 发展改革工作>就业与收入>地方经验
        'http://www.ndrc.gov.cn/fzgggz/jyysr/zcyj/',  # 发展改革工作>就业与收入>政策研究
        'http://www.ndrc.gov.cn/fzgggz/jjmy/zhdt/',  # 发展改革工作>经济贸易>综合情况
        'http://www.ndrc.gov.cn/fzgggz/jjmy/lyzc/',  # 发展改革工作>经济贸易>粮油政策
        'http://www.ndrc.gov.cn/fzgggz/jjmy/mhstfz/',  # 发展改革工作>经济贸易>棉花食糖产业发展
        'http://www.ndrc.gov.cn/fzgggz/jjmy/ltyfz/',  # 发展改革工作>经济贸易>流通业发展
        'http://www.ndrc.gov.cn/fzgggz/jjmy/dwjmhz/',  # 发展改革工作>经济贸易>对外经贸合作
        'http://cjs.ndrc.gov.cn/shxytxjs/zcfg02/',  # 信用建设>政策法规
        'http://cjs.ndrc.gov.cn/shxytxjs/gzjl/',  # 信用建设>工作交流
        'http://www.ndrc.gov.cn/fzgggz/jggl/zhdt/',  # 发展改革工作>价格管理>综合情况
        'http://www.ndrc.gov.cn/fzgggz/jggl/zcfg/',  # 发展改革工作>价格管理>政策法规

        'http://www.ndrc.gov.cn/zwfwzx/tztg/',  # 政务服务中心>通知通告
        'http://www.ndrc.gov.cn/zwfwzx/xzxknew/',  # 政务服务中心>行政许可
        'http://www.ndrc.gov.cn/zwfwzx/xzzq/bgxz/',  # 政务服务中心>下载专区>表格下载
        'http://www.ndrc.gov.cn/zwfwzx/zfdj/djfw/',  # 政务服务中心>政府定价>定价范围
        'http://www.ndrc.gov.cn/zwfwzx/zfdj/jggg/',  # 政务服务中心>政府定价>价格公告
        'http://www.ndrc.gov.cn/zcfb/zcfbl/',  # 政策发布中心>发展改革委令
        'http://www.ndrc.gov.cn/zcfb/gfxwj/',  # 政策发布中心>规范性文件
        'http://www.ndrc.gov.cn/zcfb/zcfbgg/',  # 政策发布中心>公告
        'http://www.ndrc.gov.cn/zcfb/zcfbghwb/',  # 政策发布中心>规划文本
        'http://www.ndrc.gov.cn/zcfb/zcfbtz/',  # 政策发布中心>通知
        'http://www.ndrc.gov.cn/zcfb/jd/',  # 政策发布中心>解读
        'http://www.ndrc.gov.cn/zcfb/zcfbqt/',  # 政策发布中心>其他
        'http://www.ndrc.gov.cn/govszyw/',  # 时政要闻
        'http://www.ndrc.gov.cn/gzdt/',  # 委工作动态
        'http://www.ndrc.gov.cn/dffgwdt/',  # 地方动态
        'http://www.ndrc.gov.cn/jjxsfx/',  # 经济形势分析
        """
    ]  # 发展改革工作>价格管理>价格监测 专题专栏 政府信息公开目录

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse)

    def parse(self, response):
        linklist_raw = response.xpath('//div[@class="box1 "]//ul[@class="list_02 clearfix"]//li//a/@href').extract()
        titlelist = response.xpath('//div[@class="box1 "]//ul[@class="list_02 clearfix"]//li//a/text()').extract()
        linklist = []
        for link in linklist_raw:
            linklist.append(response.urljoin(link))
        datelist = response.xpath('//font[@class="date"]/text()').extract()
        for i in range(len(linklist)):
            yield scrapy.Request(url=linklist[i], callback=self.parse_content, dont_filter=True, meta={'date': datelist[i], 'title': titlelist[i]})

        next = response.urljoin(response.xpath('//li//a[text()="下一页"]/@href').extract_first())
        global count
        if next and count < 2:
            yield scrapy.Request(url=next, callback=self.parse, dont_filter=True)
            count += 1

    def parse_content(self, response):
        if response.xpath('//div[@class="txt_title1 tleft"]/text()').extract_first():
            title = response.meta['title']
            date = response.meta['date']
            author = response.xpath('//span[@id="dSource"]//a/@title').extract_first()
            paralist = response.xpath('//*[@id="zoom"]//div//p/text()').extract()

            item = NdrcItem()
            item['class0'] = ''
            item['class1'] = ''
            item['class2'] = ''
            item['class3'] = ''
            item['attachments'] = []
            item['content'] = ['']
            item['image_urls'] = []
            item['file_content'] = []
            item['author'] = author
            item['title'] = title
            item['date'] = date
            date_struct = datetime.datetime.strptime(date, "%Y/%m/%d")
            item['year'] = date_struct.year
            item['month'] = date_struct.month
            item['day'] = date_struct.day
            item['content'] = paralist
            item['url'] = response.url
            if response.xpath('//p//img/@src').extract_first():
                for image in response.xpath('//p//img/@src').extract():
                    image = response.urljoin(image)
                    item['image_urls'].append(image)
            if response.xpath('//*[@id="zoom"]//div//p//@href').extract_first():
                attachments = response.xpath('//*[@id="zoom"]//div//p//@href').extract()
                attachments_cleaned = cleanattachment(attachments)
                attachments_joined = []
                if attachments_cleaned:
                    for attachment in attachments_cleaned:
                        attachment = response.urljoin(attachment)
                        attachments_joined.append(attachment)
                item['attachments'] = attachments_joined
            yield item
        elif response.xpath('//div[@class="tit2b "]/text()').extract_first():
            title = response.meta['title']
            date = response.meta['date']
            paralist = response.xpath('//div[@class="txt1"]/text()').extract()

            item = NdrcItem()
            item['class0'] = ''
            item['class1'] = ''
            item['class2'] = ''
            item['class3'] = ''
            item['attachments'] = []
            item['image_urls'] = []
            item['file_content'] = []
            item['title'] = title
            item['date'] = date
            date_struct = datetime.datetime.strptime(date, "%Y/%m/%d")
            item['year'] = date_struct.year
            item['month'] = date_struct.month
            item['day'] = date_struct.day
            item['content'] = paralist
            item['url'] = response.url
            if response.xpath('//p//img/@src').extract_first():
                for image in response.xpath('//p//img/@src').extract():
                    image = response.urljoin(image)
                    item['image_urls'].append(image)
            if response.xpath('//div[@class="txt1"]//@href').extract_first():
                attachments = response.xpath('//div[@class="txt1"]//@href').extract()
                attachments_cleaned = cleanattachment(attachments)
                item['attachments'] = attachments_cleaned
            yield item
        elif response.xpath('//font[@style="font-size: 18pt"]/text()').extract_first():
            title = response.meta['title']
            date = response.meta['date']
            paralist = response.xpath('//*[@id="zoom"]//div//p/text()').extract()

            item = NdrcItem()
            item['class0'] = ''
            item['class1'] = ''
            item['class2'] = ''
            item['class3'] = ''
            item['attachments'] = []
            item['image_urls'] = []
            item['file_content'] = []
            item['title'] = title
            item['date'] = date
            date_struct = datetime.datetime.strptime(date, "%Y/%m/%d")
            item['year'] = date_struct.year
            item['month'] = date_struct.month
            item['day'] = date_struct.day
            item['content'] = paralist
            item['author'] = response.xpath('//span[@id="dSourceText"]//@title').extract_first()
            item['url'] = response.url
            if response.xpath('//p//img/@src').extract_first():
                for image in response.xpath('//p//img/@src').extract():
                    image = response.urljoin(image)
                    item['image_urls'].append(image)
            if response.xpath('//div[@class="txt1"]//@href').extract_first():
                attachments = response.xpath('//*[@id="zoom"]//div//p//@href').extract()
                attachments_cleaned = cleanattachment(attachments)
                attachments_joined = []
                if attachments_cleaned:
                    for attachment in attachments_cleaned:
                        attachment = response.urljoin(attachment)
                        attachments_joined.append(attachment)
                item['attachments'] = attachments_joined
            yield item
        elif response.xpath('//font[@face="微软雅黑"]/text()').extract_first():
            title = response.meta['title']
            date = response.meta['date']
            paralist = response.xpath('//*[@id="zoom"]//div//p/text()').extract()

            item = NdrcItem()
            item['class0'] = ''
            item['class1'] = ''
            item['class2'] = ''
            item['class3'] = ''
            item['attachments'] = []
            item['image_urls'] = []
            item['file_content'] = []
            item['title'] = title
            item['date'] = date
            date_struct = datetime.datetime.strptime(date, "%Y/%m/%d")
            item['year'] = date_struct.year
            item['month'] = date_struct.month
            item['day'] = date_struct.day
            item['content'] = paralist
            item['author'] = response.xpath('//span[@id="dSourceText"]//@title').extract_first()
            item['url'] = response.url
            if response.xpath('//p//img/@src').extract_first():
                for image in response.xpath('//p//img/@src').extract():
                    image = response.urljoin(image)
                    item['image_urls'].append(image)
            if response.xpath('//div[@class="txt1"]//@href').extract_first():
                attachments = response.xpath('//*[@id="zoom"]//div//p//@href').extract()
                attachments_cleaned = cleanattachment(attachments)
                attachments_joined = []
                if attachments_cleaned:
                    for attachment in attachments_cleaned:
                        attachment = response.urljoin(attachment)
                        attachments_joined.append(attachment)
                item['attachments'] = attachments_joined
            yield item
        else:
            title = response.meta['title']
            date = response.meta['date']
            paralist = response.xpath('//*[@id="zoom"]//div/text()').extract()

            item = NdrcItem()
            item['class0'] = ''
            item['class1'] = ''
            item['class2'] = ''
            item['class3'] = ''
            item['attachments'] = []
            item['image_urls'] = []
            item['file_content'] = []
            item['title'] = title
            item['date'] = date
            date_struct = datetime.datetime.strptime(date, "%Y/%m/%d")
            item['year'] = date_struct.year
            item['month'] = date_struct.month
            item['day'] = date_struct.day
            item['content'] = paralist
            item['author'] = response.xpath('//span[@id="dSourceText"]//@title').extract_first()
            item['url'] = response.url
            if response.xpath('//p//img/@src').extract_first():
                for image in response.xpath('//p//img/@src').extract():
                    image = response.urljoin(image)
                    item['image_urls'].append(image)
            if response.xpath('//div[@class="txt1"]//@href').extract_first():
                attachments = response.xpath('//*[@id="zoom"]//div//p//@href').extract()
                attachments_cleaned = cleanattachment(attachments)
                attachments_joined = []
                if attachments_cleaned:
                    for attachment in attachments_cleaned:
                        attachment = response.urljoin(attachment)
                        attachments_joined.append(attachment)
                item['attachments'] = attachments_joined
            yield item
