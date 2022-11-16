<template>
  <div>
    <h1>MovieListItem</h1>
    <router-link :to="{ name : 'MovieDetailView'}">[영화정보보기]</router-link>
  </div>
</template>

<script>
export default {
    name: 'MovieListItem'

}
</script>

<style>

</style>