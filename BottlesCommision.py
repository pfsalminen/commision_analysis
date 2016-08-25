#!usr/bin/env python

'''
Program made to play with 
paying pn commision at Bottles
Author: Paul Salminen 2016
'''

import numpy as np
import argparse

class analyzeInfo:
    def __init__(self, numPeople=6., days=106., curWage=9., paulWage=15.,\
                                                percentEarned=0.3):
        self.people = numPeople
        self.days = days
        self.curWage = curWage
        self.paulWage = paulWage
        self.percentEarned = percentEarned

    def findAvgHours(self, hourRev):
        '''
        Returns the average hourly income
        Based on number of days and percent earned
        after cost of product
        '''
        for x in hourRev:
            hourRev[x]*= 0.3
            hourRev[x] /= self.days

        return hourRev

    def avgMornTotal(self, dailyHrAvg):
        morn = dailyHrAvg['nine'] + dailyHrAvg['ten'] + dailyHrAvg['eleven'] + \
            dailyHrAvg['twelve'] + dailyHrAvg['thirteen'] + dailyHrAvg['fourteen'] +\
            dailyHrAvg['fifteen']
        return morn

    def avgNightTotal(self, dailyHrAvg):
        night = dailyHrAvg['sixteen'] + dailyHrAvg['seventeen'] +\
                dailyHrAvg['eightteen'] + dailyHrAvg['nineteen'] +\
                dailyHrAvg['twenty'] + dailyHrAvg['twentyone'] +\
                dailyHrAvg['twentytwo'] + dailyHrAvg['twentythree']
        return night

    def curSpent(self):
        return (self.paulWage * 7 * 5) + (self.curWage * 7 * 2 * 7)
    
    '''
    Hodgepodge, come back and clean up!!!!
    '''
    def randWageCalc(self):
        newTotalWagesSpent = (7.5 * 3 * 7)
        niceTotalWages = (self.paulWage * 7 * 5) + (self.curWage * 7 * 2 * 7)
        diffWagesSpent = curTotalWagesSpent - newTotalWagesSpent
def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ppl', dest='ppl')
    parser.add_argument('--days', dest='days')
    parser.add_argument('--curWage', dest='curWage')
    parser.add_argument('--paulWage', dest='paulWage')
    parser.add_argument('--percent', dest='percentEarned')
    args = parser.parse_args()
    if args.ppl:
        ppl = args.ppl
    else:
        ppl = 6
    if args.days:
        days = args.days
    else:
        days = 106
    if args.curWage:
        curWage = args.curWage
    else:
        curWage = 9
    if args.paulWage:
        paulWage = args.paulWage
    else:
        paulWage = 15
    if args.percentEarned:
        percentEarned = args.percentEarned
    else:
        percentEarned = 0.3

    # Hard Coded Information for default
    # POS system deatuls 3/1 - 8/15
    hourRev = {'nine' : 9144.77, 'ten' : 17485.81, 'eleven' : 26293.80,\
                'twelve' : 33391.99, 'thirteen' : 39248.26, 'fourteen' : 48142.70, \
                'fifteen' : 59574.46, 'sixteen' : 71712.48, 'seventeen' : 84473.48, \
                'eightteen' : 727284.84, 'nineteen' : 63007.18, 'twenty' : 51568.47, \
                'twentyone' : 37697.50, 'twentytwo' : 20883.22, 'twentythree' : 2695.94}

    info = analyzeInfo()
    dailyHrInc = info.findAvgHours(hourRev)
    morn = info.avgMornTotal(dailyHrInc)
    night = info.avgNightTotal(dailyHrInc)

    print morn
    print night
    current_expenditures = info.curSpent()

if __name__=='__main__':
    run()
