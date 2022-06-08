<template>
  <nuxt-link :to="to" @click.native="clickedLink">
    <slot></slot>
  </nuxt-link>
</template>

<script>
/**
 * This component wraps NuxtLink in order to track where users
 * go on the site so that navigation arrows work.
 */
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
