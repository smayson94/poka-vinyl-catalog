from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Base, Album, User

engine = create_engine('sqlite:///vinylcatalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

User2 = User(name = "Sahe Mayson", email="smayson@jolahouse.org")
session.add(User2)
session.commit()

genre1 = Genre(name="Rock", user_id =1)

album1 = Album(album_name = "No Plan EP",year = "2017", artist = "David Bowie", genre= genre1
	, catalog_id ="88985419612", picture_url="https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/No_Plan_EP_%28Front_Cover%29.jpg/220px-No_Plan_EP_%28Front_Cover%29.jpg" )

session.add(album1)
session.commit()

album2 = Album(album_name = "The Eyes",year = "2017", artist = "Plastic Tones", genre= genre1
	, catalog_id ="MONO-004", picture_url="http://stupidorecords.com/1065-home_default/plastic-tones-more-trouble-7.jpg" )

session.add(album2)
session.commit()

album3 = Album(album_name = "Synchronicity",year = "1983", artist = "The Police", genre= genre1
	, catalog_id ="A&M SP-3735", picture_url="http://www.thepolice.com/sites/g/files/g2000003646/f/styles/opengraph_thumbnail/public/albums/600_3.jpg?itok=gzla1OoC" )

session.add(album3)
session.commit()

album4 = Album(album_name = "American Beauty/ American Psyco",year = "2015", artist = "Fall Out Boy", genre= genre1
	, catalog_id ="B0022549-01", picture_url="https://upload.wikimedia.org/wikipedia/en/b/b6/American_Beauty_American_Psycho_cover.png" )

session.add(album4)
session.commit()

album5 = Album(album_name = "Face Value",year = "1981", artist = "Phil Collins", genre= genre1
	, catalog_id ="SD 16029", picture_url="https://upload.wikimedia.org/wikipedia/en/c/c9/Phil_Collins_-_Face_Value.png" )

session.add(album5)
session.commit()

genre2 = Genre(name="Pop", user_id = 1)

album1 = Album(album_name = "Futuresex/Lovesounds",year = "2006", artist = "Justin Timberlake", genre= genre2, catalog_id ="88985365711", picture_url="https://images-na.ssl-images-amazon.com/images/I/71sxIXZ2BsL._SL1500_.jpg" )

session.add(album1)
session.commit()

album2 = Album(album_name = "Back To Black",year = "2007", artist = "Amy Winehouse", genre= genre2, catalog_id ="1734128", picture_url="https://upload.wikimedia.org/wikipedia/en/6/67/Amy_Winehouse_-_Back_to_Black_(album).png" )

session.add(album2)
session.commit()

album3 = Album(album_name = "Touch",year = "1983", artist = "Eurythmics", genre= genre2, catalog_id ="82876561162", picture_url="https://upload.wikimedia.org/wikipedia/en/thumb/7/79/Eurythmics_-_Touch.jpg/220px-Eurythmics_-_Touch.jpg" )

session.add(album3)
session.commit()

album4 = Album(album_name = "12 Songs",year = "2005", artist = "Neil Diamond", genre= genre2, catalog_id ="82876761312", picture_url="https://images-na.ssl-images-amazon.com/images/I/41rCRJvchYL.jpg" )

session.add(album4)
session.commit()

album5 = Album(album_name = "Songs I Heard",year = "2001", artist = "Harry Connick, Jr.", genre= genre2, catalog_id ="504775-2", picture_url="https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/Songsiheard.jpg/220px-Songsiheard.jpg" )

session.add(album5)
session.commit()