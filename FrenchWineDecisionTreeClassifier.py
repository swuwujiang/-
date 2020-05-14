#coding:gbk
"""
����Ŀ�꣺���þ������㷨���з���
���ߣ��⽭
���ڣ�2020.05.14
"""
 # ������Ҫ�õĿ�
import pandas as pd          
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sb
#%matplotlib inline

# ��������
df = pd.read_csv('frenchwine.csv')
df.columns = ['species', 'magnesium','ash','alcalinity_ash','alcohol', 'mailc_acid'  ]

# �鿴ǰ5������
df.head()
print(df.head()) 

# �鿴����������ͳ����Ϣ
df.describe()
print(df.describe())

#���ݵĿ��ӻ� 
def scatter_plot_by_category(feat, x, y): 
    alpha = 0.5
    gs = df.groupby(feat)
    cs = cm.rainbow(np.linspace(0, 1, len(gs)))
    for g, c in zip(gs, cs):
        plt.scatter(g[1][x], g[1][y], color=c, alpha=alpha)

plt.figure(figsize=(20,5))
plt.subplot(131)
scatter_plot_by_category('species', 'mailc_acid', 'alcohol')
plt.xlabel('mailc_acid')
plt.ylabel('alcohol')
plt.title('species')
plt.show()

#����seaborn���������Iris����ͬ����ͼ
plt.figure(figsize=(20, 10)) 
for column_index, column in enumerate(df.columns):
    if column == 'species':
        continue
    plt.subplot(3, 2, column_index + 1)
    sb.violinplot(x='species', y=column, data=df)
plt.show()

# ���ȶ����ݽ����з֣������ֳ�ѵ�����Ͳ��Լ�
from sklearn.cross_validation import train_test_split #����sklearn���н�����飬����ѵ�����Ͳ��Լ�
all_inputs = df[['alcohol', 'mailc_acid',
                             'ash', 'alcalinity_ash','magnesium']].values
all_species = df['species'].values

(X_train,
 X_test,
 Y_train,
 Y_test) = train_test_split(all_inputs, all_species, train_size=0.8, random_state=1)#80%������ѡΪѵ����

# ʹ�þ������㷨����ѵ��
from sklearn.tree import DecisionTreeClassifier #����sklearn���е�DecisionTreeClassifier������������

# ����һ������������
decision_tree_classifier = DecisionTreeClassifier()

# ѵ��ģ��
model = decision_tree_classifier.fit(X_train, Y_train)
# ���ģ�͵�׼ȷ��
print(decision_tree_classifier.score(X_test, Y_test)) 

# ʹ��ѵ����ģ�ͽ���Ԥ��
print(X_test[0:3])
model.predict(X_test[0:3])

# �Խ�������ı�ʾ
def a():
	result = []
	for i in model.predict(X_test[0:3]):
		if i == 'Zinfandel':
			result.append('������')
		elif i == 'Syrah':
			result.append('����')
		elif i == 'Sauvignon':
			result.append('��ϼ��')
	return result

# print(model.predict(X_test[0:3]))#������ԵĽ���������ģ��Ԥ��Ľ��
print(a())
