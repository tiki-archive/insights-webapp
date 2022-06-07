export const state = () => ({
  pagesVisited: [],
  currentIndex: 0,
})

export const mutations = {
  visitedPage(state, routeName) {
    // remove all forward history if they go down a different path
    if (state.pagesVisited.length > state.currentIndex + 1) {
      state.pagesVisited.splice(
        state.currentIndex,
        state.pagesVisited.length,
        routeName
      )
    } else {
      state.pagesVisited.push(routeName)
    }

    state.currentIndex++
  },
  navigateBack(state) {
    state.currentIndex--
  },
  navigateForward(state) {
    state.currentIndex++
  },
}

export const getters = {
  getCurrentPage(state) {
    return state.pagesVisited[state.currentIndex]
  },
  hasPrevPage(state) {
    return state.currentIndex > 0
  },
  hasNextPage(state) {
    return state.pagesVisited.length > state.currentIndex + 1
  },
}
