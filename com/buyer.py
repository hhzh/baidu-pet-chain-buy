import requests, threading, time, json
import pymysql
import time

requests.packages.urllib3.disable_warnings()
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
refer = 'https://pet-chain.baidu.com/'
Cookie = ''  # 换成你自己的Cookie
headers = {'Cookie': Cookie, 'Referer': refer, 'User-Agent': UA, 'accept': 'application/json',
           'Pragma': 'no-cache', 'Cache-Control': 'no-cache',
           'content-type': 'application/json'}

# def __init__(self, conn=None, cursor=None):
#     self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='SCMD_2017_scmd', db='pets',
#                                 charset='utf8')
#     self.cursor = self.conn.cursor()

# def get_all_pets():
#     data = {}
#     param = json.loads(
#         '{"pageNo":1,"pageSize":20,"querySortType":"AMOUNT_ASC","petIds":[],"lastAmount":null,"lastRareDegree":null,"requestId":123,"appId":1,"tpl":""}')
#     param['requestId'] = int(time.time() * 1000)
#     url = 'https://pet-chain.baidu.com/data/market/queryPetsOnSale'
#     try:
#         r = requests.post(url, data=json.dumps(param), headers=headers, verify=False)
#         pets = r.json()['data']['petsOnSale']
#         for pet in pets:
#             data[pet['petId']] = float(pet['amount'])
#     except Exception:
#         pass
#     return data
#
#
# def insert_all_pets():
#     conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='SCMD_2017_scmd', db='pets',
#                            charset='utf8')
#     cursor = conn.cursor()
#     for i in range(1, 5):
#         param = json.loads(
#             '{"pageNo":' + str(
#                 i) + ',"pageSize":20,"querySortType":"CREATETIME_DESC","petIds":[],"lastAmount":null,"lastRareDegree":null,"requestId":123,"appId":1,"tpl":""}')
#         param['requestId'] = int(time.time() * 1000)
#         url = 'https://pet-chain.baidu.com/data/market/queryPetsOnSale'
#         try:
#             r = requests.post(url, data=json.dumps(param), headers=headers, verify=False)
#             pets = r.json()['data']['petsOnSale']
#             for pet in pets:
#                 sql = 'insert into pets(genId,petId,birthType,mutation,generation,rareDegree,desc,petType,amount,bgColor,petUrl,validCode) ' \
#                       'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#                 cursor.execute(sql, (
#                     pet['id'], pet['petId'], pet['birthType'], pet['mutation'], pet['generation'],
#                     pet['rareDegree'],
#                     pet['desc'], pet['petType'], pet['amount'],
#                     pet['bgColor'], pet['petUrl'], pet['validCode']))
#                 conn.commit()
#                 # data[pet['petId']] = float(pet['amount'])
#         except Exception:
#             pass
#     conn.close()
#
#
# def buy_pet(petId):
#     param = json.loads('{"petId": "007", "requestId": 1517726374504, "appId": 1, "tpl": ""}')
#     param['petId'] = petId
#     param['requestId'] = int(time.time() * 1000)
#     url = 'https://pet-chain.baidu.com/data/txn/create'
#     r = requests.post(url, data=json.dumps(param), headers=headers, verify=False)
#     return r.json()
#
#
# def buy_all_pets(max_price):
#     while True:
#         data = get_all_pets()
#         for petId in [id for id in data if data[id] <= 800]:
#             try:
#                 msg = buy_pet(petId)['errorMsg']
#                 print('{0} ----> {1} : {2}'.format(petId, data[petId], msg))
#             except Exception as err:
#                 pass


# def __del__(self):
#     if self.conn:
#         # self.cur.close()
#         self.conn.close()


if __name__ == '__main__':
    # insert_all_pets()
    # for i in range(10):
    #     t = threading.Thread(target=buy_all_pets, args=(10,))
    #     t.start()

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='SCMD_2017_scmd', db='pets',
                           charset='utf8')
    cursor = conn.cursor()
    # sql = 'insert into pets(genId) ' \
    #       'values (%s)'
    # cursor.execute(sql, (99))
    # conn.commit()
    for i in range(1, 50000):
        param = json.loads(
            '{"pageNo":' + str(
                i) + ',"pageSize":20,"querySortType":"CREATETIME_DESC","petIds":[],"lastAmount":null,"lastRareDegree":null,"requestId":123,"appId":1,"tpl":""}')
        param['requestId'] = int(time.time() * 1000)
        url = 'https://pet-chain.baidu.com/data/market/queryPetsOnSale'
        try:
            r = requests.post(url, data=json.dumps(param), headers=headers, verify=False)
            pets = r.json()['data']['petsOnSale']
            print(pets)
            for pet in pets:
                sql = 'insert into pets(genId,petId,birthType,mutation,generation,rareDegree,description,petType,amount,bgColor,petUrl,validCode) ' \
                      'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cursor.execute(sql, (
                    pet['id'], pet['petId'], pet['birthType'], pet['mutation'], pet['generation'],
                    pet['rareDegree'], pet['desc'], pet['petType'], pet['amount'],
                    pet['bgColor'], pet['petUrl'], pet['validCode'],))
                conn.commit()
                # data[pet['petId']] = float(pet['amount'])
                time.sleep(0.5)
        except Exception as err:
            print(err)
            # if conn:
            #     conn.close()
            pass
    if conn:
        conn.close()
