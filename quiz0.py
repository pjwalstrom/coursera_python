n = 276
print n%100
# 12
print (n - n % 10) / 10
# 2
print (n % 100 - n % 10) / 10
# 2
print ((n - n % 10) % 100) / 10

#f(x) = -5 x5 + 69 x2 - 47

def fu(x):
    return -5*x*x*x*x*x + 69*x*x -47

print fu(0)
print fu(1)
print fu(2)
print fu(3)

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
        
    # Put your code here.
    return present_value * pow((1+rate_per_period), periods)
print future_value(500, .04, 10, 10)

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
