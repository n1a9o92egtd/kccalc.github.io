from math import log10, sqrt

def kelly_bet(prob, odds, bankroll, reduce_volitility):
    kc = ((prob * (odds + 1) - 1) / odds) * reduce_volitility
    bet = kc * bankroll
    return round(kc, 4), round(bet, 2)

def main():
    print('Kelly Criterion with Kelly Betting System.')
    prob = float(input('Probability: '))
    odds = float(input('Odds: '))
    bankroll = float(input('Bankroll: '))
    reduce_volitility = float(input('Adjusted Kelly: '))

    bet = 1.0
    counter = 0
    txt = "<tr style=\"background: #f8fadb;\"><th style=\"text-align: center; vertical-align: center; font-weight: bold; padding: 4px;\">{bankRoll:.2f}</th><td style=\"text-align: right; vertical-align: center; padding: 8px;\">{betThisMuch:.2f}</td></tr>"
    while bet != 0.0:
        kc, bet = kelly_bet(prob, odds, bankroll, reduce_volitility)

        print(txt.format(bankRoll = bankroll, betThisMuch = bet))
        # print('counter:%.f' % counter)
        # print('Kelly Criterion (Adjusted): %.4f' % kc)
        # print('Bet This Much (Adjusted): %.2f\n' % bet)
        if bet < 2500:
            break
        bankroll -= bet
        counter += 1

if __name__ == '__main__':
    main()