import random
import statistics
from matplotlib.pyplot import hist, show

historical_stock_returns = [.1348, .3215, .1589, .0210, .1482, .2594, -.3655, .0548, .1561,
                            .0483, .1074, .2836, -.2197, -.1185, -.0903, .2089, .2834, .3310, .2268,
                            .3720, .0133, .0997, .0749, .3023, -.0306, .3148, .1654, .0581, .1849,
                            .3124, .0615, .2234, .2042, -.0470, .3174, .1852, .0651, -.0698, .2383,
                            .3700, -.2590, -.1431, .1876, .1422, .0356, -.0824, .1081, .2380, -.0997,
                            .1240, .1642, .2261, -.0881, .2664, .0034, .1206, .4372, -.1046, .0744,
                            .3260, .5256, -.0121, .1815, .2368, .3081, .1830, .0570, .0520, -.0843]

historical_bond_performance = [-.0202, .0422, .0784, .0654, .0593, .0524, .0697, .0433,
                               .0243, .0434, .0410, .1026, .0843, .1163 -.0082, .0870, .0964, .0364,
                              .1846, -.0292, .0975, .0740, .1600, .0896, .1453, .0789, .0275, .1530,
                               .2213, .1515, .0819, .3265, .0626, .271]

historical_bond_yields = [.0485, .051, .0494, .0566, .0604, .0729, .0744, .0648, .0648,
                          .0606, .0639, .0676, .078, .0795, .0837, .0788, .0722, .0787, .0805,
                          .082, .0863, .0793, .0898, .098, .1036, .1018, .1083, .1053, .1039,
                          .1272, .1419, .135, .1611, .1604, .1367, .1069, .0949, .0897, .0975]

historical_treasury_rates = [.0254, .0235, .018, .0278, .0322, .0326, .0366, .0463, .048,
                             .0429, .0427, .0401, .0461, .0502, .0603, .0565, .0526, .0635, .0644,
                             .0657, .0709, .0587, .0701, .0786, .0855, .0849, .0885, .0839, .0767,
                             .1062, .1246, .111, .1301, .1392, .1143, .0943, .0841, .0742, .0761,
                             .0799, .0756, .0685, .0621, .0616, .0735, .0667, .0564, .0507, .0493,
                             .0428, .0419, .0400, .0395]

historical_inflation = [.0, .016, .015, .021, .032, .016, -.004, .038, .028, .032,
                        .034, .027, .023, .016, .028, .034, .022, .016, .023, .030,
                        .028, .026, .030, .030, .042, .054, .048, .041, .036, .019,
                        .036, .043, .032, .062, .103, .135, .113, .076, .065, .058,
                        .091, .110, .062, .032, .044, .057, .055, .042, .031, .029,
                        .016, .013, .013, .010, .010, .017, .007, .028, .033, .015,
                        -.004, .007, .008, .019, .079, .013, -.012, .081, .144, .083]

def ChangeInBalanceStocks(initial_balance):
    rate = random.choice(historical_stock_returns)
    return initial_balance*rate

def ChangeInBalanceBonds(initial_balance):
    rate = random.choice(historical_bond_performance)
    return initial_balance*rate

def YearData():
    ''' Returns a rate of change for stocks, bonds, and inflation in a single tuple'''
    year = random.randrange(33)
    return (historical_stock_returns[year], historical_bond_performance[year])


number_years = 10
number_sims = 10000
final_balances_stocks = []
final_balances_bonds = []
final_balances_mixed = []
final_balances_mixed_norebalance = []
for i in range(number_sims):
    #Set initial conditions
    time = 0
    balance_stocks = 1000
    balance_bonds = 1000
    balance_mixed_stocks = 500
    balance_mixed_bonds = 500
    balance_mixed_stocks_norebalance = 500
    balance_mixed_bonds_norebalance = 500

    while (time < number_years):
        #Increase balance and time
        stock_perform, bond_perform = YearData()
        balance_stocks *= (1.0+stock_perform)
        balance_bonds *= (1.0+bond_perform)
        balance_mixed_stocks *= (1.0+stock_perform)
        balance_mixed_bonds *= (1.0+bond_perform)
        balance_mixed_stocks_norebalance *= (1.0+stock_perform)
        balance_mixed_bonds_norebalance *= (1.0+bond_perform)
        #Rebalance account
        balance_mixed = balance_mixed_stocks + balance_mixed_bonds
        target_stocks = balance_mixed * 0.5
        amount_to_move = balance_mixed_stocks - target_stocks
        balance_mixed_stocks -= amount_to_move
        balance_mixed_bonds += amount_to_move
        time += 1

    final_balances_stocks.append(balance_stocks)
    final_balances_bonds.append(balance_bonds)
    final_balances_mixed.append(balance_mixed)
    final_balances_mixed_norebalance.append(balance_mixed_stocks_norebalance + balance_mixed_bonds_norebalance)

final_balance_average = statistics.mean(final_balances_stocks)
final_balance_average = statistics.mean(final_balances_stocks)
final_balance_standard_deviation = statistics.stdev(final_balances_stocks)
print("The average final balance for a stock account was", final_balance_average)
print("The standard deviation in the final balance for a stock account was", final_balance_standard_deviation)
final_balance_average = statistics.mean(final_balances_bonds)
final_balance_standard_deviation = statistics.stdev(final_balances_bonds)
print("The average final balance for a bond account was", final_balance_average)
print("The standard deviation in the final balance for a bond account was", final_balance_standard_deviation)
final_balance_average = statistics.mean(final_balances_mixed)
final_balance_standard_deviation = statistics.stdev(final_balances_mixed)
print("The average final balance for a 50-50 mixed account with rebalancing was", final_balance_average)
print("The standard deviation in the final balance for a 50-50 mixed account with rebalancing was", final_balance_standard_deviation)
final_balance_average = statistics.mean(final_balances_mixed_norebalance)
final_balance_standard_deviation = statistics.stdev(final_balances_mixed_norebalance)
print("The average final balance for a 50-50 mixed account with NO Rebalancing was", final_balance_average)
print("The standard deviation in the final balance for a 50-50 mixed account with NO Rebalancing was", final_balance_standard_deviation)

#Output the simulation results
hist([final_balances_stocks, final_balances_bonds, final_balances_mixed, final_balances_mixed_norebalance], bins=40)
#hist(final_balances_bonds, bins=20)
show()
