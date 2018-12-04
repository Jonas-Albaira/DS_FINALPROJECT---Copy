<h2>Distributed Music Player</h2>
Our aim in this project is to develop an application that allows devices to create a network of their own and stream music in real time coming from a source.
<br>
<br>
The app is developed through a <em>full-stack P2P</em> approach with HTML5 as the view and <a href="https://www.python.org/downloads/">Python</a> as the controller. 
<br>
<br>
<img src="http://jonasalbaira.com/images/Screenshot.png" height=400/>

<br>
<h2>Getting Started</h2>
The following dependencies are required before you run the application.

<h4>Python3</h4>
<a href="https://www.python.org/downloads/">Python</a> serves as the backend language. All communications and methods are developed within python.

<h4>Flask</h4>
<a href="http://flask.pocoo.org/">Flask</a> is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. To install:
<br>

	pip install flask
<h4>Flask SocketIO</h4>
The app would also need to install <a href="https://flask-socketio.readthedocs.io/en/latest/">Flask SocketIO</a> which allows access to low latency bi-directional communications between the clients and the server

	pip install flask-socketio
	
<h4>Mediaelement.js</h4>
An HTML5 library for handling Media on browsers. Full instructions on how to install MediaElement.js can be found on their <a href="https://github.com/mediaelement/mediaelement/blob/master/docs/installation.md">website</a>.

<h2>Installation</h2>
Download and extract the folder into a local directory.

<h2>Running the app</h2>
On the main directory, open Command Line and run:
<br>
	<code>python main.py</code>
<br>
<br>
The app is ran by default on Port 5000 of Localhost. Open a <em>browser</em>, then type in address:
<br>
	<code>http://localhost:5000/</code>
