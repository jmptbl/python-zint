# Copyright (c) 2019-2023, Aragon Gouveia
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of python-zint nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from ctypes import POINTER, Structure, c_char, c_char_p, c_float, c_int, c_ubyte, c_uint, cast, cdll, create_string_buffer
from ._version import __version__

try:
	_lib = cdll.LoadLibrary('libzint.so')
except:
	try:
		_lib = cdll.LoadLibrary('libzint.dylib')
	except:
		_lib = cdll.LoadLibrary('libzint.dll')

ZBarcode_ValidID = _lib.ZBarcode_ValidID
ZBarcode_ValidID.restype = c_int
ZBarcode_ValidID.argtypes = [c_int]

try:
	ZBarcode_Version = _lib.ZBarcode_Version
	ZBarcode_Version.restype = c_int
	ZBarcode_Version.argtypes = []
except:
	def ZBarcode_Version ():
		# if BARCODE_DOTCODE is valid, version is 2.6.0
		if ZBarcode_ValidID(115) == 1:
			return 20600
		return 0

__libzint_ver = ZBarcode_Version()

if __libzint_ver < 20600:
	raise RuntimeError('libzint >=2.6.0 required')

BARCODE_CODE11 = 1
BARCODE_C25MATRIX = 2
BARCODE_C25INTER = 3
BARCODE_C25IATA = 4
BARCODE_C25LOGIC = 6
BARCODE_C25IND = 7
BARCODE_CODE39 = 8
BARCODE_EXCODE39 = 9
BARCODE_EANX = 13
BARCODE_EANX_CHK = 14
BARCODE_EAN128 = 16
BARCODE_CODABAR = 18
BARCODE_CODE128 = 20
BARCODE_DPLEIT = 21
BARCODE_DPIDENT = 22
BARCODE_CODE16K = 23
BARCODE_CODE49 = 24
BARCODE_CODE93 = 25
BARCODE_FLAT = 28
BARCODE_RSS14 = 29
BARCODE_RSS_LTD = 30
BARCODE_RSS_EXP = 31
BARCODE_TELEPEN = 32
BARCODE_UPCA = 34
BARCODE_UPCA_CHK = 35
BARCODE_UPCE = 37
BARCODE_UPCE_CHK = 38
BARCODE_POSTNET = 40
BARCODE_MSI_PLESSEY = 47
BARCODE_FIM = 49
BARCODE_LOGMARS = 50
BARCODE_PHARMA = 51
BARCODE_PZN = 52
BARCODE_PHARMA_TWO = 53
if __libzint_ver >= 21101:
	BARCODE_CEPNET = 54
BARCODE_PDF417 = 55
BARCODE_PDF417TRUNC = 56
BARCODE_MAXICODE = 57
BARCODE_QRCODE = 58
BARCODE_CODE128B = 60
if __libzint_ver >= 21200:
	BARCODE_CODE128AB = 60
BARCODE_AUSPOST = 63
BARCODE_AUSREPLY = 66
BARCODE_AUSROUTE = 67
BARCODE_AUSREDIRECT = 68
BARCODE_ISBNX = 69
BARCODE_RM4SCC = 70
BARCODE_DATAMATRIX = 71
BARCODE_EAN14 = 72
if __libzint_ver >= 20603:
	BARCODE_VIN = 73
BARCODE_CODABLOCKF = 74
BARCODE_NVE18 = 75
BARCODE_JAPANPOST = 76
BARCODE_KOREAPOST = 77
BARCODE_RSS14STACK = 79
BARCODE_RSS14STACK_OMNI = 80
BARCODE_RSS_EXPSTACK = 81
BARCODE_PLANET = 82
BARCODE_MICROPDF417 = 84
BARCODE_ONECODE = 85
BARCODE_PLESSEY = 86
BARCODE_TELEPEN_NUM = 87
BARCODE_ITF14 = 89
BARCODE_KIX = 90
BARCODE_AZTEC = 92
BARCODE_DAFT = 93
if __libzint_ver >= 20901:
	BARCODE_DPD = 96
BARCODE_MICROQR = 97
BARCODE_HIBC_128 = 98
BARCODE_HIBC_39 = 99
BARCODE_HIBC_DM = 102
BARCODE_HIBC_QR = 104
BARCODE_HIBC_PDF = 106
BARCODE_HIBC_MICPDF = 108
BARCODE_HIBC_BLOCKF = 110
BARCODE_HIBC_AZTEC = 112
BARCODE_DOTCODE = 115
BARCODE_HANXIN = 116
if __libzint_ver >= 21200:
	BARCODE_MAILMARK_2D = 119
	BARCODE_UPU_S10 = 120
	BARCODE_MAILMARK_4S = 121
if __libzint_ver >= 20603:
	BARCODE_MAILMARK = 121
