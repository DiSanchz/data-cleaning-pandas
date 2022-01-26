# Data cleaning with pandas
## Project made as part of the Ironhack Data Analytics bootcamp program

This project's aim is to clean a dataset employing mainly python's library Pandas in order to be able to use the data to put at test a series of predefined hypothesis employing by employing only python visualization tools. The dataset that is to be employed is the *"Global Shark Attack"* dataset which contains information on the historical record of shark attacks to humans.

### > The hypotheses:

Hypothesis 1. Shark attacks' fatality rate has fallen over time

Hypothesis 2: Shark attacks' fatality rate is negatively correlated with the level of income per capita of the country where the attack takes place

### > The Data:

- Main source: Global Shark Attack dataset.

Link: [Kaggle](https://www.kaggle.com/teajay/global-shark-attacks)

- Data on GDP per capita: World Bank national accounts data, and OECD National Accounts data files.

Link: [World Bank](https://data.worldbank.org/indicator/NY.GDP.PCAP.KD)

### > Technology Stack:

- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Plotly](https://plotly.com/)
- [RegEx](https://docs.python.org/3/library/re.html) (Regular Expressions)

### > Summary

The focus at the time of cleaning the *Shark Attack* dataset after the conversion into a Pandas DataFrame was on the columns that contained relevant information for the proposed hypothesis. Those were the essentially the columns containing information relative to time (year was the final unit of measurement selected to account for time) location (the country where the attack took place was the one deemed as most useful for the conducted analysis) and wheter the attack was fatal for the victim or not. 

Afterwards, the data on GDP per capita was added <sup>(1)</sup> to the set  and fatality ratios (defined as number of fatal attacks over total attacks) were computed. These fatality ratios were calculated in two ways: 1. On  yearly basis for the period 1946-2018, and 2. On a per-country basis for each country with at least 20 observations <sup>(2)</sup>.

Regardig hypothesis 1, the resusts show that the fatality ratio decreases over time. Regarding hypothesis 2, while for the sample employed a strong linear relation between GDP per capita and fatality ration is not evident, it can be argued that countries with higher income per capita tend to have lower fatality ratios than their lower income counterparts.


(1) The figure of GDP per capita used as refference for the analysis was the average GDP per capita in constant 2015 usd for the sample period (1960-2018).

(2) The countries with less than 20 observations for the sample period (1960-2018) were grouped according to their income level (High, Middle-Upper, Middle-Lower and Low income) except for Micronesia and Spain.