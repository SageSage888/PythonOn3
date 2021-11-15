import socket


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.bind(('127.0.0.1', 9696))
        soc.listen(1)
        timeout_value = 60
        soc.settimeout(timeout_value)
        print('server started')

        try:
            while True:
                user_socket, address = soc.accept()
                with user_socket:
                    print(f'user {address[0]} connected')
                    data = user_socket.recv(2048).decode('utf-8')
                    if data == 'exit':
                        user_socket.close
                    print(f'{address[0]}: {data}')
                    user_socket.send(('OK').encode('utf-8'))
                    user_socket.close
                    soc.settimeout(timeout_value)
        except socket.timeout:
            print(
                f'Did not receive any data for {timeout_value} seconds \nConnection closed by Timeout')
        finally:
            soc.close()


if __name__ == "__main__":

    start_server()
