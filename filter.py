def main():
    f=open("filtered.txt","w+")

    for i in range(100):
        f.write("site %d" %(i+1))

    f.close



if __name__=="__main__":
    main()
