<template>
  <div class="hello">
   
   

    <div class="top4">
      <div class="t42">
        <div class="list-group">
          <button class="list-group-item" active>Présentation</button>
          <button class="list-group-item">Staff</button>
          <button class="list-group-item">Annuaire</button>
        </div>
      </div>

      <div class="t41">
        <div class="section">
          DRDHN > {{current_section}}
        </div>
        <b-card>
          <b-card-text>
            L’évolution d’Internet et le développement des technologies numériques ont révolutionné la production et les usages de l’information en général et de l’information scientifique et technique en particulier. L’information Scientifique et Technique constitue la brique de base de la société de la connaissance devenant ainsi un contenu numérique qu’il s’agit de rendre intelligible pour chacun selon ses besoins spécifiques tout en maitrisant l’environnement juridique et socio-économique lié au numérique.

Grâce à sa composante multidisciplinaire avec des chercheurs issus de l’informatique, des mathématiques et des sciences humaines, la division recherche et développement en Humanités Numériques s’attèle à développer des outils d’analyse et d’interprétation de grands corpus plurilingues en utilisant les techniques de l’Intelligence Artificielle et du Traitement Automatique des Langues Naturelles, proposer des modèles mathématiques pour l’évaluation de l’information et la modélisation des usages numériques, proposer une approche nationale de veille stratégique de l’IST, mener une réflexion sur l’accès ouvert à l’information et aux données, les nouveaux modèles économiques, le cadre juridique de l’IST et l’éthique Numérique de façon plus générale.
          </b-card-text>
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
  },
  data : () =>({
    current_section : "Présentation"
  })
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
  margin-left : 5%;
  width : 70%;
  text-align : start;
}

.t41 .section{
  display: flex;
  flex-direction: row;
  width: 100%;
}



.t42 {
  margin-right : 5%;
  width : 30%;
}



.t42 div button{
  background : #3975d5;
  color : white;
  cursor: pointer;
}

.t42 div button:focus {
  background: white;
  color: black;
}



/* search */

/* end search */

</style>
