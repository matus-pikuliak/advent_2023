print(
    sum(
        i + 1
        for i, line in enumerate(open('input'))
        if all(
            eval(x) <= 14
            for x in line.split(':')[1].replace(';', ',').replace('red', '+2').replace('green', '+1').replace('blue', '+0').split(',')
        )
    )
)