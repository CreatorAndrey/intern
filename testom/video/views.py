from django.http import HttpResponse, HttpResponseNotFound
from make_video import make_video_from_text
from video.models import Video2
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'index.html')

def index(request):
    text = request.GET.get("text")
    if text is None:
        text="Введите текст"

    time_video = request.GET.get("time")
    if time_video is None:
        time_video = 3
    else:
        time_video = int(time_video)

    fps = request.GET.get("fps")
    if fps is None:
        fps = 30
    else:
        fps = int(fps)

    red = request.GET.get("r")
    if red is None:
        red = 100
    else:
        red = int(red)

    green = request.GET.get("g")
    if green is None:
        green = 100
    else:
        green = int(green)

    blue = request.GET.get("b")
    if blue is None:
        blue = 100
    else:
        blue = int(blue)

    Video2(req_text=text,
           time_video=time_video,
           fps = fps,
           red=red,
           green=green,
           blue=blue).save()
    make_video_from_text(text, time_video, fps, red, green, blue)
    file_location = './media/running_text.mp4'
    try:
        with open(file_location, 'rb') as f:
            file_data = f.read()

        # sending response
        response = HttpResponse(file_data, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename="running_text.mp4"'

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')
    return response