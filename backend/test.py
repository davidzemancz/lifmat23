import sys
from restapi import ask

question = sys.argv[1]
answer = ask(question).get('text')
print(answer)