BARCODE_AZRUNE = 128
BARCODE_CODE32 = 129
BARCODE_EANX_CC = 130
BARCODE_EAN128_CC = 131
BARCODE_RSS14_CC = 132
BARCODE_RSS_LTD_CC = 133
BARCODE_RSS_EXP_CC = 134
BARCODE_UPCA_CC = 135
BARCODE_UPCE_CC = 136
BARCODE_RSS14STACK_CC = 137
BARCODE_RSS14_OMNI_CC = 138
BARCODE_RSS_EXPSTACK_CC = 139
BARCODE_CHANNEL = 140
BARCODE_CODEONE = 141
BARCODE_GRIDMATRIX = 142
if __libzint_ver >= 20601:
	BARCODE_UPNQR = 143
if __libzint_ver >= 20604:
	BARCODE_ULTRA = 144
if __libzint_ver >= 20700:
	BARCODE_RMQR = 145
if __libzint_ver >= 21101:
	BARCODE_BC412 = 146
if __libzint_ver >= 20900:
	BARCODE_C25STANDARD = 2
	BARCODE_GS1_128 = 16
	BARCODE_DBAR_OMN = 29
	BARCODE_DBAR_LTD = 30
	BARCODE_DBAR_EXP = 31
	BARCODE_PDF417COMP = 56
	BARCODE_DBAR_STK = 79
	BARCODE_DBAR_OMNSTK = 80
	BARCODE_DBAR_EXPSTK = 81
	BARCODE_USPS_IMAIL = 85
	BARCODE_GS1_128_CC = 131
	BARCODE_DBAR_OMN_CC = 132
	BARCODE_DBAR_LTD_CC = 133
	BARCODE_DBAR_EXP_CC = 134
	BARCODE_DBAR_STK_CC = 137
	BARCODE_DBAR_OMNSTK_CC = 138
	BARCODE_DBAR_EXPSTK_CC = 139
if __libzint_ver >= 21100:
	BARCODE_LAST = 145
elif __libzint_ver >= 21101:
	BARCODE_LAST = 146

if __libzint_ver >= 21200:
	BARCODE_BIND_TOP = 0x0001
else:
	BARCODE_NO_ASCII = 0x0001
BARCODE_BIND = 0x0002
BARCODE_BOX = 0x0004
BARCODE_STDOUT = 0x0008
READER_INIT = 0x0010
SMALL_TEXT = 0x0020
BOLD_TEXT = 0x0040
CMYK_COLOUR = 0x0080
BARCODE_DOTTY_MODE = 0x0100
if __libzint_ver >= 20604:
	GS1_GS_SEPARATOR = 0x0200
if __libzint_ver >= 21100:
	OUT_BUFFER_INTERMEDIATE = 0x0400
	BARCODE_QUIET_ZONES = 0x0800
	BARCODE_NO_QUIET_ZONES = 0x1000
	COMPLIANT_HEIGHT = 0x2000
if __libzint_ver >= 21300:
	EANUPC_GUARD_WHITESPACE = 0x4000
	EMBED_VECTOR_FONT = 0x8000

DATA_MODE = 0
UNICODE_MODE = 1
GS1_MODE = 2
if __libzint_ver < 20604:
	KANJI_MODE = 3
	SJIS_MODE = 4
if __libzint_ver >= 20602:
	ESCAPE_MODE = 0x0008
if __libzint_ver >= 21000:
	GS1PARENS_MODE = 0x0010
	GS1NOCHECK_MODE = 0x0020
if __libzint_ver >= 21100:
	HEIGHTPERROW_MODE = 0x0040
	FAST_MODE = 0x0080
if __libzint_ver >= 21300:
	EXTRA_ESCAPE_MODE = 0x0100

DM_SQUARE = 100
DM_DMRE = 101
if __libzint_ver >= 21300:
	DM_ISO_144 = 128

if __libzint_ver >= 20800:
	ZINT_FULL_MULTIBYTE = 200
	ULTRA_COMPRESSION = 128

if __libzint_ver >= 21300:
	ZINT_WARN_HRT_TRUNCATED = 1
ZINT_WARN_INVALID_OPTION = 2
ZINT_WARN_USES_ECI = 3
if __libzint_ver >= 21000:
	ZINT_WARN_NONCOMPLIANT = 4
	ZINT_ERROR = 5
ZINT_ERROR_TOO_LONG = 5
ZINT_ERROR_INVALID_DATA = 6
ZINT_ERROR_INVALID_CHECK = 7
ZINT_ERROR_INVALID_OPTION = 8
ZINT_ERROR_ENCODING_PROBLEM = 9
ZINT_ERROR_FILE_ACCESS = 10
ZINT_ERROR_MEMORY = 11
if __libzint_ver >= 21000:
	ZINT_ERROR_FILE_WRITE = 12
	ZINT_ERROR_USES_ECI = 13
	ZINT_ERROR_NONCOMPLIANT = 14
