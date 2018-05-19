from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from qiniuyun.backend import QiniuPush as QP
from .models import ImageAtQiniu


class UploadForm(forms.Form):
    name = forms.CharField(required=False)
    img = forms.FileField()


def upload(request):
    if request.method == 'POST':
        uf = UploadForm(request.POST, request.FILES)
        if uf.is_valid():
            name = uf.cleaned_data['name']
            img = uf.cleaned_data['img']
            if not name or not name.strip():
                name = img.name
            u = ImageAtQiniu.objects.create(fullname=QP.put_data(name, img))
            request.session['img_fullname'] = u.fullname
            return HttpResponseRedirect('/upload/done/')
    else:
        uf = UploadForm()
        uf.img = QP.private_download_url(QP.get_url('default.jpg'))
    return render(request, 'qiniuyun/upload.html', {'uf': uf})


def upload_result(request):
    name = request.session['img_fullname']
    img_url = QP.private_download_url(name)
    return render(request, 'qiniuyun/upload_result.html', {
        'img_fullname': name, 'img_url': img_url,
    })


def show_imgs(request):
    imglist = [
        {'name': i.fullname, 'url': QP.private_download_url(i.fullname)}
        for i in ImageAtQiniu.objects.all()
    ]
    return render(request, 'qiniuyun/show_imgs.html', {'imgList': imglist})
