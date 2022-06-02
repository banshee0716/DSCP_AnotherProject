import csv
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats
from scipy.stats import describe
import seaborn as sns


Prostate_Cancer,Lung_Cancer,Colorectal_Cancer,Female_Breast_Cancer,Cervical_Cancer=np.zeros(19,dtype=float),np.zeros(19,dtype=float),np.zeros(19,dtype=float),np.zeros(19,dtype=float),np.zeros(19,dtype=float)
CO2=[226978,229927,237651,248402,257883,266460,276159,279800,266594,252506,270148,276282,272755,273797,276311,275835,279705,284812,282842]

with open('歷年腫瘤.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    count=0
  # 以迴圈輸出每一列
    for row in rows:
        if count != 0:
            Prostate_Cancer[count-1]=float(row[1])
            Lung_Cancer[count-1]=float(row[2])
            Colorectal_Cancer[count-1]=float(row[3])
            Female_Breast_Cancer[count-1]=float(row[4])
            Cervical_Cancer[count-1]=float(row[5])

            #Prostate_Cancer.append(float(row[1]))
            #Lung_Cancer.append(float(row[2]))
            #Colorectal_Cancer.append(float(row[3]))
            #Female_Breast_Cancer.append(float(row[4]))
            #Cervical_Cancer.append(float(row[5]))
        count+=1

type=[]
dat = {'CO2':CO2,'Prostate Cancer':Prostate_Cancer,'Lung Cancer':Lung_Cancer,'Colorectal Cancer':Colorectal_Cancer,'Female Breast Cancer':Female_Breast_Cancer,'Cervical Cancer':Cervical_Cancer}
df = pd.DataFrame(dat)

for i in range(2000,2019):
    type.append(i)
#print (type)

plt.style.use("ggplot")
sns.set()
plt.figure(figsize=(10,7),dpi=100)
plt.plot(type, Prostate_Cancer,c = "red",label='Prostate Cancer',marker=".")
plt.plot(type, Lung_Cancer, c ="green",label='Lung Cancer',marker=".")
plt.plot(type, Colorectal_Cancer,c = "blue",label="Colorectal Cancer",marker=".")
plt.plot(type, Female_Breast_Cancer,"yellow",label="Female Breast Cancer",marker=".")
plt.plot(type, Cervical_Cancer,c = "black",label="Cervical Cancer",marker=".")
plt.xlim(2000, 2018)
#畫線，plt.plot(x, y, c)參數分別為x軸資料、y軸資料、線顏色 = 綠色及線型式 = -.

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.title('歷年惡性腫瘤發生率')
plt.xlabel("年份")
plt.ylabel("數量(每十萬人)")
plt.legend()
plt.show()

plt.style.use("ggplot")
sns.set()
plt.figure(figsize=(10,10))
plt.bar(type,Prostate_Cancer,color="red",label="Prostate Cancer")
plt.bar(type,Lung_Cancer,color="green",bottom=np.array(Prostate_Cancer),label="Lung Cancer")
plt.bar(type,Colorectal_Cancer,color="blue",bottom=np.array(Prostate_Cancer)+np.array(Lung_Cancer),label="Colorectal Cancer")
plt.bar(type, Female_Breast_Cancer,color="yellow",bottom=np.array(Prostate_Cancer)+np.array(Lung_Cancer)+np.array(Colorectal_Cancer),label="Female Breast Cancer")
plt.bar(type, Cervical_Cancer,color = "black",bottom=np.array(Prostate_Cancer)+np.array(Lung_Cancer)+np.array(Colorectal_Cancer)+np.array(Female_Breast_Cancer),label="Cervical Cancer")
plt.xlim(2000, 2018)
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.xlabel("年份")
plt.ylabel("數量(每十萬人)")
plt.legend()
plt.show()



print(df.describe())

print(describe(Prostate_Cancer))
print(describe(Lung_Cancer))
print(describe(Colorectal_Cancer))
print(describe(Female_Breast_Cancer))
print(describe(Cervical_Cancer))
print(describe(CO2),'\n')

res=[]
res_name=['Prostate_Cancer','Lung_Cancer','Colorectal_Cancer' ,'Female_Breast_Cancer','Cervical_Cancer']
res.append(Prostate_Cancer)
res.append(Lung_Cancer)
res.append(Colorectal_Cancer)
res.append(Female_Breast_Cancer)
res.append(Cervical_Cancer)
pearson_list=[]
#儲存p值
for i in range (5):
    for j in range (i,5):
        if i == j:
          continue
        else:
          #ttest_list.append(ttest_ind(res[i],res[j]).pvalue)
          pearson_list.append(scipy.stats.pearsonr(res[i], res[j]))


count=0
'''
for i in range (5):
    for j in range (i,5):
        if i == j:
          continue
        else:
          print(res_name[i] , '與' , res_name[j] , '獨立樣本t檢定的p值為' , ttest_list[count])

          if (ttest_list[count])<0.05:
              print ('落於拒絕域，拒絕虛無假設')

          else:
              print ('落於接受域，不拒絕虛無假設\n')
          count += 1
print("t檢定結束\n")
'''
#迴歸
#fig, axes = plt.subplots(3, 2)

#fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True)
sns.lmplot(x = "CO2", y = "Prostate Cancer", data = df)#,ax = ax1),ci=0.95#,)
sns.lmplot(x = "CO2", y = "Lung Cancer", data = df)#,ax = ax1),ci=0.95#)
sns.lmplot(x = "CO2", y = "Colorectal Cancer", data = df)#,ax = ax2)#,ci=0.95#)
sns.lmplot(x = "CO2", y = "Female Breast Cancer", data = df)#,ci=0.95#,ax = axes[1][1])
sns.lmplot(x = "CO2", y = "Cervical Cancer", data = df)#,ci=0.95#,ax = axes[2][0])
plt.show()
#相關係數
plt.figure(figsize=(10,10))
sns.heatmap(df.corr())
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.show()

for i in range(5):
    print(res_name[i] , '與CO2 相關係數的p值為' , scipy.stats.pearsonr(res[i], CO2)[1])
    if (scipy.stats.pearsonr(res[i], CO2)[1])<0.05:
        print ('落於拒絕域，拒絕虛無假設')
count=0
    #p值等于0，说明接受原假设概率非常小，几乎可认为两者有相关性。

for i in range(5):
    result = scipy.stats.linregress(CO2,res[i])
    print(result)

'''
for i in range (5):
    for j in range (i,5):
        if i == j:
          continue
        else:
          print(res_name[i] , '與' , res_name[j] , '相關係數的p值為' , pearson_list[count][1])

          if (pearson_list[count][1])<0.05:
              print ('落於拒絕域，拒絕虛無假設')

          else:
              print ('落於接受域，不拒絕虛無假設\n')
          count += 1
'''

#df_transposed = df.T # or df1.transpose()
#print(df_transposed)



#print(pearson_list)
#print(scipy.stats.pearsonr(, Prostate_Cancer).pvalue)





#獨立樣本t檢定,
#想想看有沒有因子可以用來做相關係數分析
#直接用seaborn,scipy跑相關係數跟迴歸分析就好
#考驗不同的癌症發病率，分年度考慮，（但因子變異數）卡方：某一種癌症在不同年度的發病率，或是不同癌症在不同年度