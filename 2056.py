list_month_1=['01','03','05','07','08','10','12']
list_month_2=['04','06','09','11']
input_date_n=int(input())

for i in range(input_date_n):

    input_date=input()
    input_date_s=f'{input_date[0:4]}/{input_date[4:6]}/{input_date[6:]}'
    print(f'#{i+1} ', end='')
    if input_date[4:6] in list_month_1:
        if int(input_date[-2:]) > 31:
            print('-1')
        else:
            print(input_date_s)
    elif input_date[4:6] in list_month_2:
        if int(input_date[-2:]) > 30:
            print('-1')
        else:
            print(input_date_s)
    elif input_date[4:6]=='02':
        if int(input_date[-2:]) > 28:
            print('-1')
        else:
            print(input_date_s)
    else:
        print('-1')