from PIL.ImageDraw import *  # noqa: F401,F403
import PIL.ImageDraw as _PILImageDraw

# Pillow removed textsize; provide compatibility using textbbox.
if not hasattr(_PILImageDraw.ImageDraw, 'textsize'):
	def _textsize(self, text, font=None, *args, **kwargs):
		l, t, r, b = self.textbbox((0, 0), text, font=font)
		return r - l, b - t
	_PILImageDraw.ImageDraw.textsize = _textsize
