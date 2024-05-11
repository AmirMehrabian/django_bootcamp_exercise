str=list(input().split())

units = {
    'me' : 1,
    'km' : 0.001,
    'fe' : 3.280,
    'mi' : 0.000621,
}

output = float(str[0]) * (units[str[2]] / units[str[1]])

print(f'{output:.6f}')