from os import listdir
from os.path import basename
from sys import argv
from subprocess import call

from icecream import ic


IGNORE_FILES = (basename(__file__),)


def _run_python_file(file_name, *argv):
    argv = [str(e) for e in argv]
    call(["python", file_name, *argv])


def _run_file(file_name, *argv):
    argv = [str(e) for e in argv]
    call([file_name, *argv])


EXTENSIONS = {"py": _run_python_file, "exe": _run_file, "bat": _run_file}


def _is_accept_extension(file_name):
    file_extension = file_name.split(".")[-1]
    return any([file_extension == extension for extension in EXTENSIONS])


def _is_ignore_file(file_name):
    return any([ingore_file == file_name for ingore_file in IGNORE_FILES])


def _get_scripts():
    return [(x, x.split(".")[0]) for x in listdir()
            if _is_accept_extension(x)
            and not _is_ignore_file(x)
            ]


if __name__ == '__main__':
    all_scripts = _get_scripts()
    try:
        chose_script = argv[argv.index(basename(__file__)) + 1]
    except IndexError as e:
        text = "List all sripts:"
        print(text)
        for script in all_scripts:
            print("{}{}".format(" " * int(len(text) / 2), script[1]))
        exit()
    only_argv = argv[argv.index(chose_script) + 1:]
    for script in all_scripts:
        if chose_script in script:
            EXTENSIONS[script[0].split(
                ".")[-1]](script[0], only_argv)
            break

    else:
        text = "List all sripts:"
        print(text)
        for script in all_scripts:
            print("{}{}".format(" " * len(text), script[1]))
