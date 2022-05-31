<template>
  <form>
    <input
      class="searchBar"
      type="text"
      v-model="searchTerm"
      placeholder="Search insights, companies, dashboards..."
      v-on:submit="search()"
    />

    <span>{{ searchTerm }}</span>
  </form>
</template>

<script>
export default {
  components: {},
  name: 'SearchBar',
  data() {
    return {
      searchTerm: '',
    }
  },
  methods: {
    search() {
      console.log('test push ' + this.searchTerm)
      this.$router.push('home')
    },
  },
}
</script>

<style scoped lang="sass">
form
  display: flex
  width: 20%
  border: 0
  border-radius: 300px

.searchBar
  margin: auto 0

  width: 100%

  border: 0
  border-radius: inherit
  outline-width: 0

  padding: 6px 15px 6px 48px
  text-overflow: ellipsis

  height: 38px

  font-size: 0.875rem
  line-height: 1rem

  background: white url("../../assets/images/svg/icon_search_form.svg") no-repeat 14px/22px

::-webkit-search-cancel-button
    -webkit-appearance: none
    cursor: pointer

    height: 20px
    width: 20px

    background: url("../../assets/images/svg/icon_search_form_x.svg") no-repeat 0px/20px
</style>
