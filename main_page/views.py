from django.shortcuts import render
from django.http import HttpResponse
import glob
import os


def project_files(dir: str) -> list:
    files = []
    folders = []
    for file in glob.glob(f'{dir}/*', recursive=True):
        if os.path.isdir(file):
            folders.append(file.strip(".\\"))
        else:
            files.append(file.strip(".\\"))
    return files, folders


def previous_page(dir) -> str:
    if dir == ".":
        return "main_page"
    path = dir.split("\\")
    if len(path) > 1:
        path.pop()
        file_path = "\\".join(path)
        return file_path
    else:
        return "."


def greeting_view(request):
    return render(request, 'main_page/greeting.html')


def biography_view(request):
    return render(request, 'main_page/biography.html')


def project_view(request):
    file_path = request.GET["dir"]
    files, folders = project_files(file_path)
    previous_path = previous_page(file_path)
    content = {"files": files,
            "folders": folders,
            "previous_page": previous_path}
    return render(request, 'main_page/project.html', content)
