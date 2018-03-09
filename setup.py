from setuptools import setup

setup(name='vortex',
      version='1.0',
      description='Exploring data visualization tools',
      author='Shareef Dabdoub && Niharika Gupta',
      author_email='gupta.526@buckeyemail.osu.edu,dabdoub.2@osu.edu',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask>=0.10.1','MarkupSafe', 'flask-login>=0.2.7',
      					'sqlalchemy>=0.8.2' 'Flask-SQLAlchemy>=0.16',
      					'Flask-Bcryppt>=0.7.7', 'Flask-WTF>=0.12'],
     )
