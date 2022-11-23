<template>
  <div class="col">
    <div class="card h-100">
      <img class="movieimg mb-3" :src="getImgUrl" alt="">
      <div class="title">
        <b>{{ movie.title }}</b>
      </div>
      <div class="link">
        <router-link 
          :to="{ 
            name : 'MovieDetailView',
            params: {id:movie.id}
          }"
        >
        <button type="button" class="btn btn-outline-danger">영화정보보기</button>
        <!-- [영화정보보기] -->
        </router-link>
      </div>
      <!-- <hr> -->
    </div>
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
.movieimg{
  height: 25vw;
}
/* 
.link{
  align-content: flex-end;
	align-items: flex-end;
} 
*/
</style>