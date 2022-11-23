<template>
  <div class="box mx-5">
    <br><h1>인기순으로 보여드립니당</h1><br>
    <!-- {{popularitymovies}} -->
    <div class="row row-cols-3 row-cols-md-5 g-4" id="test">
      <PopularityListItem
        v-for="p_movie in popularitymovies"
        :key="p_movie.id"
        :p_movie="p_movie"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PopularityListItem from '@/components/PopularityListItem'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'PopularityList',
    components:{
      PopularityListItem,
    }, 
    data(){
      return{
        popularitymovies : null,
      }
    },
    created(){
      this.popularityMovies()
    },
    methods: {
      popularityMovies() {
        axios({
          method: 'get',
          url: `${API_URL}/main/recommend/popularity/`,
        })
        .then((res)=>{
          this.popularitymovies=res.data
        })
        .catch(err=>console.log(err))
      }
    }
}
</script>

<style>
#test{
  margin-left: 200px;
}
</style>