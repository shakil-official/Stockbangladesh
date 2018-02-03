from bs4 import BeautifulSoup
import requests
import json
import re
import HistoryChart
import Combination
import Profit
import EPSPerQuarter
import TotalNetProfit
import TotalESPUpto
import YearlyNav
import YearlyESP


class AssignObject:
    def __init__(self , url):
        self.url = url
        self.source_code = requests.get(self.url)
        self.plain_text = self.source_code.content
        self.soup = BeautifulSoup(self.plain_text, "lxml")
        #=================================================
        #print(self.soup )


        #self.historyChart = HistoryChart.HistoryChart(self.soup)
        #self.historyChart.historyChart()


        #self.combination = Combination.Combination(self.soup)
        #self.combination.combination()

        #self.profit = Profit.Profit(self.soup)
        #self.profit.profit()

        #self.ESP = EPSPerQuarter.EPSPerQuarter(self.soup)
        #self.ESP.epsPerQuarter()

        #self.totalNetProfit = TotalNetProfit.TotalNetProfit(self.soup)
        #self.totalNetProfit.totalNetProfit()

        #self.totalESPUpto = TotalESPUpto.TotalESPUpto(self.soup)
        #self.totalESPUpto.totalESPUpto()


        #self.yearlyNav = YearlyNav.YearlyNav(self.soup)
        #self.yearlyNav.yearlyNav()


        self.yearlyESP = YearlyESP.YearlyESP(self.soup)
        self.yearlyESP.yearlyESP()
