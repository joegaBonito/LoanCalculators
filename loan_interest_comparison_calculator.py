def loan_interest_comparison_calculator():
    principal = input("Please input the principal: $")
    principal_float = float(principal)
    interest_rate = input("Please input the interest rate (In %): ")
    interest_rate_float = float(interest_rate)
    months_left = input("How many months left to payoff? ")
    months_left_int = int(months_left)
    payment = input("How much per month are you paying off? $")
    payment_float = float(payment)

    total_interest_paid = 0.0
    total_number_of_months = 1

    print('')
    while 0 < months_left_int:
        print('Month #', total_number_of_months)
        monthly_interest = ((principal_float/months_left_int) * (interest_rate_float/100))
        minimum = principal_float/months_left_int + monthly_interest
        print('Monthly (without interest) $', principal_float/months_left_int)
        print('Interest Amount $', monthly_interest)
        total_interest_paid += monthly_interest

        print('Expected Monthly Payment $', minimum)
        print('Actual Monthly Payment: $', payment_float)

        principal_float -= payment_float
        print('Remaining Principal: $', principal_float)

        if principal_float > 0:
            total_number_of_months += 1
        else:
            print('Total number of months paid for ', total_number_of_months)
            print('\n')
            break

        months_left_int -= 1
        print('\n')

    print('Total Interest Paid at the end: $', total_interest_paid)