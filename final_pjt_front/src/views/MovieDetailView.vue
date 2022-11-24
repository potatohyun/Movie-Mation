<template>
  <div>
    <div style="float:left; margin-right:20px;">
      <img :src="movie?.poster_path" alt="">
    </div>
    <div style="text-align:left">
      <h1>{{movie?.title}}</h1> <!-- 스크롤 찾다 말  -->
      <div 
        data-bs-spy="scroll" 
        data-bs-root-margin="0px 0px -40%" 
        data-bs-smooth-scroll="true" 
        class="scrollspy-example bg-light p-3 rounded-2" 
        tabindex="0">
      <!-- <p>{{movie?.overview}}</p> -->
      <h5>{{movie?.overview}}</h5>
      </div>
    </div>
    <div style="text-align:left">
      <hr>
      <router-link style="text-align:right" :to="{ name : 'CommentCreateView' }">[댓글쓰기]</router-link>
      <CommentList :comments="movie?.comments"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '@/components/CommentList'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'MovieDetailView',
    components:{
      CommentList,
    }, 
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
          // console.log(res)
          this.movie=res.data
        })
        .catch(err=>console.log(err))
      },
    },
    
}
</script>

<style>

</style>