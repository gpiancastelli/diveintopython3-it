'''Conversione di interi in numeri romani e viceversa.

Questo programma fa parte di 'Immersione in Python 3', un libro gratuito
sul linguaggio Python per programmatori esperti. Visitate l'indirizzo
http://gpiancastelli.altervista.org/dip3-it per la versione più recente.
'''
import re

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass
class InvalidRomanNumeralError(ValueError): pass

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

roman_numeral_pattern = re.compile('''
    ^                   # inizio della stringa
    M{0,4}              # migliaia - da 0 a 4 M
    (CM|CD|D?C{0,3})    # centinaia - 900 (CM), 400 (CD), 0-300 (da 0 a 3 C),
                        #             o 500-800 (D, seguita da 0 fino a 3 C)
    (XC|XL|L?X{0,3})    # decine - 90 (XC), 40 (XL), 0-30 (da 0 a 3 X),
                        #          o 50-80 (L, seguita da 0 fino a 3 X)
    (IX|IV|V?I{0,3})    # unità - 9 (IX), 4 (IV), 0-3 (da 0 a 3 I),
                        #         o 5-8 (V, seguita da 0 fino a 3 I)
    $                   # fine della stringa
    ''', re.VERBOSE)

def to_roman(n):
    '''converte un intero in un numero romano'''
    if not (0 < n < 5000):
        raise OutOfRangeError("numero fuori dall'intervallo (deve essere tra 1 e 4999)")
    if not isinstance(n, int):
        raise NotIntegerError('numeri non interi non possono essere convertiti')

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result

def from_roman(s):
    '''converte un numero romano in un intero'''
    if not isinstance(s, str):
        raise InvalidRomanNumeralError("L'ingresso deve essere una stringa")
    if not s:
        raise InvalidRomanNumeralError('La stringa in ingresso non può essere vuota')
    if not roman_numeral_pattern.search(s):
        raise InvalidRomanNumeralError('Numero romano non valido: {0}'.format(s))

    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index : index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result

# Copyright (c) 2009, Mark Pilgrim, All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
