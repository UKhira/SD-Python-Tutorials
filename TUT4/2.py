total = 0
count = 0

mark = input('Enter score: \n')

try:
    mark = int(mark)
    while mark != -9:
        try:
            count+= 1
            total+= mark
            mark = input('Enter score: \n')
            try:
                mark = int(mark)
            except Exception:
                print('Score must be an sInteger')
        except TypeError:
            continue
    if count == 0:
        print('Atleast enter one score')
    else:
        print('Class average is ',total/count)
    
except ValueError:
    print('Score must be an Integer')
