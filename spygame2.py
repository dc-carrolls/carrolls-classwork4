def gen_dec_integers(n):
    while n != 0:
        yield n
        if n > 0:
            n = -(n - 1)
        else:
            n = -n
        #end if
    #end while
    yield n
#end generator



def gen_inc_nz_integers(n):
    i=1
    while i != n:
        yield i
        if i < 0:
            i = -i + 1
        else:
            i = -i
        #end if
    #end while
#end generator

t = 0
n = 1
game_over = False
while t < 10 and not game_over:
    list_a = gen_dec_integers(n)
    list_b = gen_inc_nz_integers(n)
    for _ in range(n):
        a = next(list_a)
        b = next(list_b)
        print(a,b)
        t += 1
    #next a
    n+=1
#end while


# for x in gen_dec_integers(-2):
#     print(x)





