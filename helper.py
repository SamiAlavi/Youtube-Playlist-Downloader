from bs4 import BeautifulSoup, SoupStrainer
from os import makedirs, chdir
import youtube_dl

def getLinks(pathYoutubeLiked, limit):
    listt = list()
    
    try:
        limit = limit*2
        
        with open(pathYoutubeLiked, 'r',encoding='utf8') as f:
            webpage = f.read()
            count=0
            for link in BeautifulSoup(webpage,'html.parser', parse_only=SoupStrainer('a')):
                if link.has_attr('href'):
                    a = link['href']
                    if '&index=' in a:
                        count+=1
                        listt.append(a[:43])
                if count==limit:
                    break
        listt = list(set(listt))
        [print(i) for i in listt]
        print(f'Got {len(listt)} links')
    except:
        print(f'Error reading html file at {pathYoutubeLiked}')
    return listt

def createFolder(dirDownload):
    try:
        makedirs(dirDownload)    
        print(f"Directory {dirDownload} created ")
    except FileExistsError:
        print(f"Directory {dirDownload} already exists")
    chdir(dirDownload)
        
def downloadMp3(urls, options):
    # options, see youtube_dl documentation for more options
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': options['quality'],
            }],
            'keepvideo': False,
            'outtmpl': '%(title)s.%(etx)s',
            'quiet' : not options['verbose']
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            for i, url in enumerate(urls):
                ydl.download([url])
                print(f'Downloaded {i+1} audio(s)')
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    except:
        print("Could not set up youtube_dl. See documentation.")
