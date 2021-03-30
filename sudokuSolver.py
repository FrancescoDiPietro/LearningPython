
rows, cols = (9,9)
# sudoku = [[0,0,9,8,0,5,0,0,2],
# [0,4,0,1,0,2,0,0,0],
# [7,0,0,0,4,0,0,0,0],
# [0,0,7,0,6,4,0,5,1],
# [2,5,0,9,1,7,0,8,3],
# [4,1,0,2,4,0,7,0,0],
# [0,0,0,0,3,0,0,0,5],
# [0,0,0,5,0,1,0,2,0],
# [8,0,0,7,0,9,3,0,0]]

sudoku = [[0]*cols for i in range(rows)]

def read_file(fname):
    i,j = (0,0)
    f = open(fname, "r")

    for line in f:
        while i < rows :
            sudoku[j][i] = int(line[i])
            i += 1
        j+=1
        i=0
        
def valid_check(value,posx,posy):
    for i in range(cols):
        if value == sudoku[posy][i] and posx != i:
            return 0
        else:
            for j in range(rows):
                if value == sudoku[j][posx] and posy != j:
                    return 0

    return 1

def check_in_box(value,posx,posy):
    reminder_x,reminder_y = (posx%3,posy%3)
    check = [(0,1,2),(-1,0,1),(-2,-1,0)]
    tmp = True
    for i in check[reminder_x]:
        for j in check[reminder_y]:
            if value == sudoku[posy+j][posx+i] and (posx+i != posx and posy+j != posy):
                tmp = False
    
    if tmp:
        return 1
    else:
        return 0

def run():

    for y in range(rows):
        for x in range(cols):
            if sudoku[y][x] == 0 :
                for n in range(1,10):
                    if valid_check(n,x,y) == 1 and check_in_box(n,x,y) == 1:
                        sudoku[y][x] = n
                        run()
                        sudoku[y][x] = 0
                return
    
    for j in range(9):
            print(sudoku[j])
    input("More? \n")

if __name__ == '__main__':
    read_file("sudoku")
    run()