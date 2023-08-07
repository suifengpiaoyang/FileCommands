# FileCommands
Provides a set of user-friendly file manipulation commands to simplify common file management tasks.

## install

```
python setup.py install
```

## usage

Provide four commands: zcopy, zmove, zdel, zrecycle

### get supported commands
```
$ python -m FileCommands -l
Supported Commands:

zcopy
zmove
zdel
zrecycle

type <command> -h for more details
```

### command usage
```
$zcopy -h
usage: zcopy [-h] src dst

copy files to destination

positional arguments:
  src         source, can be file or folder
  dst         destination

optional arguments:
  -h, --help  show this help message and exit
```

## basic usage

use python fnmatch for wildcards. the supported characters as follows:

| Pattern  | Meaning                            |
| -------- | ---------------------------------- |
| `*`      | matches everything                 |
| `?`      | matches any single character       |
| `[seq]`  | matches any character in *seq*     |
| `[!seq]` | matches any character not in *seq* |

### example

copy all the .html files to new path

```
zcopy *.html new_path
```

delete all the .jpg and send to trash

```
zrecycle *.jpg
```
