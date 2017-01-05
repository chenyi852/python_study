# -*- coding: utf-8 -*-

import os
import shutil
import time
import logging
import filecmp
#��־�ļ�����
log_filename ='synchro.log'
#��־�����ʽ��
log_format = '%(filename)s [%(asctime)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S %p',level=logging.DEBUG) 
#��־�������־�ļ�
fileLogger = logging.getLogger('fileLogger')
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.INFO)
fileLogger.addHandler(fh);
#��Ҫͬ�����ļ���·��,����ʹ�þ���·��,Ҳ����ʹ�����·��
#synchroPath1 = r'/home/xxx/image1'
#synchroPath2 = r'/home/xxx/image2'
synchroPath1 = r'D:\03_personal\01_music'
synchroPath2 = r'\\192.168.2.176\chenyi\����'

#ͬ������
def synchro(synchroPath1,synchroPath2):
        leftDiffList = filecmp.dircmp(synchroPath1,synchroPath2).left_only
        rightDiffList = filecmp.dircmp(synchroPath1,synchroPath2).right_only
        commondirsList =filecmp.dircmp(synchroPath1,synchroPath2).common_dirs
        for item in leftDiffList:
                copyPath = synchroPath1 + '\\' + item
                pastePath = synchroPath2 + '\\' + item
                if(os.path.isdir(copyPath)):
                        copyDir(copyPath,pastePath)
                else :
                        shutil.copy2(copyPath,pastePath)
                        fileLogger.info('copy '+copyPath +" to "+pastePath)
        for item in rightDiffList:
                copyPath = synchroPath2 + '\\' + item
                pastePath = synchroPath1 +'\\' + item
                if(os.path.isdir(copyPath)):
                        copyDir(copyPath,pastePath)
                else :
                        shutil.copy2(copyPath,pastePath)
                        fileLogger.info('copy '+copyPath +" to "+pastePath)
        for item in commondirsList:
                copyPath = synchroPath2 + '\\' + item
                pastePath = synchroPath1 +'\\' + item
                syncDir(copyPath,pastePath)
#�����ļ���,����ļ��в����ڴ���֮��ֱ�ӿ���ȫ��,����ļ����Ѵ�����ô��ͬ���ļ���                
def copyDir(copyPath,pastePath):
        if(os.path.exists(pastePath)):
                synchro(copyPath,pastePath)
        else :
                os.mkdir(pastePath)
                shutil.copytree(copyPath,pastePath)
#���ļ������������ļ��ж�����,��ͬ���������ļ���
def syncDir(copyPath,pastePath):
         copyDir(copyPath,pastePath)
         copyDir(pastePath,copyPath)
while(True):
        synchro(synchroPath1,synchroPath2)
        logging.debug('synchro run')
        #��������,��һ��ִ�н�����ȴ�����
        time.sleep(5)