from Date import Date


def main(): 

     while(True): 

        try: 
            date = input("Input Your Date: ")
            d = Date(date)
            
            if (d.returnCheck()): 
                print(d.getFormattedDate())

        except EOFError as e:
            print("\nClosing Dates Program")
            quit()



if __name__ == "__main__": 
    main()