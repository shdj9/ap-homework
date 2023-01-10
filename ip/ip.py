def ip_v0(ip):
    ip2 = ip.split('.')
    for x in ip2:
        x = int(x)
    return ip2

def ip_v1(ip):
    ip2 = ip_v0(ip)
    return hex(ip2[0]*2**24+ip2[1]*2**16+ip2[2]*2**8+ip[3])