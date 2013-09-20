from scipy.stats import bernoulli
#wins = bernoulli.rvs(0.5,size=80)
#print wins
#bet = 5
## keep doubling bet until you win
#total_money = bet
#for win in wins:
	#if(not win):
		## if I didnt win, I lose what I bet
		#total_money = total_money - bet
		## I double the bet
		#wonorlost = win*"won" ++ (1-win)*"lost"
		#print "I bet %i, and I %s. I now have %i." %(bet, wonorlost, total_money)
		#bet *= 2
		#continue
	## I I did win, I add what I bet to total money
	#total_money = total_money + bet
	#wonorlost = win*"won" ++ (1-win)*"lost"
	#print "I bet %i, and I %s. I now have %i." %(bet, wonorlost, total_money)
	#bet = 5
import sys

class TailRecurseException:
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs

def tail_call_optimized(g):
  """
  This function decorates a function with tail call
  optimization. It does this by throwing an exception
  if it is it's own grandparent, and catching such
  exceptions to fake the tail call optimization.
  
  This function fails if the decorated
  function recurses in a non-tail context.
  """
  def func(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back \
        and f.f_back.f_back.f_code == f.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except TailRecurseException, e:
          args = e.args
          kwargs = e.kwargs
  func.__doc__ = g.__doc__
  return func


total_money = 0
bet = 5
@tail_call_optimized
def martingale(total_money, bet):
	while(bet <= 500):
		win = bernoulli.rvs(0.5)
		if(win):
			total_money += bet
			#print "I bet %i, and I won. I now have %i." %(bet, total_money)
			bet = 5
			return martingale(total_money, bet)
		else:
			total_money -= bet
			#print "I bet %i, and I lost. I now have %i." %(bet, total_money)
			return martingale(total_money, 2*bet)
	return total_money

def helper(total_money):
	return martingale(total_money, bet)

n = 1000
wins = map(helper, [0]*n)
print "wins <- c(" + ", ".join(map(str,wins)) + ")"
