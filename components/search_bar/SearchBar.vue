<template>
  <form class="searchBarContainer">
    <input
      class="searchBar"
      type="search"
      v-model="searchTerm"
      placeholder="Search insights, companies, dashboards, ..."
    />
  </form>
</template>

<script>
export default {
  components: {},
  name: 'SearchBar',
  data() {
    return {
      searchTerm: null,
    }
  },
  methods: {
    submit() {
      this.$router.push({ path: 'search', query: { search: 'gello' } })
    },
    onScroll(event) {
      if (event.target.className === 'mainContainer') {
        this.pos = event.target.scrollTop
        if (event.target.scrollTop < 64) {
          const opa = event.target.scrollTop / 64.0
          document.getElementById('navbar').style.backgroundColor =
            'rgb(64, 44, 67, ' + opa + ')'
        } else {
          document.getElementById('navbar').style.backgroundColor =
            'rgb(64, 44, 67)'
        }
      }
    },
  },
  watch: {
    searchTerm(newTerm, prevTerm) {
      // this.$router.push({
      //   path: '/search/' + newTerm,
      // })

      history.pushState({}, null, '/search/' + newTerm)
    },
  },
  mounted() {
    window.addEventListener('scroll', this.onScroll, true)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.onScroll, true)
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.searchBarContainer
  display: flex
  height: $navbar-height

  width: 22%
  min-width: 300px

  border: 0
  border-radius: 300px
  z-index: 200

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

  background: url("../../assets/images/svg/icon_search_form_x.svg")
</style>
