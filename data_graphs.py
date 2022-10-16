import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('homebuyerinfo.csv')

approved_count = []
for i in range(len(df['ApprovedOrNot'])):
    if df['ApprovedOrNot'][i] == 'N':
        approved_count.append(0)
    else:
        approved_count.append(1)
df['ApprovedCount'] = approved_count
num_approved = sum(df['ApprovedCount'])

total = df.shape[0]
data = [num_approved, total - num_approved]
series = pd.Series(data, index=("Approved", "Not Approved"))
series.plot.pie(label="", title="% Approved")
plt.savefig('approved_percent.png')
plt.show(block=True)

credit_score_count = []
ltv_count = []
dti_count = []
fedti_count = []

for i in range(len(df)):
    if 'approved' in df['WhyNotApproved'][i]:
        pass
    if 'credit score' in df['WhyNotApproved'][i]:
        credit_score_count.append(1)
    else:
        credit_score_count.append(0)
    if 'LTV' in df['WhyNotApproved'][i]:
        ltv_count.append(1)
    else:
        ltv_count.append(0)
    if 'DTI' in df['WhyNotApproved'][i]:
        dti_count.append(1)
    else:
        dti_count.append(0)
    if 'FEDTI' in df['WhyNotApproved'][i]:
        fedti_count.append(1)
    else:
        fedti_count.append(0)

df['CreditScoreCount'] = credit_score_count
df['LTVCount'] = ltv_count
df['DTICount'] = dti_count
df['FEDTICount'] = fedti_count

num_credit_score = sum(df['CreditScoreCount'])
num_ltv = sum(df['LTVCount'])
num_dti = sum(df['DTICount'])
num_fedti = sum(df['FEDTICount'])

data2 = [num_credit_score, num_ltv, num_dti, num_fedti]
series2 = pd.Series(data2, index=('Credit Score', 'LTV', 'DTI', 'FEDTI'))
series2.plot.pie(label="", title="Not Approved Breakdown")
plt.savefig('whynotapproved.png')
plt.show(block=True)