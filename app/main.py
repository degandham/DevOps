from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return "<body style='background-color:powederblue;'><p style='text-align:center'><font face='verdana' color='black' size='6'>Deloitte Cloud Demo Client Web Application</p></font></body>"
    
if __name__ == '__main__':
    app.run()

