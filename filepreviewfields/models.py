# -*- encoding: utf-8 -*-

from django import forms
from django.db.models import FileField
from filepreviewfields.widgets import ImagePreviewWidget, VideoPreviewWidget


class ImagePreviewField(FileField):
    def formfield(self, **kwargs):
        kwargs['widget'] = ImagePreviewWidget
        return super(ImagePreviewField, self).formfield(**kwargs)


class VideoPreviewField(FileField):
    def formfield(self, **kwargs):
        kwargs['widget'] = VideoPreviewWidget
        return super(VideoPreviewField, self).formfield(**kwargs)
