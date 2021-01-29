import socket, random, pickle
import func

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)                   
host = socket.gethostname()                      
port = random.randint(0, 65535)
s.bind((host, port))
server_port = 11111
server = (host, server_port)
firt_time = False
while True:
    if not firt_time:
        print('Client - Server Info:', server)
        msg = "Hi, server! I sent u my location."
        reply = list()
        reply.append(msg)
        bytes_reply = pickle.dumps(reply)
        print('Client - Sending client info...')
        s.sendto(bytes_reply, server)
        print('Client - Sent!')
        firt_time = True

    print('Client - Waiting Server Ball Data...')
    (data, server) = s.recvfrom(5120000)
    msg = pickle.loads(data)
    if msg[0] == 'kill':
        print('Client - Client', s.getsockname(), 'Dead!')
        print()
        break
    else:
        ball = msg[0]
        print('Client - Ball Data Received!')
        print('Client - Ball Data:', ball)
        print('Client - Processing Ball Data...')
        new_ball = func.Ball.mov_collisions(ball)
        print('Client - New Ball Data:', new_ball)
        new_data = list()
        new_data.append(new_ball)
        print('Client - Sending Client New Ball Data...')
        bytes_reply = pickle.dumps(new_data)
        s.sendto(bytes_reply, server)
        print('Client - New Ball Data Sent!')

s.close()