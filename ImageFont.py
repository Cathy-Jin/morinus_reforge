from PIL.ImageFont import *  # noqa: F401,F403
import PIL.ImageFont as _PILImageFont

# Pillow removed getsize on FreeTypeFont; provide compatibility alias.
if not hasattr(_PILImageFont.FreeTypeFont, 'getsize'):
	def _getsize(self, text, *args, **kwargs):
		l, t, r, b = self.getbbox(text, *args, **kwargs)
		return r - l, b - t
	_PILImageFont.FreeTypeFont.getsize = _getsize

# Guard against float/zero sizes from legacy code.
_orig_truetype = _PILImageFont.truetype
def _truetype(font=None, size=10, index=0, encoding="", layout_engine=None):
	try:
		size = int(size)
	except Exception:
		size = 10
	if size <= 0:
		size = 1
	return _orig_truetype(font, size, index, encoding, layout_engine)
_PILImageFont.truetype = _truetype
