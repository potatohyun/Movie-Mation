<template>
  <div>
    <h1>{{movie?.title}}</h1>
    <img :src="movie?.poster_path" alt="">
    <h5>{{movie?.overview}}</h5>
    <!-- <h5>{{movie?.comments}}</h5> -->
    <CommentList/>
    <router-link :to="{ name : 'CommentCreateView' }">[댓글쓰기]</router-link>
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '@/components/CommentList'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'MovieDetailView',
    components:{
      CommentList
    }, 
    data(){
      return{
        movie : null,
      }
    },
    created(){
      this.getMovieDetail()
      this.getComments()
    },
    methods:{
      getMovieDetail(){
        axios({
          method: 'get',
          url: `${API_URL}/main/movies/${this.$route.params.id}`,
        })
        .then((res)=>{
          // console.log(res)
          this.movie=res.data
        })
        .catch(err=>console.log(err))
      },
      getComments(){
        this.$store.dispatch('getComments')
      }
    },
    
}
</script>

<style>

</style>