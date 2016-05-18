Python-Zint is a ctypes interface to libzint of 
Robin Stuart's Zint project:

<http://www.zint.org.uk/>

<https://zint.github.io>

Usage closely follows the C API:

<http://www.zint.org.uk/Manual.aspx?type=p&page=5>

Usage
=====
Generate a QRCode saved to file out.png::

    import zint
    import sys
    
    symbol = zint.ZBarcode_Create()
    symbol.contents.symbology = zint.BARCODE_QRCODE
    symbol.contents.scale = 2.5
    symbol.contents.option_1 = 4
    symbol.contents.border_width = 4
    input = zint.instr('https://github.com/jmptbl/python-zint')
    if zint.ZBarcode_Encode_and_Print(symbol, input, 0, 0) != 0:
        print 'error: %s' % symbol.contents.errtxt
        sys.exit(1)
    zint.ZBarcode_Delete(symbol)

Result
------
.. image:: sample/out.png?raw=true
