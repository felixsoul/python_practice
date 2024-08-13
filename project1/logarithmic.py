def logarithmic(n)->int:
    count = 0
    while n>1:
        n = n/2
        count+=1
    return count

if __name__ == "__main__":
    print(logarithmic(8))