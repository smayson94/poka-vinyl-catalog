# poka-vinyl-catalog


## Dependencies

**VirtualBox**

https://www.virtualbox.org/

**Vagrant**

https://www.vagrantup.com/

**SQL Alchemy**

http://www.sqlalchemy.org/

**Flask**

http://flask.pocoo.org/

**dicttoxml**

https://pypi.python.org/pypi/dicttoxml

## Setup

Set up VirtualBox and Vagrant to create your own server. With Vagrant installed, run:

```
$ vagrant up
$ vagrant ssh
$ cd <SYNCED PATH TO REPOSITORY>
```

Initialize and fill the database with these scripts.

```
$ python database_setup.py
$ python populate_db.py
```
## Run

Run the web app finalproject.py:

```
$ python finalproject.py
```

The app runs on port `5000`:

```
http://localhost:5000/
```

## API Endpoints

Available in JSON:

List all genres:

```
http://localhost:5000/genre/json

```
List album

```
http://localhost:5000/genre/<int:genre_id>/<int:album_id>/JSON

