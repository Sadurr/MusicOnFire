from io import BytesIO
import re
from ssl import AlertDescription
import string
from flask import Flask, render_template, request, flash, session
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy import desc, or_
import urllib3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:zyZiek1999XD!@localhost/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

class MusicOnFire(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    band = db.Column(db.String(80), nullable=False)
    album = db.Column(db.String(120), nullable=False)
    genre =  db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    recommended = db.Column(db.Integer, nullable=True)

    def __init__(self, band, album, genre, description):
        self.band = band
        self.album = album
        self.genre = genre
        self.description = description

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/addmusic")
def addmusic():
    return render_template("index.html")


@app.route("/musicadd", methods=['POST'])
def musicadd():
    if request.method == "POST":
        band = request.form["modalBandText"]
        album = request.form["modalAlbumText"]
        genre = request.form["modalGenreText"]
        description = request.form["modalDescriptionText"]

        entry = MusicOnFire(band, album, genre, description)
        db.session.add(entry)
        db.session.commit()
        db.session.close() #added test

    return render_template("index.html")

@app.route("/musicsearch",  methods=['POST', 'GET'])
def musicsearch():
    inputForQuery = request.form["inputText"]
    inputType = request.form["inputType"]

    output_bands = [ ]
    output_albums = [ ]
    output_genres = [ ]
    output_descriptions = [ ]
    output_recommended_bands = [ ]
    output_recommended_albums = [ ]

    # try: 
    if inputType == "band":
        bands = db.session.query(MusicOnFire.band).filter_by(band=inputForQuery).all()
        for band1 in bands:
            output_bands.append(band1.band)

        albums = db.session.query(MusicOnFire.album).filter_by(band=inputForQuery).all()
        for album in albums:
            output_albums.append(album.album)

        genres = db.session.query(MusicOnFire.genre).filter_by(band=inputForQuery).all() 
        for genre in genres:
            output_genres.append(genre.genre)

        descriptions =  db.session.query(MusicOnFire.description).filter_by(band=inputForQuery).all() 
        for description in descriptions:
            output_descriptions.append(description.description)

        if "happy" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="calm").all()  #and recommended = True
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="calm").all() 
            # recommended_bands =  db.session.query(MusicOnFire.band).filter(MusicOnFire.description=="calm" and MusicOnFire.recommended=="true").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "calm" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="happy").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="happy").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "peaceful" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="poetic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="poetic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "poetic" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="peaceful").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="peaceful").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "aggressive" in output_descriptions or "heavy" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="energetic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="energetic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "energetic" in output_descriptions or "heavy" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="aggressive").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="aggressive").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "instrumental" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="repetitive").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="repetitive").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "repetitive" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="instrumental").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="instrumental").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "atmospheric" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="hypnotic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="hypnotic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "hypnotic" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="atmospheric").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="atmospheric").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "melodic" in output_descriptions: #tutaj cos zmienic
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="progressive").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="progressive").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "progressive" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="melodic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="melodic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)        
        # else:
        #    recommended_band =  ["Not found","Not found","Not found","Not found","Not found"]
        #    recommended_album = ["Not found","Not found","Not found","Not found","Not found"]
        #    cover_photo = 'error.jpg'   
    elif inputType == 'genre':
        if inputForQuery == "Jazz":
            # bands =  db.session.query(MusicOnFire.band).filter(MusicOnFire.genre=="Avant-Garde Jazz", MusicOnFire.genre=="Jazz Fusion", MusicOnFire.genre=="Modal Jazz").all() 
            bands = db.session.query(MusicOnFire.band).filter_by(genre="Avant-Garde Jazz").all()
            albums = db.session.query(MusicOnFire.album).filter_by(genre="Avant-Garde Jazz").all()
            genres =  db.session.query(MusicOnFire.genre).filter_by(genre="Avant-Garde Jazz").all()
            descriptions = db.session.query(MusicOnFire.description).filter_by(genre="Avant-Garde Jazz").all()
            for band in bands:  
                output_bands.append(band.band)
            for album in albums:
                output_albums.append(album.album)
            for genre in genres:
                output_genres.append(genre.genre)
            for description in descriptions:
                output_descriptions.append(description.description)    

        bands = db.session.query(MusicOnFire.band).filter_by(genre=inputForQuery).all()
        for band1 in bands:
            output_bands.append(band1.band)

        albums = db.session.query(MusicOnFire.album).filter_by(genre=inputForQuery).all()
        for album in albums:
            output_albums.append(album.album)

        genres = db.session.query(MusicOnFire.genre).filter_by(genre=inputForQuery).all()
        for genre in genres:
            output_genres.append(genre.genre)

        descriptions =  db.session.query(MusicOnFire.description).filter_by(genre=inputForQuery).all()
        for description in descriptions:
            output_descriptions.append(description.description)
        if "Art Pop" in output_genres:
            recommended_bands =  db.session.query(MusicOnFire.band).filter(MusicOnFire.genre=="Art Rock", MusicOnFire.recommended=="true").all()  #and recommended = True
            recommended_albums = db.session.query(MusicOnFire.album).filter(MusicOnFire.genre=="Art Rock", MusicOnFire.recommended=="true").all()
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        if "happy" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="calm").all()  #and recommended = True
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="calm").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "calm" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="happy").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="happy").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "peaceful" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="poetic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="poetic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "poetic" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="peaceful").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="peaceful").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "aggressive" in output_descriptions or "heavy" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="energetic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="energetic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "energetic" in output_descriptions or "heavy" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="aggressive").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="aggressive").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "instrumental" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="repetitive").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="repetitive").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "repetitive" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="instrumental").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="instrumental").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "atmospheric" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="hypnotic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="hypnotic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "hypnotic" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="atmospheric").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="atmospheric").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "melodic" in output_descriptions: #tutaj cos zmienic
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="progressive").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="progressive").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "progressive" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="melodic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="melodic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)  
    elif inputType == 'description':
        bands = db.session.query(MusicOnFire.band).filter_by(description=inputForQuery).all()
        for band1 in bands:
            output_bands.append(band1.band)

        albums = db.session.query(MusicOnFire.album).filter_by(description=inputForQuery).all()
        for album in albums:
            output_albums.append(album.album)

        genres = db.session.query(MusicOnFire.genre).filter_by(description=inputForQuery).all()
        for genre in genres:
            output_genres.append(genre.genre)

        descriptions =  db.session.query(MusicOnFire.description).filter_by(description=inputForQuery).all()
        for description in descriptions:
            output_descriptions.append(description.description)
        if "happy" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="calm").all()  #and recommended = True
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="calm").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "calm" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="happy").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="happy").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "peaceful" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="poetic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="poetic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "poetic" in output_descriptions: 
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="peaceful").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="peaceful").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "aggressive" in output_descriptions or "heavy" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="energetic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="energetic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "energetic" in output_descriptions or "heavy" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="aggressive").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="aggressive").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "instrumental" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="repetitive").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="repetitive").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "repetitive" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="instrumental").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="instrumental").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "atmospheric" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="hypnotic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="hypnotic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "hypnotic" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="atmospheric").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="atmospheric").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "melodic" in output_descriptions: #tutaj cos zmienic
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="progressive").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="progressive").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)
        elif "progressive" in output_descriptions:
            recommended_bands =  db.session.query(MusicOnFire.band).filter_by(description="melodic").all() 
            recommended_albums = db.session.query(MusicOnFire.album).filter_by(description="melodic").all() 
            for recommended_band in recommended_bands:
                output_recommended_bands.append(recommended_band.band)                
            for recommended_album in recommended_albums:
                output_recommended_albums.append(recommended_album.album)  

    cover_photos = [ ]

    album_length = len(output_recommended_albums)

    match album_length:
        case 4:
            output_recommended_bands.insert(4,"Not found")
            output_recommended_albums.insert(4,"Not found")
            cover_photos.insert(4,"no_image.jpg") #not working
        case 3:
            output_recommended_bands.insert(3,"Not found")
            output_recommended_albums.insert(3,"Not found")
            cover_photos.insert(3,"no_image.jpg")
            output_recommended_bands.insert(4,"Not found")
            output_recommended_albums.insert(4,"Not found")
            cover_photos.insert(4,"no_image.jpg") 
        case 2:
            output_recommended_bands.insert(2,"Not found")
            output_recommended_albums.insert(2,"Not found")
            cover_photos.insert(2,"no_image.jpg")
            output_recommended_bands.insert(3,"Not found")
            output_recommended_albums.insert(3,"Not found")
            cover_photos.insert(3,"no_image.jpg")
            output_recommended_bands.insert(4,"Not found")
            output_recommended_albums.insert(4,"Not found")
            cover_photos.insert(4,"no_image.jpg")
        case 1:
            output_recommended_bands.insert(1,"Not found")
            output_recommended_albums.insert(1,"Not found")
            cover_photos.insert(1,"no_image.jpg")
            output_recommended_bands.insert(2,"Not found")
            output_recommended_albums.insert(2,"Not found")
            cover_photos.insert(2,"no_image.jpg")
            output_recommended_bands.insert(3,"Not found")
            output_recommended_albums.insert(3,"Not found")
            cover_photos.insert(3,"no_image.jpg")
            output_recommended_bands.insert(4,"Not found")
            output_recommended_albums.insert(4,"Not found")
            cover_photos.insert(4,"no_image.jpg")
        case 0:
            output_recommended_bands.insert(0,"Not found")
            output_recommended_albums.insert(0,"Not found")
            cover_photos.insert(0,"no_image.jpg")
            output_recommended_bands.insert(1,"Not found")
            output_recommended_albums.insert(1,"Not found")
            cover_photos.insert(1,"no_image.jpg")
            output_recommended_bands.insert(2,"Not found")
            output_recommended_albums.insert(2,"Not found")
            cover_photos.insert(2,"no_image.jpg")
            output_recommended_bands.insert(3,"Not found")
            output_recommended_albums.insert(3,"Not found")
            cover_photos.insert(3,"no_image.jpg")
            output_recommended_bands.insert(4,"Not found")
            output_recommended_albums.insert(4,"Not found")
            cover_photos.insert(4,"no_image.jpg")


    for i in range(album_length):
        for r in output_recommended_albums: #in range(len(output_recommended_albums)): potrzebny for?
    # for r in output_recommended_albums:
            if output_recommended_albums[i] == "Abbey Road":
                cover_photo = "abbey-road.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Around the Fur":
                cover_photo = "around-the-fur.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] ==  "Closer":
                cover_photo = "closer.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] ==  "Doolittle":
                cover_photo = "doolittle.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] ==  "Green River":
                cover_photo = "green-river.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] ==  "Kill 'Em All":
                cover_photo = "kill-em-all.jpg"
                cover_photos.append(cover_photo)    
                break
            elif output_recommended_albums[i] ==  "Kind of Blue":
                cover_photo = "kind-of-blue.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] ==  "Led Zeppelin [IV]":
                cover_photo = "led-zeppelin-iv.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Master of Puppets":
                cover_photo = "master-of-puppets.jpg"
                cover_photos.append(cover_photo)    
                break
            elif output_recommended_albums[i] == "Revolver":
                cover_photo = "revolver.jpg"
                cover_photos.append(cover_photo)    
                break
            elif output_recommended_albums[i] == "Sgt. Pepper's Lonely Hearts Club Band":
                cover_photo = "sgt-peppers-lonely-hearts-club-band.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "The Queen Is Dead":
                cover_photo = "the-queen-is-dead.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Unknown Pleasures":
                cover_photo = "unknown-pleasures.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Hatful of Hollow":
                cover_photo = "hatful-of-hollow.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Thick as a Brick":
                cover_photo = "thick-as-a-brick.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Aqualung":
                cover_photo = "aqualung.jpg"
                cover_photos.append(cover_photo) 
                break
            elif output_recommended_albums[i] == "Stand Up":
                cover_photo = "stand-up.jpg"
                cover_photos.append(cover_photo) 
                break
            elif output_recommended_albums[i] == "Benefit":
                cover_photo = "benefit.jpg"
                cover_photos.append(cover_photo) 
                break
            elif output_recommended_albums[i] == "Minstrel in the Gallery":
                cover_photo = "minstrel-in-the-gallery.jpg"
                cover_photos.append(cover_photo) 
                break
            elif output_recommended_albums[i] == "Songs From the Wood":
                cover_photo = "songs-from-the-wood.jpg"
                cover_photos.append(cover_photo) 
                break
            elif output_recommended_albums[i] == "Heavy Horses":
                cover_photo = "heavy-horses.jpg"
                cover_photos.append(cover_photo) 
                break
            elif output_recommended_albums[i] == "Rage Against the Machine":
                cover_photo = "rage-against-the-machine.jpg"
                cover_photos.append(cover_photo) 
                break
            elif output_recommended_albums[i] == "Behold.Total.Rejection":
                cover_photo = "behold_total_rejection.jpg"
                cover_photos.append(cover_photo) 
                break
            elif output_recommended_albums[i] == "Wrong":
                cover_photo = "wrong.jpg"
                cover_photos.append(cover_photo) 
                break
            elif output_recommended_albums[i] == "Paranoid":
                cover_photo = "paranoid.jpg"
                cover_photos.append(cover_photo) 
                break
            elif output_recommended_albums[i] == "Black Sabbath":
                cover_photo = "black-sabbath.jpg"
                cover_photos.append(cover_photo) 
                break
            elif output_recommended_albums[i] == "Sabbath Bloody Sabbath":
                cover_photo = "sabbath-bloody-sabbath.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "The Boatman's Call":
                cover_photo = "the-boatmans-call.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Mezzanine":
                cover_photo = "mezzanine.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Dummy":
                cover_photo = "dummy.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Selected Ambient Works 85-92":
                cover_photo = "selected-ambient-works-85-92.jpg"
                cover_photos.append(cover_photo)               
                break
            elif output_recommended_albums[i] == "Black Metal":
                cover_photo = "black-metal.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Seasons in the Abyss":
                cover_photo = "seasons-in-the-abyss.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Reign in Blood":
                cover_photo = "reign-in-blood.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Bitches Brew":
                cover_photo = "bitches-brew.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "In a Silent Way":
                cover_photo = "in-a-silent-way.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Blue Train":
                cover_photo = "blue-train.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Giant Steps":
                cover_photo = "giant-steps.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Ys":
                cover_photo = "ys.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Have One on Me":
                cover_photo = "have-one-on-me.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Highway 61 Revisited":
                cover_photo = "highway-61-revisited.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Blonde on Blonde":
                cover_photo = "blonde-on-blonde.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Blood on the Tracks":
                cover_photo = "blood-on-the-tracks.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Full Moon Fever":
                cover_photo = "full-moon-fever.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Wildflowers":
                cover_photo = "wildflowers.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Pink Moon":
                cover_photo = "pink-moon.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Spirit of Eden":
                cover_photo = "spirit-of-eden.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Laughing Stock":
                cover_photo = "laughing-stock.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Naked City":
                cover_photo = "naked-city.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "The Circle Maker":
                cover_photo = "the-circle-maker.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "All Things Must Pass":
                cover_photo = "all-things-must-pass.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i]  == "Songs of Leonard Cohen":
                cover_photo = "songs-of-leonard-cohen.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "A Love Supreme":
                cover_photo = "a-love-supreme.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Ride the Lightning":
                cover_photo = "ride-the-lightning.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Endtroducing.....":
                cover_photo = "endtroducing.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Loveless":
                cover_photo = "loveless.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "All Screwed Up":
                cover_photo = "all-screwed-up.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "3 'n the Mornin'":
                cover_photo = "3-n-the-mornin.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Vulgar Display of Power":
                cover_photo = "vulgar-display-of-power.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Korn":
                cover_photo = "korn.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Ladies and Gentlemen We Are Floating in Space":
                cover_photo = "ladies-and-gentlemen-we-are-floating-in-space.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Long Season":
                cover_photo = "long-season.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Pearl":
                cover_photo = "pearl.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Music for 18 Musicians":
                cover_photo = "music-for-18-musicians.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Strumming Music":
                cover_photo = "strumming-music.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "The Disintegration Loops":
                cover_photo = "the-disintegration-loops.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "To Be Kind":
                cover_photo = "to-be-kind.jpg"
                cover_photos.append(cover_photo)
                break
            elif output_recommended_albums[i] == "Illinois":
                cover_photo = "illinois.jpg"
                cover_photos.append(cover_photo)
                break                       
            elif output_recommended_albums[i] == "Master of Reality":
                cover_photo = "master-of-reality.jpg"
                cover_photos.append(cover_photo)
                break 
            elif output_recommended_albums[i] == "Sabotage":
                cover_photo = "sabotage.jpg"
                cover_photos.append(cover_photo)
                break 
            elif output_recommended_albums[i] == "Low":
                cover_photo = "low.jpg"
                cover_photos.append(cover_photo)
                break            
        
            else:
                cover_photo = "no_image.jpg"
                cover_photos.append(cover_photo)
                break
        # else:
        #     continue
        # break

    return render_template("result.html",
     band = output_bands, album=output_albums, genre=output_genres, description=output_descriptions, cover_photo=cover_photos,
    recommended_band=output_recommended_bands, recommended_album=output_recommended_albums)

