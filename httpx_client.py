import time

import httpx

clinet = httpx.Client(base_url="http://localhost:8003", timeout=100, headers={"AutorizationV2": "Bearer ..."})

payload = {
   "email": f"user.{time.time()}@example.com",
   "lastName": "string",
   "firstName": "string",
   "middleName": "string",
   "phoneNumber": "string"
 }

response = clinet.post("/api/v1/users", json=payload)
print(response.text)
