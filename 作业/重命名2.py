import os

def reName(dirname):
    '''
    实现将所有类别中的所有文章重新命名
    '''
    # 该文件夹下所有的文件（包括文件夹）
    for category in os.listdir(dirname):
        # print(category)
        catdir = os.path.join(dirname, category)
        # 如果不是文件夹则跳过
        if not os.path.isdir(catdir):
            continue
        files = os.listdir(catdir)
        # print(files)
        # files.remove('.DS_Store')
        count = 0
        for cur_file in files:
            print("正在处理" + category + "分类下的" + cur_file)
            filename = os.path.join(catdir,cur_file)
            count = count + 1
            # 原来的文件路径
            oldDir = os.path.join(catdir,cur_file)
            # 如果是文件夹则跳过
            if os.path.isdir(oldDir):
                continue
            # 文件名
            filename=os.path.splitext(cur_file)[0]
            # 文件扩展
            filetype=os.path.splitext(cur_file)[1]
            # 新的文件路径
            newDir=os.path.join(catdir,str(count)+filetype)
            # 重命名
            os.rename(oldDir,newDir)

if __name__ == '__main__':
        dirname = 'D:\pycharm 文件\作业'
        reName(dirname)
