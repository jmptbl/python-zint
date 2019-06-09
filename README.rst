Python-Zint is a ctypes interface to libzint of 
Robin Stuart's Zint project:

<http://www.zint.org.uk/>

<https://zint.github.io>

Usage closely follows the C API:

<http://www.zint.org.uk/Manual.aspx?type=p&page=5>

Example #1
==========
Generate a QRCode saved to file out.png::

    import zint
    import sys
    
    symbol = zint.ZBarcode_Create()
    symbol.contents.symbology = zint.BARCODE_QRCODE
    symbol.contents.scale = 2.5
    symbol.contents.option_1 = 4
    symbol.contents.border_width = 4
    input = zint.instr(b'https://github.com/jmptbl/python-zint')
    if zint.ZBarcode_Encode_and_Print(symbol, input, 0, 0) != 0:
        print('error: %s' % symbol.contents.errtxt)
        sys.exit(1)
    zint.ZBarcode_Delete(symbol)

Result
------
.. image:: sample/out.png?raw=true


Example #2
==========
Generate a QRCode in memory only::

    import zint
    import sys
    
    symbol = zint.ZBarcode_Create()
    symbol.contents.symbology = zint.BARCODE_QRCODE
    symbol.contents.scale = 0
    symbol.contents.option_1 = 4
    symbol.contents.border_width = 0
    input = zint.instr(b'https://github.com/jmptbl/python-zint')
    if zint.ZBarcode_Encode_and_Buffer(symbol, input, 0, 0) != 0:
        print('error: %s' % symbol.contents.errtxt)
        sys.exit(1)
    bitmap = zint.bitmapbuf(symbol)
    pixel = 0
    for y in range(symbol.contents.bitmap_height):
        line = ''
        for x in range(symbol.contents.bitmap_width):
            # Each pixel represented by a 3 byte
            # RGB value
            if ord(bitmap[pixel]) > 0:
                line += ' '
            else:
                line += '*'
            pixel += 3
        print(line)
    zint.ZBarcode_Delete(symbol)

Result
------
::

    ******* *****  *     * * ** * *******
    *     *  *    *** *  ** * * * *     *
    * *** * *     * * **  ***  ** * *** *
    * *** *  *   **  *  ** *** ** * *** *
    * *** * *     ** **     *     * *** *
    *     *   * *  *  * ****    * *     *
    ******* * * * * * * * * * * * *******
            ** *   *  **  **  ***        
         **  *  ** *  ** * *      * * * *
      *  * * ** *  *     *** *    * *  * 
     **********    *  **  *  **   *  ****
     **  *   ** * *  *   *    *** ** *  *
    ***   * **   ****** * **      ** * **
    *****  * *  ***  * ***** * ***    *  
    ***** * **    ** *     *******   * **
         * ****   ** * **  *    *  * ** *
       ****    *    * ** ** ***  ** * ***
       * * *   ***   *** **  * **     *  
    **  **** **** *    *** * ***   * ** *
    *  **   *** **   * **** *  ***   * **
    ** ** * ** **  *   ** *****  **** ***
       *   *  ****   **  *  ****** ***** 
    *    ****  ** *   *  ******* *   * **
     *** * *  * *** ****** * * *   * * **
    *  * ******  *** **     **       *   
    *  ***    *  * ****           **  ** 
    * *****  ** *  ***   ******** * *  **
    *   *    ** ** *    ****    ** * ****
    * *** ** * ** ** **   ************** 
            ******  *   * **** **   ** * 
    *******   *  * *   * **** * * * *** *
    *     * *  **   **   * *   **   ** **
    * *** *  *** **   **  ** ******** *  
    * *** *  *** *   ** **  *** * *  **  
    * *** *  * * *  * *      *** * *    *
    *     *    ** *  **** * * * * * **  *
    *******  * ****  *  ** **   *  ***  *
