<template>
  <div>
    <h1>댓글 작성</h1>
    <form @submit.prevent="createComment">
      <label for="title">제목: </label>
      <input type="text" id="title" v-model="title"><br>
      <label for="content">내용: </label>
      <textarea 
        id="content" cols="30" rows="10"
        v-model="content">
      </textarea><br>
      <label for="grade">평점: </label>
      <input type="int" id="grade" v-model="grade">
      <!-- <input type="submit" id="submit"> -->
      <!-- 유저 -->
      <!-- <label for="user">user: </label>
      <input type="int" id="user" v-model="user"> -->
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

const API_URL = "http://127.0.0.1:8000"
// const ID = ""

export default {
    name: 'CommentCreateView',
    props: {
      id:Number
    },
    data(){
      return{
        title : '제목을 입력하세요',
        content : '내용을 입력하세요',
        grade : 0,
        // user : null,
      }
    },
    methods:{
      getToken: function () {
        
        const config = {
          headers:{
            Authorization: `Token ${ this.$store.state.token }`
          }
        }
        return config
      },
      createComment(){
        const config = this.getToken

        const commentItem ={
          title : this.title,
          content : this.content,
          grade : this.grade,
        }
        
        // const user = this.user
        // if(!title){
        //   alert('제목이 없어요')
        //   return
        // } else if(!content){
        //   console.log(this.title)
        //   console.log(title)
        //   alert('내용이 없어요')
        //   return
        // } else if(!grade){
        //   alert('평점주세요!')
        //   return
        // }
        axios.post(`${API_URL}/main/movies/${this.$route.params.id}/createcomments/`,commentItem, config)
          .then((res)=>{
            console.log(res)
            alert("소중한 리뷰 고맙습니다!")
            router.push({ name: "MovieDetailView" })
            
          })
          .catch(err=>console.log(err))
      }
    }
}
</script>

<style>

</style>