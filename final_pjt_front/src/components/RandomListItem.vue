<template>
  <div>
    <!-- {{r_movie}} -->
    <img :src="getImgUrl" alt="">
    <h2>{{ r_movie.title }}</h2>
    <p>{{ r_movie.overview }}</p>
    <p>인기도 : {{ r_movie.popularity }}</p>
    <p>평점 : {{ r_movie.vote_average }}</p>
    <p>개봉일 : {{ r_movie.release_date }}</p>

    <router-link 
      :to="{ 
        name : 'MovieDetailView',
        params: {id:r_movie.id}
      }"
    >
      [영화정보보기]
    </router-link> 
    <hr>

  </div>
</template>

<script>
export default {
  name: 'RandomListItem',
  props: {
    r_movie:Object,
  },
  data() {
    return{
      getImgUrl: `${this.r_movie?.poster_path}`
    }
  },
}
</script>

<style>

</style>