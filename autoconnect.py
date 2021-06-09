import logging
import webbrowser
import os
import argparse
from time import sleep
from signal import signal, SIGINT
from sys import exit

logging.basicConfig(format='[%(asctime)s] %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

parser = argparse.ArgumentParser()
parser.add_argument('--drive', default='F')
parser.add_argument('--ip', default="172.93.101.24:27017")
args = parser.parse_args()

log_path = args.drive + r":/Program Files (x86)/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/console.log"
server_ip = args.ip
dc_msg = "Disconnect: Server shutting down.\n"
timeout_msg = "Server connection timed out.\n"
manual_dc = r"ChangeGameUIState: CSGO_GAME_UI_STATE_INGAME -> CSGO_GAME_UI_STATE_MAINMENU"
sleep_sec = 10
path = args.drive + r":\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\autoexec.cfg"
log_str = 'con_logfile console.log\n'
writecfg = 'host_writeconfig\n'
already_connected = False
connected_str = "Connected to"

if not os.path.isfile(path):
    a = open(path, "w")
    a.write("")
    a.close()

if not os.path.isfile(log_path):
    log = open(log_path, "w")
    log.write("")
    log.close()

fi = open(path, "r", encoding='utf-8', errors='ignore')
lines = fi.readlines()
fi.close()
in_file = False
has_end = False
for i in lines:
    if i == log_str:
        in_file = True
    if i == writecfg:
        has_end = True
    if connected_str in i:
        already_connected = True

if lines == []:
    lines = ["", ""]
if not in_file:
    g = open(path, "w")
    lines[0] = lines[0] + log_str
    for j in lines:
        g.write(j)
    if not has_end:
        g.write(writecfg)
    g.close()


def scan():
    f = open(log_path, "r", encoding='utf-8', errors='ignore')
    lines = f.readlines()
    for x in lines:
        logging.info(x)
        if dc_msg in x or timeout_msg in x or manual_dc in x:
            f.close()
            logging.info("Disconnected from server, reconnecting...")
            open(log_path, 'w').close()
            sleep(60)
            connect(server_ip)
            return
    f.close()


def handler(signal_received, frame):
    open(log_path, 'w').close()
    print('Exiting...')
    exit(0)


def connect(ip):
    logging.info("Connecting to server " + server_ip)
    webbrowser.open_new("steam://connect/" + server_ip)


if not already_connected:
    webbrowser.open_new("steam://run/730//%2Bexec%20autoexec.cfg/")
    sleep(15)
    connect(server_ip)
    sleep(10)
    open(log_path, 'w').close()

if __name__ == '__main__':
    signal(SIGINT, handler)
    while True:
        scan()
        sleep(sleep_sec)
        print("Waiting...")
