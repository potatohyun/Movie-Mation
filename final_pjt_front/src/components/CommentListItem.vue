<template>
  <div class="contatiner" @click="goCommentDetail">
    <div class="row">
      <div class="box col-2"><p>평점 : {{comment.grade}}</p></div>
      <div class="box col-7"><h4>{{comment.title}}</h4></div>
      <div class="box col-3 pe-5" style="text-align:right"><p>아이디 : {{comment.id}}</p></div>
    <!-- <router-link
      :to="{
        name: 'CommentDetailView',
        params: {pk: comment.id}
      }"
    >
      [리뷰상세보기]
    </router-link> -->
    <hr>
  </div>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props:{
    comment: Object
  },
  methods:{
    goCommentDetail(){
      if(this.$store.state.token === null){
        alert("로그인이 필요합니다.")
        this.$router.push({name : 'LogInView'})
      }else{
        this.$router.push({name : 'CommentDetailView', params: {pk:this.comment.id}})
      }
    }
  }
}
</script>

<style>

</style>