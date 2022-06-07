export default function ({ store, route }) {
  store.commit('navigation/visitedPage', route.path)
  console.log(route)

  route.path = route.path + 'hello'
}
