#ノイズを除去
import pdb

with open('raw_sentence.txt') as f:
    for line in f:
        #pdb.set_trace()
        line_list = line.split('\t')
        if len(line_list) > 2:
            print(line_list,len(line_list))
            with open('/Users/kawamurariku/word_cloud/full_sentence.txt','a') as g:
                g.write(line)
