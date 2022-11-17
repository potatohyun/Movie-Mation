<template>
  <div>
    <h1>{{movie?.title}}</h1>
    <img :src="movie?.poster_path" alt="">
    <h5>{{movie?.overview}}</h5>
    <router-link :to="{ name : 'CommentCreateView' }">[댓글쓰기]</router-link>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'MovieDetailView',
    data(){
      return{
        movie : null,
      }
    },
    created(){
      this.getMovieDetail()
    },
    methods:{
      getMovieDetail(){
        axios({
          method: 'get',
          url: `${API_URL}/main/movies/${this.$route.params.id}`,
        })
        .then((res)=>{
          console.log(res)
          this.movie=res.data
        })
        .catch(err=>console.log(err))
      }
    }   
}
</script>

<style>

</style>