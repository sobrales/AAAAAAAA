def abc():
    def c(x):
        print(x)
    for i in range(10):
        x=i
        printa(x)

def printa(x):
    
    c(x)


def main():
    abc()
main()