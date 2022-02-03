
let pagina =1;
const botonSiguente= document.getElementById("siguiente");
const botonAnterior= document.getElementById("anterior");


botonSiguente.addEventListener('click',()=>{
    if(pagina< 1000){
        pagina+=1;
        cargarPeliculas();
    }
})

botonAnterior.addEventListener('click',()=>{
    if(pagina >1){
        pagina-=1;
        cargarPeliculas();
    }
})


const cargarPeliculas= async () =>{
    Response = await fetch(`https://api.themoviedb.org/3/movie/popular?api_key=eb4bdb96c0a34109aaa056232d3c1986&page=${pagina}`);
    Data = await Response.json();
        let mov='';
        Data.results.forEach(movie => {
            mov+=`<div class="pelicula">
            <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}">
            <p class="id"> ${movie.id}</p>
            <button class="btn_pelicula"  onclick="getPelicula(${movie.id})"> Ver Pelicula  <i class="far fa-play-circle"></i> </button>
            </div>
            `;

            
        });
        document.getElementById("contenedor").innerHTML=mov;
    }

cargarPeliculas();







