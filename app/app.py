from flask import Flask,render_template
import socket
import functions

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        #suma = add()
        print('xd')
        #print(typeof(host_ip),suma)
        return render_template('index.html', suma = functions.add(),hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')

#def add(a=1,b=2):
#	print('xd2')
#	return str(a+b)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7080)
