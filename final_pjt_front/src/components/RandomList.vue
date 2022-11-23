<template>
  <div class="box mx-5">
    <br><h1>고르기 어려우시다구요?<br>그럼 이건 어떤가요?</h1><br>
    <div class="row row-cols-3 row-cols-md-5 g-4" id="randlist">
    <RandomListItem
      v-for="r_movie in randommovies"
      :key="r_movie.id"
      :r_movie="r_movie"
    />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import RandomListItem from '@/components/RandomListItem'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'RandomList',
    components:{
      RandomListItem,
    }, 
    data(){
      return{
        randommovies : null,
      }
    },
    created(){
      this.randomMovies()
    },
    methods: {
      randomMovies() {
        axios({
          method: 'get',
          url: `${API_URL}/main/recommend/random/`,
        })
        .then((res)=>{
          this.randommovies=res.data
        })
        .catch(err=>console.log(err))
      }
    }
}
</script>

<style>
#randlist{
  margin-left: 200px;
}
</style>