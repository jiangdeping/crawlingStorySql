# # # # -*- coding: utf-8 -*-
# # # # Author:jiang
# # # # 2020/10/27 15:16
# # # import re
# # # # from fake_useragent import UserAgent
# # # # from util.get_url import get_url
# # # # from config import config
# # # # #
# # # # #  import requests
# # # # # dic={'82785': ['/book/66/82785/1', '/book/66/82785/2', '/book/66/82785/3', '/book/66/82785/4', '/book/66/82785/5', '/book/66/82785/6', '/book/66/82785/7', '/book/66/82785/8', '/book/66/82785/9', '/book/66/82785/10', '/book/66/82785/11', '/book/66/82785/12', '/book/66/82785/13', '/book/66/82785/14', '/book/66/82785/15', '/book/66/82785/16', '/book/66/82785/17', '/book/66/82785/18', '/book/66/82785/19', '/book/66/82785/20', '/book/66/82785/21', '/book/66/82785/22', '/book/66/82785/23', '/book/66/82785/24', '/book/66/82785/25', '/book/66/82785/26', '/book/66/82785/27', '/book/66/82785/28', '/book/66/82785/29', '/book/66/82785/30', '/book/66/82785/31', '/book/66/82785/32', '/book/66/82785/33', '/book/66/82785/34', '/book/66/82785/35', '/book/66/82785/36', '/book/66/82785/37', '/book/66/82785/38', '/book/66/82785/39', '/book/66/82785/40', '/book/66/82785/41', '/book/66/82785/42', '/book/66/82785/43', '/book/66/82785/44', '/book/66/82785/45', '/book/66/82785/46', '/book/66/82785/47', '/book/66/82785/48', '/book/66/82785/49', '/book/66/82785/50', '/book/66/82785/51', '/book/66/82785/52', '/book/66/82785/53', '/book/66/82785/54', '/book/66/82785/55', '/book/66/82785/56', '/book/66/82785/57', '/book/66/82785/58', '/book/66/82785/59', '/book/66/82785/60', '/book/66/82785/61', '/book/66/82785/62', '/book/66/82785/63', '/book/66/82785/64', '/book/66/82785/65', '/book/66/82785/66', '/book/66/82785/67', '/book/66/82785/68', '/book/66/82785/69', '/book/66/82785/70', '/book/66/82785/71', '/book/66/82785/72', '/book/66/82785/73', '/book/66/82785/74', '/book/66/82785/75', '/book/66/82785/76', '/book/66/82785/77', '/book/66/82785/78', '/book/66/82785/79', '/book/66/82785/80', '/book/66/82785/81', '/book/66/82785/82', '/book/66/82785/83', '/book/66/82785/84', '/book/66/82785/85', '/book/66/82785/86', '/book/66/82785/87', '/book/66/82785/88', '/book/66/82785/89', '/book/66/82785/90', '/book/66/82785/91', '/book/66/82785/92', '/book/66/82785/93', '/book/66/82785/94', '/book/66/82785/95', '/book/66/82785/96', '/book/66/82785/97', '/book/66/82785/98', '/book/66/82785/99', '/book/66/82785/100', '/book/66/82785/101', '/book/66/82785/102', '/book/66/82785/103', '/book/66/82785/104', '/book/66/82785/105', '/book/66/82785/106', '/book/66/82785/107', '/book/66/82785/108', '/book/66/82785/109', '/book/66/82785/110', '/book/66/82785/111', '/book/66/82785/112', '/book/66/82785/113', '/book/66/82785/114', '/book/66/82785/115', '/book/66/82785/116', '/book/66/82785/117', '/book/66/82785/118', '/book/66/82785/119', '/book/66/82785/120', '/book/66/82785/121', '/book/66/82785/122', '/book/66/82785/123', '/book/66/82785/124', '/book/66/82785/125', '/book/66/82785/126', '/book/66/82785/127', '/book/66/82785/128', '/book/66/82785/129', '/book/66/82785/130', '/book/66/82785/131', '/book/66/82785/132', '/book/66/82785/133', '/book/66/82785/134', '/book/66/82785/135', '/book/66/82785/136', '/book/66/82785/137', '/book/66/82785/138', '/book/66/82785/139', '/book/66/82785/140', '/book/66/82785/141', '/book/66/82785/142', '/book/66/82785/143', '/book/66/82785/144', '/book/66/82785/145', '/book/66/82785/146', '/book/66/82785/147', '/book/66/82785/148', '/book/66/82785/149', '/book/66/82785/150', '/book/66/82785/151', '/book/66/82785/152', '/book/66/82785/153', '/book/66/82785/154', '/book/66/82785/155', '/book/66/82785/156', '/book/66/82785/157', '/book/66/82785/158', '/book/66/82785/159', '/book/66/82785/160', '/book/66/82785/161', '/book/66/82785/162', '/book/66/82785/163', '/book/66/82785/164', '/book/66/82785/165', '/book/66/82785/166', '/book/66/82785/167', '/book/66/82785/168', '/book/66/82785/169', '/book/66/82785/170', '/book/66/82785/171', '/book/66/82785/172', '/book/66/82785/173', '/book/66/82785/174', '/book/66/82785/175', '/book/66/82785/176', '/book/66/82785/177', '/book/66/82785/178', '/book/66/82785/179', '/book/66/82785/180', '/book/66/82785/181', '/book/66/82785/182', '/book/66/82785/183', '/book/66/82785/184', '/book/66/82785/185', '/book/66/82785/186', '/book/66/82785/187', '/book/66/82785/188', '/book/66/82785/189', '/book/66/82785/190', '/book/66/82785/191', '/book/66/82785/192', '/book/66/82785/193', '/book/66/82785/194', '/book/66/82785/195', '/book/66/82785/196', '/book/66/82785/197', '/book/66/82785/198', '/book/66/82785/199', '/book/66/82785/200', '/book/66/82785/201', '/book/66/82785/202', '/book/66/82785/203', '/book/66/82785/204', '/book/66/82785/205', '/book/66/82785/206', '/book/66/82785/207', '/book/66/82785/208', '/book/66/82785/209', '/book/66/82785/210', '/book/66/82785/211', '/book/66/82785/212', '/book/66/82785/213', '/book/66/82785/214', '/book/66/82785/215', '/book/66/82785/216', '/book/66/82785/217', '/book/66/82785/218', '/book/66/82785/219', '/book/66/82785/220', '/book/66/82785/221', '/book/66/82785/222', '/book/66/82785/223', '/book/66/82785/224', '/book/66/82785/225', '/book/66/82785/226', '/book/66/82785/227', '/book/66/82785/228', '/book/66/82785/229', '/book/66/82785/230', '/book/66/82785/231', '/book/66/82785/232', '/book/66/82785/233', '/book/66/82785/234', '/book/66/82785/235', '/book/66/82785/236', '/book/66/82785/237', '/book/66/82785/238', '/book/66/82785/239', '/book/66/82785/240', '/book/66/82785/241', '/book/66/82785/242', '/book/66/82785/243', '/book/66/82785/244', '/book/66/82785/245', '/book/66/82785/246', '/book/66/82785/247', '/book/66/82785/248', '/book/66/82785/249', '/book/66/82785/250', '/book/66/82785/251', '/book/66/82785/252', '/book/66/82785/253', '/book/66/82785/254', '/book/66/82785/255', '/book/66/82785/256', '/book/66/82785/257', '/book/66/82785/258', '/book/66/82785/259', '/book/66/82785/260', '/book/66/82785/261', '/book/66/82785/262', '/book/66/82785/263', '/book/66/82785/264', '/book/66/82785/265', '/book/66/82785/266', '/book/66/82785/267', '/book/66/82785/268', '/book/66/82785/269', '/book/66/82785/270', '/book/66/82785/271', '/book/66/82785/272', '/book/66/82785/273', '/book/66/82785/274', '/book/66/82785/275', '/book/66/82785/276', '/book/66/82785/277', '/book/66/82785/278', '/book/66/82785/279', '/book/66/82785/280', '/book/66/82785/281', '/book/66/82785/282', '/book/66/82785/283', '/book/66/82785/284', '/book/66/82785/285', '/book/66/82785/286', '/book/66/82785/287', '/book/66/82785/288', '/book/66/82785/289', '/book/66/82785/290', '/book/66/82785/291', '/book/66/82785/292', '/book/66/82785/293', '/book/66/82785/294', '/book/66/82785/295', '/book/66/82785/296', '/book/66/82785/297', '/book/66/82785/298', '/book/66/82785/299', '/book/66/82785/300', '/book/66/82785/301', '/book/66/82785/302', '/book/66/82785/303', '/book/66/82785/304', '/book/66/82785/305', '/book/66/82785/306', '/book/66/82785/307', '/book/66/82785/308', '/book/66/82785/309', '/book/66/82785/310', '/book/66/82785/311', '/book/66/82785/312', '/book/66/82785/313', '/book/66/82785/314', '/book/66/82785/315', '/book/66/82785/316', '/book/66/82785/317', '/book/66/82785/318', '/book/66/82785/319', '/book/66/82785/320', '/book/66/82785/321', '/book/66/82785/322', '/book/66/82785/323', '/book/66/82785/324', '/book/66/82785/325', '/book/66/82785/326', '/book/66/82785/327', '/book/66/82785/328', '/book/66/82785/329', '/book/66/82785/330', '/book/66/82785/331', '/book/66/82785/332', '/book/66/82785/333', '/book/66/82785/334', '/book/66/82785/335', '/book/66/82785/336', '/book/66/82785/337', '/book/66/82785/338', '/book/66/82785/339', '/book/66/82785/340', '/book/66/82785/341', '/book/66/82785/342', '/book/66/82785/343', '/book/66/82785/344', '/book/66/82785/345', '/book/66/82785/346', '/book/66/82785/347', '/book/66/82785/348', '/book/66/82785/349', '/book/66/82785/350', '/book/66/82785/351', '/book/66/82785/352', '/book/66/82785/353', '/book/66/82785/354', '/book/66/82785/355', '/book/66/82785/356', '/book/66/82785/357', '/book/66/82785/358', '/book/66/82785/359', '/book/66/82785/360', '/book/66/82785/361', '/book/66/82785/362', '/book/66/82785/363', '/book/66/82785/364', '/book/66/82785/365', '/book/66/82785/366', '/book/66/82785/367', '/book/66/82785/368', '/book/66/82785/369', '/book/66/82785/370', '/book/66/82785/371', '/book/66/82785/372', '/book/66/82785/373', '/book/66/82785/374', '/book/66/82785/375', '/book/66/82785/376', '/book/66/82785/377', '/book/66/82785/378', '/book/66/82785/379', '/book/66/82785/380', '/book/66/82785/381', '/book/66/82785/382', '/book/66/82785/383', '/book/66/82785/384', '/book/66/82785/385', '/book/66/82785/386', '/book/66/82785/387', '/book/66/82785/388', '/book/66/82785/389', '/book/66/82785/390', '/book/66/82785/391', '/book/66/82785/392', '/book/66/82785/393', '/book/66/82785/394', '/book/66/82785/395', '/book/66/82785/396', '/book/66/82785/397', '/book/66/82785/398', '/book/66/82785/399', '/book/66/82785/400', '/book/66/82785/401', '/book/66/82785/402', '/book/66/82785/403', '/book/66/82785/404', '/book/66/82785/405', '/book/66/82785/406', '/book/66/82785/407', '/book/66/82785/408', '/book/66/82785/409', '/book/66/82785/410', '/book/66/82785/411', '/book/66/82785/412', '/book/66/82785/413', '/book/66/82785/414', '/book/66/82785/415', '/book/66/82785/416', '/book/66/82785/417', '/book/66/82785/418', '/book/66/82785/419', '/book/66/82785/420', '/book/66/82785/421', '/book/66/82785/422', '/book/66/82785/423', '/book/66/82785/424', '/book/66/82785/425', '/book/66/82785/426', '/book/66/82785/427', '/book/66/82785/428', '/book/66/82785/429', '/book/66/82785/430', '/book/66/82785/431', '/book/66/82785/432', '/book/66/82785/433', '/book/66/82785/434', '/book/66/82785/435', '/book/66/82785/436']}
# # # # # for k,v in dic.items():
# # # # #     print(k,v)
# # # #
# # # # str=['8278400002', '8278400003', '8278400004','8278400005','8278400006','8278400007']
# # # # str=['8278400002', '8278400003', '8278400008','8278400009','82784000010','82784000011']
# # # # def ll():
# # # #     str=['8278400002', '8278400003', '8278400008','8278400009','8278400010','8278400011']
# # # #     str1=['8278400002', '8278400003', '8278400004','8278400005','8278400006','8278400007']
# # # #     newstr=[]
# # # #     last_str=str[len(str)-1]
# # # #     first_str=False
# # # #     for i in range(len(str)):
# # # #         if i<len(str)-1:
# # # #             if int(str[i+1])-int(str[i])>1:
# # # #                 first_str=str[i]
# # # #                 break
# # # #         else:
# # # #             newstr=str
# # # #     if first_str:
# # # #         for i in range(int(first_str),int(last_str)):
# # # #             print(i)
# # # #             newstr.append(i+1)
# # # #     # if int(first_str)==int(str[])
# # # #     return newstr
# # # # print(ll())
# # # from threading import Thread,Lock,RLock
# # # import time
# # # mutexA = Lock()
# # # mutexB = Lock()
# # # class MyThread(Thread):
# # #      def run(self):
# # #          self.f1()
# # #          self.f2()
# # #      def f1(self):
# # #          mutexA.acquire()
# # #          print("%s 拿到了A锁"%self.name)
# # #          mutexB.acquire()
# # #          print("%s 拿到了B锁"%self.name)    #第线程二个抢到A锁后，等待B锁
# # #          mutexB.release()
# # #          mutexA.release()   #第一个线程释放A锁，立即被第二个线程抢到
# # #      def f2(self):
# # #          mutexB.acquire()     #第一个线程等待B锁
# # #          print("%s 拿到了B锁"%self.name)
# # #          time.sleep(0.1)
# # #          mutexA.acquire()
# # #          print("%s 拿到了A锁"%self.name)
# # #          mutexA.release()
# # #          mutexB.release()
# # #
# # # if __name__=="__main__":
# # #      for i in range(10):
# # #          t = MyThread()
# # #          t.start()
# # #
# # from mysql.mySQL import MySQL
# # from threading import  Thread
# # import  time
# # import requests
# # db=MySQL()
# # urls=db.getStoryDownLoadUrl(82919)
# # print(len(urls))
# # thread=[]
# # def get(url):
# #     try:
# #         r = requests.get(url, allow_redirects=False, timeout=2.0)
# #     except:
# #         pass
# #     else:
# #         print(r.status_code, r.url)
# # starttime= time.time()
# # for i in urls:
# #     t=Thread(target=get,args=[i])
# #     t.start()
# #     thread.append(t)
# # for t in thread:
# #     t.join()
# # endtime=time.time()
# # print(endtime-starttime)
# # starttime= time.time()
# # for i in urls:
# #     t=Thread(target=get,args=[i])
# #     t.start()
# #     thread.append(t)
# # for t in thread:
# #     t.join()
# # endtime=time.time()
# # print(endtime-starttime)
# #
# # starttime= time.time()
# # for i in urls:
# #     get(i)
# # endtime=time.time()
# # print(endtime-starttime)
# #coding=utf-8
# import requests #请求模块
# from lxml import etree #解析模块
# #import re #正则表达式(备用)
# #import os #操作访问系统的模块（此处用于创建文件夹）
# #import xlsxwriter #操作xls文件
# import pymysql #操作数据库模块
# #import smtplibfrom email.mime.text
# #import MIMEText #此模块可以用于发送正文
# #from email.mime.multipart import MIMEMultipart #此模块用于发送带附件的邮件
# #from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED
# import time
# from queue import Queue
# from threading import Thread
# import threading
#
#
#
#
#
# class comSpider(object):
#     """docstring for comSpider"""
#     def __init__(self):
#         super(comSpider, self).__init__()
#         self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
#         self.url_head='http://detail.zol.com.cn'
#         #url队列
#         self.url_queue=Queue()
#         #单个页面队列
#         self.page_queue=Queue()
#         #数据队列
#         self.data_queue=Queue()
#     def addurl_queue(self):
#         L1=[]
#         home_url='http://detail.zol.com.cn/notebook_index/subcate16_list_1.html'
#         home_data=requests.get(home_url,headers=self.headers).text
#         home_html = etree.HTML(home_data)
#         brand_url=home_html.xpath('//*[@id="J_ParamBrand"]/a/@href')
#         for x in range(len(brand_url)):
#             brand_data=requests.get('http://detail.zol.com.cn'+brand_url[x],headers=self.headers).text
#             brand_html= etree.HTML(brand_data)
#             page_url=brand_html.xpath('//*[@id="J_PicMode"]/li/a/@href')
#             L1=L1+page_url
# #        print(L1)
#         for i in range(len(L1)):
#             self.url_queue.put(self.url_head+L1[i])
#
#
#     def addpage_queue(self):
#         url=self.url_queue.get()
# #        print(url)
#         resp=requests.get(url,headers=self.headers)
#         self.page_queue.put(resp.text)
#         self.url_queue.task_done()
#
#
#     def adddata_queue(self):
#         page=self.page_queue.get()
# #        print(page)
#         page_html=etree.HTML(page)
#         name=page_html.xpath('/html/body/div/h1/text()')
# #        for i in range(len(name)):
# #            name=name[i]
# #            name.encode('utf-8')
# #        name_list=list(name)
# #        print(name)
#         price=page_html.xpath('/html/body/div/div/div/div/span/b[2]/text()')
# #        for i in range(len(price)):
# #           price=price[i]
# #            price.encode('utf-8')
# #        price_list=list(price)
#         parameter=page_html.xpath('/html/body/div/div/div/div/ul/li/p/text()')
# #        for i in range(len(parameter)):
# #            parameter=parameter[i]
# #            parameter.encode('utf-8')
# #        parameter_list=list(parameter)
#
#         data=name+price+parameter
#         data=[str(i)for i in data]
# #        print(type(data[0]),type(data[1]),type(data[2]),type(data[3]),type(data[4]),type(data[5]),type(data[6]),type(data[7]),type(data[8]),type(data[9]),)
#         self.data_queue.put(data)
#         self.page_queue.task_done()
#
#     def sava_mysql(self):
#         data=self.data_queue.get()
#         print(data)
#         db=pymysql.connect(host='localhost', user='root', password='XXXXXXXX', port=3306, db='comeputerdata')
#         cursor= db.cursor()
# #        time.sleep(2)
# #        sql1=sql='''CREATE TABLE IF NOT EXISTS com_chart(Brand VARCHAR(255) NOT NULL,Price INT NOT NULL,ScreenSize VARCHAR(255) NOT NULL,ScreenResolution VARCHAR(255) NOT NULL,CPUmodel VARCHAR(255) NOT NULL,Core VARCHAR(255) NOT NULL,GPU VARCHAR(255) NOT NULL,MemoryCapacity VARCHAR(255) NOT NULL,BatteryLife VARCHAR(255) NOT NULL,Endurance VARCHAR(255) NOT NULL,PRIMARY KEY (Brand))'''
# #        cursor.execute(sql1)
#         time.sleep(2)
#         sql2='''INSERT INTO com_chart(Brand,Price,ScreenSize,ScreenResolution,CPUmodel,Core,GPU,MemoryCapacity,BatteryLife,Endurance)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
# #        try:
#         cursor.execute(sql2,data)
#         db.commit()
# #        except:
# #            print('数据写入失败')
# #            db.rollback()
#         db.close()
#         self.data_queue.task_done()
#
#
#     def run(self):
#         list1=[]
#         list2=[]
#         list3=[]
#         # 开启线程执行上面的几个方法
#         url_t=threading.Thread(target=self.addurl_queue)
#         # url_t.setDaemon(True)
#         url_t.start()
#         for i in range(500):
#             t=Thread(target=self.addpage_queue())
#             list1.append(t)
#             t.start()
#
#         for i in range(500):
#             t=Thread(target=self.adddata_queue())
#             list2.append(t)
#             t.start()
#
#         for i in range(500):
#             t=Thread(target=self.sava_mysql())
#             list3.append(t)
#             t.start()
# #        self.run_use_more_task(self.adddata_queue, 2)
# #        self.run_use_more_task(self.sava_mysql, 2)
#         # 使用队列join方法,等待队列任务都完成了才结束
# #        self.url_queue.join()
# #        self.page_queue.join()
# #        self.data_queue.join()
#
#         for t in list1:
#             t.join()
#
#         for t in list2:
#             t.join()
#
#         for t in list3:
#             t.join()
# class Person(object):
#     def __init__(self):
#         print("__init__")
#         self.name="张三"
#     def __new__(cls):
#         print('__new__')
#         ob=object.__new__(cls)
#         print(ob)
#         return ob
# p1=Person()
# print(p1.name)
class CLanguage:
    #类构造方法，也属于实例方法
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    # 下面定义了一个say实例方法
    @classmethod
    def info(cls):
        print(cls)
        print("正在调用 say() 实例方法")
# c=CLanguage()
# c.info()
# CLanguage().info()
# CLanguage.info()
# # CLanguage.info(CLanguage)
# # CLanguage.info(CLanguage())


class CLanguage1:
    # @staticmethod
    def info(name,add):
        print(name,add)
CLanguage1.info("LILEI","1111")
C=CLanguage1()
C.info("LILEI","1111")