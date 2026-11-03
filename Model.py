import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

#data cleaning and structuring

def clean_statement(data):
    """Treat values of 0 as missing (left empty)."""
    return data.replace(0, np.nan)


def load_statement(path):
    """Load a statement CSV (variables in the first column, periods left to right)
    and return it with one row per period end date and one column per variable."""
    raw = pd.read_csv(path, sep=";", header=None, index_col=0, dtype=str, encoding="utf-8-sig")
    labels = list(raw.index)
    dates = pd.to_datetime(raw.iloc[labels.index("Period End Date")], format="%d-%m-%Y")
    data = raw.iloc[labels.index("Field Name") + 1:]
    data = data.dropna(how="all")  # section headers have no values

    # repeated labels (one per share class) get a suffix: "X", "X (2)", ...
    counts = data.groupby(level=0).cumcount() + 1
    data.index = [label if n == 1 else f"{label} ({n})" for label, n in zip(data.index, counts)]

    # "11’161" -> 11161, "12.1%" -> 0.121
    data = data.apply(lambda col: col.str.replace("’", "", regex=False))
    is_pct = data.apply(lambda col: col.str.endswith("%", na=False))
    data = data.apply(lambda col: pd.to_numeric(col.str.rstrip("%"), errors="coerce"))
    data = data.where(~is_pct, data / 100)

    data.columns = dates
    data = data.T
    data.index.name = "Period End Date"
    data = data[~data.index.duplicated()]  # same period exported twice
    data.insert(0, "Company Name", raw.iloc[labels.index("Company Name"), 0])
    return clean_statement(data.sort_index())






#data collection


##ABB
ABB_balancesheet = load_statement("data/ABB/ABB_balancesheet.csv")
ABB_cashflow = load_statement("data/ABB/ABB_cashflow.csv")
ABB_income = load_statement("data/ABB/ABB_income.csv")

##Alcon
Alcon_balancesheet = load_statement("data/Alcon/Alcon_balancesheet.csv")
Alcon_cashflow = load_statement("data/Alcon/Alcon_cashflow.csv")
Alcon_income = load_statement("data/Alcon/Alcon_income.csv")

##Amrize
Amrize_balancesheet = load_statement("data/Amrize/Amrize_balancesheet.csv")
Amrize_cashflow = load_statement("data/Amrize/Amrize_cashflow.csv")
Amrize_income = load_statement("data/Amrize/Amrize_income.csv")

##Galderma
Galderma_balancesheet = load_statement("data/Galderma/Galderma_balancesheet.csv")
Galderma_cashflow = load_statement("data/Galderma/Galderma_cashflow.csv")
Galderma_income = load_statement("data/Galderma/Galderma_income.csv")

##Geberit
Geberit_balancesheet = load_statement("data/Geberit/Geberit_balancesheet.csv")
Geberit_cashflow = load_statement("data/Geberit/Geberit_cashflow.csv")
Geberit_income = load_statement("data/Geberit/Geberit_income.csv")

##Givaudan
Givaudan_balancesheet = load_statement("data/Givaudan/Givaudan_balancesheet.csv")
Givaudan_cashflow = load_statement("data/Givaudan/Givaudan_cashflow.csv")
Givaudan_income = load_statement("data/Givaudan/Givaudan_income.csv")

##Holcim
Holcim_balancesheet = load_statement("data/Holcim/Holcim_balancesheet.csv")
Holcim_cashflow = load_statement("data/Holcim/Holcim_cashflow.csv")
Holcim_income = load_statement("data/Holcim/Holcim_income.csv")

##Logitech
Logitech_balancesheet = load_statement("data/Logitech/Logitech_balancesheet.csv")
Logitech_cashflow = load_statement("data/Logitech/Logitech_cashflow.csv")
Logitech_income = load_statement("data/Logitech/Logitech_income.csv")

