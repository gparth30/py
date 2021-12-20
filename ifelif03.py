monthly_income=int(input("Enter Monthly Income.:"))
gross_income=monthly_income*12
print("Gross Income=",gross_income)

if gross_income>=800000:
    tax=gross_income*.3
    print("Tax=",tax)
elif gross_income>=500000:
    tax=gross_income*.2
    print("Tax=",tax)
elif gross_income>=300000:
    tax=gross_income*.1
    print("Tax=",tax)
elif gross_income<300000:
    tax=gross_income*.05
    print("Tax=",tax)

net_income=gross_income-tax
print("Net Income=",net_income)