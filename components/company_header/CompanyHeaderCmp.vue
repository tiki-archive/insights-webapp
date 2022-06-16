<template>
  <div
    class="companyHeader"
    :style="'background: linear-gradient(180deg, rgba(68, 35, 75, 0) 0%, #44234b 100%) no-repeat, url(\'https://i.gyazo.com/24c74c14a569513e17d30a0272398e71.png\') no-repeat'"
  >
    <span class="headerInfo">
      <span class="themeHeaderLabel">Company</span>
      <span class="themeBigHeaderText">{{ name }}</span>

      <span>
        <span class="monthlyUsersText">{{ monthly_users }} monthly users</span>

        <button
          :class="'companyFollow ' + [this.following ? 'companyFollowing' : '']"
          @click="toggleFollowing()"
        >
          {{ following ? 'FOLLOWING' : 'FOLLOW' }}
        </button>
      </span>
    </span>
  </div>
</template>

<script>
export default {
  props: ['name', 'monthly_users', 'following'],
  methods: {
    toggleFollowing() {
      this.$emit('setFollowing', !this.following)
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"

.companyHeader
  width: 100%
  height: 40vh
  min-height: 340px
  background-size: cover !important
  display: flex

.headerInfo
  display: flex
  flex-direction: column

  margin: auto auto calc($page-section-padding + $page-row-gap) $page-main-content-padding
.monthlyUsersText
  color: white
  font-size: 1rem

.companyFollow
  color: white
  font-size: 12px
  font-weight: 800

  cursor: pointer

  background: transparent

  margin-left: 24px

  padding: 6px 14px

  border: 1px solid rgba(240, 240, 240, 0.5)
  border-radius: 8px

  &:hover, &.companyFollowing
    border: 1px solid white
</style>
