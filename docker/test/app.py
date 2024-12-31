import os

print('hello app')

path = os.environ.get('HF_HOME')

print(path)

if os.path.exists(path):
    print(f'{path} existed')
    # 列出当前目录下的文件和目录
    items = os.listdir(path)
    # 打印所有文件和目录
    print("当前目录是:", path)
    print("目录中的内容:")
    for item in items:
        print(item)
else:
    print(f'{path} not exist')