if __libzint_ver >= 21300:
	ZINT_ERROR_HRT_TRUNCATED = 15
if __libzint_ver >= 21000:
	WARN_DEFAULT = 0
	WARN_FAIL_ALL = 2
	ZINT_DEBUG_PRINT = 0x0001
	ZINT_DEBUG_TEST = 0x0002
	ZINT_CAP_HRT = 0x0001
	ZINT_CAP_STACKABLE = 0x0002
if __libzint_ver >= 21300:
	ZINT_CAP_EANUPC = 0x0004
if __libzint_ver >= 21000:
	ZINT_CAP_EXTENDABLE = 0x0004
	ZINT_CAP_COMPOSITE = 0x0008
	ZINT_CAP_ECI = 0x0010
	ZINT_CAP_GS1 = 0x0020
	ZINT_CAP_DOTTY = 0x0040
	ZINT_CAP_FIXED_RATIO = 0x0100
	ZINT_CAP_READER_INIT = 0x0200
	ZINT_CAP_FULL_MULTIBYTE = 0x0400
	ZINT_CAP_MASK = 0x0800
	ZINT_MAX_DATA_LEN = 17400
if __libzint_ver >= 21100:
	ZINT_CAP_QUIET_ZONES = 0x0080
	ZINT_CAP_STRUCTAPP = 0x1000
	ZINT_CAP_COMPLIANT_HEIGHT = 0x2000
	ZINT_MAX_SEG_COUNT = 256

OUT_BUFFER = 0
if __libzint_ver >= 20604:
	OUT_SVG_FILE = 10
	OUT_EPS_FILE = 20
	OUT_EMF_FILE = 30
OUT_PNG_FILE = 100
OUT_BMP_FILE = 120
OUT_GIF_FILE = 140
OUT_PCX_FILE = 160
OUT_JPG_FILE = 180
OUT_TIF_FILE = 200

if __libzint_ver >= 21300:
	ZINT_COLOUR_SIZE = 16
	ZINT_TEXT_SIZE = 200
else:
	ZINT_COLOUR_SIZE = 10
	ZINT_TEXT_SIZE = 128
ZINT_PRIMARY_SIZE = 128
ZINT_ROWS_MAX = 200
if __libzint_ver >= 21100:
	ZINT_COLS_MAX = 144
else:
	ZINT_COLS_MAX = 143
ZINT_ERR_SIZE = 100

FILENAME_MAX = 256

def instr (text):
	l = len(text) + 1
	return (c_ubyte * l).from_buffer_copy(create_string_buffer(text))

def infile (path):
	return create_string_buffer(path)

def bitmapbuf (z):
	if not type(z) is POINTER(zint_symbol):
		raise TypeError(
			'Expected %s not %s' % (
				str(type(POINTER(zint_symbol))),
				str(type(z))
			)
		)
	blen = z.contents.bitmap_width * z.contents.bitmap_height * 3
	return cast(z.contents.bitmap, POINTER(c_char * blen))[0]

if __libzint_ver >= 20604:
	class zint_vector_rect(Structure):
		pass
	zint_vector_rect._fields_ = [
		('x', c_float),
		('y', c_float),
		('height', c_float),
		('width', c_float),
		('colour', c_int),
		('next', POINTER(zint_vector_rect))
	]
	
	class zint_vector_hexagon(Structure):
		pass
	fields = [
		('x', c_float),
		('y', c_float),
		('diameter', c_float)
	]
	if __libzint_ver >= 21000:
		fields.append(('rotation', c_int))
	fields.append(('next', POINTER(zint_vector_hexagon)))
	zint_vector_hexagon._fields_ = fields
	
	class zint_vector_string(Structure):
		pass
	fields = [
		('x', c_float),
		('y', c_float),
		('fsize', c_float),
		('width', c_float),
		('length', c_int)
	]
	if __libzint_ver >= 21000:
		fields.extend([
			('rotation', c_int),
			('halign', c_int)
		])
	fields.extend([
		('text', POINTER(c_ubyte)),
		('next', POINTER(zint_vector_string))
	])
	zint_vector_string._fields_ = fields
	
	class zint_vector_circle(Structure):
		pass
	fields = [
		('x', c_float),
		('y', c_float),
		('diameter', c_float)
	]
	if __libzint_ver >= 21100:
		fields.append(('width', c_float))
	fields.extend([
		('colour', c_int),
		('next', POINTER(zint_vector_circle))
	])
	zint_vector_circle._fields_ = fields
	
	class zint_vector(Structure):
		_fields_ = [
			('width', c_float),
			('height', c_float),
			('rectangles', POINTER(zint_vector_rect)),
			('hexagons', POINTER(zint_vector_hexagon)),
			('strings', POINTER(zint_vector_string)),
			('circles', POINTER(zint_vector_circle))
		]

