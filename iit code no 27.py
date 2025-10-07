def main():
    try:
        infile = open("salaries.txt",'r')
        salary = int(infile.readline())
        print("salary:", salary)
    except FileNotFoundError:
            print("File Salaries.txt not found.")
    except ValueError:
            print("File Salaries.txt contains an invalid salary.")
            infile.close()
    else:
            infile.close()

     finally: 
         print("Thank you for using our program>")

        main()
                        
