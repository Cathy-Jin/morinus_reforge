from PIL.Image import *  # noqa: F401,F403
import PIL.Image as _PILImage

# Pillow removed fromstring/tostring; provide compatibility aliases.
if not hasattr(_PILImage.Image, 'fromstring'):
	_PILImage.Image.fromstring = _PILImage.Image.frombytes
if not hasattr(_PILImage.Image, 'tostring'):
	_PILImage.Image.tostring = _PILImage.Image.tobytes

# Ensure size tuples are ints for legacy callers.
def new(mode, size, color=0):
	try:
		size = (int(size[0]), int(size[1]))
	except Exception:
		pass
	return _PILImage.new(mode, size, color)
