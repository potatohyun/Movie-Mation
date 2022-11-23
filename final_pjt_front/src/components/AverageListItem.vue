<template>
  <div class="col">
    <div class="card h-100" @click="goMovieDetail">
    <img class="movieimg mb-3" :src="getImgUrl" alt="">
    <b>{{ a_movie.title }}</b>
    <!-- <p>{{ a_movie.overview }}</p>
    <p>평점 : {{ a_movie.vote_average }}</p>
    <p>개봉일 : {{ a_movie.release_date }}</p>
    
    <router-link 
      :to="{ 
        name : 'MovieDetailView',
        params: {id:a_movie.id}
      }"
    >
      [영화정보보기]
    </router-link> 
    <hr> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'AverageListItem',
  props: {
    a_movie:Object,
  },
  data() {
    return{
      getImgUrl: `${this.a_movie?.poster_path}`
    }
  },
}
</script>

<style>
.movieimg{
  height: 23vw;
  width: auto;
  object-fit:cover
}
</style>