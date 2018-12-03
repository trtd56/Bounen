# use module

- flask
- pandas

~~~bash
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
~~~

~~~bash
$ echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ source ~/.bashrc
$ pyenv -v
pyenv 1.0.10-2-geef042a
~~~

~~~bash
$ sudo yum imstall -y openssl-devel make zlib zlib-devel sqlite-devel  bzip2 lib
~~~

~~~bash
$ pyenv install 3.6.1
$ echo 'pyenv shell 3.6.1' >> ~/.bashrc
~~~

~~~
$ pip install flask pandas
~~~

~~~
$ yum install httpd
~~~

# exec check

## initialize


~~~bash
$ python init_db.py
initialize db completed
~~~

## start app

~~~bash
$ python api.py
~~~

## check DB

~~~bash
$ python src/get_db_info.py
~~~
