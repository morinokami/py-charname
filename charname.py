#!/usr/bin/env python3

import argparse
import unicodedata

general_category_values = {
    # See http://www.unicode.org/reports/tr44/#General_Category_Values
    'Lu': {'Long': 'Uppercase_Letter', 'Description': 'an uppercase letter'},
    'Ll': {'Long': 'Lowercase_Letter', 'Description': 'a lowercase letter'},
    'Lt': {'Long': 'Titlecase_Letter', 'Description': 'a digraphic character, with first part uppercase'},
    'LC': {'Long': 'Cased_Letter', 'Description': 'Lu | Ll | Lt'},
    'Lm': {'Long': 'Modifier_Letter', 'Description': 'a modifier letter'},
    'Lo': {'Long': 'Other_Letter', 'Description': 'other letters, including syllables and ideographs'},
    'L': {'Long': 'Letter', 'Description': 'Lu | Ll | Lt | Lm | Lo'},
    'Mn': {'Long': 'Nonspacing_Mark', 'Description': 'a nonspacing combining mark (zero advance width)'},
    'Mc': {'Long': 'Spacing_Mark', 'Description': 'a spacing combining mark (positive advance width)'},
    'Me': {'Long': 'Enclosing_Mark', 'Description': 'an enclosing combining mark'},
    'M': {'Long': 'Mark', 'Description': 'Mn | Mc | Me'},
    'Nd': {'Long': 'Decimal_Number', 'Description': 'a decimal digit'},
    'Nl': {'Long': 'Letter_Number', 'Description': 'a letterlike numeric character'},
    'No': {'Long': 'Other_Number', 'Description': 'a numeric character of other type'},
    'N': {'Long': 'Number', 'Description': 'Nd | Nl | No'},
    'Pc': {'Long': 'Connector_Punctuation', 'Description': 'a connecting punctuation mark, like a tie'},
    'Pd': {'Long': 'Dash_Punctuation', 'Description': 'a dash or hyphen punctuation mark'},
    'Ps': {'Long': 'Open_Punctuation', 'Description': 'an opening punctuation mark (of a pair)'},
    'Pe': {'Long': 'Close_Punctuation', 'Description': 'a closing punctuation mark (of a pair)'},
    'Pi': {'Long': 'Initial_Punctuation', 'Description': 'an initial quotation mark'},
    'Pf': {'Long': 'Final_Punctuation', 'Description': 'a final quotation mark'},
    'Po': {'Long': 'Other_Punctuation', 'Description': 'a punctuation mark of other type'},
    'P': {'Long': 'Punctuation', 'Description': 'Pc | Pd | Ps | Pe | Pi | Pf | Po'},
    'Sm': {'Long': 'Math_Symbol', 'Description': 'a symbol of mathematical use'},
    'Sc': {'Long': 'Currency_Symbol', 'Description': 'a currency sign'},
    'Sk': {'Long': 'Modifier_Symbol', 'Description': 'a non-letterlike modifier symbol'},
    'So': {'Long': 'Other_Symbol', 'Description': 'a symbol of other type'},
    'S': {'Long': 'Symbol', 'Description': 'Sm | Sc | Sk | So'},
    'Zs': {'Long': 'Space_Separator', 'Description': 'a space character (of various non-zero widths)'},
    'Zl': {'Long': 'Line_Separator', 'Description': 'U+2028 LINE SEPARATOR only'},
    'Zp': {'Long': 'Paragraph_Separator', 'Description': 'U+2029 PARAGRAPH SEPARATOR only'},
    'Z': {'Long': 'Separator', 'Description': 'Zs | Zl | Zp'},
    'Cc': {'Long': 'Control', 'Description': 'a C0 or C1 control code'},
    'Cf': {'Long': 'Format', 'Description': 'a format control character'},
    'Cs': {'Long': 'Surrogate', 'Description': 'a surrogate code point'},
    'Co': {'Long': 'Private_Use', 'Description': 'a private-use character'},
    'Cn': {'Long': 'Unassigned', 'Description': 'a reserved unassigned code point or a noncharacter'},
    'C': {'Long': 'Other', 'Description': 'Cc | Cf | Cs | Co | Cn'}
}

def charname(s, verbose=False):
    if type(s) != str:
        print('Error: argument must be a str.')
    for i, c in enumerate(s):
        name = unicodedata.name(c)
        if verbose:
            long = general_category_values[unicodedata.category(c)]['Long']
            desc = general_category_values[unicodedata.category(c)]['Description']
            print('%d "%s" %s (%s: %s)' % (i, c, name, long, desc))
        else:
            category = unicodedata.category(c)
            print('%d "%s" %s (%s)' % (i, c, name, category))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print unicode character name of each character in a string')
    parser.add_argument('string', type=str, help='arbitrary string')
    parser.add_argument('-v', action='store_true', default=False, help='show long value aliases for General_Category values with a brief description of each category')
    args = parser.parse_args()

    charname(args.string, args.v)




























