
# coding: utf-8

# # LAB 1
# ## 1. Linear regression
# 
# ### 자료 가져오기
# - https://github.com/JWarmenhoven/ISLR-python/blob/master/Notebooks/Data/Hitters.csv
# 
# ### 자료 설명
# - 1986년도부터 1987년도까지의 MLB 자료.
# - 20개의 변수와 322개의 관측값으로 구성
# - 변수설명
#     - AtBat, Hits, HmRun, Runs, RBI, Walks : 1986년도 타수, 안타, 홈런, 득점, 타점, 볼넷 수.
#     - Years : Major leagues에 있던 연수.
#     - CAtBat, CHits, CHmRun, CRuns, CRBI, CWalks : 해당 선수의 총 경력기간 동안의 타격, 안타, 홈런, 득점, 타점, 볼넷 수.
#     - League : A or N, 1986년도 말 American 또는 National 리그.
#     - Division : E or W, 1986년도 동부 또는 서부 리그.
#     - PutOuts, Assists, Errors : 1986년도 아웃 카운트, 어시스트, 실책 수
#     - Salary : 1987년도 연봉
#     - NewLeague : 1987년도 초 American 또는 National 리그.
# 
# 
# ### 데이터 불러오기

# In[1]:


import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
hitters = pd.read_csv("Hitters.csv", index_col = 0)
hitters.head()


# In[2]:


print('data shape:', hitters.shape)
hitters.describe()


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('pinfo sns.barplot')


# In[4]:


counts = hitters['League'].value_counts(normalize = True)
counts


# In[5]:


sns.barplot(x=counts.index, y = counts)
plt.show()


# ###  자료 전처리 1: 결측치 수 확인 및 제거

# In[6]:


hitters.isnull().sum()


# In[7]:


hitters = hitters.dropna(axis = 0)
print(hitters.shape)


# ### 자료 전처리 2: 범주형 변수에 대한 가변수 생성

# In[8]:


hitters1 = pd.get_dummies(hitters, drop_first=True)
print(hitters1.shape)
hitters1.head(3)


# ### 자료 전처리 3: 학습자료/예측자료 분할

# In[9]:


from sklearn.model_selection import train_test_split
train, test = train_test_split(hitters1, test_size = 0.3, random_state = 42)
X_train, y_train = train.drop("Salary", axis = 1), train.Salary
X_train = sm.add_constant(X_train)
X_test, y_test = test.drop("Salary", axis = 1), test.Salary
X_test= sm.add_constant(X_test)


# ### 선형 회귀 모형 적합

# In[10]:


linear_model = sm.OLS(y_train, X_train)
model_fit = linear_model.fit()
print(model_fit.summary())


# In[11]:


train[['League_N', 'NewLeague_N']].corr()


# In[12]:


X_train.drop('const', axis = 1).corr()


# ### 잔차분석
# - 회귀분석의 가정(선형성, 등분산성, 정규성)을 만족하는지 확인하기 위해 잔차분석을 진행.
# 

# In[13]:


# fitted values (need a constant term for intercept)
model_fitted_y = model_fit.fittedvalues
# model residuals
model_residuals = model_fit.resid
# normalized residuals
model_norm_residuals = model_fit.get_influence().resid_studentized_internal
# absolute squared normalized residuals
model_norm_residuals_abs_sqrt = np.sqrt(np.abs(model_norm_residuals))
# absolute residuals
model_abs_resid = np.abs(model_residuals)
# leverage, from statsmodels internals
model_leverage = model_fit.get_influence().hat_matrix_diag
# cook's distance, from statsmodels internals
model_cooks = model_fit.get_influence().cooks_distance[0]


# In[14]:


import matplotlib.pyplot as plt
import seaborn as sns
plot_lm_1 = plt.figure(1)
plot_lm_1.set_figheight(8)
plot_lm_1.set_figwidth(12)
plot_lm_1.axes[0] = sns.residplot(model_fitted_y, 'Salary', data=train, 
                          lowess=True, 
                          scatter_kws={'alpha': 0.5}, 
                          line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
plot_lm_1.axes[0].set_title('Residuals vs Fitted')
plot_lm_1.axes[0].set_xlabel('Fitted values')
plot_lm_1.axes[0].set_ylabel('Residuals')

# annotations
abs_resid = model_abs_resid.sort_values(ascending=False)
abs_resid_top_3 = abs_resid[:3]
for i in abs_resid_top_3.index:
    plot_lm_1.axes[0].annotate(i, 
                               xy=(model_fitted_y[i], 
                                   model_residuals[i]));
plt.show()


# In[15]:


from statsmodels.graphics.gofplots import ProbPlot
QQ = ProbPlot(model_norm_residuals)
plot_lm_2 = QQ.qqplot(line='45', alpha=0.5, color='#4C72B0', lw=1)
plot_lm_2.set_figheight(8)
plot_lm_2.set_figwidth(12)
plot_lm_2.axes[0].set_title('Normal Q-Q')
plot_lm_2.axes[0].set_xlabel('Theoretical Quantiles')
plot_lm_2.axes[0].set_ylabel('Standardized Residuals');
# annotations
abs_norm_resid = np.flip(np.argsort(np.abs(model_norm_residuals)), 0)
abs_norm_resid_top_3 = abs_norm_resid[:3]
for r, i in enumerate(abs_norm_resid_top_3):
    plot_lm_2.axes[0].annotate(i, 
                               xy=(np.flip(QQ.theoretical_quantiles, 0)[r],
                                   model_norm_residuals[i]));
plt.show()


# ### 이상점과 영향점
# - 자료들이 추세와 동떨어져 있는 점을 이상점(outlier)라고 하고, 선형 회귀 분석에서 회귀 결과에 영향을 크게 주는 점을 영향점이라 한다.
# ![outlier1.jpg](attachment:outlier1.jpg)
# - 영향점을 찾는 기준:
# ![influence.jpg](attachment:influence.jpg)

# In[16]:


influences = model_fit.get_influence()
influences.summary_table()


# ### DFFITS을 이용한 영향점 확인 및 제거

# In[17]:


dffits = influences.dffits
print('number of outliers:', sum(abs(dffits[0])> dffits[1]))

train_rm_outliers = train[abs(dffits[0]) <= dffits[1]]
X_rm_outliers, y_rm_outliers =  train_rm_outliers.drop("Salary", axis = 1), train_rm_outliers.Salary


# ### 영향점 제거된 선형회귀모형

# In[18]:


X_rm_outliers = sm.add_constant(X_rm_outliers)
linear_model2 = sm.OLS(y_rm_outliers, X_rm_outliers)
model_fit2 = linear_model2.fit()
print(model_fit2.summary())

model_fitted_y2 = model_fit2.fittedvalues


# In[19]:


plot_lm_2 = plt.figure()
plot_lm_2.set_figheight(4)
plot_lm_2.set_figwidth(6)
plot_lm_2.axes[0] = sns.residplot(model_fitted_y2, 'Salary', data=train_rm_outliers, 
                          lowess=True, 
                          scatter_kws={'alpha': 0.5}, 
                          line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
plot_lm_2.axes[0].set_title('Residuals vs Fitted')
plot_lm_2.axes[0].set_xlabel('Fitted values')
plot_lm_2.axes[0].set_ylabel('Residuals')
plt.show()


# In[20]:


plot_lm_1 = plt.figure()
plot_lm_1.set_figheight(4)
plot_lm_1.set_figwidth(6)
plot_lm_1.axes[0] = sns.residplot(model_fitted_y, 'Salary', data=train, 
                          lowess=True, 
                          scatter_kws={'alpha': 0.5}, 
                          line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
plot_lm_1.axes[0].set_title('Residuals vs Fitted')
plot_lm_1.axes[0].set_xlabel('Fitted values')
plot_lm_1.axes[0].set_ylabel('Residuals')
plot_lm_1.axes[0].set_ylim(-1000, 1000)
plt.show()


# In[21]:


plot_lm_2 = plt.figure()
plot_lm_2.set_figheight(4)
plot_lm_2.set_figwidth(6)
plot_lm_2.axes[0] = sns.residplot(model_fitted_y2, 'Salary', data=train_rm_outliers, 
                          lowess=True, 
                          scatter_kws={'alpha': 0.5}, 
                          line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
plot_lm_2.axes[0].set_title('Residuals vs Fitted')
plot_lm_2.axes[0].set_xlabel('Fitted values')
plot_lm_2.axes[0].set_ylabel('Residuals')
plot_lm_2.axes[0].set_ylim(-1000, 1000)
plt.show()


# ### 평균 반응 및 평균 반응의 신뢰구간

# In[22]:


train_prediction = model_fit.get_prediction(X_test)
print(train_prediction.summary_frame(alpha = 0.05).head())
y_test_pred = model_fit.predict(X_test)


# ### 예측자료에서의 성능 평가

# In[23]:


from statsmodels.tools.eval_measures import mse
y_test_pred1 = model_fit.predict(X_test)
y_test_pred2 = model_fit2.predict(X_test)
print('Test MSE with all train data,',mse(y_test, y_test_pred1))
print('Test MSE without influence data,',mse(y_test, y_test_pred2))


# ### 참고: scikit-learn 라이브러리 이용

# In[24]:


from sklearn import linear_model
lm = linear_model.LinearRegression(fit_intercept=False)
lm.fit(X_train, y_train)
lm.coef_


# In[25]:


y_pred = lm.predict(X_test)
print('Test MSE with scikit learn', mse(y_test, y_pred))


# ## 2. Linear regression with variable selection
# 
# - $R^2 = 1- \frac{SS_{res}}{SS_{tot}}$
# where $SS_{tot} = \sum_i (y_i - \bar{y})^2 $, $ \bar{y} = \frac{1}{n} \sum_i y_i$, $SS_{res} = \sum_i (y_i - \hat{y}_i)^2 = \sum_i e_i^2$.
# 
# - $R^2_{adj} = 1-\frac{n-1}{n-p}(1-R^2)$
# 
# - $ AIC = -2 \text{log-likelihood} +2p$
# - $BIC =  -2\text{log-likelihood} +p \log n$

# ### Adjusted $R^2$을 이용한 최적부분집합 선택

# In[26]:


import itertools
def processSubset(feature_set, X, y):
    # Fit model on feature_set and calculate RSS
    X = X[list(feature_set)]
    X = sm.add_constant(X)
    model = sm.OLS(y,X)
    regr = model.fit()
    adj_r2 = regr.rsquared_adj
    return {"model":regr, "adj_r2":adj_r2}

def getBest(k, X, y):
    results = []
    for combo in itertools.combinations(X.columns[1:], k):
        results.append(processSubset(combo, X, y))
    # Wrap everything up in a nice dataframe
    models = pd.DataFrame(results)
    # Choose the model with the highest RSS
    best_model = models.loc[models['adj_r2'].argmax()]
    print("Processed ", models.shape[0], "models on", k, "predictors")
    # Return the best model, along with some other useful information about the model
    return best_model


# In[27]:


import time
models = pd.DataFrame(columns=["adj_r2", "model"])
tic = time.time()
for i in range(1,10):
    models.loc[i] = getBest(i, X_train, y_train)
toc = time.time()
print("Total elapsed time:", (toc-tic), "seconds.")


# In[28]:


print(models.loc[2, "model"].summary())


# In[29]:


models


# ### AIC을 이용한 전진선택법

# In[30]:


# forward selection using AIC
def forward_selected(data, response):
    """
    Parameters:
    -----------
    data : pandas DataFrame with all possible predictors and response
    response: string, name of response column in data
    Returns:
    --------
    model: an "optimal" fitted statsmodels linear model
           with an intercept
           selected by forward selection
           evaluated by AIC
    """
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score =10000.0, 0.0
    iteration = 0
    while remaining and iteration < len(remaining):
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {} + 1".format(response,
                                           ' + '.join(selected + [candidate]))
            score = smf.ols(formula, data).fit().aic
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop(0)
        if current_score > best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
        iteration = iteration +1
    formula = "{} ~ {} + 1".format(response,' + '.join(selected))
    model = smf.ols(formula, data).fit()
    return model


# In[31]:


model_w_fselect = forward_selected(train, 'Salary')


# In[32]:


print(model_w_fselect.summary())


# In[33]:


print(model_w_fselect.model.formula)


# In[34]:


y_test_pred3 = model_w_fselect.predict(X_test)
print('Test MSE with all train data,',mse(y_test, y_test_pred1))
print('Test MSE with variable selection,',mse(y_test, y_test_pred3))


# ### 참고: Polynomial regression

# In[35]:


poly_reg = smf.ols(formula = 'Salary ~ Hits + CAtBat + I(Walks**2)', data = train).fit()
poly_reg.summary()


# ### BIC을 이용한 후진소거법 직접 해보기
# ## 3. 직접해보기
# - 미국 보스턴시의 주택가격 자료를 사용하여 아래 분석 실행.
#     - 선형회귀분석 및 잔차 분석
#     - 영향점 제거한 선형회귀분석
#     - 변수선택법(best subset selection, 전진선택법, 후진선택법)
#     
# ### Boston 자료 설명
# - 자료 수는 506이고, 총 14개의 변수로 이루어져있다.
# - 설명 변수: 마을의 평균 범죄율 (crim), 주거지 비율 (zn), 상업용지비율 (indus), 강 인접여부 (chas), 질소산화물의 농도 (nox), 집 당 평균 방의 수 (rm), 자가거주 주택 비율 (age), 보스턴의 5개 고용 중심지와의 가중 평균 거리 (dis), 고속도로 접근 지수 (rad), 10000달러 당 재산세 비율 (tax), 마을의 교사당 학생 비율 (ptratio), 마을의 흑인 비율 (black), 하층민의 비율 (lstat)
# - 반응변수: 자가거주 주택의 중앙값 (medv)
# 
# ### 데이터 불러오기

# In[36]:


Boston = pd.read_csv("Boston.csv")
print('Data shape:', Boston.shape)
Boston = Boston.iloc[:, 1:]
Boston.head()