if __libzint_ver <= 20900:
	class zint_render_line(Structure):
		_fields_ = [
			('x', c_float),
			('y', c_float),
			('length', c_float),
			('width', c_float),
			('next', POINTER(zint_render_line))
		]

	class zint_render_string(Structure):
		_fields_ = [
			('x', c_float),
			('y', c_float),
			('length', c_float),
			('width', c_int),
			('text', POINTER(c_ubyte)),
			('next', POINTER(zint_render_string))
		]

	class zint_render_ring(Structure):
		_fields_ = [
			('x', c_float),
			('y', c_float),
			('radius', c_float),
			('line_width', c_float),
			('next', POINTER(zint_render_ring))
		]

	class zint_render_hexagon(Structure):
		pass
	fields = [
		('x', c_float),
		('y', c_float)
	]
	if __libzint_ver >= 20602:
		fields.append(('height', c_float))
	fields.append(('next', POINTER(zint_render_hexagon)))
	zint_render_hexagon._fields_ = fields

	class zint_render(Structure):
		_fields_ = [
			('width', c_float),
			('height', c_float),
			('lines', POINTER(zint_render_line)),
			('strings', POINTER(zint_render_string)),
			('rings', POINTER(zint_render_ring)),
			('hexagons', POINTER(zint_render_hexagon))
		]

if __libzint_ver >= 21100:
	class zint_structapp(Structure):
		_fields_ = [
			('index', c_int),
			('count', c_int),
			('id', (c_char * 32))
		]

class zint_symbol(Structure):
	pass
fields = [('symbology', c_int)]
if __libzint_ver >= 21000:
	fields.append(('height', c_float))
else:
	fields.append(('height', c_int))
if __libzint_ver >= 21100:
	fields.append(('scale', c_float))
fields.append(('whitespace_width', c_int))
if __libzint_ver >= 21000:
	fields.append(('whitespace_height', c_int))
fields.extend([
	('border_width', c_int),
	('output_options', c_int),
	('fgcolour', (c_char * ZINT_COLOUR_SIZE))
])
if __libzint_ver >= 21000 or __libzint_ver < 20901:
	fields.append(('bgcolour', (c_char * ZINT_COLOUR_SIZE)))
else: # __libzint_ver == 20901:
	fields.append(('fgcolor', POINTER(c_char)))
	fields.append(('bgcolour', (c_char * ZINT_COLOUR_SIZE)))
	fields.append(('bgcolor', POINTER(c_char)))
if __libzint_ver >= 21000:
	fields.append(('fgcolor', POINTER(c_char)))
	fields.append(('bgcolor', POINTER(c_char)))
fields.append(('outfile', (c_char * FILENAME_MAX)))
if __libzint_ver < 21100:
	fields.append(('scale', c_float))
if __libzint_ver >= 21100:
	fields.append(('primary', (c_char * ZINT_PRIMARY_SIZE)))
fields.extend([
	('option_1', c_int),
	('option_2', c_int),
	('option_3', c_int),
	('show_hrt', c_int)
])
if 21300 > __libzint_ver >= 20603:
	fields.append(('fontsize', c_int))
fields.extend([
	('input_mode', c_int),
	('eci', c_int)
])
if __libzint_ver >= 21200:
	fields.append(('dpmm', c_float))
if __libzint_ver >= 21100:
	fields.append(('dot_size', c_float))
if __libzint_ver >= 21300:
	fields.append(('text_gap', c_float))
if __libzint_ver >= 21100:
	fields.extend([
		('guard_descent', c_float),
		('structapp', zint_structapp),
		('warn_level', c_int),
		('debug', c_int)
	])
fields.extend([
	('text', (c_ubyte * ZINT_TEXT_SIZE)),
	('rows', c_int),
	('width', c_int)
])
if __libzint_ver < 21100:
	fields.append(('primary', (c_char * ZINT_PRIMARY_SIZE)))
fields.append(('encoded_data', ((c_ubyte * ZINT_COLS_MAX) * ZINT_ROWS_MAX)))
if __libzint_ver >= 21000:
	fields.append(('row_height', (c_float * ZINT_ROWS_MAX)))
else:
	fields.append(('row_height', (c_int * ZINT_ROWS_MAX)))
fields.append(('errtxt', (c_char * ZINT_ERR_SIZE)))
if __libzint_ver >= 20800:
	fields.append(('bitmap', POINTER(c_ubyte)))
else:
	fields.append(('bitmap', POINTER(c_char)))
