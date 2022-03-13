# How it works - client

## Libraries used

1. socket - used to implement and manage sockets
2. cv2 - used for video capture
3. pickle - used for serialisation of python objects to character streams 
4. struct - used to pack and unpack data 

---

## Creation and establishment of socket connection

```py
	socket(socket.AF_INET,socket.SOCK_STREAM)
```
1. `socket.AF_INET` specifies the address family being used for the connection , which is IPv4
2. `socket.SOCK_STREAM` declares that the connection is a TCP connection
```py
	connect((host_ip_server,port))
```
3. the host IP server and port are declared and the client is connected
4. a `data` variable of `<class 'bytes'>` is created 
```py
	struct.calcsize("Q")
```
5. the payload size is calculated and is of the format `long long int`

---

## Data transmission loop

1. loop to receive new packet 
```py
	packet=client_socket.recv(2160)
```
- the packet is received from the server and its size is limited to 2160 bytes
-  on exceeding the size, `packet` will contain an empty string - which is used to declare errors
- this packet is concatenated to `data` 
```py
	msg_size-struct,unpack("Q",packed_msg_size)[0]
```
2. the first `payload_size` bytes are sliced from `data` and unpacked - [0] is used as the return type of `unpack()` is a tuple  
 is used as the return type of `unpack()` is a tuple is used as the return type of `unpack()` is a tuple is used as the return type of `unpack()` is a tuple
3. the data is divided and oaded into frames
```py
	cv2.shwow("RECEIVING VIDEEO",frame)
```
4. the frames are displayed

---

## Connection is closed 
---

