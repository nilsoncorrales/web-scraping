


# import youtube_dl
#
# url = 'https://www.youtube.com/watch?v=UUhfNbhM7Zg'
#
# video_info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)
# video_title = video_info['title']
#
# path = 'D:/dowload-youtube'
#
# opciones = {
#     'format': 'bestaudio/best',
#     'outtmpl': f'{path}/{video_title}.mp3',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
# }
#
# with youtube_dl.YoutubeDL(opciones) as ydl:
#     ydl.download([url])