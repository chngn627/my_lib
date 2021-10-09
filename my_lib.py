# coding:utf-8
# 个人常用函数库

def findAllfile(path, allfile):
    '''
    返回一个list，包含路径文件夹下所有文件的路径
    '''
    filelist =  os.listdir(path)  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):
            #print(filepath)  
            findAllfile(filepath, allfile)  
        else:  
            allfile.append(filepath)  
    return allfile 


import json
def modify_json_data(filename:str):
    '''
    从json文件读取数据，修改某一项后保存到文件
    '''
    data = json.load(open(filename, 'rb'))
    # 修改'imagePath'，绝对路径改为相对路径
    # data['imagePath'] = os.path.basename(data['imagePath'])
    json.dump(data, open(filename, 'w'))


import argparse
def get_parser():
    '''
    添加运行时的命令行参数。
    '''
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("--example",
                        default="i am a example",
                        required=False,
                        help="example")
    parser.add_argument("--host",
                        default="127.0.0.1",
                        required=False,
                        help="host")
    parser.add_argument("--port", 
                        default=8080, 
                        required=False, 
                        help="port")

    args = parser.parse_args()
    '''
    args.example
    args.host
    args.port
    '''

    return args