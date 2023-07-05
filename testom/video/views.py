from django.http import HttpResponse, HttpResponseNotFound
from make_video import make_video_from_text
from video.models import Video2

# Create your views here.
def index(request):
    text = request.GET.get("text")
    time_video = int(request.GET.get("time"))
    fps = int(request.GET.get("fps"))
    red = int(request.GET.get("r"))
    green = int(request.GET.get("g"))
    blue = int(request.GET.get("b"))

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