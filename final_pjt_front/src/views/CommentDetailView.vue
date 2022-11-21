<template>
  <div>
    <h1><router-link :to="{ name:'MovieDetailView' }">{{comment?.movie.title}}</router-link></h1>
    <hr>
    <h1>리뷰 제목 : {{comment?.title}}</h1>
    <button @click="updateComment"> 수정 </button>
    <button @click="deleteComment"> 삭제 </button>
    <h3>리뷰 내용 : {{comment?.content}}</h3>
    <hr>
    <h5>작성 날짜 : {{comment?.created_at}}</h5>
    <h5>수정 날짜 : {{comment?.updated_at}}</h5>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'CommentDetailView',
    data(){
        return{
            comment : null,
        }
    },
    created(){
        this.getCommentDetail()
    },
    
    methods:{
        getCommentDetail(){
            axios({
                method: 'get',
                url: `${API_URL}/main/movies/comments/${this.$route.params.pk}`,
            })
            .then((res)=>{
                console.log(res.data)
                this.comment=res.data
            })
            .catch(err=>console.log(err))
        },
        updateComment(){
            router.push({
                name: "CommentUpdateView",
                params:{
                    comment: this.comment
                }
            })
        },
        deleteComment(){
            axios({
                method: 'delete',
                url: `${API_URL}/main/movies/comments/${this.$route.params.pk}`,
            })
            .then(
                alert('삭제완료!'),
                router.push({ name: "MovieDetailView" })
            )
            .catch(err=>console.log(err))
            
        }
    }
}
</script>

<style>

</style>