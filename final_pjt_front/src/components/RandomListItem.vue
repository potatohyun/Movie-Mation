<template>
  <div class="col">
    <div class="card h-100" @click="goMovieDetail">
      <img class="movieimg mb-3" :src="getImgUrl" alt="">
      <h2>{{ r_movie.title }}</h2>
        <!-- <p>{{ r_movie.overview }}</p>
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
        <hr> -->
    </div>
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
.movieimg{
  height: 23vw;
  width: auto;
  object-fit:cover
}
</style>