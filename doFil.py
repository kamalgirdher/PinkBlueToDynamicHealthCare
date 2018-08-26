import requests
import time

__all__ = ['fileDownload','getfilename','Replace_line_in_file']

def fileDownload(url,c):
    filename = str(c)# + '.' + url.split('.')[-1] # + '_' + url.split('/')[-1]
    r = requests.get(url, allow_redirects=True)
    f = open("img/" + filename, 'wb')
    f.write(r.content)
    f.close()

def getfilename(url):
    return time.strftime("%Y%m%d%H%M%S") + '.' + url.split('.')[-1]

def Replace_line_in_file(file,searchExp1,replaceLine):
    for line in fileinput.input(file, inplace=1):
        if searchExp1 in line:
            line = replaceLine+'\n'
        sys.stdout.write(line)
