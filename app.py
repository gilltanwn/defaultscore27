#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app=Flask(__name__)


# In[3]:


from flask import request, render_template
import pickle

@app.route("/",methods=["GET","POST"])  #this is the first function you run in flask; the route
def index(): #can name the function anything; this is the flask method
    if request.method == "POST":
        income = request.form.get("I")
        age = request.form.get("A")
        loan = request.form.get("L")
        print(income,age,loan)
        with open('model1.pkl','rb') as f:
            model1 = pickle.load(f)
        with open('model2.pkl','rb') as f:
            model2 = pickle.load(f)
        with open('model3.pkl','rb') as f:
            model3 = pickle.load(f)
        with open('model4.pkl','rb') as f:
            model4 = pickle.load(f)
        with open('model5.pkl','rb') as f:
            model5 = pickle.load(f)
        pred1 = model1.predict([[float(income),float(age),float(loan)]])
        pred2 = model2.predict([[float(income),float(age),float(loan)]])
        pred3 = model3.predict([[float(income),float(age),float(loan)]])
        pred4 = model4.predict([[float(income),float(age),float(loan)]])
        pred5 = model5.predict([[float(income),float(age),float(loan)]])
        print(pred1, pred2, pred3, pred4, pred5)
        s = "The predicted default score is : " + str(pred1[0]) +", " + str(pred2[0]) + ", " + str(pred3[0]) +", " + str(pred4[0]) +" and "+ str(pred5[0]) +" for the Linear Regression Model, Decision Tree Model, Random Forest Model, XGBoost Model and Neural Network Model respectively."
        return render_template("index.html", result=s)
    else:
        return render_template("index.html", result="The predicted default score is : ")


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




