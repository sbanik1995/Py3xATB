# File IO

try:
    file = open('rrr.txt' , 'r')
    print(file.read())

except:
    print("Something went wrong")

finally:
    print("Executed")

    try:
        file.close()

    except NameError as ne:
        print(ne)

