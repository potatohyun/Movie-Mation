<template>
  <div>
    <h1>몰?루</h1>
    <hr>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
    name: 'MovieView',
    components:{
        MovieList,
    },
    created(){
      this.getMovies()
    },
    methods:{
      getMovies(){
        this.$store.dispatch('getMovies')
      }
    }
}
</script>

<style>

</style>