fields.extend([
	('bitmap_width', c_int),
	('bitmap_height', c_int)
])
if __libzint_ver >= 20901:
	fields.append(('alphamap', POINTER(c_ubyte)))
if __libzint_ver < 21300:
	fields.append(('bitmap_byte_length', c_uint))
if __libzint_ver < 21100:
	fields.append(('dot_size', c_float))
if __libzint_ver >= 20604:
	fields.append(('vector', POINTER(zint_vector)))
if __libzint_ver <= 20900:
	fields.append(('rendered', POINTER(zint_render)))
if __libzint_ver < 21100:
	fields.append(('debug', c_int))
	if __libzint_ver >= 21000:
		fields.append(('warn_level', c_int))
zint_symbol._fields_ = fields

if __libzint_ver >= 21100:
	class zint_seg(Structure):
		_fields_ = [
			('source', POINTER(c_ubyte)),
			('length', c_int),
			('eci', c_int)
		]

ZBarcode_Create = _lib.ZBarcode_Create
ZBarcode_Create.restype = POINTER(zint_symbol)
ZBarcode_Create.argtypes = []

if __libzint_ver >= 21300:
	ZBarcode_Reset = _lib.ZBarcode_Reset
	ZBarcode_Reset.restype = None
	ZBarcode_Reset.argtypes = [POINTER(zint_symbol)]

ZBarcode_Delete = _lib.ZBarcode_Delete
ZBarcode_Delete.restype = None
ZBarcode_Delete.argtypes = [POINTER(zint_symbol)]

ZBarcode_Encode = _lib.ZBarcode_Encode
ZBarcode_Encode.restype = c_int
ZBarcode_Encode.argtypes = [POINTER(zint_symbol), POINTER(c_ubyte), c_int]

ZBarcode_Encode_File = _lib.ZBarcode_Encode_File
ZBarcode_Encode_File.restype = c_int
ZBarcode_Encode_File.argtypes = [POINTER(zint_symbol), c_char_p]

ZBarcode_Print = _lib.ZBarcode_Print
ZBarcode_Print.restype = c_int
ZBarcode_Print.argtypes = [POINTER(zint_symbol), c_int]

ZBarcode_Encode_and_Print = _lib.ZBarcode_Encode_and_Print
ZBarcode_Encode_and_Print.restype = c_int
ZBarcode_Encode_and_Print.argtypes = [POINTER(zint_symbol), POINTER(c_ubyte), c_int, c_int]

ZBarcode_Encode_File_and_Print = _lib.ZBarcode_Encode_File_and_Print
ZBarcode_Encode_File_and_Print.restype = c_int
ZBarcode_Encode_File_and_Print.argtypes = [POINTER(zint_symbol), c_char_p, c_int]

ZBarcode_Buffer = _lib.ZBarcode_Buffer
ZBarcode_Buffer.restype = c_int
ZBarcode_Buffer.argtypes = [POINTER(zint_symbol), c_int]

ZBarcode_Encode_and_Buffer = _lib.ZBarcode_Encode_and_Buffer
ZBarcode_Encode_and_Buffer.restype = c_int
ZBarcode_Encode_and_Buffer.argtypes = [POINTER(zint_symbol), POINTER(c_ubyte), c_int, c_int]

ZBarcode_Encode_File_and_Buffer = _lib.ZBarcode_Encode_File_and_Buffer
ZBarcode_Encode_File_and_Buffer.restype = c_int
ZBarcode_Encode_File_and_Buffer.argtypes = [POINTER(zint_symbol), c_char_p, c_int]

if __libzint_ver >= 20604:
	ZBarcode_Buffer_Vector = _lib.ZBarcode_Buffer_Vector
	ZBarcode_Buffer_Vector.restype = c_int
	ZBarcode_Buffer_Vector.argtypes = [POINTER(zint_symbol), c_int]
	
	ZBarcode_Encode_and_Buffer_Vector = _lib.ZBarcode_Encode_and_Buffer_Vector
	ZBarcode_Encode_and_Buffer_Vector.restype = c_int
	ZBarcode_Encode_and_Buffer_Vector.argtypes = [POINTER(zint_symbol), POINTER(c_ubyte), c_int, c_int]

	ZBarcode_Encode_File_and_Buffer_Vector = _lib.ZBarcode_Encode_File_and_Buffer_Vector
	ZBarcode_Encode_File_and_Buffer_Vector.restype = c_int
	ZBarcode_Encode_File_and_Buffer_Vector.argtypes = [POINTER(zint_symbol), c_char_p, c_int]

if __libzint_ver >= 21000:
	ZBarcode_Cap = _lib.ZBarcode_Cap
	ZBarcode_Cap.restype = c_uint
	ZBarcode_Cap.argtypes = [c_int, c_uint]

