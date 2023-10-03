from django.shortcuts import render, redirect
from .forms import VideoForm
from pytube import YouTube
from .models import Video
from django.http import JsonResponse
from django.middleware import csrf
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VideoSerializer

def get_csrf_token(request):
    csrf_token = csrf.get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

@api_view(['POST','GET'])  # Adjust the HTTP method to POST
def download_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            yt = YouTube(video.url)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=video.download_location)
            video.save()
            return JsonResponse({'message': 'Download completed successfully'})
        else:
            # Return a failure JSON response with form errors
            return JsonResponse({'message': 'Download failed', 'errors': form.errors})
    else:
        form = VideoForm()
        return render(request, 'downloader/download.html', {'form': form})

@api_view(['GET'])
def video_list(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)
