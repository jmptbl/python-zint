# Copyright (c) 2019, Aragon Gouveia
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
BARCODE_PDF417 = 55
BARCODE_PDF417TRUNC = 56
BARCODE_MAXICODE = 57
BARCODE_QRCODE = 58
BARCODE_CODE128B = 60
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

BARCODE_NO_ASCII = 1
BARCODE_BIND = 2
BARCODE_BOX = 4
BARCODE_STDOUT = 8
READER_INIT = 16
SMALL_TEXT = 32
BOLD_TEXT = 64
CMYK_COLOUR = 128
BARCODE_DOTTY_MODE = 256

DATA_MODE = 0
UNICODE_MODE = 1
GS1_MODE = 2
KANJI_MODE = 3
SJIS_MODE = 4
if __libzint_ver >= 20602:
	ESCAPE_MODE = 8

DM_SQUARE = 100
DM_DMRE = 101

ZINT_WARN_INVALID_OPTION = 2
ZINT_WARN_USES_ECI = 3
ZINT_ERROR_TOO_LONG = 5
ZINT_ERROR_INVALID_DATA = 6
ZINT_ERROR_INVALID_CHECK = 7
ZINT_ERROR_INVALID_OPTION = 8
ZINT_ERROR_ENCODING_PROBLEM = 9
ZINT_ERROR_FILE_ACCESS = 10
ZINT_ERROR_MEMORY = 11

OUT_BUFFER = 0
OUT_PNG_FILE = 100
OUT_BMP_FILE = 120
OUT_GIF_FILE = 140
OUT_PCX_FILE = 160
OUT_JPG_FILE = 180
OUT_TIF_FILE = 200

ZINT_COLOUR_SIZE = 10
ZINT_TEXT_SIZE = 128
ZINT_PRIMARY_SIZE = 128
ZINT_ROWS_MAX = 200
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

class zint_render_line(Structure):
	pass
zint_render_line._fields_ = [
	('x', c_float),
	('y', c_float),
	('length', c_float),
	('width', c_float),
	('next', POINTER(zint_render_line))
]

class zint_render_string(Structure):
	pass
zint_render_string._fields_ = [
	('x', c_float),
	('y', c_float),
	('length', c_float),
	('width', c_int),
	('text', POINTER(c_ubyte)),
	('next', POINTER(zint_render_string))
]

class zint_render_ring(Structure):
	pass
zint_render_ring._fields_ = [
	('x', c_float),
	('y', c_float),
	('radius', c_float),
	('line_width', c_float),
	('next', POINTER(zint_render_ring))
]

class zint_render_hexagon(Structure):
	pass
zint_render_hexagon._fields_ = [
	('x', c_float),
	('y', c_float)
]
if __libzint_ver >= 20602:
	zint_render_hexagon._fields_.append(('height', c_float))
zint_render_hexagon._fields_.append(('next', POINTER(zint_render_hexagon)))

class zint_render(Structure):
	pass
zint_render._fields_ = [
	('width', c_float),
	('height', c_float),
	('lines', POINTER(zint_render_line)),
	('strings', POINTER(zint_render_string)),
	('rings', POINTER(zint_render_ring)),
	('hexagons', POINTER(zint_render_hexagon))
]

class zint_symbol(Structure):
	pass
zint_symbol._fields_ = [
	('symbology', c_int),
	('height', c_int),
	('whitespace_width', c_int),
	('border_width', c_int),
	('output_options', c_int),
	('fgcolour', (c_char * ZINT_COLOUR_SIZE)),
	('bgcolour', (c_char * ZINT_COLOUR_SIZE)),
	('outfile', (c_char * FILENAME_MAX)),
	('scale', c_float),
	('option_1', c_int),
	('option_2', c_int),
	('option_3', c_int),
	('show_hrt', c_int)
]
if __libzint_ver >= 20603:
	zint_symbol._fields_.append(('fontsize', c_int))
zint_symbol._fields_.extend([
	('input_mode', c_int),
	('eci', c_int),
	('text', (c_ubyte * ZINT_TEXT_SIZE)),
	('rows', c_int),
	('width', c_int),
	('primary', (c_char * ZINT_PRIMARY_SIZE)),
	('encoded_data', ((c_ubyte * ZINT_COLS_MAX) * ZINT_ROWS_MAX)),
	('row_height', (c_int * ZINT_ROWS_MAX)),
	('errtxt', (c_char * ZINT_ERR_SIZE)),
	('bitmap', POINTER(c_char)),
	('bitmap_width', c_int),
	('bitmap_height', c_int),
	('bitmap_byte_length', c_uint),
	('dot_size', c_float),
	('rendered', POINTER(zint_render)),
	('debug', c_int)
])

ZBarcode_Create = _lib.ZBarcode_Create
ZBarcode_Create.restype = POINTER(zint_symbol)
ZBarcode_Create.argtypes = []

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

__version__ = '1.2'

__all__ = [
	'__version__', 'instr', 'infile', 'bitmapbuf',
	'ZBarcode_Create', 'ZBarcode_Delete',
	'ZBarcode_Encode', 'ZBarcode_Encode_File', 'ZBarcode_Print',
	'ZBarcode_Encode_and_Print', 'ZBarcode_Encode_File_and_Print',
	'ZBarcode_Buffer', 'ZBarcode_Encode_and_Buffer',
	'ZBarcode_Encode_File_and_Buffer', 'ZBarcode_ValidID',
	'ZBarcode_Version',
	'zint_symbol', 'zint_render', 'zint_render_hexagon',
	'zint_render_ring', 'zint_render_string', 'zint_render_line',
	'ZINT_COLOUR_SIZE', 'ZINT_TEXT_SIZE', 'ZINT_PRIMARY_SIZE',
	'ZINT_ROWS_MAX', 'ZINT_COLS_MAX', 'ZINT_ERR_SIZE',
	'BARCODE_CODE11', 'BARCODE_C25MATRIX', 'BARCODE_C25INTER',
	'BARCODE_C25IATA', 'BARCODE_C25LOGIC', 'BARCODE_C25IND',
	'BARCODE_CODE39', 'BARCODE_EXCODE39', 'BARCODE_EANX', 'BARCODE_EANX_CHK',
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
]
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
if __libzint_ver >= 20601:
	__all__.append('BARCODE_UPNQR')
__all__.extend([
	'BARCODE_NO_ASCII', 'BARCODE_BIND',
	'BARCODE_BOX', 'BARCODE_STDOUT', 'READER_INIT',
	'SMALL_TEXT', 'BOLD_TEXT', 'CMYK_COLOUR',
	'BARCODE_DOTTY_MODE', 'DATA_MODE', 'UNICODE_MODE', 'GS1_MODE',
	'KANJI_MODE', 'SJIS_MODE'
])
if __libzint_ver >= 20602:
	__all__.append('ESCAPE_MODE')
__all__.extend([
	'DM_SQUARE', 'DM_DMRE',
	'ZINT_WARN_INVALID_OPTION', 'ZINT_WARN_USES_ECI',
	'ZINT_ERROR_TOO_LONG', 'ZINT_ERROR_INVALID_DATA',
	'ZINT_ERROR_INVALID_CHECK', 'ZINT_ERROR_INVALID_OPTION',
	'ZINT_ERROR_ENCODING_PROBLEM', 'ZINT_ERROR_FILE_ACCESS',
	'ZINT_ERROR_MEMORY', 'OUT_BUFFER',
	'OUT_PNG_FILE', 'OUT_BMP_FILE', 'OUT_GIF_FILE',
	'OUT_PCX_FILE', 'OUT_JPG_FILE', 'OUT_TIF_FILE'
])