##Lonza
Lonza_balancesheet = load_statement("data/Lonza/Lonza_balancesheet.csv")
Lonza_cashflow = load_statement("data/Lonza/Lonza_cashflow.csv")
Lonza_income = load_statement("data/Lonza/Lonza_income.csv")

##Nestle
Nestle_balancesheet = load_statement("data/Nestle/Nestle_balancesheet.csv")
Nestle_cashflow = load_statement("data/Nestle/Nestle_cashflow.csv")
Nestle_income = load_statement("data/Nestle/Nestle_income.csv")

##Novartis
Novartis_balancesheet = load_statement("data/Novartis/Novartis_balancesheet.csv")
Novartis_cashflow = load_statement("data/Novartis/Novartis_cashflow.csv")
Novartis_income = load_statement("data/Novartis/Novartis_income.csv")

##Partners Group
Partners_balancesheet = load_statement("data/PartnersGroup/Partners_balancesheet.csv")
Partners_cashflow = load_statement("data/PartnersGroup/Partners_cashflow.csv")
Partners_income = load_statement("data/PartnersGroup/Partners_income.csv")

##Richemont
Richemont_balancesheet = load_statement("data/Richemont/Richemont_balancesheet.csv")
Richemont_cashflow = load_statement("data/Richemont/Richemont_cashflow.csv")
Richemont_income = load_statement("data/Richemont/Richemont_income.csv")

##Roche
Roche_balancesheet = load_statement("data/Roche/Roche_balancesheet.csv")
Roche_cashflow = load_statement("data/Roche/Roche_cashflow.csv")
Roche_income = load_statement("data/Roche/Roche_income.csv")

##Sandoz
Sandoz_balancesheet = load_statement("data/Sandoz/Sandoz_balancesheet.csv")
Sandoz_cashflow = load_statement("data/Sandoz/Sandoz_cashflow.csv")
Sandoz_income = load_statement("data/Sandoz/Sandoz_income.csv")

##Sika
Sika_balancesheet = load_statement("data/Sika/Sika_balancesheet.csv")
Sika_cashflow = load_statement("data/Sika/Sika_cashflow.csv")
Sika_income = load_statement("data/Sika/Sika_income.csv")

##Swiss Life
SwissLife_balancesheet = load_statement("data/SwissLife/SwissLife_balancesheet.csv")
SwissLife_cashflow = load_statement("data/SwissLife/SwissLife_cashflow.csv")
SwissLife_income = load_statement("data/SwissLife/SwissLife_income.csv")


##Swiss RE
SwissRe_balancesheet = load_statement("data/SwissRe/SwissRe_balancesheet.csv")
SwissRe_cashflow = load_statement("data/SwissRe/SwissRe_cashflow.csv")
SwissRe_income = load_statement("data/SwissRe/SwissRe_income.csv")

##UBS
UBS_balancesheet = load_statement("data/UBS/UBS_balancesheet.csv")
UBS_cashflow = load_statement("data/UBS/UBS_cashflow.csv")
UBS_income = load_statement("data/UBS/UBS_income.csv")


##Zurich Insurance
ZurichIns_balancesheet = load_statement("data/ZurichIns/ZurichIns_balancesheet.csv")
ZurichIns_cashflow = load_statement("data/ZurichIns/ZurichIns_cashflow.csv")
ZurichIns_income = load_statement("data/ZurichIns/ZurichIns_income.csv")


#defining variables
balancesheets = [ABB_balancesheet, Alcon_balancesheet, Amrize_balancesheet, Galderma_balancesheet,
                 Geberit_balancesheet, Givaudan_balancesheet, Holcim_balancesheet, Logitech_balancesheet,
                 Lonza_balancesheet, Nestle_balancesheet, Novartis_balancesheet, Partners_balancesheet,
                 Richemont_balancesheet, Roche_balancesheet, Sandoz_balancesheet, Sika_balancesheet,
                 SwissLife_balancesheet, SwissRe_balancesheet, UBS_balancesheet, ZurichIns_balancesheet]
