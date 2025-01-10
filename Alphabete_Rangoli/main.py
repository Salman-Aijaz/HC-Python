a = "abcdefghijklmnopqrstuvwxyz"
def print_rangoli(size):
    
    lines = []
    for row in range(size):
        print_ = "-".join(a[row:size])
        # print("PRINT--->",print_)
        lines.append(print_[::-1] + print_[1:])
        # print("LINES=---->",lines)
    width = len(lines[0])
    print("WIDTH--->",width)
    
    for row in range(size-1, 0, -1):
        print(lines[row].center(width, '-'))
        
    for row in range(size):
        print(lines[row].center(width, '-'))

if __name__ == '__main__':
    # n = int(input())
    n=10
    print_rangoli(n)