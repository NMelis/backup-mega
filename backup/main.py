from os.path import join
from pathlib import Path
from .build_files import zipping_files


def backup():
    home_folder = str(Path.home())
    path_yaml_conf = join(home_folder, "backup-mega.txt")
    with open(path_yaml_conf) as f:
        conf_file = f.read()

    zipping_files(conf_file.split('\n'))
