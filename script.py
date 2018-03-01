from variables import *

# Print information

print 'Based on the following assumptions:' 
print 'Total number of DGX = ' + str(n_dgx)
print 'Average daily DGX transacted = ' + str(daily_dgx_transacted)
print 'Percent of DGD locked up to receive rewards = ' + str(percent_locked_up)
print 'Percent of locked up DGD actively voting = ' + str(percent_voting)

# Using units of DGX from here on

# Transaction fees that go to the locked up and voting DGD
daily_tx_fees = daily_dgx_transacted * tx_fee * 0.01 / (0.01**2 * percent_locked_up * percent_voting) 

annual_tx_fees = daily_tx_fees * 365.25
annual_tx_fees_per_dgd = annual_tx_fees / n_dgd
print 'Transaction fees (DGX) earned per DGD per annum:'
print annual_tx_fees_per_dgd
print 'Transaction fees (USD) earned per DGD per annum:'
print annual_tx_fees_per_dgd * gold_usd

# Demurrage

annual_demurrage = demurrage * 0.01 / (0.01**2 * percent_locked_up * percent_voting)
print 'Total demurrage (DGX) per DGD per annum:' 
print str(annual_demurrage)
print 'Total demurrage (USD) per DGD per annum:'
print str(annual_demurrage * gold_usd)

# Absolute total

print 'Total earnings (DGX) per DGD per annum:'
print annual_demurrage + annual_tx_fees_per_dgd
print 'Total earnings (USD) per DGD per annum:'
print (annual_demurrage + annual_tx_fees_per_dgd) * gold_usd

# Expected value of DGD
# Assume 5% rewards per year is satisfactory

print 'Expected DGD value:'
print (annual_demurrage + annual_tx_fees_per_dgd) * gold_usd * 20 

