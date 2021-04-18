<template>
  <div class="hello">
   
    <div class="top3">
      <div class="myCarousel">
        <b-carousel
          id="carousel-1"
          v-model="slide"
          :interval="3000"
          controls
          indicators
          background="#ccc"
          img-width="1024"
          img-height="480"
          style="text-shadow: 1px 1px 2px #000;"
          @sliding-start="onSlideStart"
          @sliding-end="onSlideEnd"
        >
          <!-- Text slides with image -->
          <b-carousel-slide
            caption="First slide"
            text="Nulla vitae elit libero, a pharetra augue mollis interdum."
            img-src="https://picsum.photos/1024/480/?image=52"
          ></b-carousel-slide>

          <!-- Slides with custom text -->
          <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
            <h1>Hello world!</h1>
          </b-carousel-slide>

          <!-- Slides with image only -->
          <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>

          <!-- Slides with img slot -->
          <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
          <b-carousel-slide>
            <template v-slot:img>
              <img
                class="d-block img-fluid w-100"
                width="1024"
                height="480"
                src="https://picsum.photos/1024/480/?image=55"
                alt="image slot"
              >
            </template>
          </b-carousel-slide>

          <!-- Slide with blank fluid image to maintain slide aspect ratio -->
          <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt
              a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.
            </p>
          </b-carousel-slide>
        </b-carousel>
      </div>
    </div>

    <div class="top4">
      <div class="t41">
        <b-card title="Qui Sommes nous?">
          <b-card-text>
            L’évolution d’Internet et le développement des technologies numériques ont révolutionné la production et les usages de l’information en général et de l’information scientifique et technique en particulier. L’information Scientifique et Technique constitue la brique de base de la société de la connaissance devenant ainsi un contenu numérique qu’il s’agit de rendre intelligible pour chacun selon ses besoins spécifiques tout en maitrisant l’environnement juridique et socio-économique lié au numérique.

Grâce à sa composante multidisciplinaire avec des chercheurs issus de l’informatique, des mathématiques et des sciences humaines, la division recherche et développement en Humanités Numériques s’attèle à développer des outils d’analyse et d’interprétation de grands corpus plurilingues en utilisant les techniques de l’Intelligence Artificielle et du Traitement Automatique des Langues Naturelles, proposer des modèles mathématiques pour l’évaluation de l’information et la modélisation des usages numériques, proposer une approche nationale de veille stratégique de l’IST, mener une réflexion sur l’accès ouvert à l’information et aux données, les nouveaux modèles économiques, le cadre juridique de l’IST et l’éthique Numérique de façon plus générale.
          </b-card-text>
        </b-card>
      </div>
      <div class="t42">
        <b-card title="Projets">
          <b-carousel
            id="carousel-fade"
            style="text-shadow: 0px 0px 2px #000"
            fade
            indicators
            img-width="1024"
            img-height="480"
          >
            <b-carousel-slide
              caption="Aljahiz humanities"
              img-src="https://picsum.photos/1024/480/?image=10"
            ></b-carousel-slide>
            <b-carousel-slide
              caption="Plagiarism detection"
              img-src="https://picsum.photos/1024/480/?image=12"
            ></b-carousel-slide>
            <b-carousel-slide
              caption="Algeria Portal"
              img-src="https://picsum.photos/1024/480/?image=22"
            ></b-carousel-slide>
          </b-carousel>
        </b-card>
      </div>
    </div>

  
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

@import url(https://fonts.googleapis.com/css?family=Open+Sans);

.all {
  display : column;
}

.top{
  display : flex;
  flex-direction : row;
  background : #fbfcfd;
  align-items : center;
  height : 10vh;
}

.t1 {
  display : flex;
  flex-direction : row;
  align-items : center;
  justify-content: center;
  width : 60%;
  margin : 2px;
  padding-left : 20px; 
}

.search {
  display : flex;
  flex-direction : row-reverse;
  align-items : center;
  width : 40%;
  margin : 2px;
  padding-left : 20px;
  padding-right : 20px; 
}

.search_bar {
  display : flex;
  flex-direction : row;
  align-items : center;
  padding : 5px;
  width : 50%;
}

.t11 {
  display: flex;
  flex-direction: row;
  justify-content: center;
  padding-right : 5px;
}

.t12 {
  margin-left : 5px;
}


.top2{
  display : flex;
  flex-direction : row;
  background : #3975d5;
  align-items : center;
  justify-content : right;
  margin-bottom: 10px;
}


.top2_in{
  display : flex;
  flex-direction : row;
  justify-content : center;
  width : 50%;
}

.t21{
  display : flex;
  flex-direction : row;
  margin : 2px;
  height : 8vh;
  align-items : center;
}

.top3{
  display : flex;
  flex-direction : row;
  background: #fbfcfd;
  justify-content : center;
}

.myCarousel {
  max-width : 50%;
}

.navbar {
  background : #3975d5!important;
}
.navbar-light .navbar-nav .nav-link{
  color:white!important
}

.navbar-light .navbar-nav .nav-link:hover{
  border-bottom: 3px solid rgb(255, 255, 255);
}


.top4 {
  display : flex;
  flex-direction: row;
  margin: 50px;
  align-items: center;
  justify-content: center;
}

.t41 {
  margin-right : 5%;
  width : 50%;
}

.t42 {
  margin-left : 5%;
  width : 30%;
}




/* search */

/* end search */

</style>
