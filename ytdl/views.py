from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import yt_dlp

# import youtube_dl
from .forms import DownloadForm
import re
from crispy_forms import *



# def download_video(request):
#     global context
#     form = DownloadForm(request.POST or None)
    
#     if form.is_valid():
#         video_url = form.cleaned_data.get("url")
#         regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
#         #regex = (r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$\n")
#         print(video_url)
#         if not re.match(regex,video_url):
#             print('nhi howa')
#             return HttpResponse('Enter correct url.')

#         # if 'm.' in video_url:
#         #     video_url = video_url.replace(u'm.', u'')

#         # elif 'youtu.be' in video_url:
#         #     video_id = video_url.split('/')[-1]
#         #     video_url = 'https://www.youtube.com/watch?v=' + video_id

#         # if len(video_url.split("=")[-1]) < 11:
#         #     return HttpResponse('Enter correct url.')

#         ydl_opts = {}

#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             meta = ydl.extract_info(
#                 video_url, download=False)
#         video_audio_streams = []
#         for m in meta['formats']:
#             file_size = m['filesize']
#             if file_size is not None:
#                 file_size = f'{round(int(file_size) / 1000000,2)} mb'

#             resolution = 'Audio'
#             if m['height'] is not None:
#                 resolution = f"{m['height']}x{m['width']}"
#             video_audio_streams.append({
#                 'resolution': resolution,
#                 'extension': m['ext'],
#                 'file_size': file_size,
#                 'video_url': m['url']
#             })
#         video_audio_streams = video_audio_streams[::-1]
#         context = {
#             'form': form,
#             'title': meta['title'], 'streams': video_audio_streams,
#             'description': meta['description'], 'likes': meta['like_count'],
#             'dislikes': meta['dislike_count'], 'thumb': meta['thumbnails'][3]['url'],
#             'duration': round(int(meta['duration'])/60, 2), 'views': f'{int(meta["view_count"]):,}'
#         }
#         return render(request, 'home.html', context)
#     return render(request, 'home.html', {'form': form})

# def download_video(request):
#     form = DownloadForm(request.POST or None)
#     if form.is_valid():
#         video_url = form.cleaned_data.get("url")
#         regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
#         print(video_url)
#         if not re.match(regex, video_url):
#             print('nhi howa')
#             return HttpResponse('Enter correct url.')

#         ydl_opts = {'verbose': True}

#         try:
#             with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#               meta = ydl.extract_info(video_url, download=False)
#         except Exception as e:
#             print(f"Error: {e}")


#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             meta = ydl.extract_info(video_url, download=False)

#         video_audio_streams = []
#         for m in meta['formats']:
#             file_size = m['filesize']
#             if file_size is not None:
#                 file_size = f'{round(int(file_size) / 1000000,2)} mb'

#             resolution = 'Audio'
#             if m['height'] is not None:
#                 resolution = f"{m['height']}x{m['width']}"

#             video_audio_streams.append({
#                 'resolution': resolution,
#                 'extension': m['ext'],
#                 'file_size': file_size,
#                 'video_url': m['url']
#             })

#         video_audio_streams = video_audio_streams[::-1]

#         context = {
#             'form': form,
#             'title': meta['title'], 
#             'streams': video_audio_streams,
#             'description': meta['description'], 
#             'likes': meta['like_count'],
#             'dislikes': meta['dislike_count'], 
#             'thumb': meta['thumbnails'][3]['url'],
#             'duration': round(int(meta['duration'])/60, 2), 
#             'views': f'{int(meta["view_count"]):,}'
#         }

#         return render(request, 'home.html', context)

#     return render(request, 'home.html', {'form': form})









# def download_video(request):
#     form = DownloadForm(request.POST or None)
#     if form.is_valid():
#         video_url = form.cleaned_data.get("url")
#         ydl_opts = {}
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info_dict = ydl.extract_info(video_url, download=False)
#         video_streams = []
#         audio_streams = []
#         for stream in info_dict['formats']:
#             stream_info = {
#                 'resolution': stream['height'],
#                 'extension': stream['ext'],
#                 'url': stream['url']
#             }
#             if 'filesize' in stream:
#                 stream_info['file_size'] = stream['filesize']
#             if 'audio' in stream['acodec']:
#                 audio_streams.append(stream_info)
#             else:
#                 video_streams.append(stream_info)
                
#         context = {
#             'form': form,
#             'title': info_dict['title'],
#             'description': info_dict['description'],
#             'duration': info_dict['duration'],
#             'views': info_dict['view_count'],
#             'likes': info_dict['like_count'],
           
#             'thumbnail': info_dict['thumbnail'],
#             'video_streams': video_streams,
#             'audio_streams': audio_streams
#         }
#         return render(request, 'home.html', context)
#     return render(request, 'home.html', {'form': form})

# def download_video(request):
#     form = DownloadForm(request.POST or None)
#     if form.is_valid():
#         video_url = form.cleaned_data.get("url")
#         ydl_opts = {}
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info_dict = ydl.extract_info(video_url, download=False)
#         video_streams = []
#         audio_streams = []
#         for stream in info_dict['formats']:
#             stream_info = {
#                 'resolution': stream['height'],
#                 'extension': stream['ext'],
#                 'url': stream['url']
#             }
#             if 'filesize' in stream:
#                 stream_info['file_size'] = stream['filesize']
#             if 'acodec' in stream and 'vcodec' in stream:
#                 video_streams.append(stream_info)
#             elif 'audio' in stream['acodec']:
#                 audio_streams.append(stream_info)
                
#         context = {
#             'form': form,
#             'title': info_dict['title'],
#             'description': info_dict['description'],
#             'duration': info_dict['duration'],
#             'views': info_dict['view_count'],
#             'likes': info_dict['like_count'],
           
#             'thumbnail': info_dict['thumbnail'],
#             'video_streams': video_streams,
#             'audio_streams': audio_streams
#         }
#         return render(request, 'home.html', context)
#     return render(request, 'home.html', {'form': form})



def download_video(request):
    form = DownloadForm(request.POST or None)
    if form.is_valid():
        video_url = form.cleaned_data.get("url")
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
        video_streams = []
        audio_streams = []
        onlyvideo_streams = []
        for stream in info_dict['formats']:
            stream_info = {
                'resolution': stream['height'],
                'extension': stream['ext'],
                'url': stream['url']
            }
            if 'filesize' in stream:
                stream_info['file_size'] = stream['filesize']
            if stream['vcodec'] == 'none' and stream['acodec'] != 'none':
                audio_streams.append(stream_info)
            elif stream['vcodec'] != 'none' and stream['acodec'] != 'none':
                video_streams.append(stream_info)
            # now to add the function for video only 
            elif stream['vcodec'] != 'none' and stream['acodec'] == 'none':
                onlyvideo_streams.append(stream_info)    

                
        context = {
            'form': form,
            'title': info_dict['title'],
            'description': info_dict['description'],
            'duration': info_dict['duration'],
            'views': info_dict['view_count'],
            'likes': info_dict['like_count'],
           
            'thumbnail': info_dict['thumbnail'],
            'video_streams': video_streams,
            'audio_streams': audio_streams,
            'onlyvideo_streams' : onlyvideo_streams,
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html', {'form': form})

