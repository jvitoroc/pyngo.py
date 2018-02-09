from classes.Definition import Definition
import argparse
import gc

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()

with Definition(args.path) as collections:
    for i in range(1, 2):
        collections['todo'].insert({"task": 'a   \n \na'*i, "completed": "False", "body": '12312', "age": "100"})
    print(len(collections['todo'].read()))
gc.collect()


