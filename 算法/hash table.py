"""
根据pattern和str，找到是否符合这个pattern匹配模式。
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
"""

def long_word(pattern,strs):
    '''
    :param pattern: str
    :param str: str
    :return: bool
    '''
    word = strs.split(' ')
    return list(map(pattern.find,pattern)) == list(map(strs.find,word))
result = long_word("abba","dog cat cat dog")
print(result)