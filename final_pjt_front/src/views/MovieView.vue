<template>
  <div>
    <h5>{{username}} 어린이 환영합니다</h5>
    <MovieList/>
  </div>
</template>

<script>
const API_URL = "http://127.0.0.1:8000"

import MovieList from '@/components/MovieList'
import axios from 'axios'

export default {
  name: 'MovieView',
  components:{
      MovieList,
  },
  data(){
    return{
      username : null,
    }
  },
  created(){
    this.getMovies()
    this.getUsername()
  },
  methods:{
    getToken: function (){
        const key = this.$store.state.token

        const config = {
          headers:{
              Authorization: `Token ${ key }`
          }
        }
      return config
    },
    getMovies(){
      this.$store.dispatch('getMovies')
    },
    getUsername(){
      const config = this.getToken()
      axios.get(`${API_URL}/accounts/user/`, config)
      .then((res) => {
        console.log(res.data)
        this.username = res.data.username
      }
    )}
  }
}
</script>

<style>

</style>