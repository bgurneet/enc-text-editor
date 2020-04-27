from pygments import highlight
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from bs4 import BeautifulSoup

#styles = HtmlFormatter().get_style_defs('.highlight .k')
styles = HtmlFormatter(style='colorful').style.styles
#'[color=#008000]print[/color]([color=#BA2121]"hello world"[/color])\n'

def getColour(token):
    return styles[token]

def getColours(code):
    tokens = lex(code, PythonLexer())
    startindex = 0
    endindex = 0
    # data[x][0] -- startindex
    # data[x][1] -- endindex
    # data[x][2] -- colour
    data = []
    for token in list(tokens):
        #import
        endindex = startindex + len(token[1]) - 1
        colour = getColour(token[0])
        data.append([startindex, endindex, colour])
        startindex = endindex + 1
    return data

    # html = highlight(code, PythonLexer(), HtmlFormatter(lineos=True, cssclass="source"))
    # soup = BeautifulSoup(html)
    # elems = soup.find_all('span')
    # startindex = 0
    # endindex = 0
    # # data[x][0] -- startindex
    # # data[x][1] -- endindex
    # # data[x][2] -- colour
    # data = []
    # for elem in elems:
    #     endindex = len(elem.text)
    #     elem_data = [startindex, endindex, colour]
    #     startindex =
    #
    # return html
code = open('filesystem.py').read()