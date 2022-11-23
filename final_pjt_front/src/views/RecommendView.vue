<template>
  <div>
    <!-- <div class="recommend-info my-4"> -->
      <!-- <h1>영화찾기 힘드시다구요? 저희가 찾아드리죠!</h1> -->
      <!-- <span>영화찾기 힘드시다구요? 저희가 찾아드리죠!</span> -->
    <!-- </div> -->
    <nav class="recommend-nav" >
      <ul class="menu">
        <li><router-link id="link" :to="{ name:'PopularityView' }">인기순</router-link></li>
        <li><router-link id="link" :to="{ name:'AverageView' }">평점순</router-link></li>
        <li><router-link id="link" :to="{ name:'RandomView' }">랜덤!</router-link></li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>

<script>

export default {
    name: 'RecommendView',
}
</script>

<style>
li{
  list-style: none;
}
.recommend-nav{
  width: 200px;
  background-color: rgb(184, 184, 184);
  /* border-right: 1px solid rgb(255, 122, 122); */
  
  position: fixed;
  height: 100%;
}
.menu li #link{
  height: 40px;
  line-height: 25px;
  display:block;
  /* padding: 0 20px; */
  font-size: 16px;
  color: black;
  text-decoration-line: none;
}
.menu li #link:hover {
  background-color: rgb(65, 64, 64); /* 마우스 올렸을때 배경색*/
  color: red /* 마우스 올렸을때 글자색*/
}
</style>