from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, Metadata
)

# executing the instructions from our localhost "chonook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create varuiable for "Album" table
album_table = Table(
    "Album", meta, 
    Column("AlbumId", Integer, primary_key=True),
    Colum("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer), 
    Column("Bytes", Integer), 
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection: