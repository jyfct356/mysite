# views.py

from django.shortcuts import render, redirect
from .forms import VideoForm


def upload_video(request):
    return render(request, 'videosum/upload_video.html')

# views.py

from django.http import JsonResponse

from django.shortcuts import render


def data_analysis(request):
    if request.method == "POST":
        # print("in post")
        # 获取上传的视频文件
        mp4_file = request.FILES.get('videoFile')
        # 获取上传的标注文件
        json_file = request.FILES.get('labelFile')
        print(json_file, mp4_file)
        # 这里可以根据需要对上传的文件进行处理，比如保存到服务器上
        if mp4_file and json_file:
            print("save file")
            # 保存视频文件到本地
            with open('media/videos/video.mp4', 'wb+') as destination:
                for chunk in mp4_file.chunks():
                    destination.write(chunk)

            # 保存 JSON 文件到本地
            with open('media/labels/label.json', 'wb+') as destination:
                for chunk in json_file.chunks():
                    destination.write(chunk)

        # 在这里添加逻辑来获取视频相关的信息和指标数据
        # 这里只是一个示例，你需要根据实际情况获取数据并传递给模板

        video_url = "http://127.0.0.1:8000/media/videos/video.mp4"

        video_info = {
            'duration': 125,  # 视频时长（假设单位为秒）
            'frame_count': 500,  # 视频帧数
            'video_url': video_url
        }

        key_frame_idx = 0
        image_url = "http://127.0.0.1:8000/media/frames/" + str(key_frame_idx) + ".jpg"

        key_frame_info = {
            'image_url': image_url,  # 关键帧图片URL
            'frame_index': 250  # 关键帧在视频中的下标
        }

        metrics = {
            'F_Score': 0.85,
            'Precision': 0.92,
            'Recall': 0.78,
            'Accuracy': 0.88,
            'Overlapping_Area': 0.75
        }
        # print("before return ")
        return render(request, 'videosum/data_analysis.html', {
            'video_info': video_info,
            'key_frame_info': key_frame_info,
            'metrics': metrics
        })







