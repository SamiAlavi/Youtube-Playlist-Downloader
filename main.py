from helper import getLinks, createFolder, downloadMp3

dirDownload = './Music' # path to store downloaded file(s)
pathYoutubeLiked = './Pop Music Playlist - Timeless Pop Songs (Updated Weekly 2021) - YouTube.html' # path of downloaded youtube liked page
limit = 1 # limit number of youtube audio(s) to download

# options for ydl
options = {
    'quality': '320',
    'verbose': False,
}

urls = getLinks(pathYoutubeLiked, limit)
createFolder(dirDownload)
downloadMp3(urls, options)
