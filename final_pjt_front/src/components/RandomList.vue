<template>
  <div>
    <h3>RandomList</h3>
    <!-- {{randommovies}} -->
    <RandomListItem
      v-for="r_movie in randommovies"
      :key="r_movie.id"
      :r_movie="r_movie"
    />
  </div>
</template>

<script>
import axios from 'axios'
import RandomListItem from '@/components/RandomListItem'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'RandomList',
    components:{
      RandomListItem,
    }, 
    data(){
      return{
        randommovies : null,
      }
    },
    created(){
      this.randomMovies()
    },
    methods: {
      randomMovies() {
        axios({
          method: 'get',
          url: `${API_URL}/main/recommend/random/`,
        })
        .then((res)=>{
          this.randommovies=res.data
        })
        .catch(err=>console.log(err))
      }
    }
}
</script>

<style>

</style>