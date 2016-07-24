# -*- encoding: utf-8 -*-

from django.conf import settings
from django.forms.widgets import ClearableFileInput, FileInput


class FilePreviewWidget(ClearableFileInput):
    def get_preview_html(self, value):
        pass

    def render(self, name, value, attrs=None):
        preview_html = self.get_preview_html(value)
        video = '<video src="%s%s" controls></video>' % (settings.MEDIA_URL, value) if value else ''
        clear_class = ' hidden' if not hasattr(value, 'file') else ''
        output = '''
            <div class="filepreviewfield">
                %(preview_html)s
                <div class="buttons">
                    <input type="button" value="Choose file" class="default choose">
                    <input type="button" value="Clear" class="default clear%(clear_class)s">
                </div>
                <span></span>
                <input id="id_%(name)s" name="video" type="file" class="hidden" />
                <input id="%(name)s-clear_id" name="%(name)s-clear" type="checkbox" class="hidden" />
            </div>
        ''' % {'name': name, 'preview_html': preview_html, 'clear_class': clear_class}
        return output

    class Media:
        css = {'all': ('filepreviewfields/css/widget.css', )}
        js = ('filepreviewfields/js/widget.js', )


class ImagePreviewWidget(FilePreviewWidget):
    def get_preview_html(self, value):
        return '<img src="%s%s" />' % (settings.MEDIA_URL, value) if value else ''


class VideoPreviewWidget(FilePreviewWidget):
    def get_preview_html(self, value):
        return '<video src="%s%s" controls></video>' % (settings.MEDIA_URL, value) if value else ''
