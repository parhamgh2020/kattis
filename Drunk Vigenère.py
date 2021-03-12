'''alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
word = 'calgary'
key = 'alberta'
answer = str()
for i in range(len(key)):
    shift = alphabet.index(key[i])
    position = alphabet.index(word[i])
    if position + shift <= len(alphabet) - 1:
        answer += alphabet[position + shift]
    else:
        answer += alphabet[position + shift - len(alphabet)]


print(answer)

# ==========================================================================
alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
word = 'calgary'
key = 'alberta'
answer = str()
for i in range(len(key)):
    shift = alphabet.index(key[i])
    position = alphabet.index(word[i])
    answer += alphabet[position - shift]

print(answer)'''
# ========================================================================
'''alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
word = 'calgary'
key = 'alberta'
answer = str()
for i in range(len(key)):
    if i % 2 == 0:
        shift = alphabet.index(key[i])
        position = alphabet.index(word[i])
        if position + shift <= len(alphabet) - 1:
            answer += alphabet[position + shift]
        else:
            answer += alphabet[position + shift - len(alphabet)]
    else:
        shift = alphabet.index(key[i])
        position = alphabet.index(word[i])
        answer += alphabet[position - shift]

print(answer)
'''
# ============================================================================
'''alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.upper().split(',')
encrypted = input()
key = input()
word = str()
for i in range(len(key)):
    if i % 2 == 0:
        shift = alphabet.index(key[i])
        position = alphabet.index(encrypted[i])
        word += alphabet[position - shift - len(alphabet)]
    else:
        shift = alphabet.index(key[i])
        position = alphabet.index(encrypted[i])
        if position + shift >= len(alphabet):
            word += alphabet[(position + shift) - len(alphabet)]
        else:
            word += alphabet[position + shift]

print(word)
'''
# ================================================
# print(''.join(chr(ord('A') + ((ord(a) - ord('A')) + (1 if i & 1 else -1) * (ord(b) - ord('A'))) % 26) for i, (a, b) in
#               enumerate(zip(input(), input()))))
# ==============================================
encrypted = input()
key = input()
out_1 = str()

for i, j, k in zip(encrypted, key, range(len(encrypted))):
    a = ord(i) - ord('A')
    b = ord(j) - ord('A')
    if k % 2 == 0:
        c = (a - b) % 26
        out_1 += chr(ord('A') + c)
    else:
        c = (a + b) % 26
        out_1 += chr(ord('A') + c)

print(out_1)
# =======================================
