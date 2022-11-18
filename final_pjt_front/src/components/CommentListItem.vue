<template>
  <div>
    <!-- <h5>{{comments.grade}}</h5> -->
    <h5>{{comment.title}}</h5>
    <router-link
      :to="{
        name: 'CommentDetailView',
        params: {pk: comment.id}
      }"
    >
      [리뷰내용보기]
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