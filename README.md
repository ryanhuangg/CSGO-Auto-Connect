# CSGO-Auto-Connect
Python script to automatically connect and keep you connected you to a given CSGO server

Uses steam browser protocol to launch and connect to servers. Will modify your autocfg (if you have one) or the script will create one.

Usage:
Download the script onto your local computer and open cmd where it is stored. Run it with the cmd command '.\autoconnect.py --drive <DRIVE> --ip <IP>'
<DRIVE> is a single letter corresponding to your CSGO install drive (for example, C D F) with no : or \ after it
<IP> is your server's info formatted in [IP/DNS]:[PORT][/PASSWORD], for example 1.2.3.4:15/higuys or 1.2.3.4 or 1.2.3.4:5000
