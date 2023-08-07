import ping3

def ping_host(host):
    try:
        rtt = ping3.ping(host)
        if rtt is not None:
            print(f"Ping to {host} successful (RTT: {rtt} ms)")
        else:
            print(f"Ping to {host} failed")
    except Exception as e:
        print(f"Error while pinging the host: {e}")

def verbose_ping_host(host):
    try:
        rtt = ping3.verbose_ping(host)
        if rtt is not None:
            print(f"Ping to {host} successful (RTT: {rtt} ms)")
        else:
            print(f"Ping to {host} failed")
    except Exception as e:
        print(f"Error while pinging to host: {e}")

def start(address):
    print('Using ping:')
    ping_host(host=address)

    print('\nUsing verbose ping:')
    verbose_ping_host(host=address)