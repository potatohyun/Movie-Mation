<template>
  <div>
    <!-- {{p_movie}} -->
    <img :src="getImgUrl" alt="">
    <h2>{{ p_movie.title }}</h2>
    <p>{{ p_movie.overview }}</p>
    <p>인기도 : {{ p_movie.popularity }}</p>
    <p>개봉일 : {{ p_movie.release_date }}</p>

    <router-link 
      :to="{ 
        name : 'MovieDetailView',
        params: {id:p_movie.id}
      }"
    >
      [영화정보보기]
    </router-link> 
    <hr>

  </div>
</template>

<script>
export default {
  name: 'PopularityListItem',
  props: {
    p_movie:Object,
  },
  data() {
    return{
      getImgUrl: `${this.p_movie?.poster_path}`
    }
  },
}
</script>

<style>

</style>