#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 06:12:02 2020

@author: tylerpruitt
"""

"""
Problem Set 2
"""
"""
Problem 1
"""

# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

balance = 4900
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

def yearEndBalance(annualInterestRate, monthlyPaymentRate, balance):
    for i in range(1, 13):
        balance = balance - monthlyPaymentRate * balance
        balance = balance + (balance * annualInterestRate) / 12.0
        #print("Remaining balance of month", i, ":", round(balance, 2))
    return print("Remaining balance: " + str(round(balance, 2)))

yearEndBalance(annualInterestRate, monthlyPaymentRate, balance)

"""
Problem 2
"""

#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal

balance = 262
annualInterestRate = 0.40

monthlyPayment = 1

def yearBalance(annualInterestRate, monthlyPayment, balance):
    for i in range(1, 13):
        balance = balance - 10 * monthlyPayment
        balance = balance + (balance * annualInterestRate) / 12.0
        #print("Remaining balance of month", i, ":", balance)
    return balance

while yearBalance(annualInterestRate, monthlyPayment, balance) >= 0:
    monthlyPayment += 1
    
print("Lowest Payment: " + str(10 * monthlyPayment))

"""
Problem 3
"""
#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
low = balance / 12
high = (balance * (1 + monthlyInterestRate) ** 12) / 12
monthlyPayment = (high + low) / 2

def endYearBalance(annualInterestRate, monthlyPayment, balance):
    for i in range(1, 13):
        balance = balance - monthlyPayment
        balance = balance + (balance * annualInterestRate) / 12.0
        #if i == 12:
            #print("balance " + str(i) + ": " + str(balance))
    return balance

while endYearBalance(annualInterestRate, monthlyPayment, balance) < -0.001 or endYearBalance(annualInterestRate, monthlyPayment, balance) > 0:
    if endYearBalance(annualInterestRate, monthlyPayment, balance) < - 0.001:
        high = monthlyPayment
    else:
        low = monthlyPayment
    monthlyPayment = (high + low) / 2
    
    
print("Lowest Payment: " + str(round(monthlyPayment, 2)))
