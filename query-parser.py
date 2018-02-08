import pyparsing as pp
from re import DOTALL

identifier = pp.Word(pp.alphas, pp.alphanums+'_')

collection = identifier()

cmd_keyword = pp.Keyword('insert') | pp.Keyword('get')

query = (cmd_keyword('cmd') 
         + collection('collection') 
         + pp.Regex('.+', DOTALL)('test'))

print(query.parseString("get todos completed=True"))
