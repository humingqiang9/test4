<template>
  <div class="click-counter-component">
    <h2>Vue Click Counter</h2>
    <p>Count: {{ count }}</p>
    <button @click="incrementCounter">Click Me!</button>
  </div>
</template>

<script>
export default {
  name: 'ClickCounterComponent',
  data() {
    return {
      count: 0
    }
  },
  methods: {
    incrementCounter() {
      this.count++
    }
  }
}
</script>

<style scoped>
.click-counter-component {
  text-align: center;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  max-width: 300px;
  margin: 20px auto;
}

button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #359c6d;
}
</style>