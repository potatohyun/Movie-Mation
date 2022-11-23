<template>
  <div class="box mx-5">
    <!-- <br>
    <h1>MOVIE LIST</h1> 
    <br> -->
    <div class="row row-cols-1 row-cols-md-5 g-4">  <!-- row-cols-1 row-cols-md-3 두개 뭔차이야(뒤에껀 대충알겠는데 앞에껀 뭐야)-->
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem';

export default {
    name: 'MovieList',
    components:{
        MovieListItem
    },
    computed: {
      movies() {
        return this.$store.state.movies
      }
    }

}
</script>

<style>

</style>