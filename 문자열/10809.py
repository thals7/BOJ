import string
S = list(input())
Apb_list = list(string.ascii_lowercase)

for Alphabet in Apb_list:
    if S.count(Alphabet) >= 1:
        print(S.index(Alphabet), end=' ')
    else:
        print(-1, end=' ')

# map(chr,range(97,123))
# chr() -> 유니코드 코드 포인트가 i인 문자를 나타내는 문자열을 돌려줌
# 예를 들어 chr(97)은 문자열 'a'를 돌려줌