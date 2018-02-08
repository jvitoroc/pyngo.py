from classes.Definition import Definition
import argparse
import gc

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()

with Definition(args.path) as collections:
    collections['todo'].insert({"task": 'a\na', "completed": "True", "body": '12312', "age": "100"})
    collections['todo'].read()

gc.collect()


