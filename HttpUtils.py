# -*- coding: utf-8 -*-

import urllib3
import json
import requests
import random


urllib3.disable_warnings()

http = urllib3.PoolManager(retries=2,timeout=10,num_pools=200,maxsize=200)

def post_request():

    access_token = "24.ffbf71adc02e8f2217f9b2db82018367.2592000.1562314949.282335-16439157"
    url = "https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token={access_token}".format(access_token=access_token)
    headers = {'Content-type': 'application/json'}
    data = {"log_id":"UNITTEST_10000","version":"3.0","service_id":"S18960","session_id":"","request":{"query":"上海有什么好玩的","user_id":"88888"},"dialog_state":{"contexts":{"SYS_REMEMBERED_SKILLS":["59170"]}}}
    print data,url

    print data, url

    data["request"]["query"] = "上海好吃的"
    print data

    json_data = json.dumps(data).encode("utf-8")

    # r = http.request("post", url, headers=headers,fields=json_data)
    # data2 = {"attribute":"value"}
    # encode_data = json.dumps(data2).encode("utf-8")

    r =  http.request('POST', url, headers=headers, body=json_data)

    res_data = json.loads(r.data)

    final_result = ""
    if res_data.get("error_code") == "0":
        print "error result"
    else:
        response_list =  res_data["result"]["response_list"]
        if(response_list.__sizeof__()>0):
            '''取结果集中的第一个结果集 的actionlist'''
            action_list = response_list[0]["action_list"]
            choice_index = random.randint(1,len(action_list))-1

            choice_list = list(action_list)
            final_result = choice_list[choice_index]
            final_result = final_result["say"]

    return final_result

def do_ai_reply():

    access_token = "24.ffbf71adc02e8f2217f9b2db82018367.2592000.1562314949.282335-16439157"
    baseUrl = "https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token={access_token}".format(access_token=access_token)
    headers = {'Content-type': 'application/json'}
    data = {"log_id":"UNITTEST_10000","version":"3.0","service_id":"S18960","session_id":"","request":{"query":"上海有什么好玩的","user_id":"88888"},"dialog_state":{"contexts":{"SYS_REMEMBERED_SKILLS":["59170"]}}}
    print data,baseUrl

    data_json = json.dumps(data)  # dumps：将python对象解码为json数据

    content = requests.post(url=baseUrl,data=data_json).content.decode("utf-8")
    print content

if __name__ == '__main__':

    res = post_request()
    print 99999999999999
    print res



