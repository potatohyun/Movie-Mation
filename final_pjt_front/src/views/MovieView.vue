<template>
  <div>
    <h5>{{username}}어린이 환영합니다</h5>
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