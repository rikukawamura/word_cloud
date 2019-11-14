#発言者と文だけを抽出
import pdb

with open('full_sentence.txt') as f:
    for line in f:
        #pdb.set_trace()
        line_list = line.split('\t')
        if '谷口' in line_list[1]:
            delete = str(line_list[2]).replace("「"," ")
            delete_kagikakko = delete.replace("」","")
            with open('/Users/kawamurariku/word_cloud/sentence2.txt','a') as g:
                g.write(delete_kagikakko.rstrip('\n') + '\n')
        if 'Kazuki' in line_list[1]:
                delete = str(line_list[2]).replace("「"," ")
                delete_kagikakko = delete.replace("」","")
                with open('/Users/kawamurariku/word_cloud/sentence2.txt','a') as g:
                    g.write(delete_kagikakko.rstrip('\n') + '\n')
        if 'Riku' in line_list[1]:
                delete = str(line_list[2]).replace("「"," ")
                delete_kagikakko = delete.replace("」","")
                with open('/Users/kawamurariku/word_cloud/sentence2.txt','a') as g:
                    g.write(delete_kagikakko.rstrip('\n') + '\n')
        if '安井' in line_list[1] and '尊師' in line_list[1]:
                delete = str(line_list[2]).replace("「"," ")
                delete_kagikakko = delete.replace("」","")
                with open('/Users/kawamurariku/word_cloud/sentence2.txt','a') as g:
                    g.write(delete_kagikakko.rstrip('\n') + '\n')
        if 'ÿ' in line_list[1]:
                delete = str(line_list[2]).replace("「"," ")
                delete_kagikakko = delete.replace("」","")
                with open('/Users/kawamurariku/word_cloud/sentence2.txt','a') as g:
                    g.write(delete_kagikakko.rstrip('\n') + '\n')
        if '中川' in line_list[1]:
                delete = str(line_list[2]).replace("「"," ")
                delete_kagikakko = delete.replace("」","")
                with open('/Users/kawamurariku/word_cloud/sentence2.txt','a') as g:
                    g.write(delete_kagikakko.rstrip('\n') + '\n')
        if '中津' in line_list[1] and '準尊師' in line_list[1]:
                delete = str(line_list[2]).replace("「"," ")
                delete_kagikakko = delete.replace("」","")
                with open('/Users/kawamurariku/word_cloud/sentence2.txt','a') as g:
                    g.write(delete_kagikakko.rstrip('\n') + '\n')
