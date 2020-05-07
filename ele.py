import requests 
import json 
import base64 
import io 
from PIL import Image  

headers = { 
    'Accept': 'application/json, text/plain, */*', 
    'Content-Type': 'application/json; charset=UTF-8', 
    'Origin': 'https://h5.ele.me', 
    'Referer': 'https://h5.ele.me/login/', 
    'Sec-Fetch-Mode': 'cors', 
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1' 
}  
phoneNum = input('请输入你的手机号,回车键确认:') 

send_msg_url = 'https://h5.ele.me/restapi/eus/login/mobile_send_code' 
send_msg_payloadData = {"mobile":phoneNum, "captcha_value":"", "captcha_hash":"", "scf":"ms"} 
res1 = requests.post(url=send_msg_url, data=json.dumps(send_msg_payloadData), headers=headers) 
print('res1:', res1) 
 
if 'message' in res1.json(): 
    getCaptcha_url = 'https://h5.ele.me/restapi/eus/v3/captchas' 
    getCaptcha_data = json.dumps({"captcha_str":phoneNum}) 
    res2 = requests.post(url=getCaptcha_url, data=getCaptcha_data, headers=headers).json() 
    captcha_hash = res2['captcha_hash'] 
    captcha_image = res2['captcha_image'] 
 
    captcha = base64.b64decode(captcha_image.split(',')[-1]) 
  
    byte_stream = io.BytesIO(captcha) 
    Image.open(byte_stream).show() 
    captcha_code = input('请输入验证码，回车键确认:') 
 
    sendCaptcha_data = {"mobile":phoneNum, "captcha_value":captcha_code, "captcha_hash":captcha_hash,"scf":"ms"} 
    res3 = requests.post(url=send_msg_url, data=json.dumps(sendCaptcha_data), headers=headers) 
    print(res3.json())
else:
     pass