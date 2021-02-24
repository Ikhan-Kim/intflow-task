<template>
  <div>
    <iframe :src="videoSrc" frameborder="0" width="100%" height="400px"></iframe></div>  
</template>

<script>
export default {
  name: 'Video',

  props: {
    video: {
      type: String,
    }
  },

  computed: {
    videoSrc() {
      return `https://www.youtube.com/embed/${this.video}`
    }
  }
}
</script>