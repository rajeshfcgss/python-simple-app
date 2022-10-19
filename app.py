from flask import Flask,render_template,request
import pywhatkit as py




app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":  
        phone_number  = str(request.form.get('phone_number'))
        message  = str(request.form.get('phone_number'))
        time_hour  = int(request.form.get('time_hour'))
        time_min  = int(request.form.get('time_min'))
        py.sendwhatmsg(phone_number,message,time_hour, time_min)
       
        return render_template('result.html', add=message)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()