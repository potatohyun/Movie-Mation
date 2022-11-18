<template>
  <div>
    <h1>댓글보기</h1>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'CommentDetailView',
    created(){
        this.getCommentDetail()
    },
    methods:{
        getCommentDetail(){
            axios({
                method: 'get',
                url: `${API_URL}/main/movies/comments/${this.$route.params.id}`,
            })
            .then((res)=>{
                console.log(res)
            })
            .catch(err=>console.log(err))
        }
    }
}
</script>

<style>

</style>