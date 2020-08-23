import requests 
import pdb
from requests.auth import HTTPBasicAuth
import base64
public_key = 'M73srjY2Fbv5AnQ5sydwQUxRHSnJHGgQ3ie3lYEs'
secret_key =  'qPVhiJJbWQtCgB2Jw3N4C3feYdbMpjk58ls5cmmPnbgZlXy7ADAzI6lrXR9536RWGkUc5zOaz4Fi8eIh5DmTkdjnYTTZ4fCAtmOasIHRk2qeZRwQP6yk9RVCwStsnYjO'
token_k = base64.b64encode(bytes(f"{public_key}:{secret_key}", "ISO-8859-1")).decode("ascii")

print(token_k)
try:
	pdb.set_trace()
	req = requests.post("http://localhost:8000/oauth/token?grant_type=authorization-code",headers=headers)
	pdb.set_trace()
	print(req)
except requests.exceptions.RequestException as e:
	print(e)


"""
1) Get request redirect from app to auth server => http://localhost:8000/oauth/authorize/?response_type=code&client_id=xzFisMHERT97LmmKQwloYePmd3bFc93Ctq8F4uDA&redirect_uri=http://localhost:8000/api/index
2) Post request :
http://localhost:8000/oauth/token/

Post form data:
[{"key":"grant_type","value":"authorization_code","equals":true,"description":"","enabled":true},{"key":"code","value":"SeI3tBmB3Dl2x1bVsVHdGruZHq5Nsm","equals":true,"description":"","enabled":true},{"key":"redirect_uri","value":"http://localhost:8000/api/index","equals":true,"description":"","enabled":true},{"key":"client_id","value":"123456","description":"","type":"text","enabled":true}]
"""

# https://medium.com/@halfspring/guide-to-an-oauth2-api-with-django-6ba66a31d6d