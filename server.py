from flask import Flask,render_template,request

import requests
app=Flask(__name__)

url='https://weather-by-api-ninjas.p.rapidapi.com/v1/weather'

headers= {
    'X-RapidAPI-Key': '90adb73682mshdf2fe32a62ec7fdp14056djsn2ccf5972b858',
    'X-RapidAPI-Host': 'weather-by-api-ninjas.p.rapidapi.com'
}

temp=''
city=''
cloud=''
code=0
@app.route('/',methods=["POST","GET"])
def home():
    global code
    global temp,city,cloud
    code = 0
    print(code)
    if request.method=="POST":
        location=(request.form.get('data'))
        params = {'city': location}
        response=requests.get(url=url,headers=headers,params=params)
        code=response.status_code

        city = location.capitalize()
        if code==200:
            temp = response.json()['temp']

            if temp>=41:
                cloud="Extremely hot weather"
            elif temp>=31:
                cloud="Very hot weather"
            elif temp>=21:
                cloud="Sunny cloud"
            elif temp>=11:
                cloud="mild weather"
            else:
                cloud="cold weather"

        return render_template("index.html",temp=temp,city=city,cloud=cloud,code=code)
    return render_template("index.html",temp=temp,city=city,cloud=cloud,code=code)



if __name__=="__main__":
    app.run(debug=True)
