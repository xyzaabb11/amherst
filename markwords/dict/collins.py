#!/usr/bin/env python
# encoding: utf-8


from readmdict import MDX
import os
import re
from lxml import etree, html

def collins(filename):
    mdx = MDX(filename)
    items = mdx.items()
    for i in range(12):
        item = next(items)
        print(item[0])
        dom = etree.HTML(item[1])
        explains = dom.xpath(r'//*[@class="C1_explanation_item"]')
        for e in explains:
            seealso = e.xpath(r'div/*/a[@class="C1_explain"]/text()')
            if len(seealso) != 0:
                print('see also', seealso)
            else:
                cn = e.xpath(r'div/span[@class="C1_explanation_label"]/text()') + e.xpath(r'div/span[@class="C1_text_blue"]/text()')
                print(''.join(cn))
                entemp = e.xpath(r'div/text()')
                enword = e.xpath(r'div/span[@class="C1_inline_word"]/text()')
                en = []
                for i in range(len(enword)):
                    en.append(entemp[i])
                    en.append(enword[i])
                en.append(entemp.pop())
                en = e.xpath(r'div/span[@class="C1_word_gram"]/text()') + en
                print(''.join(en))
                sentence = e.xpath(r'ul/li')
                for sen in sentence:
                    entemp = sen.xpath(r'p[1]/text()')
                    enword = sen.xpath(r'p[1]/span[@class="C1_text_blue"]/text()')
                    sentence_en = []
                    for i in range(len(enword)):
                        sentence_en.append(entemp[i])
                        sentence_en.append(enword[i])
                    print(entemp)
                    sentence_en.append(entemp.pop())
                    print(''.join(sentence_en))
                    sentence_cn = sen.xpath(r'p[2]/text()')
                    print(''.join(sentence_cn))

    #print(next(mdx.items())[1])

if __name__ == "__main__":
    import os
    import os.path
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs='?', help="mdx file name")
    args = parser.parse_args()

    collins(args.filename)
