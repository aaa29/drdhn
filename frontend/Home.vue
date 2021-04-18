<template>
  <div class="home">
    <div class="all">
        <div class="top">
          <div class="t1">
            <div class="t11">
              <h5>CERIST | Division Recherche et Développement en Sciences de l'Information et  Humanités Numériques</h5>
            </div>
          </div>
          <div class="search">
            <div class="search_bar">
              <b-form-input type="search" placeholder="recherche"></b-form-input>
              <font-awesome-icon :icon="['fas', 'fa-search']" />
            </div>
          </div>
        </div>
        <div class="top2">
          <div class="top2_in">
            <a href="#" class="home_page"><h2 style="color:white;" @click="change_page(0)">DRDHN</h2></a>
          </div>
          <div class="top2_in">
            <b-navbar type="light" variant="light">
              <b-navbar-nav>
                <b-nav-item href="#" @click="change_page(1)">axes de recherche</b-nav-item>
                <b-nav-item href="#" @click="change_page(4)">equipes de recherche</b-nav-item>
                <b-nav-item href="#" @click="change_page(7)">projets</b-nav-item>
                <b-nav-item href="#" @click="change_page(3)">DL</b-nav-item>
                <b-nav-item href="#" @click="change_page(6)">produits</b-nav-item>
                <b-nav-item href="#" @click="change_page(5)">nouvelles</b-nav-item>
                <b-nav-item href="#" @click="change_page(9)">vulgarisation</b-nav-item>
                <b-nav-item href="#" @click="change_page(8)">staff</b-nav-item>
                <b-nav-item href="#" @click="change_page(2)">contact</b-nav-item>

              

        
              </b-navbar-nav>
            </b-navbar>
          </div>
        </div>

        <div v-if="current_page==0" :key="current_page">
          <HelloWorld msg="Welcome to Your Vue.js App"/>
        </div>
        <div v-else-if="current_page==1" :key="current_page">
          <Axes/>
        </div>
        <div v-else-if="current_page==2" :key="current_page">
          <Contact/>
        </div>
        <div v-else-if="current_page==3" :key="current_page">
          <DL/>
        </div>
        <div v-else-if="current_page==4" :key="current_page">
          <Equipes/>
        </div>
        <div v-else-if="current_page==5" :key="current_page">
          <Nouvelles/>
        </div>
        <div v-else-if="current_page==6" :key="current_page">
          <Produits/>
        </div>
        <div v-else-if="current_page==7" :key="current_page">
          <Projets/>
        </div>
        <div v-else-if="current_page==8" :key="current_page">
          <Staff/>
        </div>
        <div v-else-if="current_page==9" :key="current_page">
          <Vulgarisation/>
        </div>
        

        <div class="footer">
          
            <img src="@/assets/s33.png" style="padding-top : 5px;">
            <p>Tous droits réservés : CERIST | DRDHN</p>
            <div class="contact">
              <div class="c_icon">
                <font-awesome-icon :icon="['fas', 'envelope']" size="2" color="#3975d5"/>
              </div>
              <div>
                <p>haliane@cerist.dz</p>
              </div>
            </div>

            <div class="contact">
              <div class="c_icon">
                <font-awesome-icon :icon="['fas', 'phone']" size="2" color="#3975d5"/>
              </div>
              <div>
                <p>(+213) 21 91 21 98</p>
              </div>
            </div>
           
          
          
        </div>
      
      
      
      
      
    </div>
    

  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Axes from '@/components/Axes.vue'
import Contact from '@/components/Contact.vue'
import DL from '@/components/DL.vue'
import Equipes from '@/components/Equipes.vue'
import Nouvelles from '@/components/Nouvelles.vue'
import Produits from '@/components/Produits.vue'
import Projets from '@/components/Projets.vue'
import Staff from '@/components/Staff.vue'
import Vulgarisation from '@/components/Vulgarisation.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld,
    Axes,
    Contact,
    DL,
    Equipes,
    Nouvelles,
    Produits,
    Projets,
    Staff,
    Vulgarisation,
  },
  data : () =>({
    current_page : 0,
  }),

  methods : {
    change_page(page) {
      this.current_page = page
    }
  }
}
</script>

<style scoped>
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

.home_page:hover {
  text-decoration: none;
}

.contact {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.c_icon {
  margin-top : 1px;
  margin-right : 8px;
}

.footer {
  margin-top : 20px;
  position: relative;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #3975d5;
  color: white;
  text-align: center;
}

</style>
