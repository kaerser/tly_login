# -*- coding:utf-8 -*-
import requests as req
import base64

def captche_main(image_data, ak, sk):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}'.format(ak,sk)
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = req.post(host) #获取百度access_token
    access_token = res.json()['access_token']
    # general_basic  标准版 免费额度：1000次/月
    # general        标准含位置版 免费额度：1000次/月
    # accurate_basic 高精度版 免费额度：1000次/月
    # accurate       高精度含位置版 免费额度：500次/月
    temp_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token=' + access_token
    temp_data = {
        'image': base64.b64encode(image_data)
    }
    data = req.post(temp_url, data=temp_data, headers=header) # 提交验证码图
    cap_code = ''
    for i in data.json()['words_result']:
        cap_code = cap_code + i['words']
    # Code = data.json()['words_result'][0]['words'].replace(' ', '')
    return cap_code # 返回识别的结果