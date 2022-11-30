import socket
import binascii
import os

for i in range(0, 10):
    IP = input()
    try:
        socket.inet_aton(IP)
        ip2bin = ".".join(map(str, ["{0:08b}".format(int(x)) for x in IP.split(".")]))
        ip2oct = '.'.join(["%04o" % int(x) for x in IP.split('.')])
        ip2hex = binascii.hexlify(socket.inet_aton(IP)).decode().upper()
        address = [IP, ip2bin, ip2oct, ip2hex]
        try:
            with open(r'C:\Users\Anushree\PycharmProjects\Cisco_Internship\conversion.txt', 'a') as fp:
                for item in address:
                    fp.write("%s " % item)
                fp.write("\n")
        except IOError:
            print("oops!")

    except socket.error:
        print("Invalid IP")

with open("conversion.txt", "r") as inFile:
    lines = [l.strip().replace(' ',',') for l in inFile]
    print("The first IP address in Decimal, Binary, Octal and hexadecimal format is",lines[0])
    print("The second IP address in Decimal, Binary, Octal and hexadecimal format is", lines[1])
    print("The third IP address in Decimal, Binary, Octal and hexadecimal format is", lines[2])
    print("The fourth IP address in Decimal, Binary, Octal and hexadecimal format is", lines[3])
    print("The fifth IP address in Decimal, Binary, Octal and hexadecimal format is", lines[4])
    print("The sixth IP address in Decimal, Binary, Octal and hexadecimal format is", lines[5])
    print("The seventh IP address in Decimal, Binary, Octal and hexadecimal format is", lines[6])
    print("The eighth IP address in Decimal, Binary, Octal and hexadecimal format is", lines[7])
    print("The ninth IP address in Decimal, Binary, Octal and hexadecimal format is", lines[8])
    print("The tenth IP address in Decimal, Binary, Octal and hexadecimal format is", lines[9])

if os.path.exists("conversion.txt"):
    os.remove("conversion.txt")
