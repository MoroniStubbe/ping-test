import time
import socket
import os

ip = '217.105.175.182'
port = 50000 + int(input('port: '))
pingCount = int(input('pingCount: '))
pings = []
pongs = []
timeoutCount = 0

for ping in range(pingCount):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1)
    start = time.time()
    message = bytes(str(start), 'utf-8')
    addr = (ip, port)

    print(f'{round(ping / pingCount * 100)}%    timeouts: {timeoutCount}', end='\r')
    client_socket.sendto(message, addr)
    try:
        data, server = client_socket.recvfrom(32)
        intermediate = float(data.decode('utf-8'))
        end = time.time()
        pings.append((intermediate - start) * 1000)
        pongs.append((end - intermediate) * 1000)
    except socket.timeout:
        timeoutCount += 1

def calcJitters(l):
    j = []
    for i in range(len(l) - 1):
        j.append(abs(l[i + 1] - l[i]))
    return j


pings.sort()
pongs.sort()
minPing = pings[0]
minPong = pongs[0]
minPingPong = minPing + minPong
low001Ping = pings[round(len(pings) * 0.0001)]
low001Pong = pongs[round(len(pongs) * 0.0001)]
low001PingPong = low001Ping + low001Pong
low01Ping = pings[round(len(pings) * 0.001)]
low01Pong = pongs[round(len(pongs) * 0.001)]
low01PingPong = low01Ping + low01Pong
low1Ping = pings[round(len(pings) * 0.01)]
low1Pong = pongs[round(len(pongs) * 0.01)]
low1PingPong = low1Ping + low1Pong
low10Ping = pings[round(len(pings) * 0.1)]
low10Pong = pongs[round(len(pongs) * 0.1)]
low10PingPong = low10Ping + low10Pong
medPing = pings[round(len(pings) / 2)]
medPong = pongs[round(len(pongs) / 2)]
medPingPong = medPing + medPong
high10Ping = pings[round(len(pings) * 0.9 - 1)]
high10Pong = pongs[round(len(pongs) * 0.9 - 1)]
high10PingPong = high10Ping + high10Pong
high1Ping = pings[round(len(pings) * 0.99 - 1)]
high1Pong = pongs[round(len(pongs) * 0.99 - 1)]
high1PingPong = high1Ping + high1Pong
high01Ping = pings[round(len(pings) * 0.999 - 1)]
high01Pong = pongs[round(len(pongs) * 0.999 - 1)]
high01PingPong = high01Ping + high01Pong
high001Ping = pings[round(len(pings) * 0.9999 - 1)]
high001Pong = pongs[round(len(pongs) * 0.9999 - 1)]
high001PingPong = high001Ping + high001Pong
maxPing = pings[len(pings) -1]
maxPong = pongs[len(pongs) -1]
maxPingPong = maxPing + maxPong

pingJitters = sorted(calcJitters(pings))
pongJitters = sorted(calcJitters(pongs))
minPingJitter = pingJitters[0]
minPongJitter = pongJitters[0]
minJitter = minPingJitter + minPongJitter
low001PingJitter = pingJitters[round(len(pingJitters) * 0.0001)]
low001PongJitter = pongJitters[round(len(pongJitters) * 0.0001)]
low001Jitter = low001PingJitter + low001PongJitter
low01PingJitter = pingJitters[round(len(pingJitters) * 0.001)]
low01PongJitter = pongJitters[round(len(pongJitters) * 0.001)]
low01Jitter = low01PingJitter + low01PongJitter
low1PingJitter = pingJitters[round(len(pingJitters) * 0.01)]
low1PongJitter = pongJitters[round(len(pongJitters) * 0.01)]
low1Jitter = low1PingJitter + low1PongJitter
low10PingJitter = pingJitters[round(len(pingJitters) * 0.1)]
low10PongJitter = pongJitters[round(len(pongJitters) * 0.1)]
low10Jitter = low10PingJitter + low10PongJitter
medPingJitter = pingJitters[round(len(pingJitters) / 2)]
medPongJitter = pongJitters[round(len(pongJitters) / 2)]
high10PingJitter = pingJitters[round(len(pingJitters) * 0.9 - 1)]
high10PongJitter = pongJitters[round(len(pongJitters) * 0.9 - 1)]
high10Jitter = high10PingJitter + high10PongJitter
high1PingJitter = pingJitters[round(len(pingJitters) * 0.99 - 1)]
high1PongJitter = pongJitters[round(len(pongJitters) * 0.99 - 1)]
high1Jitter = high1PingJitter + high1PongJitter
high01PingJitter = pingJitters[round(len(pingJitters) * 0.999 - 1)]
high01PongJitter = pongJitters[round(len(pongJitters) * 0.999 - 1)]
high01Jitter = high01PingJitter + high01PongJitter
high001PingJitter = pingJitters[round(len(pingJitters) * 0.9999 - 1)]
high001PongJitter = pongJitters[round(len(pongJitters) * 0.9999 - 1)]
high001Jitter = high001PingJitter + high001PongJitter
medJitter = medPingJitter + medPongJitter
maxPingJitter = pingJitters[len(pingJitters) -1]
maxPongJitter = pongJitters[len(pingJitters) -1]
maxJitter = maxPingJitter + maxPongJitter

