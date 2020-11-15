
from deleteSpace import *
import requests


def google_translate(content):
    '''google translation'''
    js = Pytrans()
    tk = js.getTk(content)

    if len(content) > 4891:
        print("too long！！！")
        return

    param = {'tk': tk, 'q': content}

    result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en
        &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
        &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param)

    trans = result.json()[0]
    ret = ''
    for i in range(len(trans)):
        line = trans[i][0]
        if line != None:
            ret += trans[i][0]

    return ret


a = google_translate("hello，Input file will be translated, please be patient")
print(a)

genotype_annotation_list = []

translate_file = open('transScript.txt', "a+", encoding='utf-8')

# deleteSpace("Z.mays_enhancer_record.txt", "Z.mays_enhancer_record_noSpace.txt")

with open('Z.mays_enhancer_record_noSpace.txt', 'r') as f: #有空行会报错！!
    for element in f:
        genotype_annotation_list.append(element.strip())
# print(genotype_annotation_list)
count = 0
for ga in genotype_annotation_list:
    translation = google_translate(ga)
    #translate_file.write(ga + '\t' + translation + '\n')
    translate_file.write(translation + '\n')
    count += 1
    print('complete', '%.1f%%' % ((count / len(genotype_annotation_list)) * 100))
