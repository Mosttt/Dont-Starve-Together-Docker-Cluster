import os
import sys


def add_mod_file(file, mod_id, mod_format):
    with open(file, 'r+') as f:
        for line in f.readlines():
            if line[:2] == '--':
                continue
            elif mod_id in line:
                print(mod_id+'已经存在于'+file)
                return False
        if line[-1] != '\n':
            f.write('\n')
        f.write(mod_format.format(mod_id))
        print(mod_id+'成功添加到文件'+file)


def add_mod_path(path, mod_id):
    file1 = os.path.join(d, 'dedicated_server_mods_setup.lua')
    file2 = os.path.join(d, 'modsettings.lua')
    if not(os.path.exists(file1) and os.path.exists(file2)):
        print(f'请检查目录 {path} 是否存在dedicated_server_mods_setup.lua和modsettings.lua')
        return False
    else:
        add_mod_file(file1, mod_id, 'ServerModSetup("{}")\n')
        add_mod_file(file2, mod_id, 'ForceEnableMod("workshop-{}")\n')


if __name__ == "__main__":
    self_path = os.path.dirname(os.path.abspath(__file__))
    self_path = os.path.abspath(os.path.join(self_path, '..'))
    if len(sys.argv) == 1:
        mod_list = []
        if not os.path.exists(os.path.join(self_path, 'mod_list.txt')):
            print('请创建mod_list.txt或者通过参数传递mod id')
            sys.exit(0)
        else:
            with open(os.path.join(self_path, 'mod_list.txt'), 'r') as f:
                for line in f.readlines():
                    mod_list.append(line.strip())
    else:
        mod_list = [m.strip() for m in sys.argv[1:]]
    print(mod_list)
    root_path = os.path.join(self_path, 'data')
    if not os.path.exists(root_path):
        print('配置mod前必须生成data文件夹')
        sys.exit(0)
    dirs = [os.path.join(root_path, d) for d in os.listdir(root_path)]
    dirs = [d for d in dirs if os.path.isdir(d)]
    # print(dirs)
    if not dirs:
        print('data文件夹中的配置异常')
        sys.exit(0)
    for d in dirs:
        for mod in mod_list:
            add_mod_path(d, mod)
