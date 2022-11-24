<template>
  <div>
    <h2>내가 작성한 리뷰들</h2>
    <MyReviewListItem
        v-for="myreview in myreviews"
        :key="myreview.id"
        :myreview="myreview"
    />
  </div>
</template>

<script>
import MyReviewListItem from '@/components/MyReviewListItem'

export default {
    name: 'MyReviewList',
    components:{
        MyReviewListItem,
    },
    props:{
        myreviews:Array
    },
}
</script>

<style>

</style>