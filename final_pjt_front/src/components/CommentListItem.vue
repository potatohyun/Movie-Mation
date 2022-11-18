<template>
  <div>
    <!-- <h5>{{comments.grade}}</h5> -->
    <h5>{{comment.title}}</h5>
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