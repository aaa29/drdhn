<template>
  <div class="hello">
   <div class="all">
      <div class="top">
        <div class="t1">
          <div class="t11">
            <h5>Division Recherche et Développement en Sciences de l'Information et  Humanités Numériques</h5>
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
          <h2 style="color:white;">DRDHN</h2>
        </div>
        <div class="top2_in">
          <b-navbar type="light" variant="light">
            <b-navbar-nav>
              <b-nav-item href="#">axes de recherche</b-nav-item>
              <b-nav-item href="#">equipes de recherche</b-nav-item>
              <b-nav-item href="#">projets</b-nav-item>
              <b-nav-item href="#">DL</b-nav-item>
              <b-nav-item href="#">produits</b-nav-item>
              <b-nav-item href="#">nouvelles</b-nav-item>
              <b-nav-item href="#">vulgarisation</b-nav-item>
              <b-nav-item href="#">staff</b-nav-item>
              <b-nav-item href="#">contact</b-nav-item>

             

       
            </b-navbar-nav>
          </b-navbar>
        </div>
      </div>
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
  background : pink;
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
  width : 50%;
  margin : 2px;
  padding-left : 20px; 
}

.search {
  display : flex;
  flex-direction : row-reverse;
  align-items : center;
  width : 60%;
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




/* search */

/* end search */

</style>
