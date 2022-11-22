<template>
  <div>
    <h1>Popularity</h1>
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

</style>