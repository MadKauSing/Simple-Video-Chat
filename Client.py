# client side program
# libraries
import socket  # library to manage socket
import cv2  # library to capture video
import pickle  # library to implement 'pickling' ie serialisation of a python object
import struct  # library to pack and unpack data


def client():
<<<<<<< HEAD
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host_ip_server = '192.168.43.162' 
    port = 1235
=======
    # creation of socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip_server = "192.168.43.162"
    port = 1234
>>>>>>> 5c98333614cc7910460613c85999b6d5a301c641
    print("Socket Created Successfully")

    # establishment of connection
    client_socket.connect((host_ip_server, port))
    data = b""
    payload_size = struct.calcsize("Q")
    print("Socket Accepted")

    # data transmission loop
    while True:
        print("CLIENT:")
        # loop to receive new packet
        while len(data) < payload_size:
            packet = client_socket.recv(2160)
            if not packet:
                break  # error condition
            data += packet
        # slice packet based on payload size and store separately
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        # unpack the received data
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        # loop to receive more data
        while len(data) < msg_size:
            data += client_socket.recv(2160)
        # dividing data into frames
        frame_data = data[:msg_size]
        data = data[msg_size:]
        # loading and display of frames
        frame = pickle.loads(frame_data)
        cv2.imshow("RECEIVING VIDEO", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    # closing of connection
    client_socket.close()


# client()
