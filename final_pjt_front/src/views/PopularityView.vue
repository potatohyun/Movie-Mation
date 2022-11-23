<template>
  <div>
    <!-- <h1>인기순으로 보여드립니당</h1> -->
    <PopularityList/>
  </div>
</template>

<script>
import PopularityList from '@/components/PopularityList'

export default {
    name: 'PopularityView',
    components:{
      PopularityList,
    },

}
</script>

<style>
/* h1{
  margin: 10px;
} */
</style>