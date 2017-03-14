#CRUD operation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
                output += "<input name = 'newRestaurantName' type='text' placeholder = 'New Restaurant Name'>"
                output += "<input type = 'submit' value='Create'>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                restaurantID = self.path.split("/")[2]
                restaurantQuery = session.query(Restaurant).filter_by(id=restaurantID).one()
                if restaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output =""
                    output += "<html><body>"
                    output += "<h1>"
                    output += restaurantQuery.name
                    output +="</h1>"
                    output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/%s/edit'>" % restaurantID
                    output += "<input name = 'newRestaurantName' type='text' placeholder = 'New Restaurant Name'>"
                    output += "<input type = 'submit' value='Rename'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)

            if self.path.endswith("/delete"):
                restaurantID = self.path.split("/")[2]
                restaurantQuery = session.query(Restaurant).filter_by(id=restaurantID).one()
                if restaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output =""
                    output += "<html><body>"
                    output += "<h1> Are you sure you want to delete %s? <h1>" %restaurantQuery.name
                
                 
                    output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/%s/delete'>" % restaurantID
                    output += "<input type = 'submit' value='Delete'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)

            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""
                output += "<a href = '/restaurants/new'>  Make a New Restaurant Here </a></br></br>"
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name 
                    output += "<br><a href ='/restaurants/%s/edit'> Edit </a>" %restaurant.id
                    output += "<br>"
                    output += "<a href ='/restaurants/%s/delete'> Delete </a>" %restaurant.id
                    output += "<br>"
                    output += "<br><br><br>"

                output += "</body></html>"
                self.wfile.write(output)
                print output
                return


        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    restaurantID = self.path.split("/")[2]

                    restaurantQuery = session.query(Restaurant).filter_by(
                        id=restaurantID).one()
                    if restaurantQuery != []:
                        restaurantQuery.name = messagecontent[0]
                        session.add(restaurantQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            if self.path.endswith("/delete"):
               
                restaurantID = self.path.split("/")[2]

                restaurantQuery = session.query(Restaurant).filter_by(
                    id=restaurantID).one()
                if restaurantQuery != []:
                    session.delete(restaurantQuery)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')

            newRestaurant = Restaurant(name = messagecontent[0])
            session.add(newRestaurant)
            session.commit()

            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.send_header('Location', '/restaurants')
            self.end_headers()

            return
        
        
        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()