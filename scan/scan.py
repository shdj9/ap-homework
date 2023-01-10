import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="indiquer le nom du fichier")
parser.add_argument("extension", default="py", help="indiquer le type de dossier qu'on ouvre")
args=parser.parse_args()
FILENAME = args.filename
EXT = args.extension


from datetime import datetime as DateTime
from pathlib import Path

def scanv1(folder, truc):
    globbing = Path("folder")
    list = list(globbing.glob("**/*.truc"))
    for p in list : 
        date = DateTime.fromtimestamp(p.stat().st_mtime)
        with p.open() as file : 
            line = file[0] 
        print(str(p.resolve()), 
        p.stat().st_size, "last modified on {date}",
        "first line :",line, end="" )




