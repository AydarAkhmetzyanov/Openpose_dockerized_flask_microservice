Openpose dockerized flask microservice

Dockerized openpose web microservice based on flask with thin cpu implementation of pose estimation. Suitable for systems, when you need isolated pose estimation service.
Microservice based on https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch

Postman documentation https://www.getpostman.com/collections/a108214eff536f4bbcd5

Python code to call service and upload photo:

```
import requests

url = "http://127.0.0.1:5000/upload"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\"hand2.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
```

How to run
```
git clone https://github.com/AydarAkhmetzyanov/Openpose_dockerized_flask_microservice.git
cd Openpose_dockerized_flask_microservice
docker build -t poseapi:latest .
docker run -p 5000:5000 poseapi
docker run -d -p 5000:5000 poseapi
```

Simple local demo with image
```
python demo.py --checkpoint-path checkpoint_iter_370000.pth.tar --cpu --video 0
```
