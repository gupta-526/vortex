from app import flask_app


#make view module containing all views
	#init file to be the controler
#make models modules for data base models
#make 1 forms file in app

if __name__ == '__main__':
	flask_app.debug = True
	# flask_app.register_blueprint(authentication)
	# flask_app.register_blueprint(portfolio)
	#flask_app.register_blueprint(views)

#	app.run(host='0.0.0.0', port=int("5000"))
	flask_app.run()
