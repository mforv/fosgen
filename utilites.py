from sys import stderr
from json import  load as jload
from numpy import load as nload
from json import  dump as jdump
from numpy import save as ndump
from nltk.tokenize import WordPunctTokenizer
from itertools import product
from math import tanh

def load(filename):
    filetype = filename.split('.')[-1]
    try:
        rez = None
        print('Loading %s ...' % filename, end = '', file = stderr)
        if filetype == 'json':
            rez = jload(open(filename))
        elif filetype == 'dat':
            rez = nload(open(filename, 'rb'))
        print(' done', file = stderr)
        return rez
    except Exception as e:
        print(' error! %s' % e, file = stderr)
        raise e
    
def dump(object, filename, quiet = 0):
    filetype = filename.split('.')[-1]
    if not quiet: print('Saving %s ...' % filename, end = '', file = stderr)
    if filetype == 'json':
        jdump(object, open(filename, 'w'), indent = 2, ensure_ascii = 0)
    elif filetype == 'dat':
        ndump(open(filename, 'wb'), object)
    if not quiet: print('done', file = stderr)

                
def join(tokens = ['очень', 'длинная', 'строка', ',', 'с', 'пробелами', ',', 'и', 'знаками', 'препинания']):
    PUNKT = list(".,:;-")
    rez = []
    for i in range(len(tokens)):
        token = tokens[i]
        if token in PUNKT:
            rez[-1] += token
        else:
            rez += [token]
    return rez


def wrap(wpt, _str = "очень длинная строка,с пробелами, и знаками препинания"):
    _len = 0
    rez = ""
    for token in join(wpt.tokenize(_str)):
        _len += len(token)
        rez += " " + token
        if _len > 20:
            rez += "\n"
            _len = 0
    return rez.strip()


def compare(S1,S2):
    ngrams = [S1[i:i+3] for i in range(len(S1))]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)

    return count/max(len(S1), len(S2))

def compare_phrase(P1, P2):
    def func(x, a=0.00093168, b=-0.04015416, c=0.53029845):
        return a * x ** 2 + b * x ** 1 + c 
    
    P1 = P1.lower().split() if type(P1) == str else [ x.lower() for x in P1 ]
    P2 = P2.lower().split() if type(P2) == str else [ x.lower() for x in P2 ]
    n, v = 0, 0
    for a, b in set([ tuple(sorted((a, b))) for a, b in product(P1, P2)]):
        v += compare(a,b)
        n += 1
    try:
        return tanh((v / n) / func(max(len(P1),len(P2))))
    except ZeroDivisionError:
        return 0
    
text = """Лексика, на первый взгляд, отталкивает дактиль. Мифопорождающее текстовое устройство кумулятивно. Ударение дает композиционный анализ. Генезис свободного стиха, в первом приближении, традиционен. Ю.Лотман, не дав ответа, тут же запутывается в проблеме превращения не-текста в текст, поэтому нет смысла утверждать, что художественная гармония диссонирует литературный анжамбеман, заметим, каждое стихотворение объединено вокруг основного философского стержня.

Наряду с нейтральной лексикой строфоид изящно аллитерирует сюжетный палимпсест. Драма, как бы это ни казалось парадоксальным, последовательно дает урбанистический ямб. Различное расположение текстологически представляет собой глубокий метаязык. Мифопорождающее текстовое устройство упруго-пластично. Мелькание мыслей параллельно. Кроме того, постоянно воспроизводится постулат о письме как о технике, обслуживающей язык, поэтому жанр традиционно отталкивает диалектический характер, и это придает ему свое звучание, свой характер.

Абстрактное высказывание интегрирует орнаментальный сказ, и это является некими межсловесными отношениями другого типа, природу которых еще предстоит конкретизировать далее. Эвокация, как справедливо считает И.Гальперин, многопланово притягивает стих. Наш «сумароковский» классицизм – чисто русское явление, но лексика интегрирует прозаический символ – это уже пятая стадия понимания по М.Бахтину. Скрытый смысл приводит метафоричный речевой акт. Похоже, что самого Бахтина удивила эта всеобщая порабощенность тайной "чужого" слова, тем не менее олицетворение многопланово аллитерирует скрытый смысл."""

from nltk.tokenize import PunktSentenceTokenizer
from itertools import product

pst = PunktSentenceTokenizer()

X = []
Y = []
if __name__ == "__main__":
    print(compare('привет', 'првиет'))
    sents = [ s for s in pst.tokenize(text) ]
    for textA, textB in product(sents, sents):
        x = compare_phrase(textA, textB)
        X += [(x, textA, textB)]
    X = sorted(X, key=lambda x: x[0])


    
