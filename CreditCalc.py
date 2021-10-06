import math
import argparse

""" Example python creditcalc.py --type annuity --principal=1000000 --periods=10 --interest=10
"""

parser = argparse.ArgumentParser()
parser.add_argument('--type',  nargs='?',const='all', choices=['annuity','diff'],type=str)
parser.add_argument('--principal', type=int, default=None)
parser.add_argument('--periods', type=int, default=None)
parser.add_argument('--interest', type=float, default=None)
parser.add_argument('--payment', type=float, default=None)

args = parser.parse_args()
type = args.type
loan_principal = args.principal
number_of_periods = args.periods
loan_interest = args.interest
monthly_payment = args.payment

def creditcalc(type,loan_principal,number_of_periods,loan_interest,monthly_payment):

    if loan_interest == None:
        print('Incorrect parameters')
        return

    args_list = [type] + [float(i) for i in [loan_principal,number_of_periods,loan_interest,monthly_payment] if i != None]
    c = 0
    for i in args_list:
        if i == None:
            c += 1
        if c > 1 or i != None and str(i)[0] == '-':
            print('Incorrect parameters')
            return
    if type == 'annuity':
        if loan_principal != None and number_of_periods != None:
            nominal_interest_rate = (loan_interest / 12) / 100
            #print('loan_principal,nominal_interest_rate,number_of_periods',loan_principal,nominal_interest_rate,number_of_periods)
            monthly_payment = loan_principal / ((((1 + nominal_interest_rate) ** number_of_periods) - 1) / (
                        nominal_interest_rate * (1 + nominal_interest_rate) ** number_of_periods))
            monthly_payment = math.ceil(monthly_payment)
            #print(f'Your monthly payment = {monthly_payment}!')

        elif number_of_periods != None:
            #print(monthly_payment,loan_interest,number_of_periods)
            annuity_payment = monthly_payment
            n = number_of_periods
            coef = loan_interest/100/12
            loan_principal = math.floor(annuity_payment/((coef*((1+coef)**n))/(((1+coef)**n)-1)))
            print(f"Your loan principal = {loan_principal}!")
        else:
            principal = loan_principal
            mp = monthly_payment
            interest = loan_interest
            coef = interest / (12 * 100)
            n = math.ceil(math.log(mp / (mp - coef * principal), 1 + coef))
            d = {years: n - months for years, months in enumerate(range(0, n+1, 12))}
            years, months = list(d.items())[-1][0], list(d.items())[-1][1]
            if months != 0:
                print(f"It will take {years} years and {months} months to repay this loan!")
            else:
                if years == 1:
                    print(f"It will take {years} year to repay this loan!")
                else:
                    print(f"It will take {years} years to repay this loan!")

    elif type == 'diff':
        if monthly_payment != None:
            print('Incorrect parameters')
            return
        coef = loan_interest / (12 * 100)
        monthly_payment_l = []
        for month in range(1, number_of_periods + 1):
            monthly_payment = math.ceil((loan_principal / number_of_periods) + coef * (loan_principal - (loan_principal * (month - 1)) / number_of_periods))
            print(f"Month {month}: payment is {monthly_payment}")
            monthly_payment_l.append(monthly_payment)
        monthly_payment = sum(monthly_payment_l) / len(monthly_payment_l)
    else:
        print('Incorrect parameters.')

    #print(f"loan_principal,{loan_principal},number_of_periods {number_of_periods}, monthly_payment {monthly_payment}")
    if number_of_periods == None:
        number_of_periods = n
    overpayment = monthly_payment * number_of_periods - loan_principal
    print(f"Overpayment  {int(overpayment)}")

creditcalc(type,loan_principal,number_of_periods,loan_interest,monthly_payment)
