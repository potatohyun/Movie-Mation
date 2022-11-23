<template>
  <div>
    <h3>AverageList</h3>
    <AverageListItem
      v-for="a_movie in averagemovies"
      :key="a_movie.id"
      :a_movie="a_movie"
    />
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

</style>