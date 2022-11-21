<template>
    <div>
      <h1>댓글 수정</h1>
      <form @submit.prevent="updateComment">
        <label for="title">제목: </label>
        <input type="text" id="title" v-model="comment.title"><br>
        <label for="content">내용: </label>
        <textarea 
          id="content" cols="30" rows="10"
          v-model="comment.content">
        </textarea><br>
        <label for="grade">평점: </label>
        <input type="int" id="grade" v-model="comment.grade">
        <input type="submit" id="submit">

        <label for="user">user: </label>
        <input type="int" id="user" v-model="comment.user">

      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import router from '@/router'
  const API_URL = "http://127.0.0.1:8000"
  // const ID = ""
  
  export default {
      name: 'CommentUpdateView',
      props: {
        pk:Number
      },
      data(){
        return{
          comment : null,
          // title : null,
          // content : null,
          // grade : null,
        }
      },
      created(){
        this.getCommentDetail()
      },
      methods:{
        getCommentDetail(){
            axios({
                method: 'get',
                url: `${API_URL}/main/comment/${this.$route.params.pk}`,
                headers:{
                    Authorization: `Token ${ this.$store.state.token }`
                }
            })
            .then((res)=>{
                console.log(res)
                this.comment=res.data
            })
            .catch(err=>console.log(err))
        },
        updateComment(){
          const title = this.comment.title
          const content = this.comment.content
          const grade = this.comment.grade
          const user = this.comment.user
          if(!title){
            alert('제목이 없어요')
            return
          } else if(!content){
            console.log(title)
            alert('내용이 없어요')
            return
          } else if(!grade){
            alert('평점주세요!')
            return
          }
          axios({
            method: 'put',
            url:`${API_URL}/main/comment/${this.$route.params.pk}/`,
            headers:{
                    Authorization: `Token ${ this.$store.state.token }`
                },
            data: {title, content, grade, user},
  
          })
            .then((res)=>{
              console.log(res)
              alert("리뷰가 수정되었습니다.")
              router.push({ name: "MovieDetailView" })
            })
            .catch(err=>console.log(err))
        }
      }
  }
  </script>
  
  <style>
  
  </style>