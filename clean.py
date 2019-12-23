import pandas as pd
import numpy as np

mWIG40 = pd.read_csv("mwig40_d.csv")
eleven_B = pd.read_csv("11b_d.csv")
ACP = pd.read_csv("acp_d.csv")
AMC = pd.read_csv("amc_d.csv")
ATT = pd.read_csv("att_d.csv")
BDX = pd.read_csv("bdx_d.csv")
BFT = pd.read_csv("bft_d.csv")
BHW = pd.read_csv("bhw_d.csv")
BNP = pd.read_csv("bnp_d.csv")
BRS = pd.read_csv("brs_d.csv")
CAR = pd.read_csv("car_d.csv")
CIE = pd.read_csv("cie_d.csv")
CIG = pd.read_csv("cig_d.csv")
CLN = pd.read_csv("cln_d.csv")
CMR = pd.read_csv("cmr_d.csv")
DVL = pd.read_csv("dvl_d.csv")
EAT = pd.read_csv("eat_d.csv")
ECH = pd.read_csv("ech_d.csv")
ENA = pd.read_csv("ena_d.csv")
ENG = pd.read_csv("eng_d.csv")
EUR = pd.read_csv("eur_d.csv")
FMF = pd.read_csv("fmf_d.csv")
FTE = pd.read_csv("fte_d.csv")
GPW = pd.read_csv("gpw_d.csv")
TEN = pd.read_csv("ten_d.csv")
GTN = pd.read_csv("gtn_d.csv")
ING = pd.read_csv("ing_d.csv")
KER = pd.read_csv("ker_d.csv")
KRU = pd.read_csv("kru_d.csv")
KTY = pd.read_csv("kty_d.csv")
LVC = pd.read_csv("lvc_d.csv")
LWB = pd.read_csv("lwb_d.csv")
MAB = pd.read_csv("mab_d.csv")
MIL = pd.read_csv("mil_d.csv")
ORB = pd.read_csv("orb_d.csv")
PKP = pd.read_csv("pkp_d.csv")
PLW = pd.read_csv("plw_d.csv")
STP = pd.read_csv("stp_d.csv")
TEN = pd.read_csv("ten_d.csv")
VRG = pd.read_csv("vrg_d.csv")
WPL = pd.read_csv("wpl_d.csv")

database = pd.read_csv("database.csv")

name_abbreviation_mWIG40_dict = {
    'mWIG40': 'mWIG40',
    '11_bit_studios': '11B',
    'Asseco_Poland': 'ACP',
    'Amica': 'AMC',
    'Grupa_Azoty': 'ATT',
    'Budimex': 'BDX',
    'Benefit_Systems': 'BFT',
    'Bank_Handlowy_w_Warszawie': 'BHW',
    'BNP_Paribas_Bank_Polska': 'BNP',
    'Boryszew': 'BRS',
    'Inter_Cars': 'CAR',
    'Ciech': 'CIE',
    'CI_Games': 'CIG',
    'Celon_Pharma': 'CLN',
    'Comarch': 'CMR',
    'Develia': 'DVL',
    'AmRest_Holdings': 'EAT',
    'Echo_Investment': 'ECH',
    'Enea': 'ENA',
    'Energa': 'ENG',
    'Eurocash': 'EUR',
    'Fabryka_Maszyn_Famur': 'FMF',
    'Fabryki_Mebli_Forte': 'FTE',
    'Giełda_Papierów_Wartościowych_w_Warszawie': 'GPW',
    'Globe_Trade_Centre': 'GTC',
    'Getin_Holding': 'GTN',
    'ING_Bank_Śląski': 'ING',
    'Kernel_Holding': 'KER',
    'Kruk': 'KRU',
    'Grupa_Kęty': 'KTY',
    'LiveChat_Software': 'LVC',
    'Lubelski_Węgiel_Bogdanka': 'LWB',
    'Mabion': 'MAB',
    'Bank_Millennium': 'MIL',
    'Orbis': 'ORB',
    'PKP_Cargo': 'PKP',
    'PlayWay': 'PLW',
    'Stalprodukt': 'STP',
    'Ten_Square_Games': 'TEN',
    'VRG': 'VRG',
    'Wirtualna_Polska_Holding': 'WPL'
}

class Parameters:

    def __init__(self, abbreviation=input("Input the abbreviation of the company:")):
        self.source_df = pd.read_csv('%s_d.csv' % abbreviation, delimiter=',')

    def describe_company_df(self):
        print(self.source_df.describe(include='all'))

    def high_price(self):
        high_price = self.source_df['Najwyzszy']
        return high_price

    def low_price(self):
        low_price = self.source_df['Najnizszy']
        return low_price

    def open_price(self):
        open_price = self.source_df['Otwarcie']
        return open_price

    def close_price(self):
        close_price = self.source_df['Zamkniecie']
        return close_price

    def volume_stock(self):
        volume_stock = self.source_df['Wolumen']
        return volume_stock

    def daily_movement(self, abbreviations_of_companies=input("Enter abbreviations of companies: ").split()):
        self.abbreviations_of_companies = [] #?
    #    database = pd.read_csv("database.csv") #duplika

        list_open_close_price = []

        column_headlines = []

        for i in abbreviations_of_companies:
            open_price = database['Open_price_%s' % i]
            close_price = pd.Series(database['Close_price_%s' % i])
            list_open_close_price.append(open_price)
            open_price_subtract = open_price.sub(close_price)
            list_open_close_price.append(open_price_subtract)

            column_headlines.append('Open_price_%s' % i)
            column_headlines.append('Daily_movement_%s' % i)

        daily_movement = pd.concat(list_open_close_price, axis=1)

        daily_movement.columns = column_headlines

        print(abbreviations_of_companies)

        return print(daily_movement.head(20))

    def sum_of_movements(self, abbreviations_of_companies=input("Enter abbreviations of companies: ").split()):
        self.abbreviations_of_companies = [] #?

        for i in abbreviations_of_companies:
            open_price = database['Open_price_%s' % i]
            close_price = pd.Series(database['Close_price_%s' % i])
            open_price_subtract = open_price.sub(close_price)
            price_subtract_sum = np.sum(open_price_subtract)
            x = 'price_subtract_sum for %s: ' % i, price_subtract_sum
            print(x)


    if __init__ == "__main__":
        print("run directly")
    else:
        print("imported into another module")

class DatabaseCreator:

    def __init__(self):
        pass

    def database_creator(self):

        abbreviation_values = name_abbreviation_mWIG40_dict.values()


        pre_column_names = ['Open_price', 'Max', 'Min', 'Close_price', 'Volume']
        df_to_merge_list = []

        for j in abbreviation_values:

            column_names_with_suffix = [(column_headline + '_%s' % j) for column_headline in pre_column_names]

            df_to_merge = pd.read_csv('%s_d.csv' % j,
                                      delimiter=',',
                                      index_col='Data')  # turbowazne

            df_to_merge.columns = column_names_with_suffix


            df_to_merge_list.append(df_to_merge)
            database = pd.concat(df_to_merge_list,
                                 axis=1,
                                 sort=True)  # turbowazne

        return database.to_csv(r'database.csv')

    if __init__ == "__main__":
        print("run directly")
    else:
        print("imported into another module")
