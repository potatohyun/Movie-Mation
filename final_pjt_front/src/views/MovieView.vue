<template>
  <div>
<<<<<<< HEAD
    <h1>몰?루</h1>
    <hr>
=======
    <h5>{{username}}어린이 환영합니다</h5>
>>>>>>> c8a4a4c515241c72b595bccc099f4d3b5e2e9314
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