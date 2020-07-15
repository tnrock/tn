from flask import Flask, redirect, url_for, request, render_template

app=Flask(__name__)

#donot use flask as var name or link,it will through 404

@app.route('/')
def index():
   return 'this index'



@app.route('/hello/<n>')		#here hello is the sublink and here n is variable string with <>'s
def hello_world(n):
	return 'Hello '+n
#app.add_url_rule('/', 'hello', hello_world) can be used instead of decorator JFI


@app.route('/integer/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/floating/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo




@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('index'))              #redirect by url for function name and its var if needed
   else:
      return redirect(url_for('show_blog',postID = 2))




@app.route('/results1/<user1>')
def results(user1):
   return render_template('indexfile2.htm', name = user1)


@app.route('/login',methods=['POST','GET'])
def login():
	if request.method=='POST':				#post request
		user=request.form['name']
		return redirect(url_for('results',user1=user))
	else:				
	     	user=request.args.get('name')			#get request
	     	return redirect(url_for('results',user1=user))
     


@app.route('/colorful')
def color():
   return render_template('indexfile.htm')





@app.route('/dataforjinge')                      #we can use statements in jinja templates
def dataforginge():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('indexfile3.htm', result = dict)








if __name__=='__main__':
	app.run(debug=True)		#debug can be enabled,also host,port and options
