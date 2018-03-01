# dgd_rewards
Calculate annual DGD token rewards 

```python

from variables import *

# Print information
print 'Calculate DGD rewards...'
print '\n'
print 'Based on the following assumptions:' 
print 'Total number of DGX = ' + str(n_dgx/1e6) + 'm'
print 'Average daily DGX transacted = ' + str(daily_dgx_transacted/1e6) + 'm' + ' (' + str(gold_usd*daily_dgx_transacted/1e6) + 'm USD)'
print 'Percent of DGD locked up to receive rewards = ' + str(ratio_locked_up*100)
print 'Percent of locked up DGD actively voting = ' + str(ratio_voting*100)
print '\n'

# Using units of DGX from here on
# Transaction fees that go to the locked up and voting DGD
daily_tx_fees = daily_dgx_transacted * tx_fee / ( ratio_locked_up * ratio_voting) 

annual_tx_fees = daily_tx_fees * 360
annual_tx_fees_per_dgd = annual_tx_fees / n_dgd
print 'Transaction fees (DGX) earned per DGD per annum:'
print annual_tx_fees_per_dgd
print 'Transaction fees (USD) earned per DGD per annum:'
print annual_tx_fees_per_dgd * gold_usd

# Expected value of DGD
# Assume 5% rewards per year is satisfactory

print 'Expected DGD value:'
print annual_tx_fees_per_dgd * gold_usd * 20 

```