if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.run()
    db.session.close()




    # print(len(cover_photos))
    # if len(cover_photos) < 5:
    #     # cover_photos[0] = "no_image.jpg"
    #     return "Error 2"

    # if not band and not album and not genre and not description:
    #     band = ["No results,"]  
    #     album =["add missing"]
    #     genre = ["music on"]
    #     description = ["home page"]

    # description = relaxing, fast, slow, noisy, chill, 

    # bands = db.session.query(Music.band).all() #all bands from db
    # albums = db.session.query(Music.album).all()
    # genres = db.session.query(Music.genre).all()
    # descriptions = db.session.query(Music.description).all()


    # if len(band) == 2:
    #     band1,band2 = [str(e) for e in band] 
    #     album1,album2 = [str(e) for e in album]
    #     genre1,genre2 = [str(e) for e in genre]
    #     description1,description2 = [str(e) for e in description]
    #     return render_template("result.html", band1=band1, band2=band2, album1=album1, album2=album2, genre1=genre1,genre2=genre2,description1=description1,description2=description2)
    # elif len(band) == 3:
    #     band1,band2,band3 = [str(e) for e in band]
    #     album1,album2 = [str(e) for e in album]
    #     genre1,genre2 = [str(e) for e in genre]
    #     description1,description2 = [str(e) for e in description] 
    #     return render_template("result.html", band1=band1, band2=band2, band3=band3, album1=album1, album2=album2, genre1=genre1,genre2=genre2,description1=description1,description2=description2)
  

      # lst = [("aaaa8"),("bb8"),("ccc8"),("dddddd8")]
    # print([s.strip("(") for s in band]) # remove the 8 from the string borders
    # print([s.replace("(", "") for s in band]) # remove all the 8s 


     #band = [('The Beatles',), ('The Beatles',)]
    #band[1] = ('The Beatles',)
    # band.replace('()','')   new_band=new_lst,
     
    # for row in session.query(band):
    #     row.replace('()','')
    # print(row)

    # match recommended_album[1]:
    #     case "Abbey Road":
    #         cover_photo = cover_photos[1]  
    #     case 'Revolver':
    #         cover_photo = 'revolver.jpg'
    #     case 'Abbey Road':
    #          cover_photo = 'abbey.jpg'
    #     case _:
    #         cover_photo = 'error.jpg'   

    # except UnboundLocalError as exception:
    #     print(exception)

     # cover_photos = ["abbey-road.jpg","around-the-fur.jpg","closer.jpg","doolittle.jpg","green-river.jpg",
    # "kill-em-all.jpg","kind-of-blue.jpg","led-zeppelin-iv.jpg","master-of-puppets.jpg","revolver.jpg",
    # "sgt-peppers-lonely-hearts-club-band.jpg", "the-queen-is-dead.jpg","unknown-pleasures.jpg" ]
