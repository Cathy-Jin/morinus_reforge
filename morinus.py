#!/usr/bin/env python
# coding=utf-8


#Morinus, Astrology program
#Copyright (C) 2008-  Robert Nagy, robert.pluto@gmail.com

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

# Suppress wxPython 4 sizer alignment assertions from legacy layout flags.
os.environ.setdefault('WXSUPPRESS_SIZER_FLAGS_CHECK', '1')

import wx

# wxPython 4 compatibility shims for legacy API names
if not hasattr(wx, 'StandardPaths_Get'):
	def _standard_paths_get():
		return wx.StandardPaths.Get()
	wx.StandardPaths_Get = _standard_paths_get
if not hasattr(wx, 'EmptyBitmap'):
	def _empty_bitmap(w, h, depth=-1):
		return wx.Bitmap(w, h, depth)
	wx.EmptyBitmap = _empty_bitmap
if not hasattr(wx, 'BitmapFromImage'):
	def _bitmap_from_image(img):
		return wx.Bitmap(img)
	wx.BitmapFromImage = _bitmap_from_image
if not hasattr(wx, 'ImageFromBitmap'):
	def _image_from_bitmap(bmp):
		return bmp.ConvertToImage()
	wx.ImageFromBitmap = _image_from_bitmap
if not hasattr(wx, 'SystemSettings_GetColour'):
	def _system_settings_get_colour(idx):
		return wx.SystemSettings.GetColour(idx)
	wx.SystemSettings_GetColour = _system_settings_get_colour
if not hasattr(wx, 'SystemSettings_GetFont'):
	def _system_settings_get_font(idx):
		return wx.SystemSettings.GetFont(idx)
	wx.SystemSettings_GetFont = _system_settings_get_font
if not hasattr(wx, 'NamedColour'):
	def _named_colour(name):
		return wx.Colour(name)
	wx.NamedColour = _named_colour
if not hasattr(wx, '_morinus_flexgrid_shim'):
	_orig_flex_grid_sizer = wx.FlexGridSizer
	def _flex_grid_sizer(*args, **kwargs):
		if len(args) == 2 and all(isinstance(a, int) for a in args):
			return _orig_flex_grid_sizer(args[0], args[1], 0, 0)
		return _orig_flex_grid_sizer(*args, **kwargs)
	wx.FlexGridSizer = _flex_grid_sizer
	wx._morinus_flexgrid_shim = True
if not hasattr(wx.BufferedDC, 'BeginDrawing'):
	def _begin_drawing(self):
		return None
	def _end_drawing(self):
		return None
	wx.BufferedDC.BeginDrawing = _begin_drawing
	wx.BufferedDC.EndDrawing = _end_drawing
if not hasattr(wx, '_morinus_dc_int_shim'):
	def _wrap_dc_int_method(method_name):
		orig = getattr(wx.DC, method_name, None)
		if orig is None:
			return
		def _wrapped(self, *args, **kwargs):
			if method_name == 'DrawLine' and len(args) >= 4 and all(isinstance(a, (int, float)) for a in args[:4]):
				args = (int(args[0]), int(args[1]), int(args[2]), int(args[3])) + args[4:]
			elif method_name == 'DrawCircle' and len(args) >= 3 and all(isinstance(a, (int, float)) for a in args[:3]):
				args = (int(args[0]), int(args[1]), int(args[2])) + args[3:]
			return orig(self, *args, **kwargs)
		setattr(wx.DC, method_name, _wrapped)
	for _name in ('DrawCircle', 'DrawLine'):
		_wrap_dc_int_method(_name)
	wx._morinus_dc_int_shim = True
if not hasattr(wx, '_morinus_line_list_shim'):
	_orig_draw_line_list = wx.DC.DrawLineList
	def _draw_line_list(self, lines, pens=None):
		clean = []
		for ln in lines:
			if len(ln) >= 4:
				clean.append((int(ln[0]), int(ln[1]), int(ln[2]), int(ln[3])))
		return _orig_draw_line_list(self, clean, pens)
	wx.DC.DrawLineList = _draw_line_list
	wx._morinus_line_list_shim = True
if not hasattr(wx, 'PreDialog'):
	class _PreDialog:
		def __init__(self):
			self._created_args = None
			self._extra_style = 0

		def SetExtraStyle(self, style):
			self._extra_style = style

		def Create(self, parent, id=wx.ID_ANY, title='', pos=wx.DefaultPosition,
		           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE, name=wx.DialogNameStr):
			self._created_args = (parent, id, title, pos, size, style, name)
			return True

	wx.PreDialog = _PreDialog

def _post_create(self, pre):
	if hasattr(pre, '_created_args') and pre._created_args:
		parent, id, title, pos, size, style, name = pre._created_args
		wx.Dialog.__init__(self, parent, id, title, pos, size, style, name)
		if getattr(pre, '_extra_style', 0):
			self.SetExtraStyle(pre._extra_style)
		return True
	return False
wx.Dialog.PostCreate = _post_create

import options
import mtexts
import morin
import infos
import mrbaseapp


class Morinus(mrbaseapp.MrApp):
	def OnInit(self):
		super(Morinus, self).OnInit()
		try:
			progPath = os.path.dirname(sys.argv[0])
			os.chdir(progPath)
		except:
			pass

		self.SetAppName(infos.MYAPPNAME)
		# wxPython 4+ removed SetDefaultPyEncoding
		if hasattr(wx, 'SetDefaultPyEncoding'):
			wx.SetDefaultPyEncoding('utf-8')
		opts = options.Options()
		mtexts.setLang(opts.langid)

		frame = morin.MFrame(None, -1, mtexts.txts['Morinus'], opts)
		self.SetTopWindow(frame)
		frame.Show(True)

		return True


if __name__ == '__main__':
	app = Morinus(0)
	app.MainLoop()
