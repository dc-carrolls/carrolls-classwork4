def generate_coordinates():
    x, y = 0, 0
    yield (x, y)
    a, b = -1,0
    while True:
        if a < 0:
            a = (a * -1) + 1
        else:
            a = a*-1
            we
        


    for i in range(1, n):
        # Move right
        x += 1
        yield (x, y)

        # Move up
        for j in range(2 * i):
            y += 1
            yield (x, y)

        # Move left
        for j in range(2 * i):
            x -= 1
            yield (x, y)

        # Move down
        for j in range(2 * i):
            y -= 1
            yield (x, y)

        # Move right
        for j in range(2 * i):
            x += 1
            yield (x, y)

# How many coordinates you want to generate
n = 1000
coordinates = list(generate_spiral_coordinates(n))
#print(coordinates)
# for x, y in coordinates:
#     print(f"{x},{y}")

start_pos = 2
jump_num = -2
t = 0
game_over = False
while not game_over:
    spy_pos = start_pos + (t * jump_num)
    x,y = coordinates[t]
    my_guess = x + (t * y)
    if spy_pos == my_guess:
        game_over = True
    #end if
    t+=1
#end while
print("Time is:", t)
 