incomes = [ABB_income, Alcon_income, Amrize_income, Galderma_income, Geberit_income, Givaudan_income,
           Holcim_income, Logitech_income, Lonza_income, Nestle_income, Novartis_income, Partners_income,
           Richemont_income, Roche_income, Sandoz_income, Sika_income, SwissLife_income, SwissRe_income,
           UBS_income, ZurichIns_income]
cashflows = [ABB_cashflow, Alcon_cashflow, Amrize_cashflow, Galderma_cashflow, Geberit_cashflow,
             Givaudan_cashflow, Holcim_cashflow, Logitech_cashflow, Lonza_cashflow, Nestle_cashflow,
             Novartis_cashflow, Partners_cashflow, Richemont_cashflow, Roche_cashflow, Sandoz_cashflow,
             Sika_cashflow, SwissLife_cashflow, SwissRe_cashflow, UBS_cashflow, ZurichIns_cashflow]


def company_sheet(statements, variable):
    """One row per company, one column per quarter (e.g. 2025Q1), for a single variable."""
    sheet = pd.DataFrame({s["Company Name"].iloc[0]: s[variable] for s in statements}).T
    sheet = sheet[sorted(sheet.columns)]
    sheet.columns = sheet.columns.to_period("Q").astype(str)
    sheet.index.name = "Company Name"
    return sheet


def semester_sheet(statements, variable, flow=False):
    """One row per company, one column per semester (S1 = Jan-Jun, S2 = Jul-Dec), for a single variable.
    Stocks (book value) take the last report in the semester; flows (earnings, dividends)
    add up the quarters, since quarterly reporters report each quarter separately."""
    rows = {}
    for s in statements:
        dates = s.index
        semester = dates.year.astype(str) + np.where(dates.month <= 6, "S1", "S2")
        grouped = s[variable].groupby(semester)
        rows[s["Company Name"].iloc[0]] = grouped.sum(min_count=1) if flow else grouped.last()
    sheet = pd.DataFrame(rows).T
    # every semester gets a column, so shifting by one column is always half a year
    first, last = sheet.columns.min(), sheet.columns.max()
    semesters = [f"{y}{h}" for y in range(int(first[:4]), int(last[:4]) + 1) for h in ("S1", "S2")]
    sheet = sheet.reindex(columns=[c for c in semesters if first <= c <= last])
    sheet.index.name = "Company Name"
    return sheet


#creating and filling main csv files
bookvalue = semester_sheet(balancesheets, "Shareholders' Equity - Attributable to Parent Shareholders - Total")
##earnings = semester_sheet(incomes, "Income Available to Common Shares", flow=True)
dividends = semester_sheet(cashflows, "Dividends Paid - Cash - Total - Cash Flow", flow=True)
govyield = pd.read_csv("data/Sheets/10govyield.csv", sep=";", skiprows=[1], index_col=0, encoding="utf-8-sig")
govyield.index = pd.to_datetime(govyield.index, format="%d.%m.%Y")
riskfreerate = govyield["CH_RR)"].sort_index()
# same semester labels as the statement sheets; keep only the latest quote in each semester
semester = riskfreerate.index.year.astype(str) + np.where(riskfreerate.index.month <= 6, "S1", "S2")
riskfreerate = riskfreerate.groupby(semester).last()

bv_prev = bookvalue.shift(1, axis=1)   # book value one semester earlier

# book value on top, t-1 block appended below it
pd.concat({"Book Value": bookvalue, "Book Value t-1": bv_prev},
          names=["Variable", "Company Name"]).to_csv("data/Sheets/BalanceSheet.csv")
#earnings.to_csv("data/Sheets/IncomeSheet.csv")
dividends.to_csv("data/Sheets/Cashflow.csv")




###Model----------------------------------------------------------------------

###1) Calculate Risk/Discount Factor (R_f) - calculate cost of equity through CAPm
    #expected returns = R_f + beta(R_m - R_f)
R_f = riskfreerate + 1
#print(R_f.to_string())

