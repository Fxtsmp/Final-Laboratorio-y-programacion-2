/* -- SQLite commands
INSERT INTO films (title, year, director, gender, sinopsis, cover) 
VALUES ("batman","2005","Tarantino","Accion","safarelly la peli", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Batman_cosplay_-_Masked_Mateo_-_Photo_Jonin.jpg/245px-Batman_cosplay_-_Masked_Mateo_-_Photo_Jonin.jpg"); 
INSERT INTO films (title, year, director, gender, sinopsis, cover)
VALUES ("Kill Bill","2009","Guillermo ddel Toro","drama","medio pelo la peli", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Kill_Bill_svg_logo.svg/280px-Kill_Bill_svg_logo.svg.png"); 
INSERT INTO films (title, year, director, gender, sinopsis, cover)
VALUES ("Star Wars","1999","George Lucas","Ciencia Ficcion","Te vuela el tomate", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/250px-Star_Wars_Logo.svg.png");
INSERT INTO films (title, year, director, gender, sinopsis, cover)
VALUES ("Spiderman","2022","Tony Star","Ciencia Ficcion","multiversal", "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ3ksk9K-b2pT6OOczS4ucB5aH_l7hOGuIO7RUXMubkxOfbhmQX"); 
INSERT INTO films (title, year, director, gender, sinopsis, cover)
VALUES ("Eternals","2020","Tarantino","Mitologic","a la mierda la mitologia","https://as01.epimg.net/meristation/imagenes/2021/12/13/noticias/1639393965_813312_1639393999_noticia_normal.jpg");
INSERT INTO films (title, year, director, gender, sinopsis, cover)
VALUES ("batman 2","1992","Spielberg","Accion","otra de batman", "") */
/* INSERT INTO films (title, year, director, gender, sinopsis, cover)
VALUES ("Spiderman 2","2019","Tony Stark","Ciencia Ficcion","multiversal", "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ3ksk9K-b2pT6OOczS4ucB5aH_l7hOGuIO7RUXMubkxOfbhmQX"); */
/* INSERT INTO comments (film_id, author_id, created, title, body)
VALUES (4,1,"20/2/2022","7/10","ESTA INTERESANTE PERO EL MULTIVERSO VA A PROVOCAR UN CAOS");
INSERT INTO comments (film_id, author_id, created, title, body)
VALUES (4,2,"20/1/2000","meeeeeehhhh","Holland XD, Toby rules");
/*INSERT INTO comments (film_id, author_id, created, title, body)
VALUES (1,1,"25/12/1990","im batman","oscurooooooo");
INSERT INTO comments (film_id, author_id, created, title, body)
VALUES (1,2,"25/12/1991","interesting and gothic","se ve interesante yy tetrico"); */
/* DROP TABLE comments */
/* CREATE TABLE comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  film_id INTEGER NOT NULL,
  author_id INTEGER NOT NULL,
  created TEXT NOT NULL,
  title TEXT NOT NULL,
  body TEXT NOT NULL
); */
/* SELECT 
    u.username, c.created, c.body
FROM
    comments c
JOIN 
    user u 
ON 
    c.author_id = u.id
JOIN 
    films f 
ON 
    f.id = c.film_id
WHERE 
    f.id = 4
ORDER BY created DESC */