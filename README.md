# dgd_rewards
Calculate annual DGD token rewards
## Example Usage
```
$ python script.py
Calculate DGD rewards...


Based on the following assumptions:
Total number of DGX = 100.0m (4.5b USD)
Average daily DGX on-chain transactions = 2.0m (90.0m USD)
Percent of DGD locked up to receive rewards = 50.0
Percent of locked up DGD actively voting = 90.0


Transaction fees (DGX) earned per DGD per annum:
1.04
Transaction fees (USD) earned per DGD per annum:
46.8


Demurrage fees (DGX) earned per DGD per annum:
0.0111111111111
Demurrage fees (USD) earned per DGD per annum:
0.5


Rational valuation of DGD based on 5% rewards per year...
Expected DGD value (USD):
946.0
```
## Script
```python
from variables import *

# A calculation of the annual tx fee rewards gained by DGD DAO participators/voters
# ================================================================
# Start by print >> f,ing information
f=open('output.txt','w')
print >> f, 'Calculate DGD rewards...'
print >> f, '\n'
print >> f, 'Based on the following assumptions:' 
print >> f, 'Total number of DGX = ' + str(n_dgx/1e6) + 'm' + ' (' + str(gold_usd*n_dgx/1e9) + 'b USD)'
print >> f, 'Average daily DGX on-chain transactions = ' + str(daily_dgx_transacted/1e6) + 'm' + ' (' + str(gold_usd*daily_dgx_transacted/1e6) + 'm USD)'
print >> f, 'Percent of DGD locked up to receive rewards = ' + str(ratio_locked_up*100)
print >> f, 'Percent of locked up DGD actively voting = ' + str(ratio_voting*100)
print >> f, '\n'
# ================================================================


# ================================================================
# TRANSACTION FEE CALCULATION

# Daily tx fees that go to the locked up and voting DGD
daily_tx_fees = daily_dgx_transacted * tx_fee_ratio / ( ratio_locked_up * ratio_voting) 

# Annual tx fees
annual_tx_fees = daily_tx_fees * 360

# Annual tx fees per DGD token
annual_tx_fees_per_dgd = annual_tx_fees / n_dgd

# Print answers in DGX and USD
print >> f, 'Transaction fees (DGX) earned per DGD per annum:'
print >> f, annual_tx_fees_per_dgd
print >> f, 'Transaction fees (USD) earned per DGD per annum:'
print >> f, annual_tx_fees_per_dgd * gold_usd
# ================================================================

# ================================================================
# DEMURRAGE
annual_demurrage_per_dgd = ( n_dgx / n_dgd ) * demurrage_ratio * ACT / 360
print >> f, '\n'
print >> f, 'Demurrage fees (DGX) earned per DGD per annum:'
print >> f, annual_demurrage_per_dgd
print >> f, 'Demurrage fees (USD) earned per DGD per annum:'
print >> f, annual_demurrage_per_dgd * gold_usd
# ================================================================

# ================================================================
# DGD VALUATION CALCULATION
# Assume 5% rewards per year is satisfactory (thus, 20 * tx_fees_per_dgd)
print >> f, '\n'
print >> f, 'Rational valuation of DGD based on 5% rewards per year...' 
print >> f, 'Expected DGD value (USD):'
print >> f, ( annual_tx_fees_per_dgd + annual_demurrage_per_dgd ) * gold_usd * 20 
# ================================================================

f.close()
```