###2) Calculate beta

###3) Clean Surplus calcuted for income/earnings, so that relationship holds
CalcEarnings = bookvalue - bv_prev + dividends.fillna(0)
CalcEarnings.to_csv("data/Sheets/CalcEarnings.csv"
                    )
# no dividend paid in a period -> count as 0 (only book values may leave a gap)

###4) Abnormal Earnings
abnormalEarnings = CalcEarnings - (riskfreerate*bv_prev)
abnormalEarnings.to_csv("data/Sheets/abnormalEarnings.csv")
abnormalEarnings_prev = abnormalEarnings.shift(1)   # abnormal earnings one semester earlier

###5) w and y

start="2013S1"
end ="2026S2"
#relevant because this is time range of risk free rate

abnormalEarnings = abnormalEarnings.sort_index(axis=1)       # semesters in chronological order
abnormalEarnings_prev = abnormalEarnings.shift(1, axis=1)    # previous semester, same firm

mask = (abnormalEarnings.columns >= start) & (abnormalEarnings.columns <= end)   # semesters in the regression window

omegas = {}
for firm in abnormalEarnings.index:
    data = pd.concat(
        [abnormalEarnings.loc[firm, mask], abnormalEarnings_prev.loc[firm, mask]],
        axis=1, keys=["y", "x"]
    ).dropna()

    if len(data) < 3:              # too few observations to estimate
        omegas[firm] = float("NaN")
        continue

    res = sm.OLS(data["y"], data["x"]).fit()
    omegas[firm] = res.params.iloc[0]

omega = pd.Series(omegas, name="omega")
for i in range(len(omega)):
    if omega.iloc[i] >= 1:
        omega.iloc[i] = 1
    elif omega.iloc[i] < 0:
        omega.iloc[i] = 0

omega.to_csv("data/Sheets/omega.csv")
#print(omega)

###6) Calculate the valuation multipliers (alpha 1 & 2)
alpha1 = (omega)/(R_f["2026S1"] - omega)
alpha1.name = "alpha1"
alpha1.to_csv("data/Sheets/alpha1.csv")
print(R_f["2026S1"])
#print(alpha1)

###7) Calculate Equity Value through closed-form model
P_t_cf = bookvalue + abnormalEarnings.mul(alpha1, axis=0)   # align alpha1 on firms (rows), not semesters
P_t_cf.to_csv("data/Sheets/EquityValueCF.csv")
#print(P_t_cf)

###8) Calculate Earnings Multiplier 
phi = R_f["2026S1"]/(R_f["2026S1"]-1)   # same R_f as alpha1 and k
pd.Series({"phi": phi}).to_csv("data/Sheets/phi.csv")
#print(phi)

###9) Calculate Weight-Factor
k = ((R_f["2026S1"] - 1)*omega)/(R_f["2026S1"] - omega)   # same R_f as alpha1, one k per firm
k.name = "k"
k.to_csv("data/Sheets/weightFactor.csv")
#print(k)

###10) Calculate Equity Value though hybrid stock model (== Equity Value from closed-form model)
P_t_hd = (phi*CalcEarnings - dividends.fillna(0)).mul(k, axis=0) + bookvalue.mul(1-k, axis=0)
P_t_hd.to_csv("data/Sheets/EquityValueHybrid.csv")
print(P_t_hd)

###11) Comparison between both bookvalues
P_t_cf, P_t_hd = P_t_cf.align(P_t_hd)   # same firms and semesters in both
P_t_diff = P_t_cf - P_t_hd               # 0 where both models agree
P_t_diff.to_csv("data/Sheets/EquityValueDiff.csv")
models_match = pd.DataFrame(np.isclose(P_t_cf, P_t_hd), index=P_t_cf.index, columns=P_t_cf.columns)   # tolerant to float rounding
models_match.to_csv("data/Sheets/EquityValueMatch.csv")
#print(models_match["2026S1"])


###plotting Model
#plt.scatter()


