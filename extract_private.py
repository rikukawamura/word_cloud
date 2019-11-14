import pdb

with open('sentence2.txt') as f:
    for line in f:
        line_list = line.split(' ')
        #pdb.set_trace()
        if len(line_list) > 1:
            if "安井" in line_list[0]:
                with open('/Users/kawamurariku/word_cloud/yasui.txt','a') as g:
                    g.write(str(line_list[1]))
            if line_list[0] == "尊師":
                with open('/Users/kawamurariku/word_cloud/yasui.txt','a') as g:
                    g.write(str(line_list[1]))
            if "谷口" in line_list[0]:
                with open('/Users/kawamurariku/word_cloud/taniguchi.txt','a') as g:
                    g.write(str(line_list[1]))
            if "上田" in line_list[0] or "かずき" in line_list[0]:
                with open('/Users/kawamurariku/word_cloud/ueda.txt','a') as g:
                    g.write(str(line_list[1]))
            if "中津" in line_list[0] or "準尊師" in line_list[0]:
                with open('/Users/kawamurariku/word_cloud/nakatsu.txt','a') as g:
                    g.write(str(line_list[1]))
            if "りょうすけ" in line_list[0] or "中川" in line_list[0]:
                with open('/Users/kawamurariku/word_cloud/nakagawa.txt','a') as g:
                    g.write(str(line_list[1]))
            if "川村" in line_list[0]:
                with open('/Users/kawamurariku/word_cloud/kawamura.txt','a') as g:
                    g.write(str(line_list[1]))
