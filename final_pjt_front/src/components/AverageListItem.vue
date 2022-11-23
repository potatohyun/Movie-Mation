<template>
  <div>
    <!-- {{a_movie}} -->
    <img :src="getImgUrl" alt="">
    <h2>{{ a_movie.title }}</h2>
    <p>{{ a_movie.overview }}</p>
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
    <hr>

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

</style>