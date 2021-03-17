import os

files = ['initial_data\cnews.train.txt','initial_data\cnews.test.txt']
outfiles = ['体育', '娱乐', '家居', '房产', '教育','时尚', '时政', '游戏', '科技', '财经']
for file in files:
    fp = open(file, 'r', encoding='UTF-8').readlines()
    if file == 'cnews.train.txt':
        outdir = 'cnews-train'
    elif file == 'cnews.test.txt':
        outdir = 'cnews-test'
    else:
        outdir = 'cnews-val'
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    oldfile = ''
    i = 0
    for eachline in fp:
        if eachline == "\r\n":
            print('换行')
            continue
        else:
            outfile = eachline[0]+eachline[1]
        if oldfile != outfile:
            i = 0
        oldfile = outfile
        outfilename = outdir+'\\'+outfile   ##输出文件名，后续输出的文件是out0.txt,out1.txt
        if not os.path.exists(outfilename):
            os.mkdir(outfilename)#创建分类的文件夹
        eachline = eachline[3:]

        fp_w = open(outfilename + '\\' + str(i) + '.txt', 'w', encoding='UTF-8')  # 将截取出的内容保存在输出文件中
        fp_w.write(eachline)
        fp_w.close()
        i = i + 1