if __libzint_ver >= 21100:
	ZBarcode_Encode_Segs = _lib.ZBarcode_Encode_Segs
	ZBarcode_Encode_Segs.restype = c_int
	ZBarcode_Encode_Segs.argtypes = [POINTER(zint_symbol), POINTER(zint_seg), c_int]

	ZBarcode_Encode_Segs_and_Print = _lib.ZBarcode_Encode_Segs_and_Print
	ZBarcode_Encode_Segs_and_Print.restype = c_int
	ZBarcode_Encode_Segs_and_Print.argtypes = [POINTER(zint_symbol), POINTER(zint_seg), c_int, c_int]

	ZBarcode_Encode_Segs_and_Buffer = _lib.ZBarcode_Encode_Segs_and_Buffer
	ZBarcode_Encode_Segs_and_Buffer.restype = c_int
	ZBarcode_Encode_Segs_and_Buffer.argtypes = [POINTER(zint_symbol), POINTER(zint_seg), c_int, c_int]

	ZBarcode_Encode_Segs_and_Buffer_Vector = _lib.ZBarcode_Encode_Segs_and_Buffer_Vector
	ZBarcode_Encode_Segs_and_Buffer_Vector.restype = c_int
	ZBarcode_Encode_Segs_and_Buffer_Vector.argtypes = [POINTER(zint_symbol), POINTER(zint_seg), c_int, c_int]

	ZBarcode_BarcodeName = _lib.ZBarcode_BarcodeName
	ZBarcode_BarcodeName.restype = c_int
	ZBarcode_BarcodeName.argtypes = [c_int, c_char * 32]

if __libzint_ver >= 21200:
	ZBarcode_Default_Xdim = _lib.ZBarcode_Default_Xdim
	ZBarcode_Default_Xdim.restype = c_float
	ZBarcode_Default_Xdim.argtypes = [c_int]

	ZBarcode_Scale_From_XdimDp = _lib.ZBarcode_Scale_From_XdimDp
	ZBarcode_Scale_From_XdimDp.restype = c_float
	ZBarcode_Scale_From_XdimDp.argtypes = [c_int, c_float, c_float, POINTER(c_char)]

	ZBarcode_XdimDp_From_Scale = _lib.ZBarcode_XdimDp_From_Scale
	ZBarcode_XdimDp_From_Scale.restype = c_float
	ZBarcode_XdimDp_From_Scale.argtypes = [c_int, c_float, c_float, POINTER(c_char)]

	ZBarcode_NoPng = _lib.ZBarcode_NoPng
	ZBarcode_NoPng.restype = c_int
	ZBarcode_NoPng.argtypes = []

__all__ = [
	'__version__', 'instr', 'infile', 'bitmapbuf',
	'ZBarcode_Version', 'ZBarcode_Create', 'ZBarcode_Delete',
	'ZBarcode_Encode', 'ZBarcode_Encode_File', 'ZBarcode_Print',
	'ZBarcode_Encode_and_Print', 'ZBarcode_Encode_File_and_Print',
	'ZBarcode_Buffer', 'ZBarcode_Encode_and_Buffer',
	'ZBarcode_Encode_File_and_Buffer', 'ZBarcode_ValidID'
]
if __libzint_ver >= 20604:
	__all__.extend([
		'ZBarcode_Buffer_Vector', 'ZBarcode_Encode_and_Buffer_Vector',
		'ZBarcode_Encode_File_and_Buffer_Vector',
		'zint_vector_rect', 'zint_vector_hexagon', 'zint_vector_string',
		'zint_vector_circle', 'zint_vector'
	])
if __libzint_ver >= 21100:
	__all__.extend([
		'zint_structapp', 'zint_seg', 'ZBarcode_Encode_Segs',
		'ZBarcode_Encode_Segs_and_Print',
		'ZBarcode_Encode_Segs_and_Buffer',
		'ZBarcode_Encode_Segs_and_Buffer_Vector',
		'ZBarcode_BarcodeName', 'BARCODE_QUIET_ZONES',
		'BARCODE_NO_QUIET_ZONES', 'COMPLIANT_HEIGHT',
		'HEIGHTPERROW_MODE', 'FAST_MODE', 'ZINT_CAP_QUIET_ZONES',
		'ZINT_CAP_STRUCTAPP', 'ZINT_CAP_COMPLIANT_HEIGHT',
		'ZINT_MAX_SEG_COUNT', 'BARCODE_LAST'
	])
if __libzint_ver >= 21000:
	__all__.append('ZBarcode_Cap')
if __libzint_ver >= 21200:
	__all__.extend([
		'ZBarcode_Default_Xdim', 'ZBarcode_Scale_From_XdimDp',
		'ZBarcode_XdimDp_From_Scale', 'ZBarcode_NoPng'
	])
