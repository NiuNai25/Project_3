import numpy as np
import pickle
import random

from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/')
@app.route('/index')

def web_app():
        Working_Class = [{'value': 0, 'name':"Federal-gov"},
                {'value': 1, 'name':"Local-gov"},
                {'value': 2, 'name':"Never-worked"},
                {'value': 3, 'name':"Private"},
                {'value': 4, 'name':"Self-emp-inc"},
                {'value': 5, 'name':"Self-emp-not-inc"},
                {'value': 6, 'name':"State-gov"},
                {'value': 7, 'name':"Without-pay"}]
        Education = [{'value':0, 'name':'10th'},
                 {'value':1, 'name':'11th'},
                 {'value':2, 'name':'12th'},
                 {'value':3, 'name':'1st-4th'},
                 {'value':4, 'name':'5th-6th'},
                 {'value':5, 'name':'7th-8th'},
                 {'value':6, 'name':'9th'},
                 {'value':7, 'name':'Assoc-acdm'},
                 {'value':8, 'name':'Assoc-voc'},
                 {'value':9, 'name':'Bachelors'},
                 {'value':10, 'name':'Doctorate'},
                 {'value':11, 'name':'HS-grad'},
                 {'value':12, 'name':'Masters'},
                 {'value':13, 'name':'Preschool'},
                 {'value':14, 'name':'Prof-school'},
                 {'value':15, 'name':'16 - Some-college'}]
        Marital_Status = [{'value':0, 'name':'Divorced'},
                 {'value':1, 'name':'Married'},
                 {'value':2, 'name':'Not married'}]                
        Occupation = [{'value':0, 'name':'Adm-clerical'},
                 {'value':1, 'name':'Armed-Forces'},
                 {'value':2, 'name':'Craft-repair'},
                 {'value':3, 'name':'Exec-managerial'},
                 {'value':4, 'name':'Farming-fishing'},
                 {'value':5, 'name':'Handlers-cleaners'},
                 {'value':6, 'name':'Machine-op-inspct'},
                 {'value':7, 'name':'Other-service'},
                 {'value':8, 'name':'Priv-house-serv'},
                 {'value':9, 'name':'Prof-specialty'},
                 {'value':10, 'name':'Protective-serv'},
                 {'value':11, 'name':'Sales'},
                 {'value':12, 'name':'Tech-support'},
                 {'value':13, 'name':'Transport-moving'}]
        Relationship = [{'value':0, 'name':'Husband'},
                 {'value':1, 'name':'Not-in-family'},
                 {'value':2, 'name':'Other-relative'},
                 {'value':3, 'name':'Own-child'},
                 {'value':4, 'name':'Unmarried'},
                 {'value':5, 'name':'Wife'}]  
        Race = [{'value':1, 'name':'Asian'},
                    {'value':2, 'name':'Black'},
                    {'value':3, 'name':'Other'},
                    {'value':4, 'name':'White'}]        
        Native_Country = [{'value':0, 'name': "Cambodia"},
                    {'value':1, 'name': "Canada"},
                    {'value':2, 'name': "China"},
                    {'value':3, 'name': "Columbia"},
                    {'value':4, 'name': "Cuba"},
                    {'value':5, 'name': "Dominican Republic" },
                    {'value':6, 'name': "Ecuador" },
                    {'value':7, 'name': "El Salvadorr" },
                    {'value':8, 'name': "England" },
                    {'value':9, 'name': "France" },
                    {'value':10, 'name': "Germany" },
                    {'value':11, 'name': "Greece" },
                    {'value':12, 'name': "Guatemala" },
                    {'value':13, 'name': "Haiti" },
                    {'value':14, 'name': "Netherlands" },
                    {'value':15, 'name': "Honduras" },
                    {'value':16, 'name': "HongKong" },
                    {'value':17, 'name': "Hungary" },
                    {'value':18, 'name': "India" },
                    {'value':19, 'name': "Iran" },
                    {'value':20, 'name': "Ireland" },
                    {'value':21, 'name': "Italy" },
                    {'value':22, 'name': "Jamaica" },
                    {'value':23, 'name': "Japan" },
                    {'value':24, 'name': "Laos" },
                    {'value':25, 'name': "Mexico" },
                    {'value':26, 'name': "Nicaragua" },
                    {'value':27, 'name': "Outlying-US(Guam-USVI-etc)" },
                    {'value':28, 'name': "Peru" },
                    {'value':29, 'name': "Philippines" },
                    {'value':30, 'name': "Poland" },
                    {'value':31, 'name': "Portugal" },
                    {'value':32, 'name': "Puerto-Rico" },
                    {'value':33, 'name': "Scotland" },
                    {'value':34, 'name': "South" },
                    {'value':35, 'name': "Taiwan" },
                    {'value':36, 'name': "Thailand" },
                    {'value':37, 'name': "Trinadad&Tobago" },
                    {'value':38, 'name': "United States" },
                    {'value':39, 'name': "Vietnam" }]                        
        return render_template("index.html",
        Working_Class=Working_Class
        ,Education=Education
        ,Marital_Status=Marital_Status
        ,Occupation = Occupation
        ,Relationship = Relationship
        ,Race = Race
        ,Native_Country = Native_Country)



#prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,12)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
        Working_Class = [{'value': 0, 'name':"Federal-gov"},
                {'value': 1, 'name':"Local-gov"},
                {'value': 2, 'name':"Never-worked"},
                {'value': 3, 'name':"Private"},
                {'value': 4, 'name':"Self-emp-inc"},
                {'value': 5, 'name':"Self-emp-not-inc"},
                {'value': 6, 'name':"State-gov"},
                {'value': 7, 'name':"Without-pay"}]
        Education = [{'value':0, 'name':'10th'},
                 {'value':1, 'name':'11th'},
                 {'value':2, 'name':'12th'},
                 {'value':3, 'name':'1st-4th'},
                 {'value':4, 'name':'5th-6th'},
                 {'value':5, 'name':'7th-8th'},
                 {'value':6, 'name':'9th'},
                 {'value':7, 'name':'Assoc-acdm'},
                 {'value':8, 'name':'Assoc-voc'},
                 {'value':9, 'name':'Bachelors'},
                 {'value':10, 'name':'Doctorate'},
                 {'value':11, 'name':'HS-grad'},
                 {'value':12, 'name':'Masters'},
                 {'value':13, 'name':'Preschool'},
                 {'value':14, 'name':'Prof-school'},
                 {'value':15, 'name':'16 - Some-college'}]
        Marital_Status = [{'value':0, 'name':'Divorced'},
                 {'value':1, 'name':'Married'},
                 {'value':2, 'name':'Not married'}]                
        Occupation = [{'value':0, 'name':'Adm-clerical'},
                 {'value':1, 'name':'Armed-Forces'},
                 {'value':2, 'name':'Craft-repair'},
                 {'value':3, 'name':'Exec-managerial'},
                 {'value':4, 'name':'Farming-fishing'},
                 {'value':5, 'name':'Handlers-cleaners'},
                 {'value':6, 'name':'Machine-op-inspct'},
                 {'value':7, 'name':'Other-service'},
                 {'value':8, 'name':'Priv-house-serv'},
                 {'value':9, 'name':'Prof-specialty'},
                 {'value':10, 'name':'Protective-serv'},
                 {'value':11, 'name':'Sales'},
                 {'value':12, 'name':'Tech-support'},
                 {'value':13, 'name':'Transport-moving'}]
        Relationship = [{'value':0, 'name':'Husband'},
                 {'value':1, 'name':'Not-in-family'},
                 {'value':2, 'name':'Other-relative'},
                 {'value':3, 'name':'Own-child'},
                 {'value':4, 'name':'Unmarried'},
                 {'value':5, 'name':'Wife'}]  
        Race = [{'value':1, 'name':'Asian'},
                    {'value':2, 'name':'Black'},
                    {'value':3, 'name':'Other'},
                    {'value':4, 'name':'White'}]        
        Native_Country = [{'value':0, 'name': "Cambodia"},
                    {'value':1, 'name': "Canada"},
                    {'value':2, 'name': "China"},
                    {'value':3, 'name': "Columbia"},
                    {'value':4, 'name': "Cuba"},
                    {'value':5, 'name': "Dominican Republic" },
                    {'value':6, 'name': "Ecuador" },
                    {'value':7, 'name': "El Salvadorr" },
                    {'value':8, 'name': "England" },
                    {'value':9, 'name': "France" },
                    {'value':10, 'name': "Germany" },
                    {'value':11, 'name': "Greece" },
                    {'value':12, 'name': "Guatemala" },
                    {'value':13, 'name': "Haiti" },
                    {'value':14, 'name': "Netherlands" },
                    {'value':15, 'name': "Honduras" },
                    {'value':16, 'name': "HongKong" },
                    {'value':17, 'name': "Hungary" },
                    {'value':18, 'name': "India" },
                    {'value':19, 'name': "Iran" },
                    {'value':20, 'name': "Ireland" },
                    {'value':21, 'name': "Italy" },
                    {'value':22, 'name': "Jamaica" },
                    {'value':23, 'name': "Japan" },
                    {'value':24, 'name': "Laos" },
                    {'value':25, 'name': "Mexico" },
                    {'value':26, 'name': "Nicaragua" },
                    {'value':27, 'name': "Outlying-US(Guam-USVI-etc)" },
                    {'value':28, 'name': "Peru" },
                    {'value':29, 'name': "Philippines" },
                    {'value':30, 'name': "Poland" },
                    {'value':31, 'name': "Portugal" },
                    {'value':32, 'name': "Puerto-Rico" },
                    {'value':33, 'name': "Scotland" },
                    {'value':34, 'name': "South" },
                    {'value':35, 'name': "Taiwan" },
                    {'value':36, 'name': "Thailand" },
                    {'value':37, 'name': "Trinadad&Tobago" },
                    {'value':38, 'name': "United States" },
                    {'value':39, 'name': "Vietnam" }]                        
        option = random.sample(range(1, 4), 1)
        if request.method == 'POST':
                to_predict_list = request.form.to_dict()
                to_predict_list=list(to_predict_list.values())
                to_predict_list = list(map(int, to_predict_list))
                result = ValuePredictor(to_predict_list)
                if int(result)==1:
                    prediction='Income more than 50K'
                    img_var = 2
                else:
                    prediction='Income less that 50K'
                    img_var = 1
        return render_template("index.html",prediction=prediction,
        option = option,
        img_var = img_var, 
        Working_Class=Working_Class
        ,Education=Education
        ,Marital_Status=Marital_Status
        ,Occupation = Occupation
        ,Relationship = Relationship
        ,Race = Race
        ,Native_Country = Native_Country)


if __name__ == "__main__":
	app.run(debug=True)