data = {
    'ping':{
        'min': f'{round(minPingPong, 3)} (↑{round(minPing, 3)} ↓{round(minPong, 3)})',
        'low001': f'{round(low001PingPong, 3)} (↑{round(low001Ping, 3)} ↓{round(low001Pong, 3)})',
        'low01': f'{round(low01PingPong, 3)} (↑{round(low01Ping, 3)} ↓{round(low01Pong, 3)})',
        'low1': f'{round(low1PingPong, 3)} (↑{round(low1Ping, 3)} ↓{round(low1Pong, 3)})',
        'low10': f'{round(low10PingPong, 3)} (↑{round(low10Ping, 3)} ↓{round(low10Pong, 3)})',
        'med': f'{round(medPingPong, 3)} (↑{round(medPing, 3)} ↓{round(medPong, 3)})',
        'high10': f'{round(high10PingPong, 3)} (↑{round(high10Ping, 3)} ↓{round(high10Pong, 3)})',
        'high1': f'{round(high1PingPong, 3)} (↑{round(high1Ping, 3)} ↓{round(high1Pong, 3)})',
        'high01': f'{round(high01PingPong, 3)} (↑{round(high01Ping, 3)} ↓{round(high01Pong, 3)})',
        'high001': f'{round(high001PingPong, 3)} (↑{round(high001Ping, 3)} ↓{round(high001Pong, 3)})',
        'max': f'{round(maxPingPong, 3)} (↑{round(maxPing, 3)} ↓{round(maxPong, 3)})'
    },
    'jitter':{
        'min': f'{round(minJitter, 3)} (↑{round(minPingJitter, 3)} ↓{round(minPongJitter, 3)})',
        'low001': f'{round(low001Jitter, 3)} (↑{round(low001PingJitter, 3)} ↓{round(low001PongJitter, 3)})',
        'low01': f'{round(low01Jitter, 3)} (↑{round(low01PingJitter, 3)} ↓{round(low01PongJitter, 3)})',
        'low1': f'{round(low1Jitter, 3)} (↑{round(low1PingJitter, 3)} ↓{round(low1PongJitter, 3)})',
        'low10': f'{round(low10Jitter, 3)} (↑{round(low10PingJitter, 3)} ↓{round(low10PongJitter, 3)})',
        'med': f'{round(medJitter, 3)} (↑{round(medPingJitter, 3)} ↓{round(medPongJitter, 3)})',
        'high10': f'{round(high10Jitter, 3)} (↑{round(high10PingJitter, 3)} ↓{round(high10PongJitter, 3)})',
        'high1': f'{round(high1Jitter, 3)} (↑{round(high1PingJitter, 3)} ↓{round(high1PongJitter, 3)})',
        'high01': f'{round(high01Jitter, 3)} (↑{round(high01PingJitter, 3)} ↓{round(high01PongJitter, 3)})',
        'high001': f'{round(high001Jitter, 3)} (↑{round(high001PingJitter, 3)} ↓{round(high001PongJitter, 3)})',
        'max': f'{round(maxJitter, 3)} (↑{round(maxPingJitter, 3)} ↓{round(maxPongJitter, 3)})'
    }
}

os.system('cls')
print('[ping]')
print('min: ' + data['ping']['min'])
print('low001: ' + data['ping']['low001'])
print('low01: ' + data['ping']['low01'])
print('low1: ' + data['ping']['low1'])
print('low10: ' + data['ping']['low10'])
print('med: ' + data['ping']['med'])
print('high10: ' + data['ping']['high10'])
print('high1: ' + data['ping']['high1'])
print('high01: ' + data['ping']['high01'])
print('high001: ' + data['ping']['high001'])
print('max: ' + data['ping']['max'])

print('\n[jitter]')
print('min: ' + data['jitter']['min'])
print('low001: ' + data['jitter']['low001'])
print('low01: ' + data['jitter']['low01'])
print('low1: ' + data['jitter']['low1'])
print('low10: ' + data['jitter']['low10'])
print('med: ' + data['jitter']['med'])
print('high10: ' + data['jitter']['high10'])
print('high1: ' + data['jitter']['high1'])
print('high01: ' + data['jitter']['high01'])
print('high001: ' + data['jitter']['high001'])
print('max: ' + data['jitter']['max'])
print(f'timeouts (1s): {timeoutCount}')
input()