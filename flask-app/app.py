from flask import Flask, render_template
import random 

app=Flask(__name__)

#list of building images

images=[

"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img1.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img2.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img3.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img4.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img5.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img6.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img7.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img8.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img9.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img10.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img11.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img12.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img13.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img14.jpg",
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img15.jpg"
"https://img-buildings.s3.eu-west-3.amazonaws.com/static/img/img16.jpg",


]


@app.route("/")
def index():
    url=random.choice(images)
    return render_template("index.html", url=url)

if __name__=="__main__":
    app.run(host="0.0.0.0")

