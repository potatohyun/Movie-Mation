<template>
  <div class="box mx-5">
    <br><h1>투표순으로 보여드립니당</h1><br>
    <div class="row row-cols-3 row-cols-md-5 g-4" id="averlist">
      <AverageListItem
        v-for="a_movie in averagemovies"
        :key="a_movie.id"
        :a_movie="a_movie"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import AverageListItem from '@/components/AverageListItem'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'AverageList',
    components:{
      AverageListItem,
    }, 
    data(){
      return{
        averagemovies : null,
      }
    },
    created(){
      this.averageMovies()
    },
    methods: {
      averageMovies() {
        axios({
          method: 'get',
          url: `${API_URL}/main/recommend/average/`,
        })
        .then((res)=>{
          this.averagemovies=res.data
        })
        .catch(err=>console.log(err))
      }
    }
}
</script>

<style>
#averlist{
  margin-left: 200px;
}
</style>