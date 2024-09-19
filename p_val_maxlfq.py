import pandas as pd
from scipy import stats

# load data
df = pd.read_csv('DIA_NN_data.csv')

# function to calculate p-value
def calculate_p_val_maxlfq(row):
    bt_values = pd.to_numeric(row[['Bt1_DIA', 'Bt2_DIA', 'Bt3_DIA']], errors='coerce').dropna()
    st_values = pd.to_numeric(row[['STS1_DIA', 'STS2_DIA', 'STS3_DIA']], errors='coerce').dropna()

    # t-test
    if len(bt_values) > 0 and len(st_values) > 0:
        t_stat, p_val_maxlfq = stats.ttest_ind(bt_values, st_values, equal_var=False)
        return p_val_maxlfq
    else:
        return None

# calculate for each row
df['p_val_maxlfq'] = df.apply(calculate_p_val_maxlfq, axis=1)

# save to new file
df.to_csv('results_with_p_val_maxlfq.tsv', sep='\t', index=False)

# print results
# print(df[['Protein.Names', 'p_val_maxlfq']])