if __libzint_ver <= 20900:
	__all__.extend([
		'zint_render', 'zint_render_hexagon', 'zint_render_ring',
		'zint_render_string', 'zint_render_line'
	])
__all__.extend([
	'zint_symbol', 'ZINT_COLOUR_SIZE', 'ZINT_TEXT_SIZE',
	'ZINT_PRIMARY_SIZE', 'ZINT_ROWS_MAX', 'ZINT_COLS_MAX',
	'ZINT_ERR_SIZE', 'BARCODE_CODE11', 'BARCODE_C25MATRIX',
	'BARCODE_C25INTER', 'BARCODE_C25IATA', 'BARCODE_C25LOGIC',
	'BARCODE_C25IND', 'BARCODE_CODE39', 'BARCODE_EXCODE39',
	'BARCODE_EANX', 'BARCODE_EANX_CHK',
	'BARCODE_EAN128', 'BARCODE_CODABAR', 'BARCODE_CODE128',
	'BARCODE_DPLEIT', 'BARCODE_DPIDENT', 'BARCODE_CODE16K',
	'BARCODE_CODE49', 'BARCODE_CODE93', 'BARCODE_FLAT',
	'BARCODE_RSS14', 'BARCODE_RSS_LTD', 'BARCODE_RSS_EXP',
	'BARCODE_TELEPEN', 'BARCODE_UPCA', 'BARCODE_UPCA_CHK',
	'BARCODE_UPCE', 'BARCODE_UPCE_CHK',
	'BARCODE_POSTNET', 'BARCODE_MSI_PLESSEY', 'BARCODE_FIM',
	'BARCODE_LOGMARS', 'BARCODE_PHARMA', 'BARCODE_PZN',
	'BARCODE_PHARMA_TWO', 'BARCODE_PDF417', 'BARCODE_PDF417TRUNC',
	'BARCODE_MAXICODE', 'BARCODE_QRCODE', 'BARCODE_CODE128B',
	'BARCODE_AUSPOST', 'BARCODE_AUSREPLY', 'BARCODE_AUSROUTE',
	'BARCODE_AUSREDIRECT', 'BARCODE_ISBNX', 'BARCODE_RM4SCC',
	'BARCODE_DATAMATRIX', 'BARCODE_EAN14'
])
if __libzint_ver >= 20603:
	__all__.append('BARCODE_VIN')
__all__.extend([
	'BARCODE_CODABLOCKF', 'BARCODE_NVE18', 'BARCODE_JAPANPOST',
	'BARCODE_KOREAPOST', 'BARCODE_RSS14STACK',
	'BARCODE_RSS14STACK_OMNI', 'BARCODE_RSS_EXPSTACK',
	'BARCODE_PLANET', 'BARCODE_MICROPDF417', 'BARCODE_ONECODE',
	'BARCODE_PLESSEY', 'BARCODE_TELEPEN_NUM', 'BARCODE_ITF14',
	'BARCODE_KIX', 'BARCODE_AZTEC', 'BARCODE_DAFT',
	'BARCODE_MICROQR', 'BARCODE_HIBC_128', 'BARCODE_HIBC_39',
	'BARCODE_HIBC_DM', 'BARCODE_HIBC_QR', 'BARCODE_HIBC_PDF',
	'BARCODE_HIBC_MICPDF', 'BARCODE_HIBC_BLOCKF',
	'BARCODE_HIBC_AZTEC', 'BARCODE_DOTCODE', 'BARCODE_HANXIN'
])
if __libzint_ver >= 20603:
	__all__.append('BARCODE_MAILMARK')
__all__.extend([
	'BARCODE_AZRUNE', 'BARCODE_CODE32', 'BARCODE_EANX_CC',
	'BARCODE_EAN128_CC', 'BARCODE_RSS14_CC', 'BARCODE_RSS_LTD_CC',
	'BARCODE_RSS_EXP_CC', 'BARCODE_UPCA_CC', 'BARCODE_UPCE_CC',
	'BARCODE_RSS14STACK_CC', 'BARCODE_RSS14_OMNI_CC',
	'BARCODE_RSS_EXPSTACK_CC', 'BARCODE_CHANNEL', 'BARCODE_CODEONE',
	'BARCODE_GRIDMATRIX'
])
if __libzint_ver >= 20901:
	__all__.append('BARCODE_DPD')
if __libzint_ver >= 20601:
	__all__.append('BARCODE_UPNQR')
if __libzint_ver >= 20604:
	__all__.append('BARCODE_ULTRA')
if __libzint_ver >= 20700:
	__all__.append('BARCODE_RMQR')
