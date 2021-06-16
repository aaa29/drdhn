<template>
  <div class="axes">
   
    <div class="axes">
      <b-card>
        <b-card v-for="item,i in axes" :key="i">
          
          <div class="m">
            <div class="m1">{{item.name}}</div>
            <div class="m2"><b-button>+</b-button></div>
          </div>
          
          
        </b-card>
      </b-card>
      
    </div>

  </div>
</template>

<script>

import axios from 'axios'
export default {
  name: 'Recherche',
  props: {
    msg: String
  },
  data : () =>({
   
      axes: [
      
      ]
  }),

  mounted () {
    console.log(this.api_url+'axes/')
    axios.get(this.api_url+'axes/')
    .then((res) =>{
        res.data.forEach(e => {
          this.axes.push({
            name : e.name,
          })
        console.log(this.axes)
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

.axes div div {
  margin : 10px;
}

.m {
display: flex;
flex-direction: row;
width : 100%;
align-items: center;
}

.m1 {
  width : 90%;
}

.m2 {
  width : 10%;
}

.m2 button {
  background : #3975d5;
  font-size : 16px;
  border : none;
}



/* search */

/* end search */

</style>
