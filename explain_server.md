# How it works - server

## libraries used 
### same as client file 

---

## Creation and establishment of socket connection
```py
host_name=socket.gethostname()
host_ip=socket.gethostbyname(host_name)
```
1. the hostname and IP are bound to the socket using `bind()`
2. the socket begins to listen at the specified port 
