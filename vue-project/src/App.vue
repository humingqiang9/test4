<template>
  <div>
    <p>使用自定义指令聚焦输入框:</p>
    <input v-focus class="input-box" type="text" placeholder="我会自动聚焦">
    <p>另一个普通输入框:</p>
    <input class="input-box" type="text" placeholder="我不会自动聚焦">
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
.input-box {
  display: block;
  margin: 10px 0;
  padding: 8px;
  font-size: 16px;
}
</style>