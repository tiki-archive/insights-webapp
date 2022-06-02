<template>
  <div
    class="companyHeader"
    :style="'background: linear-gradient(180deg, rgba(68, 35, 75, 0) 0%, #44234b 100%) no-repeat, url(\'https://i.gyazo.com/24c74c14a569513e17d30a0272398e71.png\') no-repeat'"
  >
    <span class="headerInfo">
      <span class="companyLabel">Company</span>
      <span class="companyName">{{ name }}</span>
      <span>
        <span class="companyUsers">{{ monthly_users }} monthly users</span>

        <button class="companyFollow">FOLLOW</button>
      </span>
    </span>
  </div>
</template>

<script>
export default {
  props: ['name', 'monthly_users'],
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.companyHeader
  width: 100%

  height: 40vh

  min-height: 340px

  background-size: cover !important

  display: flex

.headerInfo
  display: flex
  flex-direction: column

  margin: auto auto 48px 32px

.companyLabel
  color: white
  font-size: 1rem

.companyName
  color: white
  font-size: 6rem
  line-height: 6rem
  padding: 8px 0

  font-weight: 800

.companyUsers
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

  &:hover
    border: 1px solid white
</style>
