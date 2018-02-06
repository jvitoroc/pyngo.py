from classes.Definition import Definition
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()

definition = Definition(args.path)
definition.collections['todo'].delete()
for i in range(1,10):
    definition.collections['todo'].insert({"task": 'a'*i, "completed": "True", "body": '12312'*i, "age": "100"})
print(definition.collections['todo'].read())

