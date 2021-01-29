import pygame, random, threading, socket, pickle, os
import interface, func

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()                         
port = 11111
s.bind((host, port))

def main():
    pygame.display.set_caption("Multiprocessing LocalHost Bouncing Balls")
    pygame.display.init()

    ### Display ###
    close = False
    clock = pygame.time.Clock()

    Processes = list()
    balls = list()
    ball = func.Ball.make_ball()
    balls.append(ball)

    while not close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
                os._exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if interface.button_add_process.collidepoint((pos[0], pos[1] - interface.DISP_PROCESS_HEIGHT_BORDER)):
                    ball = func.Ball.make_ball()
                    balls.append(ball)
                elif interface.button_add_x10_process.collidepoint((pos[0], pos[1] - interface.DISP_PROCESS_HEIGHT_BORDER)):
                    for _ in range(10):
                        ball = func.Ball.make_ball()
                        balls.append(ball)
                elif interface.button_remove_process.collidepoint((pos[0], pos[1] - interface.DISP_PROCESS_HEIGHT_BORDER)):
                    if len(balls) > 0:
                        balls.pop(0)
                        kill_process = list()
                        kill_process.append('kill')
                        bytes_reply = pickle.dumps(kill_process)
                        print('Server - Killing Client', Processes[0])
                        s.sendto(bytes_reply, Processes[0])
                        Processes.pop(0)

                elif interface.button_remove_all_process.collidepoint((pos[0], pos[1] - interface.DISP_PROCESS_HEIGHT_BORDER)):
                    for _ in range (len(balls)):
                        if len(balls) > 0:
                            balls.pop(0)
                            kill_process = list()
                            kill_process.append('kill')
                            bytes_reply = pickle.dumps(kill_process)
                            print('Server - Killing Client', Processes[0])
                            s.sendto(bytes_reply, Processes[0])
                            Processes.pop(0)
                elif interface.button_close.collidepoint((pos[0], pos[1] - interface.DISP_PROCESS_HEIGHT_BORDER)):
                    close = True
                    os._exit(0)
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = func.Ball.make_ball()
                    balls.append(ball)
                if event.key == pygame.K_x:
                    for _ in range(10):
                        ball = func.Ball.make_ball()
                        balls.append(ball)
                if event.key == pygame.K_DELETE:
                    if len(balls) > 0:
                        balls.pop(0)
                        kill_process = list()
                        kill_process.append('kill')
                        bytes_reply = pickle.dumps(kill_process)
                        print('Server - Killing Client', Processes[0])
                        s.sendto(bytes_reply, Processes[0])
                        Processes.pop(0)

        ### Processes Ball Movement ###
        new_processes_needed = len(balls) - len(Processes)
        for _ in range(new_processes_needed):
            thread = threading.Thread(target=func.spawn_server)
            thread.start()
            print('Server - Waiting Client Info...')
            (msg, client_info) = s.recvfrom(5120000)
            print('Server - Client Info Received!')
            print('Server - Client Info:', client_info)
            Processes.append(client_info)
            client_msg = pickle.loads(msg)
            print('Server - Client Msg:', client_msg[0])


        proc_count = 0
        for ball in balls:
            try:
                print('Server - Sending Ball Data to Client...')
                print('Server - Ball Data:', ball)
                ball_data = list()
                ball_data.append(ball)
                balls.remove(ball)
                bytes_reply = pickle.dumps(ball_data)
                s.sendto(bytes_reply, Processes[proc_count])
                print('Server - Ball Data Sent!')
                print('Server - Waiting Client Ball Data...')
                (new_ball_data, client_info) = s.recvfrom(5120000)
                print('Server - New Ball Data Received!')
                new_data = pickle.loads(new_ball_data)
                new_ball = new_data[0]
                balls.append(new_ball)
                proc_count += 1
                print()
            except Exception as erro:
                print(str(erro))

        interface.s.fill(interface.grey)
        
        ### Draw Balls ###
        for ball in balls:
            pygame.draw.circle(interface.s, ball.color, [ball.x, ball.y], 25)
        
        
        ### Display Processes Counter ###
        interface.display_processes(len(Processes))
        
        ass = interface.font_1.render("Dev.: Fábio R. P. Nunes", 10, interface.light_grey_2)
        interface.s.blit(ass, (630, 580))
        interface.window.blit(interface.s, (interface.DISP_PROCESS_WIDTH_BORDER, 0))
        
        pygame.display.update()
        clock.tick(60)
    pygame.display.quit()

if __name__ == "__main__":
    main()