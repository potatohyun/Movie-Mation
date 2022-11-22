<template>
  <div>
    <h1>영화추천페이지</h1>
    <nav>
      <router-link :to="{ name:'PopularityView' }">인기순</router-link> |
      <router-link :to="{ name:'AverageView' }">평점순</router-link> |
      <router-link :to="{ name:'RandomView' }">랜덤!</router-link> 
    </nav>
    <router-view/>
    선택해주세요
  </div>
</template>

<script>

export default {
    name: 'RecommendView',
}
</script>

<style>

</style>