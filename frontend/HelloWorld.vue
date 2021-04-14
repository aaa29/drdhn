<template>
  <div class="hello">
   <div class="all">
      <div class="top">
        <div class="t1">
          <div class="t11">
            <h5>Division Recherche et Développement en Sciences de l'Information et  Humanités Numériques</h5>
          </div>

          <div class="t12">DRDHN</div>
        </div>
        <div class="search">
          <h4>search</h4>
        </div>
      </div>
      <div class="top2">
        <div class="t21">axes de recherche</div>
        <div class="t21">equipe de recherche</div>
        <div class="t21">projets</div>
        <div class="t21">productions</div>
        <div class="t21">produits</div>
        <div class="t21">staff</div>
        <div class="t21">contacts</div>
      </div>
      <div class="top3">

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
.all {
  display : column;
  background : pink;
}

.top{
  display : flex;
  flex-direction : row;
  background : blue;
  align-items : center;
}

.t1 {
  display : flex;
  flex-direction : row;
  align-items : center;
  width : 50%;
  margin : 2px;
  padding-left : 20px; 
}

.search {
  display : flex;
  flex-direction : row-reverse;
  align-items : center;
  background : green;
  width : 50%;
  margin : 2px;
  padding-left : 20px;
  padding-right : 20px; 
}

.t11 {
  padding-right : 5px;
  background : pink;
}

.t12 {
  margin-left : 5px;
  background : red;
}


.top2{
  display : flex;
  flex-direction : row;
  background : pink;
  align-items : center;
  justify-content : right;
}

.t21{
  display : flex;
  flex-direction : row;
  margin : 2px;
  height : 10vh;
  background : red;
  align-items : center;
}

.top3{
  background: grey;
  height : 30vh
}
</style>
