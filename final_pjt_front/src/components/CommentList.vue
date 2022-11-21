<template>
    <div class="comment-list">
      <h3>commentlist</h3>
      <CommentListItem
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
      />
    </div>
</template>
  
<script>
  import CommentListItem from '@/components/CommentListItem'

  export default {
    name: 'CommentList',
    props:{
      comments:Array
    },
    components:{
      CommentListItem
    },
    // computed:{
    //   comments(){
    //     return this.$store.state.comments
    //   }
    // }
  }
</script>

<style>

</style>