if __libzint_ver >= 20900:
	__all__.extend([
		'BARCODE_C25STANDARD', 'BARCODE_GS1_128', 'BARCODE_DBAR_OMN',
		'BARCODE_DBAR_LTD', 'BARCODE_DBAR_EXP', 'BARCODE_PDF417COMP',
		'BARCODE_DBAR_STK', 'BARCODE_DBAR_OMNSTK', 'BARCODE_DBAR_EXPSTK',
		'BARCODE_USPS_IMAIL', 'BARCODE_GS1_128_CC', 'BARCODE_DBAR_OMN_CC',
		'BARCODE_DBAR_LTD_CC', 'BARCODE_DBAR_EXP_CC', 'BARCODE_DBAR_STK_CC',
		'BARCODE_DBAR_OMNSTK_CC', 'BARCODE_DBAR_EXPSTK_CC'
	])
if __libzint_ver >= 21101:
	__all__.extend(['BARCODE_CEPNET', 'BARCODE_BC412'])
if __libzint_ver >= 21200:
	__all__.extend([
		'BARCODE_CODE128AB', 'BARCODE_MAILMARK_2D',
		'BARCODE_UPU_S10', 'BARCODE_MAILMARK_4S'
	])
if __libzint_ver >= 21200:
	__all__.append('BARCODE_BIND_TOP')
else:
	__all__.append('BARCODE_NO_ASCII')
__all__.extend([
	'BARCODE_BIND', 'BARCODE_BOX', 'BARCODE_STDOUT', 'READER_INIT',
	'SMALL_TEXT', 'BOLD_TEXT', 'CMYK_COLOUR', 'BARCODE_DOTTY_MODE'
])
if __libzint_ver >= 20604:
	__all__.append('GS1_GS_SEPARATOR')
__all__.extend(['DATA_MODE', 'UNICODE_MODE', 'GS1_MODE'])
if __libzint_ver < 20604:
	__all__.extend(['KANJI_MODE', 'SJIS_MODE'])
if __libzint_ver >= 20602:
	__all__.append('ESCAPE_MODE')
if __libzint_ver >= 21000:
	__all__.extend(['GS1PARENS_MODE', 'GS1NOCHECK_MODE'])
__all__.extend([
	'DM_SQUARE', 'DM_DMRE',
	'ZINT_WARN_INVALID_OPTION', 'ZINT_WARN_USES_ECI',
	'ZINT_ERROR_TOO_LONG', 'ZINT_ERROR_INVALID_DATA',
	'ZINT_ERROR_INVALID_CHECK', 'ZINT_ERROR_INVALID_OPTION',
	'ZINT_ERROR_ENCODING_PROBLEM', 'ZINT_ERROR_FILE_ACCESS',
	'ZINT_ERROR_MEMORY', 'OUT_BUFFER'
])
if __libzint_ver >= 21000:
	__all__.extend([
		'ZINT_WARN_NONCOMPLIANT', 'ZINT_ERROR',
		'ZINT_ERROR_FILE_WRITE', 'ZINT_ERROR_USES_ECI',
		'ZINT_ERROR_NONCOMPLIANT', 'WARN_DEFAULT', 'WARN_FAIL_ALL',
		'ZINT_DEBUG_PRINT', 'ZINT_DEBUG_TEST',
		'ZINT_CAP_HRT', 'ZINT_CAP_STACKABLE', 'ZINT_CAP_EXTENDABLE',
		'ZINT_CAP_COMPOSITE', 'ZINT_CAP_ECI', 'ZINT_CAP_GS1',
		'ZINT_CAP_DOTTY', 'ZINT_CAP_FIXED_RATIO', 'ZINT_CAP_READER_INIT',
		'ZINT_CAP_FULL_MULTIBYTE', 'ZINT_CAP_MASK', 'ZINT_MAX_DATA_LEN'
	])
if __libzint_ver >= 20800:
	__all__.extend(['ZINT_FULL_MULTIBYTE', 'ULTRA_COMPRESSION'])
if __libzint_ver >= 20604:
	__all__.extend(['OUT_SVG_FILE', 'OUT_EPS_FILE', 'OUT_EMF_FILE'])
__all__.extend([
	'OUT_PNG_FILE', 'OUT_BMP_FILE', 'OUT_GIF_FILE',
	'OUT_PCX_FILE', 'OUT_JPG_FILE', 'OUT_TIF_FILE'
])
if __libzint_ver >= 21300:
	__all__.extend([
		'EANUPC_GUARD_WHITESPACE', 'EMBED_VECTOR_FONT',
		'EXTRA_ESCAPE_MODE', 'DM_ISO_144', 'ZINT_WARN_HRT_TRUNCATED',
		'ZINT_ERROR_HRT_TRUNCATED', 'ZINT_CAP_EANUPC', 'ZBarcode_Reset'
	])
