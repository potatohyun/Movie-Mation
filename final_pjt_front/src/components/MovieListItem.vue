<template>
  <div>
    <img :src="getImgUrl" alt="">
    <br>
    <p>{{ movie.title }}</p>
    <router-link 
      :to="{ 
        name : 'MovieDetailView',
        params: {id:movie.id}
      }"
    >
      [영화정보보기]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie:Object,
  },
  data() {
    return{
      getImgUrl: `${this.movie?.poster_path}`
    }
  },
}
</script>

<style>

</style>