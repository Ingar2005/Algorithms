

def caesar_cypher(word: str, num) -> str:
    new =""
    for i in word:
        i = chr((((ord(i)-96)+num )%27)+96)
        new +=str(i)
    return new
def rev_ceaser_cypher(word: str, num:int) -> str:
    new =""
    for i in word:
        i = chr((((ord(i)-96)-num )%27)+96)
        new +=str(i)
    return new


