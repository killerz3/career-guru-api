import json
from flask import Flask,request
from gpt import  gpt_career, gpt_ques
app = Flask(__name__)
'''
api call skeleton 
    /api?Query= {class:"9th",subjects:[maths,physics],mindset:[logical,analytical],interests:[a,b,c] }

'''
    

def normalize_query_param(value):
    return value if len(value) > 1 else value[0]


def normalize_query(params):
    params_non_flat = params.to_dict(flat=False)
    return {k: normalize_query_param(v) for k, v in params_non_flat.items()}

    
    
@app.route('/api')
def completion():
    
    init_dic=normalize_query(request.args)
    print(init_dic)
    class_current=str(init_dic["class"])# class in dic
    subjects=str(init_dic["subjects"])
    mindset=str(init_dic["mindsets"])
    interests=str(init_dic["interests"])
    result= gpt_career(class_current,subjects,mindset,interests)
    return result


@app.route('/api/question')

def question():
    
    init_dic=normalize_query(request.args)
    print(init_dic)
    class_current=str(init_dic["class"])# class in dic
    subjects=str(init_dic["subjects"])
    mindset=str(init_dic["mindsets"])
    interests=str(init_dic["interests"])
    question=str(init_dic["question"])
    result= gpt_ques(class_current,subjects,mindset,interests,question)
    return result
# api skeleton for a question is 
# /api/ques?Ques={"class":"12th","subjects":["english","science"],"mindset":["logical","linguistic"],"interests":["sci%20fi%20movies","reading%20books"],"question":"how%20to%20become%20a%20lawyer?"}
# /api/ques?Ques={"class":"12th","subjects":["english","science"],"mindset":["logical","linguistic"],"interests":["sci%20fi%20movies","reading%20books"]}
#query?Query={"class":"12th","subjects":["maths"],"mindset":["STEM"],"interests":["Space","Travel","Reading","History"]}
if __name__ == '__main__':
    app.run(debug=True)