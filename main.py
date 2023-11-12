#!/usr/bin/python3
from urllib.parse import unquote
import requests as req
import sys
import os
import time,re
from time import sleep
os.system('clear')

logo = print("""\033[0;96m


███████╗██████╗░███╗░░██╗
██╔════╝██╔══██╗████╗░██║
█████╗░░██████╔╝██╔██╗██║
██╔══╝░░██╔══██╗██║╚████║
██║░░░░░██║░░██║██║░╚███║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝\033[1;36m2.O
\033[1;36m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
 \033[1;37mOwner   :            FARHAN MUH TASIM
 \033[1;37mFacebook:            FARHAN MUH TASIM
 \033[1;37mGithub  :            gtajisan X me
 \033[1;37mWhatsapp:            +880130505723*
 \033[1;31mOne line Command:
\033[1;31

 \033[1;31mFor Help : FB-AND-TELEGRAM

 \033[1;31mNote    :       Facebook-video-downloader
\033[1;36m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;32m
""")


def down(url, path):
    testing = 1024
    content = req.get(url)
    size = round(int(content.headers.get('Content-Length'))/testing)
    print(f'\n[-] Video Size: {size} KB')
    with open(path, 'wb') as a:
        for data in content.iter_content(chunk_size=testing):
            a.write(data)
    print('[√] Download successfuly')

def parse(url):
    res = req.get(url).text
    if 'video_redirect' in res:
        url_video = re.search(r'href\=\"\/video\_redirect\/\?src\=(.*?)\"', res)
        return unquote(url_video.group(1)).replace(';', '&')
    else:
        exit('[!] Video Not Found')

if __name__ == '__main__':
    print (logo)
    print ('\n[?] Please insert a valid Video URL:')
    url = parse(input('=>: ').replace('www', 'mbasic'))
    path = input('[?] Save File To: ')
    if '.mp4' in path:
        down(url, path)
    else:
        print ('Example:')
        print ('Save To: /Download/video/farhan_video.mp4')
        sys.exit()
