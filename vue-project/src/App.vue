<template>
  <div id="app">
    <h1>Custom Focus Directive Demo</h1>
    <form>
      <label for="input1">Input 1 (Normal):</label>
      <input id="input1" type="text" placeholder="I won't be focused automatically">

      <label for="input2">Input 2 (With v-focus):</label>
      <input id="input2" type="text" v-focus placeholder="I will be focused on page load!">
    </form>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  padding: 20px;
}
input {
  display: block;
  margin-bottom: 15px;
  padding: 8px;
  font-size: 16px;
}
</style>