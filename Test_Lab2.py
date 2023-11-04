import  Lab2
def test_find_min_max():
    result = []
    input_value = [1, 2, 3, 4, 5]
    test = (1,5)

    result = Lab2.find_min_max(input_value)
    assert result == test
def test_avg():
    result =[]
    input_value =[2,2]
    test= (2.0)
    result = Lab2.calc_average(input_value)
    assert (result == test)
def test_median():
    result=[]
    input_value=[1,2,3,4,5,6,7]
    test= 4
    result =Lab2.calc_median_temperature(input_value)
    assert (result ==test)