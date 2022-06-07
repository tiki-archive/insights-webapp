<template>
  <nuxt-link :to="to" @click.native="clickedLink">
    <slot></slot>
  </nuxt-link>
</template>

<script>
export default {
  name: 'TrackedNuxtLink',
  props: ['to'],
  methods: {
    clickedLink() {
      this.$store.commit('navigation/visitedPage', this.to)
    },
  },
}
</script>
