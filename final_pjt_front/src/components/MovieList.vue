<template>
  <div class="movie-list">
    <h3>movielist</h3>
    <MovieListItem/>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem';
export default {
    name: 'MovieList',
    components:{
        MovieListItem
    }

}
</script>

<style>

</style>