import socket

def check_port():
    host = input("Enter target IP address or hostname: ")
    port = int(input("Enter port number: "))

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(3)

        result = client.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN on {host}")
        else:
            print(f"Port {port} is CLOSED or FILTERED on {host}")

        client.close()

    except ValueError:
        print("Please enter a valid port number.")

    except socket.gaierror:
        print("Invalid hostname or IP address.")

    except Exception as e:
        print("Error:", e)


check_port()
