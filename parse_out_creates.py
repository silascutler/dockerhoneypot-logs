#!/usr/bin/env python
#Author: p1nk


import os
import json
import base64



def parse_log(inpath):
    with open(inpath, 'r') as file:
        for line in file:
            # convert line to json
            jline = json.loads(line)

            source = jline.get('source', '[no source]')
            data = jline.get('data', '[no data]')
            datalen = len(data)
            url = "/".join(jline.get('url', '[no url]').split('/')[3:])


            if datalen > 20:
                print(f"[Source: {source:<15}] - URL: {url:<30} |  Len: {datalen}")

                try:
                    ddata = json.loads(base64.b64decode(data))
                    image = ddata.get('Image', '')
                    cmd = ddata.get('Cmd', '')

                    print(f" - Image: {image}")
                    print(f" - Cmd:")
                    print(cmd)
                    print('--------------------------------------')

                except Exception as e:
                    pass
                    # print(e)





def main():
    # Walk the logs directory
    for dirpath, dirnames, filenames in os.walk("./logs"):
        for filename in filenames:
            if filename.endswith('.log'):
                parse_log(os.path.join(dirpath, filename))



if __name__ == '__main__':
    main()