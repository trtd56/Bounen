<template>
  <div class="TopPage">
    <img src="../assets/logo.png">
    <h2>投票アプリ</h2>
    <input type="text" placeholder="名前を入力して下さい" v-model="InputName">
    <p>
      <router-link :to="{ name: 'Q1Page', params: {username: InputName }}">問題1に進む</router-link >
    </p>
  </div>
</template>

<script>
export default {
  data () {
    return {
      InputName: 'test'
    }
  },
  methods: {}
}
</script>

<style>
h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
.TopPage {
  margin-top: 20px;

  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center
}
input {
  margin: 10px 0;
  padding: 10px;
}
</style>
