<template>
  <div>
    <!-- <h5>{{comments.grade}}</h5> -->
    <h5>{{comment.title}}</h5>
    <h5>평점 : {{comment.grade}}</h5>
    <h5>아이디 : {{comment.id}}</h5>
    <router-link
      :to="{
        name: 'CommentDetailView',
        params: {pk: comment.id}
      }"
    >
      [리뷰상세보기]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props:{
    comment: Object
  }
}
</script>

<style>

</style>