#Tests for some of the functions in the Functions.py file
from Functions import *
df=pd.read_csv('blank.csv', sep=',', index_col=0, parse_dates=True)
def test_total_energy():
    assert round(total_energy(df),7)==20
def test_cost_function():
    assert round(cost_function(df),7)==1.805
def test_list_of_robots():
    assert list_of_robots(df)[:3]==["Robot1","Robot2","Robot3"]
def test_df_update():
    a=create_df(argument='power')
    b=a.copy()
    a=df_update(a,'power')
    assert a.shape[0]> b.shape[0]
