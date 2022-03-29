# Problem : If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily for a 
# week, how much would your $ 1000 reach at the end of the 7th day?


initial_principle_balance = 1000
interest_rate = 0.07
time_interest_applied = 7
time_periods_elapsed = 7
print(initial_principle_balance *
         (1 + interest_rate / time_interest_applied)**
         (time_interest_applied*time_periods_elapsed))