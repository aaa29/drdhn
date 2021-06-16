<template>
  <div class="hello">
   
   

    <div class="top4">
      <div class="t42">
        <div class="list-group">
          <button class="list-group-item" active>Axes de recherche</button>
          <button class="list-group-item">Equipes de recherche</button>
          <button class="list-group-item">Publications</button>
        </div>
      </div>

      <div class="t41">
        <div class="section">
          DRDHN > {{current_section}}
        </div>
        
          
            <Axes/>
          
        
      </div>
      
    </div>

  
  </div>
</template>

<script>
import Axes from './recherche/Axes.vue'
import axios from 'axios'
export default {
  name: 'Recherche',
  props: {
    msg: String
  },
  components: {
    Axes,
  },
  data : () =>({
    current_section : "Axes de Recherche",
    fields: [
          {key : 'l_name', label : 'Nom'},
          {key : 'f_name', label : 'Prénom'}, 
          // {key : 'poste', label : '	Poste'}, 
          // {key : 'email', label : 'E-mail'},  
        ],

        items: [
       
        ]
  }),

  mounted () {
    console.log("shitttttt", this.api_url+'membres/')
    axios.get(this.api_url+'membres/')
    .then((res) =>{
      var is_active = true
        res.data.forEach(e => {
          this.items.push({
            isActive : is_active,
            l_name : e.l_name,
            f_name : e.f_name
          })
          is_active = !is_active
        });
    })
    .catch((err) =>{
        console.log(err)
    })
  },

  computed : {

      auth_url() {
          return this.$store.state.auth_url;
      },

      api_url() {
          return this.$store.state.api_url;
      },

      auth_client() {
          return this.$store.state.auth_client;
      }
  },
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
  position: relative;
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
}

.t42 div {
  width : 30%;
  position: absolute;
  top : 10vh;
  left : 10%;
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
