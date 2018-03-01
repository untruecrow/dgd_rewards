from variables import *

# A calculation of the annual tx fee rewards gained by DGD DAO participators/voters
# ================================================================
# Start by printing information
print 'Calculate DGD rewards...'
print '\n'
print 'Based on the following assumptions:' 
print 'Total number of DGX = ' + str(n_dgx/1e6) + 'm'
print 'Average daily DGX transacted = ' + str(daily_dgx_transacted/1e6) + 'm' + ' (' + str(gold_usd*daily_dgx_transacted/1e6) + 'm USD)'
print 'Percent of DGD locked up to receive rewards = ' + str(ratio_locked_up*100)
print 'Percent of locked up DGD actively voting = ' + str(ratio_voting*100)
print '\n'
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
print 'Transaction fees (DGX) earned per DGD per annum:'
print annual_tx_fees_per_dgd
print 'Transaction fees (USD) earned per DGD per annum:'
print annual_tx_fees_per_dgd * gold_usd
# ================================================================


# ================================================================
# DGD VALUATION CALCULATION
# Assume 5% rewards per year is satisfactory (thus, 20 * tx_fees_per_dgd)
print 'Expected DGD value:'
print annual_tx_fees_per_dgd * gold_usd * 20 
# ================================================================

