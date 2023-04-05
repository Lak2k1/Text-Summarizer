import flask
from flask import *
import chardet
import tqdm
import transformers
import torch
from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
app = Flask(__name__)
tokenizer=AutoTokenizer.from_pretrained(r'C:\Users\Lenovo\Desktop\text summarises\tokenizer-20230405T163618Z-001\tokenizer')
model_pegasus=AutoModelForSeq2SeqLM.from_pretrained(r'C:\Users\Lenovo\Desktop\text summarises\pegasus-samsum-model-20230405T163618Z-002\pegasus-samsum-model')

gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

pipe = pipeline("summarization", model=model_pegasus,tokenizer=tokenizer)

@app.route('/')    
def home():  
    return render_template("main page.html")

@app.route('/smrz',methods=['GET','POST'])
def summarize():
    sumtext=request.form['summary']
    summary=pipe(sumtext, **gen_kwargs)[0]["summary_text"]
    return render_template("text summary page.html",summary=summary)

if __name__ =='__main__':  
    app.run(debug = True)